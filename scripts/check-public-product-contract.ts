import { createHash } from 'node:crypto'
import { readFile } from 'node:fs/promises'

interface ToolContract {
  toolCount: number
  tools: Array<{ name: string; description?: string; inputSchema?: unknown; outputSchema?: unknown }>
}

function requireMatch(value: string, pattern: RegExp, label: string): void {
  if (!pattern.test(value)) throw new Error(`${label} is missing or stale (${pattern})`)
}

const WITHHELD_TERM_DIGESTS = new Set([
  '6013857c6e7c9f0260885e487f775b1447c101076bd0b16957ff390a891ce703',
  'd5dd4c3ebd80327ddddfc8d9064770c994b4e9361dcb160fffda3021ed967ee3',
  '6923dd1bc0460082c5d55a831908c24a282860b7f1cd6c2b79cf1bc8857c639c',
  '192eb9b224e1d5d3a1973afe17cf237d40c849ec90ed40da243e1745197fa003',
  '229caf1f31e73aa2a2bfadc3f708dfb6d48d0e1d2efbb9261d87c700d856b06e',
  '954f775230679543d69509c294e19c393d50202fce576bcad71ac6add7b819d7',
  '92507c3cfb77dc2812aa6a5a378cb0f72e199e0469e939f5a0cac3408a83e7c8',
  '270e2b2706ef33ac7bef60d32caf763496210c962c89a82c66ed9e5a3226a148',
  '232bdfc7ffb8845e02596f9b7ca691b995295785287772b13f2543a670c9c87e',
])

function namesWithheldTerm(text: string): boolean {
  const words = text.toLowerCase().split(/[^a-z0-9]+/).filter(Boolean)
  const digest = (value: string) => createHash('sha256').update(value).digest('hex')
  return words.some((word, index) =>
    WITHHELD_TERM_DIGESTS.has(digest(word)) || (index > 0 && WITHHELD_TERM_DIGESTS.has(digest(`${words[index - 1]} ${word}`))))
}

async function main(): Promise<void> {
  const manifest = JSON.parse(await readFile('contracts/mcp.tools.json', 'utf8')) as ToolContract
  if (manifest.toolCount !== manifest.tools.length) {
    throw new Error(`MCP inventory count mismatch: declared ${manifest.toolCount}, received ${manifest.tools.length}`)
  }

  const byName = new Map(manifest.tools.map(tool => [tool.name, tool]))
  requireMatch(byName.get('search_serp')?.description ?? '', /Light costs 20 Credits per delivered page \(35 with fallback\); one-page full costs 45 \(when featureCompletion is pending[\s\S]*charged as light\); a date-filtered search costs 150; two-page full costs 40/i, 'search_serp mode rates')
  requireMatch(byName.get('search_serp')?.description ?? '', /Default light mode returns one organic-results page[\s\S]*Set pages:2 only when two pages are requested/, 'search_serp page default')
  requireMatch(byName.get('search_serp')?.description ?? '', /Date filters \(recency:week\/month\) and saved serpIdentity require one page/, 'search_serp two-page restrictions')
  requireMatch(byName.get('search_serp')?.description ?? '', /organic results only, no backup provider/, 'search_serp two-page routing')
  requireMatch(byName.get('harvest_paa')?.description ?? '', /Costs 500 Credits per harvest plus 35 Credits per question/, 'harvest_paa rate')
  requireMatch(byName.get('capture_serp_snapshot')?.description ?? '', /Costs 60 Credits/, 'capture_serp_snapshot rate')
  requireMatch(byName.get('maps_place_intel')?.description ?? '', /Costs 60 Credits plus 1 per saved review; 600 plus reviews when requested photos, services or a menu arrive\. If none of them can be collected, the 60-Credit price applies/, 'maps_place_intel rate')
  requireMatch(byName.get('maps_search')?.description ?? '', /Costs 5 Credits per search; includeServices adds 200 Credits for each business whose profile is opened[\s\S]*plain list is returned with profileDetailsStatus:unavailable for the 5-Credit price/, 'maps_search rate')

  const publicToolContract = JSON.stringify(manifest.tools)
  if (namesWithheldTerm(publicToolContract)) {
    throw new Error('Public MCP tool descriptions or schemas expose an infrastructure vendor')
  }

  const openapi = await readFile('contracts/scraper.openapi.yaml', 'utf8')
  requireMatch(openapi, /Full mode adds\s+available same-page SERP features for 45 Credits/, 'REST SERP mode rate')
  requireMatch(openapi, /500 Credit base \+ 35 Credits per question actually returned/, 'REST PAA rate')
  requireMatch(openapi, /600 credits plus reviews when photos or services are requested/, 'REST Maps place rate')
  requireMatch(openapi, /unit_amount_usd: \{ type: number, enum: \[5\] \}/, 'concurrency pack monthly price')
  requireMatch(openapi, /slots_per_pack: \{ type: integer, enum: \[2\] \}/, 'concurrency pack slot count')
  requireMatch(openapi, /PublicErrorEnvelope:/, 'public error envelope')
  const generatedOpenApi = JSON.parse(await readFile('contracts/scraper.openapi.generated.json', 'utf8')) as {
    components: { schemas: { PublicErrorEnvelope: { properties: {
      error_code: { enum: string[] }; error_type: { enum: string[] }
    } } } }
  }
  if (!generatedOpenApi.components.schemas.PublicErrorEnvelope.properties.error_code.enum.includes('directory_job_not_found')) {
    throw new Error('Generated REST error codes omit directory_job_not_found')
  }
  if (!generatedOpenApi.components.schemas.PublicErrorEnvelope.properties.error_type.enum.includes('not_found')) {
    throw new Error('Generated REST error types omit not_found')
  }

  const docs = await Promise.all([
    'README.md',
    'packages/cli/README.md',
    'packages/scraper/README.md',
    'packages/scraper-python/README.md',
    'docs/curl-tools.md',
  ].map(async path => ({ path, text: await readFile(path, 'utf8') })))

  const catalog = docs.find(entry => entry.path === 'docs/curl-tools.md')!
  requireMatch(catalog.text, new RegExp(String(manifest.toolCount)), `${catalog.path} inventory`)
  for (const { path, text } of docs.filter(entry => entry.path !== 'docs/curl-tools.md')) {
    requireMatch(text, /unified MCP|manifest-backed MCP/i, `${path} generated inventory guidance`)
  }
  for (const { path, text } of docs.filter(entry => entry.path !== 'docs/curl-tools.md')) {
    requireMatch(text, /20 Credits per delivered SERP page/, `${path} SERP rate`)
    requireMatch(text, /500 Credits/, `${path} PAA base rate`)
    requireMatch(text, /35 Credits per (?:returned )?question/, `${path} PAA question rate`)
    requireMatch(text, /two (?:browser slots|extra browser slots)|two-browser/i, `${path} concurrency pack size`)
    requireMatch(text, /\$5(?:\/month| per month)/, `${path} concurrency pack price`)
  }

  console.log(`Public product contract matches ${manifest.toolCount} tools, current SERP/PAA rates, two-slot packs, and vendor-neutral error schemas.`)
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
