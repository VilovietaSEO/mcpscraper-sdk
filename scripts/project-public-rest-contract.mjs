import { readFile, writeFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { resolve } from 'node:path'
import yaml from 'js-yaml'

const sourcePath = resolve('contracts/server-rest.v1.json')
const outputPath = resolve('contracts/scraper.openapi.generated.json')
const sourceArg = process.argv.find(arg => arg.startsWith('--source='))?.slice('--source='.length)
const check = process.argv.includes('--check')

const sourceText = await readFile(sourceArg ? resolve(sourceArg) : sourcePath, 'utf8')
const source = JSON.parse(sourceText)
if (source.schemaVersion !== 1 || !source.sourceContractSha256 || !Array.isArray(source.operations)) {
  throw new Error('Invalid server-owned REST contract')
}
function canonicalJson(value) {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`
  if (value && typeof value === 'object') {
    return `{${Object.entries(value).sort(([a], [b]) => a.localeCompare(b))
      .map(([key, child]) => `${JSON.stringify(key)}:${canonicalJson(child)}`).join(',')}}`
  }
  return JSON.stringify(value)
}
const { sourceContractSha256, ...contractBody } = source
const actualSha256 = createHash('sha256').update(canonicalJson(contractBody)).digest('hex')
if (actualSha256 !== sourceContractSha256) throw new Error('Server REST contract digest does not match its content')
if (sourceArg && check) {
  const checkedIn = await readFile(sourcePath, 'utf8').catch(() => '')
  if (checkedIn !== sourceText) throw new Error('SDK server REST contract differs from the supplied server source')
}

const spec = yaml.load(await readFile('contracts/scraper.openapi.yaml', 'utf8'))
const componentNames = {
  mapsSearch: { request: 'MapsSearchRequest', responses: { 200: 'MapsSearchResponse' } },
  directoryWorkflow: { request: 'DirectoryRunRequest', responses: { 200: 'DirectoryJobResponse', 202: 'DirectoryJobResponse' } },
  directoryJobStatus: { responses: { 200: 'DirectoryJobResponse', 404: 'DirectoryJobNotFound' } },
}

for (const operation of source.operations) {
  const names = componentNames[operation.operationId]
  if (!names) throw new Error(`Unmapped server operation ${operation.operationId}`)
  const method = operation.method.toLowerCase()
  const existing = spec.paths[operation.path]?.[method]
  if (existing?.operationId !== operation.operationId) throw new Error(`OpenAPI operation mismatch for ${operation.path}`)
  const projected = {
    ...existing,
    tags: [operation.tag],
    operationId: operation.operationId,
    summary: operation.summary,
    description: operation.description,
    parameters: [
      ...(existing.parameters ?? []).filter(parameter => parameter.in === 'path'),
      ...operation.requestHeaders.map(header => ({
        in: 'header', name: header.name, required: false,
        schema: { type: 'string', minLength: 1, maxLength: 500 },
        description: header.description,
      })),
    ],
    responses: { ...existing.responses },
  }
  if (operation.requestSchema) {
    spec.components.schemas[names.request] = operation.requestSchema
    projected.requestBody = {
      required: true,
      content: { 'application/json': { schema: { $ref: `#/components/schemas/${names.request}` } } },
    }
  }
  for (const [status, responseSchema] of Object.entries(operation.responses)) {
    const schemaName = names.responses[status]
    if (!schemaName) throw new Error(`Unmapped ${operation.operationId} status ${status}`)
    spec.components.schemas[schemaName] = responseSchema
    projected.responses[status] = {
      description: existing.responses[status]?.description ?? operation.summary,
      content: { 'application/json': { schema: { $ref: `#/components/schemas/${schemaName}` } } },
    }
  }
  spec.paths[operation.path][method] = projected
}
spec.components.schemas.PublicErrorEnvelope.properties.error_code.enum = source.publicErrorCodes
spec.components.schemas.PublicErrorEnvelope.properties.error_type.enum = source.publicErrorTypes
spec['x-server-rest-contract-sha256'] = source.sourceContractSha256
spec['x-server-owned-operations'] = source.operations.map(operation => operation.operationId)

const expected = `${JSON.stringify(spec, null, 2)}\n`
if (check) {
  if (await readFile(outputPath, 'utf8').catch(() => '') !== expected) {
    throw new Error('Generated OpenAPI is stale. Run npm run generate:rest.')
  }
  console.log(`REST source and OpenAPI projection current: ${source.sourceContractSha256}`)
} else {
  if (sourceArg) await writeFile(sourcePath, sourceText)
  await writeFile(outputPath, expected)
  console.log(`Wrote ${outputPath} from ${source.sourceContractSha256}`)
}
