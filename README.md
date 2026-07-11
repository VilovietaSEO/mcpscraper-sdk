# mcpscraper-sdk

Official client libraries for [mcpscraper.dev](https://mcpscraper.dev) (web intelligence: SERP/PAA research, single-page and whole-site extraction, YouTube, Facebook/Google Ads Transparency, Instagram, Reddit, video breakdown, Google Maps, and directory/rank-tracking workflows) and [memory.mcpscraper.dev](https://memory.mcpscraper.dev) (hosted per-user memory: governed capture, tags, graph traversal, search, vaults, tables, scheduled actions, and more — 86 tools).

These are thin HTTP/JSON-RPC clients — they call the same hosted APIs that back the `mcp-scraper` and `mcpscraper-memory` MCP servers. No scraping, proxy, or billing logic lives in this repo; it's typed request/response plumbing only, licensed MIT. All **153 unified MCP tools** are available through **Node.js**, **Python**, **cURL**, and the **CLI** from one generated contract.

## Install

| | Package | Install |
|---|---|---|
| Node.js — scraper | [`mcpscraper-sdk`](./packages/scraper) | `npm install mcpscraper-sdk` |
| Node.js — memory | [`mcpscraper-memory-sdk`](./packages/memory) | `npm install mcpscraper-memory-sdk` |
| Python — scraper | [`mcpscraper-sdk`](./packages/scraper-python) (source package) | `pip install "mcpscraper-sdk @ git+https://github.com/VilovietaSEO/mcpscraper-sdk.git#subdirectory=packages/scraper-python"` |
| Python — memory | [`mcpscraper-memory-sdk`](./packages/memory-python) (source package) | `pip install "mcpscraper-memory-sdk @ git+https://github.com/VilovietaSEO/mcpscraper-sdk.git#subdirectory=packages/memory-python"` |
| CLI | [`mcpscraper-cli`](./packages/cli) | `npm install -g mcpscraper-cli` |

## Getting an API key

- **mcpscraper.dev**: `npx -y -p mcp-scraper@latest mcp-scraper-cli billing concurrency info`, or the [account dashboard](https://mcpscraper.dev).
- **memory.mcpscraper.dev**: issued via the `issue-key` MCP tool, or the memory dashboard. You usually don't need a separate memory key at all — see [Memory, using only your scraper key](#memory-using-only-your-scraper-key) below.

## Feature overview

| Feature | What it does | REST endpoint | Cost |
|---|---|---|---|
| [Search](#search) | Google SERP + optional full People-Also-Ask harvest | `POST /harvest/sync` | ~0.1 credit |
| [Scrape](#scrape) | One page → markdown/HTML/headings, optional screenshot, optional deposit into your memory vault | `POST /extract-url` | 0.1 credit |
| [Crawl](#crawl) | Every page of a site, one call | `POST /extract-site` | 0.1 credit/page |
| [Map](#map) | Discover a site's full URL inventory | `POST /map-urls` | 0.5 credit flat |
| [Maps search](#maps-search) | Local businesses via Google Maps | `POST /maps/search` | — |
| [Memory search](#memory-search-using-only-your-scraper-key) | Semantic search across your mcp-memory vaults | `POST /memory/mcp-call` | — |
| YouTube, Facebook/Google Ads, Instagram, Reddit, video, directory workflows | See [`packages/scraper`](./packages/scraper) and [`contracts/scraper.openapi.yaml`](./contracts/scraper.openapi.yaml) for the full 43-operation REST contract | — | — |

Every example below runs the *same* operation four ways.

### Search

<details open><summary>Node.js</summary>

```ts
import { ScraperClient } from 'mcpscraper-sdk'

const client = new ScraperClient({ apiKey: process.env.MCPSCRAPER_API_KEY! })
const result = await client.searchSerp({ query: 'best roofing companies denver' })
```
</details>

<details><summary>Python</summary>

```python
from mcpscraper import ScraperClient

client = ScraperClient(api_key=os.environ["MCPSCRAPER_API_KEY"])
result = client.search_serp("best roofing companies denver")
```
</details>

<details><summary>cURL</summary>

```bash
curl -X POST https://mcpscraper.dev/harvest/sync \
  -H "x-api-key: $MCPSCRAPER_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":"best roofing companies denver","serpOnly":true}'
```
</details>

<details><summary>CLI</summary>

```bash
mcpscraper search "best roofing companies denver"
```
</details>

Sample output (real, captured live):

```json
{
  "job_id": "3cb54b8b-fbf3-438c-89a9-2cd9744004f0",
  "status": "done",
  "result": {
    "seed": "best roofing companies denver",
    "organicResults": [
      {
        "position": 1,
        "title": "TOP 10 BEST Roofing Companies in Denver, CO",
        "url": "https://www.yelp.com/search?find_desc=Roofing+Companies&find_loc=Denver%2C+CO",
        "domain": "yelp.com",
        "snippet": "Vivax Pros (497 reviews). Formula Roofing and Remodeling (168 reviews)...",
        "inlineRating": { "value": "4.5", "count": "(1,589)" }
      },
      {
        "position": 2,
        "title": "Recomendations for roofing company in Denver - ASAP",
        "url": "https://www.reddit.com/r/Denver/comments/1kh2gd3/...",
        "domain": "reddit.com",
        "snippet": "My neighbor used Alpaca and they did a good job..."
      }
    ]
  }
}
```

### Scrape

<details open><summary>Node.js</summary>

```ts
const page = await client.extractUrl({ url: 'https://mcpscraper.dev' })
```
</details>

<details><summary>Python</summary>

```python
page = client.extract_url("https://mcpscraper.dev")
```
</details>

<details><summary>cURL</summary>

```bash
curl -X POST https://mcpscraper.dev/extract-url \
  -H "x-api-key: $MCPSCRAPER_API_KEY" -H "Content-Type: application/json" \
  -d '{"url":"https://mcpscraper.dev"}'
```
</details>

<details><summary>CLI</summary>

```bash
mcpscraper scrape https://mcpscraper.dev
```
</details>

Sample output (real, captured live):

```json
{
  "title": "MCP Scraper — One Brain. Every AI You Use.",
  "bodyMarkdown": "Scraper · Memory · Scheduler — one account\n\n# One brain.\n_Every AI you use._\n\nSee what happens when you can get any data, have a brain, and schedule actions...",
  "headings": [
    { "level": 1, "text": "One brain. Every AI you use." },
    { "level": 2, "text": "It sees the whole web." },
    { "level": 2, "text": "It never starts from zero." }
  ]
}
```

Add `depositToVault: true` (Node: `extractUrl({ url, depositToVault: true, vaultName: 'research' })`, CLI: `--deposit-to-vault --vault research`) to save the full body server-side into your mcp-memory vault instead of returning it inline — the response gains a `memory` field: `{ deposited: true, vault: 'research', noteId, path, chunks }`.

### Crawl

<details open><summary>Node.js</summary>

```ts
const site = await client.extractSite({ url: 'https://example.com', maxPages: 100 })
```
</details>

<details><summary>Python</summary>

```python
site = client.extract_site("https://example.com", max_pages=100)
```
</details>

<details><summary>cURL</summary>

```bash
curl -X POST https://mcpscraper.dev/extract-site \
  -H "x-api-key: $MCPSCRAPER_API_KEY" -H "Content-Type: application/json" \
  -d '{"url":"https://example.com","maxPages":100}'
```
</details>

<details><summary>CLI</summary>

```bash
mcpscraper crawl https://example.com --max-pages 100
```
</details>

Above a few hundred pages, pass `background: true` (Node/Python) and poll `getExtractSiteStatus(id)` / `get_extract_site_status(job_id)` instead of waiting inline.

### Map

<details open><summary>Node.js</summary>

```ts
const { urls } = await client.mapSiteUrls({ url: 'https://example.com' })
```
</details>

<details><summary>Python</summary>

```python
result = client.map_site_urls("https://example.com")
```
</details>

<details><summary>cURL</summary>

```bash
curl -X POST https://mcpscraper.dev/map-urls \
  -H "x-api-key: $MCPSCRAPER_API_KEY" -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}'
```
</details>

<details><summary>CLI</summary>

```bash
mcpscraper map https://example.com
```
</details>

### Maps search

<details open><summary>Node.js</summary>

```ts
const places = await client.maps.search({ query: 'roofers', location: 'Denver, CO' })
```
</details>

<details><summary>Python</summary>

```python
places = client.maps.search({"query": "roofers", "location": "Denver, CO"})
```
</details>

<details><summary>cURL</summary>

```bash
curl -X POST https://mcpscraper.dev/maps/search \
  -H "x-api-key: $MCPSCRAPER_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":"roofers","location":"Denver, CO"}'
```
</details>

<details><summary>CLI</summary>

```bash
mcpscraper maps-search "roofers" --location "Denver, CO"
```
</details>

Sample output (real, captured live):

```json
{
  "query": "roofers",
  "location": "Denver, CO",
  "resultCount": 10,
  "results": [
    {
      "position": 1,
      "name": "Forest Roofs",
      "rating": "4.9",
      "category": "Roofing contractor",
      "address": "701 Birch Street",
      "phone": "(720) 766-9143",
      "hoursStatus": "Open",
      "websiteUrl": "http://www.forestroofs.com/"
    },
    {
      "position": 2,
      "name": "Mike & Sons Roofing",
      "rating": "4.8",
      "category": "Roofing contractor",
      "address": "3033 E 1st Ave Ste 415",
      "phone": "(720) 712-3560"
    }
  ]
}
```

### Memory search, using only your scraper key

Every one of memory.mcpscraper.dev's 86 tools (governed capture, tags, graph traversal, search, vaults, tables, scheduled actions, webhooks, and more — see [`contracts/memory.tools.json`](./contracts/memory.tools.json)) is callable from `mcpscraper-sdk` alone, dispatched through `POST /memory/mcp-call`. mcpscraper.dev auto-provisions a memory identity for your account on first use — no separate `mk_...` key required.

<details open><summary>Node.js</summary>

```ts
const hits = await client.memoryTools.memory.search({ query: 'roofing warranty terms' })
```
</details>

<details><summary>Python</summary>

```python
hits = client.memory_tools.call_tool("searchTool", {"query": "roofing warranty terms"})
```
</details>

<details><summary>cURL</summary>

```bash
curl -X POST https://mcpscraper.dev/memory/mcp-call \
  -H "x-api-key: $MCPSCRAPER_API_KEY" -H "Content-Type: application/json" \
  -d '{"toolName":"searchTool","args":{"query":"roofing warranty terms"}}'
```
</details>

<details><summary>CLI</summary>

```bash
mcpscraper memory search "roofing warranty terms"
```
</details>

Sample output (illustrative, matches the real, verified response schema):

```json
{
  "ok": true,
  "vaultsSearched": ["Knowledge", "Projects"],
  "results": [
    {
      "text": "Standard roofing warranty terms cover materials for 25-30 years and labor for 2-10 years depending on installer certification tier.",
      "source": "note:competitor-research/roofing-warranties.md",
      "score": 0.83,
      "vault": "Knowledge"
    }
  ]
}
```

The legacy `memoryTools`/`memory_tools.call_tool(...)` bridge remains available for compatibility. New integrations should use `client.tools`, which provides typed methods for all 153 unified tools in both Node and Python, including all 86 memory tools.

## Errors

Every SDK throws a typed error on non-2xx responses: `ScraperApiError` (Node/Python, scraper) or `MemoryApiError` (Node/Python, memory), each carrying the HTTP status, an error code, and the raw response body. `ScraperApiError` adds `isInsufficientBalance()`/`isConcurrencyLimitExceeded()` narrowing helpers (`is_insufficient_balance()`/`is_concurrency_limit_exceeded()` in Python). The CLI catches these and prints a clean one-line message instead of a stack trace.

## All 153 MCP tools

Every package exposes the same generated namespace layout through `McpToolsClient`. The scraper clients also attach it as `client.tools`:

```ts
const sessions = await client.tools.browser.listSessions()
const route = await client.tools.vaults.routeMemory({ title: 'Raw article', content: markdown, source: url })
```

```python
sessions = client.tools.browser.list_sessions()
route = client.tools.vaults.route_memory(title="Raw article", content=markdown, source=url)
```

The authoritative tool names, descriptions, schemas, annotations, categories, and generated method bindings live in [`contracts/mcp.tools.json`](./contracts/mcp.tools.json).

## The CLI

`mcpscraper-cli` keeps 7 ergonomic shortcuts (`search`, `scrape`, `crawl`, `map`, `maps-search`, `memory search`, `memory list-vaults`) and also reaches all 153 tools through `mcpscraper tools list`, `mcpscraper tools describe <name>`, and `mcpscraper tools call <name> --args '<json>'`. Tools marked destructive require `--yes`. Every command reads `MCPSCRAPER_API_KEY` from the environment or `--api-key`.

## How this compares to Firecrawl

If you're coming from [Firecrawl](https://github.com/firecrawl/firecrawl): same idea — a thin client SDK over a hosted API — but not the same thing. Firecrawl's crawling engine is itself open source and self-hostable (AGPLv3); mcpscraper.dev's engine stays closed, only this SDK layer is open (MIT). The feature sets diverge too: this repo adds SERP/PAA research, Facebook/Google Ads Transparency, Instagram, Reddit, Google Maps, and a memory/vault bridge that Firecrawl doesn't have; Firecrawl has deeper crawl-specific tooling (page actions, PDF/DOCX parsing, published reliability benchmarks) that this repo doesn't. Pick based on what you're actually building.

## Contracts

- [`contracts/mcp.tools.json`](./contracts/mcp.tools.json) — canonical live-derived contract for all 153 tools. Source of truth for every Node/Python typed namespace, CLI catalog, and [cURL catalog](./docs/curl-tools.md).
- [`contracts/scraper.openapi.yaml`](./contracts/scraper.openapi.yaml) — OpenAPI 3.0.3 spec, 43 operations, hand-curated public REST convenience contract for mcpscraper.dev. Source of truth for the additional REST-style methods in `mcpscraper-sdk` (Node and Python). Browse it rendered: `npx serve .` from the repo root, then open `http://localhost:<port>/docs/`.
- [`contracts/memory.tools.json`](./contracts/memory.tools.json) — tool manifest (name, description, input/output JSON Schema per tool) for memory.mcpscraper.dev's 86 tools. Source of truth for `mcpscraper-memory-sdk` (Node and Python) and `mcpscraper-sdk`'s `memoryTools`/`memory_tools` bridge.

Both are hand-maintained, independent of either product's internal implementation — they only change when a public-facing shape changes, and both ship a drift-checking script (`npm run validate-contracts`) that diffs them against the live servers.

## Development

```bash
npm install
npm run typecheck && npm run build && npm run test    # Node packages
cd packages/scraper-python && uv sync && uv run pytest # Python scraper SDK
cd packages/memory-python && uv sync && uv run pytest  # Python memory SDK
npm run validate-contracts   # lints the OpenAPI spec, diffs memory.tools.json against live tools/list
npm run smoke-test           # live smoke test against prod using test/throwaway accounts
```

Package-specific docs: [`packages/scraper`](./packages/scraper) · [`packages/memory`](./packages/memory) · [`packages/scraper-python`](./packages/scraper-python) · [`packages/memory-python`](./packages/memory-python) · [`packages/cli`](./packages/cli)
