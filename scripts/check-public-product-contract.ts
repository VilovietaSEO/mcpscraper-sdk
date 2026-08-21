import { readFile } from 'node:fs/promises'

interface ToolContract {
  toolCount: number
  tools: Array<{ name: string; description?: string; inputSchema?: unknown; outputSchema?: unknown }>
}

function requireMatch(value: string, pattern: RegExp, label: string): void {
  if (!pattern.test(value)) throw new Error(`${label} is missing or stale (${pattern})`)
}

async function main(): Promise<void> {
  const manifest = JSON.parse(await readFile('contracts/mcp.tools.json', 'utf8')) as ToolContract
  if (manifest.toolCount !== 252 || manifest.tools.length !== 252) {
    throw new Error(`MCP inventory must contain 252 tools; received ${manifest.toolCount}/${manifest.tools.length}`)
  }

  const byName = new Map(manifest.tools.map(tool => [tool.name, tool]))
  requireMatch(byName.get('search_serp')?.description ?? '', /Costs 60 Credits per search\./, 'search_serp rate')
  requireMatch(byName.get('harvest_paa')?.description ?? '', /Costs 400 Credits per harvest plus 10 Credits per question/, 'harvest_paa rate')
  requireMatch(byName.get('capture_serp_snapshot')?.description ?? '', /Costs 60 Credits/, 'capture_serp_snapshot rate')

  const publicToolContract = JSON.stringify(manifest.tools)
  if (/bright\s*data|brightdata|\bkernel(?:\.sh)?\b|\bnango\b/i.test(publicToolContract)) {
    throw new Error('Public MCP tool descriptions or schemas expose an infrastructure vendor')
  }

  const openapi = await readFile('contracts/scraper.openapi.yaml', 'utf8')
  requireMatch(openapi, /pure organic-results\/SERP call \(60 Credits\)/, 'REST SERP rate')
  requireMatch(openapi, /400 Credit base \+ 10 Credits per question actually returned/, 'REST PAA rate')
  requireMatch(openapi, /unit_amount_usd: \{ type: number, enum: \[5\] \}/, 'concurrency pack monthly price')
  requireMatch(openapi, /slots_per_pack: \{ type: integer, enum: \[2\] \}/, 'concurrency pack slot count')
  requireMatch(openapi, /PublicErrorEnvelope:/, 'public error envelope')

  const docs = await Promise.all([
    'README.md',
    'packages/cli/README.md',
    'packages/scraper/README.md',
    'packages/scraper-python/README.md',
    'docs/curl-tools.md',
  ].map(async path => ({ path, text: await readFile(path, 'utf8') })))

  const toolCountPattern = new RegExp(String(manifest.toolCount))
  for (const { path, text } of docs) {
    requireMatch(text, toolCountPattern, `${path} inventory`)
  }
  for (const { path, text } of docs.filter(entry => entry.path !== 'docs/curl-tools.md')) {
    requireMatch(text, /60 Credits/, `${path} SERP rate`)
    requireMatch(text, /400 Credits/, `${path} PAA base rate`)
    requireMatch(text, /10 Credits per (?:returned )?question/, `${path} PAA question rate`)
    requireMatch(text, /two (?:browser slots|extra browser slots)|two-browser/i, `${path} concurrency pack size`)
    requireMatch(text, /\$5(?:\/month| per month)/, `${path} concurrency pack price`)
  }

  console.log(`Public product contract matches ${manifest.toolCount} tools, current SERP/PAA rates, two-slot packs, and vendor-neutral error schemas.`)
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
