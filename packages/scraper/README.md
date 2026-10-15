# mcpscraper-sdk

Official TypeScript/JavaScript client for the [mcpscraper.dev](https://mcpscraper.dev) REST API — SERP search, People-Also-Ask harvesting, single-page and whole-site extraction, YouTube, Facebook/Google Ads Transparency, Instagram, Reddit, video breakdown, Google Maps, and directory/rank-tracking workflows.

[Release history](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/main/CHANGELOG.md)

This is a thin HTTP client generated against [`../../contracts/scraper.openapi.generated.json`](../../contracts/scraper.openapi.generated.json), the complete public REST contract for the hosted API. It contains no scraping, proxy, or billing logic — only typed request/response plumbing.

## Install

```bash
npm install mcpscraper-sdk
```

## Usage

```ts
import { ScraperClient, ScraperApiError } from 'mcpscraper-sdk'

const client = new ScraperClient({ apiKey: process.env.MCPSCRAPER_API_KEY! })

const serp = await client.searchSerp({ query: 'roof repair Denver' })

try {
  const places = await client.maps.search({ query: 'roofers', location: 'Denver, CO' })
  console.log(places)
} catch (err) {
  if (err instanceof ScraperApiError && err.isInsufficientBalance()) {
    console.error(`Need ${err.body.required_credits} credits, have ${err.body.balance_credits}. Top up: ${err.body.topup_url}`)
  } else {
    throw err
  }
}
```

## Errors

Every non-2xx response throws a `ScraperApiError` with `status`, `code`, and the raw response `body`. Two cases have typed narrowing helpers:

- `err.isInsufficientBalance()` — narrows `err.body` to `{ balance_credits, required_credits, topup_url, ... }`.
- `err.isConcurrencyLimitExceeded()` — narrows `err.body` to `{ active, limit, retryable, upgrade, ... }`.
- `err.isVerificationChallenge()` / `err.isTimeout()` — preserve actionable, vendor-neutral retry and charge details returned by the service.

Google Search light mode returns organic positions, URLs, titles, and descriptions for 20 Credits per delivered SERP page, or 35 Credits when the backup supplies the result. One-page full mode adds available same-page SERP features for 35 Credits. Both modes default to one page; an unfiltered two-page search costs 40 Credits when the normal provider returns both pages. Past-week and past-month searches use a managed browser for organic results at 35 Credits per delivered page. Unfiltered light searches try the primary path twice, then one API fallback; an unfiltered one-page full search uses the feature-capable API directly. If page 2 cannot be delivered, an available page 1 is returned as partial and billed at the one-page rate. A 35-Credit-per-requested-page hold is settled after delivery. PAA costs 400 Credits plus 10 Credits per returned question. One optional concurrency pack adds two browser slots for $5/month; quantity `n` adds `2n` slots for `$5n` without changing the base plan.

## API surface

`client.tools` is the generated, typed manifest-backed MCP surface from `contracts/mcp.tools.json`, including provider-neutral X-Ray surveys, attribution-impact reporting, and truthful evidence-status operations.

For multimodal results such as `meta_ad_creative_media`, call `client.tools.callToolResult(...)` to preserve native MCP image/audio/resource blocks. `callTool(...)` remains backward-compatible and returns the parsed structured or text value.

```ts
await client.tools.search.searchSerp({ query: 'roof repair Denver' })
await client.tools.web.archiveRead({
  url: 'https://github.com/octocat/Hello-World/archive/refs/heads/master.zip',
  path: 'Hello-World-master/README',
})
const method = await client.tools.editorial.readingRoomGuide({ focus: 'workflow' })
await client.tools.memory.search({ query: 'roofing warranty terms' })
await client.tools.connections.exportConnectedServiceData({
  connectionId: 'conn_123',
  dataset: 'resend_data',
  lastDays: 7,
})
const templates = await client.tools.artifacts.listArtifactTemplates({ status: 'active' })
```

Lead enrichment is available through the same generated surface. Supply mapped rows directly, or call `client.tools.leads.import(...)` first for CSV/TSV/XLSX input:

```ts
const job = await client.tools.leads.enrich({
  idempotencyKey: crypto.randomUUID(),
  source: { kind: 'rows', rows: [{ Business: 'White Rock Roofing', City: 'Dallas', Website: 'https://roofwhiterock.com' }] },
  columnMap: { name: 'Business', city: 'City', websiteUrl: 'Website' },
  defaultEntityType: 'business',
  emailSearchFallback: 'serp_snippets',
  peopleDiscovery: 'owners',
  peopleQueryTemplates: ['{business} owner of company {city}', '{business} founder {city}'],
  outputFormats: ['csv', 'xlsx'],
})
```

The connected-data export performs bounded Gmail, Calendar, Google Search Console, Zoom, Meta Marketing, or Resend pagination server-side and returns small results inline or a private seven-day JSONL artifact. Use `exportConnectedServiceData({ dataset: 'search_console_performance' })` for a fresh Search Console API extract. Existing persisted Search Console data is exposed as `listServiceConnections().tableName`; use `exportSearchConsoleTableData` for a server-filtered download from that table. Use `meta_ads_insights` for daily account, campaign, ad-set, and ad reporting across connected Meta ad accounts. Resend can aggregate sent/received mail, logs, contacts, broadcasts, and templates with `resend_data`. Resume partial exports with the returned `continuation` object; renew an expired signed URL with `client.tools.connections.renewConnectedDataDownload({ artifactId })`. Use `listServiceConnections` for verified grants and per-tool permission blockers, then `describeServiceConnectionTool` for the exact provider-native schema before calling through the generic connection bridges.

Search Console also provides six API-only batches through those connection bridges: reads `inspect-urls` and `query-search-analytics-batch`, and gated actions `add-sites-batch`, `submit-sitemaps-batch`, `delete-sites-batch`, and `delete-sitemaps-batch`. They require no database and return per-item receipts. Delete batches default to dry-run and require the live schema's exact confirmation token for execution; all actions require the connection's action switch.

Integrations are included with an active Starter plan or higher: OAuth connect/reconnect and direct connected-service reads, approved actions, exports, and snapshots do not currently have an extra connection-operation debit.

Core operations are flat on the client: `startHarvest`, `searchSerp`, `harvestPaa`, `extractUrl`, `mapSiteUrls`, `extractSite`, `auditSite`, `getExtractSiteStatus`, `archiveRead`, `listJobs`, `getJob`, `getHistory`, `getLedger`.

For a durable PAA harvest, `client.tools.other.harvestPaaStart` accepts
`pages: 1 | 2` and defaults to one. Two pages add page-two organic results when
available while expanding only the preserved page-one PAA graph. Poll the same
`jobId` with `harvestPaaStatus`; its `progress.pagination` and
`result.pagination` are nullable for older saved jobs. The complete workflow is
in [`../../examples/paa-two-page.mjs`](../../examples/paa-two-page.mjs).

### Durable acquisition

Long-running agents can start SERP work once and poll the provider-owned job
instead of holding one synchronous request open:

```ts
const started = await client.startHarvest({
  query: 'roofers dallas',
  location: 'Dallas, TX',
  serpOnly: true,
})

let job
do {
  await new Promise(resolve => setTimeout(resolve, 2_000))
  job = await client.getJob(started.job_id, { timeoutMs: 30_000 })
} while (job.status === 'pending' || job.status === 'running')

if (job.status !== 'done') throw new Error(job.error ?? `Harvest ${job.status}`)
console.log(job.result)
```

Background site extraction accepts a caller-owned idempotency key, and the
archive reader exposes the resulting ZIP without switching to the MCP surface:

```ts
const crawl = await client.extractSite(
  { url: 'https://example.com', background: true, formats: ['markdown', 'links', 'json'] },
  { idempotencyKey: 'foundation-run-123:crawl', timeoutMs: 30_000 },
)

const status = await client.getExtractSiteStatus(crawl.jobId)
const bundle = status.artifacts?.find(artifact => artifact.contentType === 'application/zip')
if (bundle?.downloadUrl) {
  const pages = await client.archiveRead({ url: bundle.downloadUrl, path: 'pages.jsonl' })
  const pageCorpus = await client.archiveRead({
    url: bundle.downloadUrl,
    pathPrefix: 'pages/',
    maxEntries: 1000,
    maxTotalBytes: 20_000_000,
  })
  console.log(pages.content)
}
```

Everything else is namespaced by product area, matching the OpenAPI spec's tags: `client.youtube`, `client.screenshot`, `client.facebook`, `client.googleAds`, `client.instagram`, `client.reddit`, `client.video`, `client.maps`, `client.directory`, `client.serpIntelligence`, `client.workflows`, `client.gmail`. The REST Gmail namespace preserves opaque path handles and requires explicit idempotency keys for mutations; the generated `client.tools.connections.gmail*` methods expose the exact MCP input/output contracts.

### Retry-safe SERP Intelligence captures

Pass a stable idempotency key when a capture may be retried. The regular method continues to return the response body; `captureWithReceipt` also returns the key accepted or generated by the server so it can be reused after a timeout or uncertain response:

```ts
const result = await client.serpIntelligence.capture(
  { query: 'roofers near me' },
  { idempotencyKey: 'serp-run-2026-07-14-001' },
)

const receipt = await client.serpIntelligence.captureWithReceipt({ query: 'roofers near me' })
console.log(receipt.data.billing.creditsUsed, receipt.idempotencyKey)
```

Reusing a key with the same body recovers the original debit and settlement. Reusing it with a different body throws `ScraperApiError` with status `409` and code `idempotency_conflict`.

## Scrape → memory vault

`extractUrl` accepts `depositToVault: true` (optionally with `vaultName`) to embed the full scraped body server-side into your mcp-memory vault instead of returning it inline — the response's `memory` field reports `{ deposited, vault, noteId, path, chunks }` (or falls back to a temporary `fileUrl` download if the vault deposit itself fails):

```ts
const page = await client.extractUrl({ url: 'https://example.com/pricing', depositToVault: true, vaultName: 'competitors' })
console.log(page.memory) // { deposited: true, vault: 'competitors', noteId: '...', path: '...', chunks: 4 }
```

## Memory tools, using only this API key

`client.memoryTools` exposes every tool from [`mcpscraper-memory-sdk`](../memory) — access/keys, channels, memory search/CRUD, tables, vaults, facts, artifacts, webhooks, video — dispatched through `POST /memory/mcp-call` with your mcpscraper.dev API key. No separate memory key needed; a memory identity is auto-provisioned for your account on first use:

```ts
const hits = await client.memoryTools.memory.search({ query: 'competitor pricing pages' })
const vaults = await client.memoryTools.vaults.listVaults({})
```

Use `mcpscraper-memory-sdk`'s `MemoryClient` when you prefer its Memory-first namespaces; it uses the same MCP Scraper key and root endpoint.

## Regenerating types

`src/schema.ts` is generated from the complete OpenAPI projection and checked in. For server-owned Maps search and directory routes, update `contracts/server-rest.v1.json` from the server artifact. Other public routes remain in the curated `contracts/scraper.openapi.yaml` base. Regenerate both language models from the repository root:

```bash
npm run generate:rest
npm run verify:rest-contract
```

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-memory-sdk`](../memory) (Node, full 121-tool direct-memory surface) · [`mcpscraper-sdk` on PyPI](https://pypi.org/project/mcpscraper-sdk/) · [`mcpscraper-cli`](../cli)

Durable PAA harvests should wait at least 20 seconds between status checks and honor a longer returned polling interval. Keep the same job ID and retry key while the original work is running.

Release changes: [SDK 0.54.1 release notes](https://github.com/VilovietaSEO/mcpscraper-sdk/releases/tag/v0.54.1).

## Client attribution and full results

Clients accept `clientAttribution: { installChannel?, aiClient?, aiModel? }` and default to calling surface `sdk`. Set only known caller labels; unspecified labels stay unknown. `onResponse({ requestId, status })` receives per-response correlation without changing results, and errors keep their own `requestId`. These options also apply to `McpToolsClient` and `MemoryClient`; labels are reporting declarations, not authorization.

Large tool outputs may be delivery envelopes instead of inline domain values. Preserve `delivery`, `scope` and `recovery`, then use `tools.artifacts.describe`, `readRetained` (follow `nextOffset` to null), or `download` with the returned artifact ID. The legacy `artifacts.read` method remains the report reader. `callToolResult` preserves native content/resource links. Download URL expiry differs from artifact retention; renew a URL through `download` without rerunning acquisition. Use the returned capability for binary files.
