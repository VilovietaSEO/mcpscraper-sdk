import { readFile } from 'node:fs/promises'
import { join } from 'node:path'
import * as memorySdk from '../packages/memory/src/index.js'
import * as scraperSdk from '../packages/scraper/src/index.js'
import { MCP_TOOL_CATALOG } from '../packages/cli/src/generated-tools.js'

const EXPECTED = 159

function namesFromBindings(bindings: ReadonlyArray<{ name: string }>): string[] {
  return bindings.map(binding => binding.name).sort()
}

function assertExact(label: string, actualNames: string[], expectedNames: string[]): void {
  const actual = [...new Set(actualNames)].sort()
  const expected = [...new Set(expectedNames)].sort()
  const actualSet = new Set(actual)
  const expectedSet = new Set(expected)
  const missing = expected.filter(name => !actualSet.has(name))
  const extra = actual.filter(name => !expectedSet.has(name))
  if (actual.length !== EXPECTED || missing.length || extra.length) {
    throw new Error(`${label} parity failed: count=${actual.length}, missing=${missing.join(',')}, extra=${extra.join(',')}`)
  }
  console.log(`${label}: ${actual.length}/${EXPECTED}`)
}

function assertBindings(
  label: string,
  actual: ReadonlyArray<{ name: string; category: string; methodName: string }>,
  expected: ReadonlyArray<{ name: string; category: string; methodName: string }>,
): void {
  assertExact(label, namesFromBindings(actual), expected.map(binding => binding.name))
  const expectedByName = new Map(expected.map(binding => [binding.name, `${binding.category}.${binding.methodName}`]))
  const drift = actual
    .filter(binding => expectedByName.get(binding.name) !== `${binding.category}.${binding.methodName}`)
    .map(binding => binding.name)
  if (drift.length) throw new Error(`${label} namespace/method drift: ${drift.join(',')}`)
}

async function main(): Promise<void> {
  const root = join(import.meta.dirname, '..')
  const manifest = JSON.parse(await readFile(join(root, 'contracts/mcp.tools.json'), 'utf8')) as {
    toolCount: number
    tools: Array<{ name: string; category: string; methodName: string; outputSchema?: Record<string, unknown> }>
  }
  if (manifest.toolCount !== EXPECTED || manifest.tools.length !== EXPECTED) {
    throw new Error(`Manifest count is ${manifest.tools.length}, expected ${EXPECTED}`)
  }
  const missingOutputSchemas = manifest.tools.filter(tool => tool.outputSchema?.type !== 'object').map(tool => tool.name)
  if (missingOutputSchemas.length) {
    throw new Error(`Manifest tools missing output schemas: ${missingOutputSchemas.join(',')}`)
  }
  const expectedNames = manifest.tools.map(tool => tool.name).sort()
  assertBindings('Node memory package', memorySdk.MCP_TOOL_BINDINGS, manifest.tools)
  assertBindings('Node scraper package', scraperSdk.MCP_TOOL_BINDINGS, manifest.tools)
  assertExact('CLI catalog', MCP_TOOL_CATALOG.map(tool => tool.name), expectedNames)
  const expectedCategories = new Map(manifest.tools.map(tool => [tool.name, tool.category]))
  const cliCategoryDrift = MCP_TOOL_CATALOG
    .filter(tool => expectedCategories.get(tool.name) !== tool.category)
    .map(tool => tool.name)
  if (cliCategoryDrift.length) throw new Error(`CLI category drift: ${cliCategoryDrift.join(',')}`)

  const curlDoc = await readFile(join(root, 'docs/curl-tools.md'), 'utf8')
  const curlNames = [...curlDoc.matchAll(/^- `([^`]+)` —/gm)].map(match => match[1])
  assertExact('cURL catalog', curlNames, expectedNames)
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
