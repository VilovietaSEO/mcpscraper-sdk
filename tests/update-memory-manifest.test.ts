import assert from 'node:assert/strict'
import { mkdtemp, mkdir, readFile, writeFile } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'
import { spawnSync } from 'node:child_process'
import { createRequire } from 'node:module'
import test from 'node:test'

const updater = resolve('scripts/update-memory-manifest.ts')
const tsxLoader = createRequire(join(process.cwd(), 'package.json')).resolve('tsx')

test('released Memory contract exposes 24 governed tools and no external CRM provider wrapper', async () => {
  const manifest = JSON.parse(await readFile(resolve('contracts/memory.tools.json'), 'utf8'))
  const governed = manifest.tools.filter((tool: { category: string }) => ['research', 'crm'].includes(tool.category))
  assert.equal(manifest.toolCount, 145)
  assert.equal(governed.filter((tool: { category: string }) => tool.category === 'research').length, 6)
  assert.equal(governed.filter((tool: { category: string }) => tool.category === 'crm').length, 18)
  assert.equal(governed.length, 24)
  assert.equal(
    manifest.tools.some((tool: { name: string; legacyId: string }) =>
      /salesforce|pipedrive|stripe|hubspot|zoho/iu.test(`${tool.name} ${tool.legacyId}`)),
    false,
  )
})

test('complete local Memory registry adds file assets without a production round trip', async () => {
  const directory = await mkdtemp(join(tmpdir(), 'mcpscraper-memory-contract-'))
  await mkdir(join(directory, 'contracts'))
  await writeFile(join(directory, 'contracts/memory.tools.json'), JSON.stringify({
    protocol: {},
    generatedFrom: 'stale',
    toolCount: 1,
    tools: [{
      name: 'memoryTool',
      description: 'old',
      category: 'memory',
      legacyId: 'memory-get',
      inputSchema: { type: 'object' },
      outputSchema: { type: 'object' },
    }],
  }))
  const sourcePath = join(directory, 'memory-server-manifest.json')
  await writeFile(sourcePath, JSON.stringify({
    generatedFrom: 'complete build manifest',
    serverInfo: { name: 'mcp-memory', version: '2.0.0' },
    tools: [
      { name: 'memoryTool', description: 'fresh', inputSchema: { type: 'object' }, outputSchema: { type: 'object' } },
      { name: 'file_asset_save', description: 'save', inputSchema: { type: 'object' }, outputSchema: { type: 'object' } },
      { name: 'file_asset_get', description: 'get', inputSchema: { type: 'object' }, outputSchema: { type: 'object' } },
      { name: 'researchPersonCaptureTool', description: 'capture research', inputSchema: { type: 'object' }, outputSchema: { type: 'object' } },
      { name: 'crmUpsertPersonTool', description: 'upsert CRM person', inputSchema: { type: 'object' }, outputSchema: { type: 'object' } },
    ],
  }))

  const result = spawnSync(process.execPath, ['--import', tsxLoader, updater], {
    cwd: directory,
    env: { ...process.env, MCP_MEMORY_TOOL_MANIFEST_PATH: sourcePath, MCP_MEMORY_API_KEY: '' },
    encoding: 'utf8',
  })
  assert.equal(result.status, 0, result.stderr)
  const generated = JSON.parse(await readFile(join(directory, 'contracts/memory.tools.json'), 'utf8'))
  assert.equal(generated.toolCount, 5)
  assert.match(generated.generatedFrom, /mcp-memory 2\.0\.0 complete build manifest/)
  assert.deepEqual(
    generated.tools.filter((tool: { name: string }) => tool.name.startsWith('file_asset_')).map((tool: { legacyId: string; category: string }) => [tool.legacyId, tool.category]),
    [['file_asset_save', 'files'], ['file_asset_get', 'files']],
  )
  assert.deepEqual(
    generated.tools.filter((tool: { name: string }) => /^(?:research|crm)/u.test(tool.name)).map((tool: { legacyId: string; category: string }) => [tool.legacyId, tool.category]),
    [['research-person-capture', 'research'], ['crm-person-upsert', 'crm']],
  )
})
