# mcpscraper-sdk

Official TypeScript/JavaScript client for the [mcpscraper.dev](https://mcpscraper.dev) REST API — SERP search, People-Also-Ask harvesting, single-page and whole-site extraction, YouTube, Facebook/Google Ads Transparency, Instagram, Reddit, video breakdown, Google Maps, and directory/rank-tracking workflows.

This is a thin HTTP client generated against [`../../contracts/scraper.openapi.yaml`](../../contracts/scraper.openapi.yaml), the public contract for the hosted API. It contains no scraping, proxy, or billing logic — only typed request/response plumbing.

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
- `err.isConcurrencyLimitExceeded()` — narrows `err.body` to `{ active, limit, retryable, ... }`.

## API surface

`client.tools` is the generated, typed 166-tool MCP surface. It includes 77 MCP Scraper tools and all 89 mirrored memory tools from `contracts/mcp.tools.json`.

For multimodal results such as `meta_ad_creative_media`, call `client.tools.callToolResult(...)` to preserve native MCP image/audio/resource blocks. `callTool(...)` remains backward-compatible and returns the parsed structured or text value.

```ts
await client.tools.search.searchSerp({ query: 'roof repair Denver' })
await client.tools.memory.search({ query: 'roofing warranty terms' })
await client.tools.connections.exportConnectedServiceData({
  connectionId: 'conn_123',
  dataset: 'resend_data',
  lastDays: 7,
})
```

The connected-data export performs bounded Gmail, Calendar, Google Search Console, Zoom, Meta Marketing, or Resend pagination server-side and returns small results inline or a private seven-day JSONL artifact. Use `exportConnectedServiceData({ dataset: 'search_console_performance' })` for a fresh Search Console API extract. A scheduled `connection_sync` maintains a typed `gsc_performance_*` table exposed as `listServiceConnections().tableName`; use `exportSearchConsoleTableData` for a server-filtered download from that persisted table. Use `meta_ads_insights` for daily account, campaign, ad-set, and ad reporting across connected Meta ad accounts. Resend can aggregate sent/received mail, logs, contacts, broadcasts, and templates with `resend_data`. Resume partial exports with the returned `continuation` object; renew an expired signed URL with `client.tools.connections.renewConnectedDataDownload({ artifactId })`. Use `listServiceConnections` for verified grants and per-tool permission blockers, then `describeServiceConnectionTool` for the exact provider-native schema before calling through the generic connection bridges.

Search Console also provides six API-only batches through those connection bridges: reads `inspect-urls` and `query-search-analytics-batch`, and gated actions `add-sites-batch`, `submit-sitemaps-batch`, `delete-sites-batch`, and `delete-sitemaps-batch`. They require no database, return per-item receipts, and can be bound to scheduled agent runs. Delete batches default to dry-run and require the live schema's exact confirmation token for execution; all actions require the connection's action switch.

Integrations are included with an active Starter plan or higher: OAuth connect/reconnect and direct connected-service reads, approved actions, exports, and snapshots do not currently have an extra connection-operation debit. Scheduled Actions use the shared Credit balance at 75 Credits per started occurrence; agent-mode runs also add 1.5 times OpenRouter's actual reported model cost. Inspect the live policy with `await client.tools.schedule.getScheduleStatus()`.

Core operations are flat on the client: `searchSerp`, `harvestPaa`, `extractUrl`, `mapSiteUrls`, `extractSite`, `auditSite`, `getExtractSiteStatus`, `listJobs`, `getJob`, `getHistory`, `getLedger`.

Everything else is namespaced by product area, matching the OpenAPI spec's tags: `client.youtube`, `client.screenshot`, `client.facebook`, `client.googleAds`, `client.instagram`, `client.reddit`, `client.video`, `client.maps`, `client.directory`, `client.serpIntelligence`, `client.workflows`.

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

`client.memoryTools` exposes every tool from [`mcpscraper-memory-sdk`](../memory) — access/keys, channels, memory search/CRUD, tables, vaults, facts, schedule, webhooks, video — dispatched through `POST /memory/mcp-call` with your mcpscraper.dev API key. No separate memory key needed; a memory identity is auto-provisioned for your account on first use:

```ts
const hits = await client.memoryTools.memory.search({ query: 'competitor pricing pages' })
const vaults = await client.memoryTools.vaults.listVaults({})
```

Use `mcpscraper-memory-sdk`'s own `MemoryClient` instead if you already have a dedicated `mk_...` memory key and want to talk to `memory.mcpscraper.dev` directly.

## Regenerating types

`src/schema.ts` is generated from the OpenAPI spec and checked in. After editing `../../contracts/scraper.openapi.yaml`, regenerate with:

```bash
npm run generate
```

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-memory-sdk`](../memory) (Node, full 89-tool typed surface) · [`mcpscraper-sdk` on PyPI](https://pypi.org/project/mcpscraper-sdk/) · [`mcpscraper-cli`](../cli)
