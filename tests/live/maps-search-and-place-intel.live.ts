import { writeFileSync } from 'node:fs'
import { ScraperClient } from '../../packages/scraper/dist/index.js'

type Loose = Record<string, unknown>

const query = process.argv[2] ?? 'plumber'
const location = process.argv[3] ?? 'Seattle, WA'
const maxResults = Number(process.argv[4] ?? 30)
const hydrateCount = Number(process.argv[5] ?? 2)
const evidencePath = process.env.MAPS_TEST_EVIDENCE ?? './maps-capability-evidence.json'

const str = (v: unknown): string | null => (typeof v === 'string' && v.trim() ? v : null)
const num = (v: unknown): number | null => (typeof v === 'number' && Number.isFinite(v) ? v : null)

function tokens(name: string): string[] {
  return name.toLowerCase().replace(/[^a-z0-9\s]/g, ' ').split(/\s+/).filter(t => t.length > 2)
}

function nameMatches(requested: string, returned: string | null): boolean {
  if (!returned) return false
  const returnedSet = new Set(tokens(returned))
  const requestedTokens = tokens(requested)
  const hits = requestedTokens.filter(t => returnedSet.has(t)).length
  return requestedTokens.length > 0 && hits / requestedTokens.length >= 0.5
}

async function main(): Promise<void> {
  const apiKey = process.env.MCP_SCRAPER_API_KEY
  if (!apiKey) throw new Error('MCP_SCRAPER_API_KEY is required')
  const client = new ScraperClient({ apiKey })

  const estCredits = 5 + hydrateCount * 60
  console.log(`maps capability test — "${query}" in "${location}", ${maxResults} results, hydrating top ${hydrateCount}`)
  console.log(`estimated cost: ~${estCredits} credits\n`)

  console.log('GATE 1 — ranked list (maps.search)')
  const startedSearch = Date.now()
  const search = (await client.maps.search({ query, location, maxResults })) as Loose
  const searchMs = Date.now() - startedSearch
  const results = (Array.isArray(search.results) ? search.results : []) as Loose[]

  const listFields: Array<[string, (r: Loose) => boolean]> = [
    ['name', r => Boolean(str(r.name))],
    ['cid', r => Boolean(str(r.cidDecimal) ?? str(r.cid))],
    ['rating', r => Boolean(str(r.rating))],
    ['reviewCount', r => Boolean(str(r.reviewCount))],
    ['address', r => Boolean(str(r.address))],
    ['phone', r => Boolean(str(r.phone))],
    ['category', r => Boolean(str(r.category))],
    ['websiteUrl', r => Boolean(str(r.websiteUrl))],
  ]
  const coverage: Record<string, string> = {}
  for (const [field, has] of listFields) {
    const n = results.filter(has).length
    coverage[field] = `${n}/${results.length}`
  }
  const positions = results.map(r => num(r.position)).filter((p): p is number => p !== null)
  const positionsOrdered = positions.every((p, i) => i === 0 || p > (positions[i - 1] as number))

  console.log(`  returned ${results.length}/${maxResults} in ${(searchMs / 1000).toFixed(1)}s, positions ordered: ${positionsOrdered}`)
  console.log(`  field coverage: ${JSON.stringify(coverage)}\n`)

  console.log(`GATE 2 — hydration (maps.place, includeServices) on top ${hydrateCount}`)
  const hydrations: Loose[] = []
  for (const target of results.slice(0, hydrateCount)) {
    const businessName = str(target.name) ?? ''
    const startedPlace = Date.now()
    let place: Loose
    try {
      place = (await client.maps.place({ businessName, location, includeServices: true })) as Loose
    } catch (err) {
      const message = err instanceof Error ? err.message : String(err)
      hydrations.push({ requested: businessName, error: message })
      console.log(`  ${businessName}: FAILED — ${message}`)
      continue
    }
    const summary = {
      requested: businessName,
      returnedName: str(place.name),
      nameMatch: nameMatches(businessName, str(place.name)),
      cid: Boolean(str(place.cidDecimal)),
      kgmid: Boolean(str(place.kgmid)),
      latLng: num(place.lat) !== null && num(place.lng) !== null,
      address: Boolean(str(place.address)),
      phone: Boolean(str(place.phone)),
      website: Boolean(str(place.website)),
      reviewCount: str(place.reviewCount),
      servicesStatus: str(place.servicesStatus),
      servicesCount: Array.isArray(place.services) ? place.services.length : 0,
      areasServedCount: Array.isArray(place.areasServed) ? place.areasServed.length : 0,
      durationMs: Date.now() - startedPlace,
    }
    hydrations.push({ ...summary, raw: place })
    console.log(`  ${businessName}: match=${summary.nameMatch} cid=${summary.cid} kgmid=${summary.kgmid} latlng=${summary.latLng} services=${summary.servicesStatus}(${summary.servicesCount}) areas=${summary.areasServedCount} ${(summary.durationMs / 1000).toFixed(1)}s`)
  }

  const hydrated = hydrations.filter(h => !h.error)
  const servicesCollected = hydrated.filter(h => h.servicesStatus === 'collected').length
  const nameMismatches = hydrated.filter(h => h.nameMatch === false).length

  console.log('\nVERDICT')
  const verdictLines = [
    `list: ${results.length}/${maxResults} results, ordered=${positionsOrdered}`,
    `hydration: ${hydrated.length}/${hydrateCount} succeeded, name mismatches: ${nameMismatches}`,
    `identifiers (cid/kgmid/latlng): ${hydrated.filter(h => h.cid && h.kgmid && h.latLng).length}/${hydrated.length}`,
    `services hop: ${servicesCollected}/${hydrated.length} collected${servicesCollected === 0 && hydrated.length > 0 ? '  << REGRESSION: SERP services hop returning unavailable' : ''}`,
    `email: not available from any Google Maps surface (requires website scrape)`,
  ]
  for (const line of verdictLines) console.log(`  ${line}`)

  writeFileSync(evidencePath, JSON.stringify({
    ranAt: new Date().toISOString(),
    input: { query, location, maxResults, hydrateCount },
    estCredits,
    gate1: { searchMs, returned: results.length, positionsOrdered, coverage, results },
    gate2: hydrations,
    verdict: verdictLines,
  }, null, 2))
  console.log(`\nevidence written to ${evidencePath}`)

  if (results.length === 0) process.exitCode = 1
}

main().catch(err => {
  console.error(err instanceof Error ? err.message : String(err))
  process.exitCode = 1
})
