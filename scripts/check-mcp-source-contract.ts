import { createHash } from 'node:crypto'
import { readFile } from 'node:fs/promises'
import { resolve } from 'node:path'

const INTERNAL_TELEMETRY_FIELDS = new Set([
  'attempts', 'observedIp', 'observedCity', 'observedRegion',
  'proxyResolutionSource', 'proxyTargetLevel', 'proxyTargetLocation', 'proxyTargetZip',
  'proxyIdSuffix', 'browserSessionId', 'browserSessionIdSuffix',
  'attemptNumber', 'maxAttempts', 'willRetry',
])

function stripInternalTelemetry(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(stripInternalTelemetry)
  if (!value || typeof value !== 'object') return value
  const out: Record<string, unknown> = {}
  for (const [key, child] of Object.entries(value as Record<string, unknown>)) {
    if (key === 'properties' && child && typeof child === 'object') {
      const properties: Record<string, unknown> = {}
      for (const [property, propertyValue] of Object.entries(child as Record<string, unknown>)) {
        if (!INTERNAL_TELEMETRY_FIELDS.has(property)) properties[property] = stripInternalTelemetry(propertyValue)
      }
      out[key] = properties
    } else if (key === 'required' && Array.isArray(child)) {
      out[key] = child.filter(name => !INTERNAL_TELEMETRY_FIELDS.has(String(name)))
    } else {
      out[key] = stripInternalTelemetry(child)
    }
  }
  return out
}

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`
  if (value && typeof value === 'object') {
    const entries = Object.entries(value as Record<string, unknown>)
      .sort(([left], [right]) => left.localeCompare(right))
    return `{${entries.map(([key, child]) => `${JSON.stringify(key)}:${canonicalJson(child)}`).join(',')}}`
  }
  return JSON.stringify(value)
}

function projectedDigest(tools: Array<Record<string, unknown>>): string {
  const projected = tools.map(tool => ({
    name: tool.name,
    ...(tool.title ? { title: tool.title } : {}),
    description: tool.description ?? '',
    inputSchema: tool.inputSchema ?? { type: 'object', additionalProperties: true },
    outputSchema: stripInternalTelemetry(tool.outputSchema) ?? { type: 'object', additionalProperties: true },
    annotations: tool.annotations ?? {},
  })).sort((left, right) => String(left.name).localeCompare(String(right.name)))
  return createHash('sha256').update(canonicalJson(projected)).digest('hex')
}

async function main(): Promise<void> {
  const sourcePath = process.argv[2] ?? process.env.MCP_TOOL_SOURCE_MANIFEST_PATH
  if (!sourcePath) throw new Error('Pass the final server manifest path or set MCP_TOOL_SOURCE_MANIFEST_PATH')

  const [source, sdk] = await Promise.all([
    readFile(resolve(sourcePath), 'utf8').then(text => JSON.parse(text) as Record<string, unknown>),
    readFile(resolve('contracts/mcp.tools.json'), 'utf8').then(text => JSON.parse(text) as Record<string, unknown>),
  ])
  const sourceTools = Array.isArray(source.tools) ? source.tools as Array<Record<string, unknown>> : []
  const sdkTools = Array.isArray(sdk.tools) ? sdk.tools as Array<Record<string, unknown>> : []
  const expectedCount = Number((source.counts as Record<string, unknown> | undefined)?.unified_stdio ?? sourceTools.length)
  const sourceVersion = String((source.serverInfo as Record<string, unknown> | undefined)?.version ?? '')
  const digest = projectedDigest(sourceTools)

  if (!sourceVersion) throw new Error('Source manifest has no serverInfo.version')
  if (sourceTools.length !== expectedCount) throw new Error(`Source manifest count mismatch: ${expectedCount} vs ${sourceTools.length}`)
  if (sdkTools.length !== sourceTools.length || Number(sdk.toolCount) !== sourceTools.length) {
    throw new Error(`SDK tool count ${sdkTools.length}/${String(sdk.toolCount)} does not match source ${sourceTools.length}`)
  }
  if (!String(sdk.generatedFrom).includes(`mcp-scraper ${sourceVersion} `)) {
    throw new Error(`SDK generatedFrom does not name mcp-scraper ${sourceVersion}`)
  }
  if (sdk.sourceContractSha256 !== digest) {
    throw new Error(`SDK sourceContractSha256 ${String(sdk.sourceContractSha256)} does not match ${digest}`)
  }
  if (projectedDigest(sdkTools) !== digest) throw new Error('SDK tool contract content does not match the source projection')

  console.log(JSON.stringify({ serverVersion: sourceVersion, toolCount: sourceTools.length, sourceContractSha256: digest }))
}

main().catch(error => {
  console.error(error instanceof Error ? error.message : String(error))
  process.exitCode = 1
})
