import assert from 'node:assert/strict'
import { mkdtemp, mkdir, readFile, writeFile } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'
import { spawnSync } from 'node:child_process'
import { createRequire } from 'node:module'
import test from 'node:test'

const updater = resolve('scripts/update-mcp-manifest.ts')
const tsxLoader = createRequire(join(process.cwd(), 'package.json')).resolve('tsx')

async function fixture(outputSchema: Record<string, unknown> | undefined) {
  const directory = await mkdtemp(join(tmpdir(), 'mcpscraper-sdk-contract-'))
  const contracts = join(directory, 'contracts')
  await mkdir(contracts)
  await writeFile(join(contracts, 'memory.tools.json'), JSON.stringify({ tools: [] }))
  const prior = {
    schemaVersion: 1,
    generatedFrom: 'stale source',
    toolCount: 1,
    tools: [{
      name: 'example_tool',
      description: 'stale',
      category: 'other',
      methodName: 'exampleTool',
      inputSchema: { type: 'object' },
      outputSchema: { type: 'object', properties: { stale: { type: 'boolean' } } },
      outputSchemaProvided: true,
      annotations: {},
    }],
  }
  const priorText = `${JSON.stringify(prior, null, 2)}\n`
  await writeFile(join(contracts, 'mcp.tools.json'), priorText)
  const sourcePath = join(directory, 'server-manifest.json')
  await writeFile(sourcePath, JSON.stringify({
    generatedFrom: 'build artifact',
    serverInfo: { name: 'mcp-scraper', version: '1.2.3' },
    counts: { unified_stdio: 1 },
    tools: [{
      name: 'example_tool',
      description: 'fresh',
      inputSchema: { type: 'object', properties: { query: { type: 'string' } } },
      ...(outputSchema === undefined ? {} : { outputSchema }),
      annotations: {},
    }],
  }))
  return { directory, sourcePath, priorText }
}

function run(directory: string, env: Record<string, string | undefined>) {
  return spawnSync(process.execPath, ['--import', tsxLoader, updater], {
    cwd: directory,
    env: { ...process.env, ...env },
    encoding: 'utf8',
  })
}

test('complete local server manifest generates the SDK contract', async () => {
  const { directory, sourcePath } = await fixture({
    type: 'object',
    properties: { answer: { type: 'string' } },
    required: ['answer'],
  })
  const result = run(directory, { MCP_TOOL_MANIFEST_PATH: sourcePath })
  assert.equal(result.status, 0, result.stderr)
  const generated = JSON.parse(await readFile(join(directory, 'contracts/mcp.tools.json'), 'utf8'))
  assert.equal(generated.tools[0].outputSchema.properties.answer.type, 'string')
  assert.equal(generated.tools[0].outputSchemaProvided, true)
  assert.match(generated.generatedFrom, /mcp-scraper 1\.2\.3/)
})

test('one missing output schema fails before overwriting a stale prior schema', async () => {
  const { directory, sourcePath, priorText } = await fixture(undefined)
  const result = run(directory, { MCP_TOOL_MANIFEST_PATH: sourcePath })
  assert.notEqual(result.status, 0)
  assert.match(result.stderr, /missing outputSchema/)
  assert.equal(await readFile(join(directory, 'contracts/mcp.tools.json'), 'utf8'), priorText)
})

test('a live-only update fails even when an API key is present', async () => {
  const { directory, priorText } = await fixture(undefined)
  const result = run(directory, { MCP_TOOL_MANIFEST_PATH: undefined, MCP_SCRAPER_API_KEY: 'test-key' })
  assert.notEqual(result.status, 0)
  assert.match(result.stderr, /MCP_TOOL_MANIFEST_PATH is required/)
  assert.equal(await readFile(join(directory, 'contracts/mcp.tools.json'), 'utf8'), priorText)
})

test('a source without server identity fails before writing', async () => {
  const { directory, sourcePath, priorText } = await fixture({ type: 'object' })
  const source = JSON.parse(await readFile(sourcePath, 'utf8'))
  delete source.serverInfo.version
  await writeFile(sourcePath, JSON.stringify(source))
  const result = run(directory, { MCP_TOOL_MANIFEST_PATH: sourcePath })
  assert.notEqual(result.status, 0)
  assert.match(result.stderr, /serverInfo\.name and serverInfo\.version/)
  assert.equal(await readFile(join(directory, 'contracts/mcp.tools.json'), 'utf8'), priorText)
})
