# mcpscraper-cli

Command-line interface for the unified [mcpscraper.dev](https://mcpscraper.dev) MCP and REST APIs.

[Release history](https://github.com/VilovietaSEO/mcpscraper-sdk/releases/tag/v0.58.1)

The CLI provides friendly shortcuts for common operations plus universal discovery and invocation for every unified MCP tool, including retained-file readers, provider-neutral X-Ray surveys, attribution-impact reporting, and truthful evidence-status operations.

## Install

```bash
npm install -g mcpscraper-cli
```

## Auth

```bash
export MCPSCRAPER_API_KEY=sk_live_your_key
```

or pass `--api-key <key>` on any command.

## Deployment and client attribution

The default API endpoint is `https://mcpscraper.dev`. To use a selected branch deployment, set `MCPSCRAPER_BASE_URL` or pass `--base-url https://your-preview.example.com`. The URL must not contain credentials, a query or a fragment; authentication still uses the API key.

Attribution labels help the operator identify client usage in reports. They do not affect authentication, credits, provider selection or tool arguments. Declare the installation channel and AI client/model when known:

```bash
mcpscraper --install-channel npm --ai-client claude-code --ai-model claude-sonnet-4 tools call credits_info --args '{}' --json
```

The equivalent environment settings are `MCP_SCRAPER_INSTALL_CHANNEL`, `MCP_SCRAPER_AI_CLIENT` and `MCP_SCRAPER_AI_MODEL`. Command flags take precedence. Installation choices are `npx`, `npm`, `source` and `mcpb`; AI client choices are `claude`, `claude-desktop`, `claude-code`, `chatgpt`, `codex`, `cursor`, `gemini` and `other`. Model identifiers are limited to 80 characters, starting with a letter or digit and containing only letters, digits, `.`, `_`, `:`, `/` and `-`.

The CLI automatically reports `npx` only when its observed executable path is inside an `_npx` cache directory. An npm or source installation and AI identity stay unspecified unless declared. Direct API shortcuts report the `rest` surface, including `/memory/mcp-call`; universal `tools call` commands report `mcp-http`. Installation channel is a separate label.

## Commands

### Every MCP tool

```bash
mcpscraper tools list
mcpscraper tools describe prepare-memory-write
mcpscraper tools call prepare-memory-write --args '{"title":"Example","content":"..."}' --json
mcpscraper tools call export_connected_service_data --args '{"connectionId":"conn_123","dataset":"emails","lastDays":7}' --json
mcpscraper tools call export_connected_service_data --args '{"connectionId":"meta_conn_123","dataset":"meta_ads_insights","lastDays":30,"delivery":"artifact"}' --json
mcpscraper tools call export_connected_service_data --args '{"connectionId":"gsc_conn_123","dataset":"search_console_performance","lastDays":28}' --json
mcpscraper tools call describe_service_connection_tool --args '{"connectionId":"conn_123","tool":"provider-tool-name"}' --json
mcpscraper tools call renew_connected_data_download --args '{"artifactId":"artifact_123"}' --json
mcpscraper tools call archive_read --args '{"url":"https://github.com/octocat/Hello-World/archive/refs/heads/master.zip"}' --json
mcpscraper tools call artifact_describe --args '{"artifactId":"artifact_123"}' --json
mcpscraper tools call artifact_read --args '{"artifactId":"artifact_123","offset":0,"maxBytes":64000}' --json
mcpscraper tools call artifact_download --args '{"artifactId":"artifact_123"}' --raw-result
mcpscraper tools call list_artifact_templates --args '{"status":"active"}' --json
mcpscraper tools call lead_list_enrich --args '{"idempotencyKey":"roofing-dallas-001","source":{"kind":"rows","rows":[{"Business":"White Rock Roofing","City":"Dallas","Website":"https://roofwhiterock.com"}]},"columnMap":{"name":"Business","city":"City","websiteUrl":"Website"},"defaultEntityType":"business","emailSearchFallback":"serp_snippets","peopleDiscovery":"owners","peopleQueryTemplates":["{business} owner of company {city}","{business} founder {city}"],"outputFormats":["csv","xlsx"]}' --json
mcpscraper tools call gmail_search_messages --args '{"connectionId":"gmail_conn_123","query":"has:attachment newer_than:30d","limit":25}' --json
mcpscraper tools call gmail_prepare_selection --args '{"connectionId":"gmail_conn_123","purpose":"memory_import","source":{"kind":"query","query":"has:attachment newer_than:30d"}}' --json
mcpscraper tools call gmail_import_status --args '{"ingestId":"opaque_ingest_id"}' --json
```

`tools list` contains the current manifest-backed names. `tools call` accepts any one of them. Tools marked destructive require `--yes`.

`tools call --json` keeps the existing output shape: parsed `structuredContent` or text for text-only results, and the MCP envelope when it includes resources or media. Use `--raw-result` to always retain the envelope, including `content`, `structuredContent`, metadata and resource links. Both modes save inline binary blocks to local files and replace their bytes with `savedPath` and byte-count metadata. Retained-file envelopes and resource links remain available in the output. For complete text, use the returned artifact ID with `artifact_read` and follow `nextOffset` until it is null. `artifact_describe` reports MIME type, size, supported readers and retention expiry; `artifact_download` returns or renews the original file's link while retention remains valid. A preview or one read window is not the whole source.

Integration connections are included with an active Starter plan or higher and have no extra connection-operation debit in this release.

Google Search light mode returns organic positions, URLs, titles, and descriptions for 20 Credits per delivered SERP page, or 35 Credits when the backup supplies the result. Unfiltered one-page light mode makes two primary attempts, then one API fallback. Two-page searches return organic results without a backup provider. Unfiltered one-page full mode adds available same-page SERP features for 35 Credits. Both modes default to one page. Past-week and past-month searches return one page of organic results at 35 Credits; omit the date filter when requesting two pages. Request a second page explicitly only for an unfiltered search. Date filters and saved search identities require one page. Combining either with two pages is rejected before acquisition or billing. A 35-Credit-per-requested-page hold is settled after delivery. PAA costs 400 Credits plus 10 Credits per returned question. One optional concurrency pack adds two browser slots for $5/month; quantity n adds 2n browser slots.

Use `mcpscraper tools call harvest_paa_start --args '{"query":"...","pages":2,"idempotencyKey":"..."}' --json`
to request a second organic-results page, then poll the returned `jobId` with
`harvest_paa_status`. One page is the default, and the second page never creates
a second PAA graph. Pagination can be null for older saved jobs.

When a tool returns inline MCP media, the CLI writes each block to a private local file and prints its path instead of dumping base64. Use `--media-dir <path>` to choose the destination; the default is `~/Downloads/mcp-scraper`.

### `mcpscraper search <query>`

```bash
$ mcpscraper search "best roofing companies denver"
1. TOP 10 BEST Roofing Companies in Denver, CO
   https://www.yelp.com/search?find_desc=Roofing+Companies&find_loc=Denver%2C+CO
2. Recomendations for roofing company in Denver - ASAP
   https://www.reddit.com/r/Denver/comments/1kh2gd3/...
```

Options: `--location <location>`, `--json`.

### `mcpscraper scrape <url>`

```bash
$ mcpscraper scrape https://example.com --deposit-to-vault --vault research
Example Domain
This domain is for use in illustrative examples...

Vault deposit: saved to research
```

Options: `--screenshot`, `--deposit-to-vault`, `--vault <name>`, `--json`.

### `mcpscraper crawl <url>`

Starts a durable background export that retains complete JSON, acquired HTML, and Markdown for every successful page. Options: `--max-pages <n>` (default 100), `--preserve-media`, `--idempotency-key <key>`, `--json`.

Poll and read the export without downloading and unpacking the ZIP:

```bash
mcpscraper export-status <job-id>
mcpscraper export-read <job-id> --format manifest
mcpscraper export-read <job-id> --format html --page-id <page-id> --output page.html
mcpscraper export-image <job-id> <image-id> --output image.jpg
```

### `mcpscraper map <url>`

Discovers all URLs on a site (no extraction). Options: `--json`.

### `mcpscraper maps-search <query> --location <location>`

```bash
$ mcpscraper maps-search "roofers" --location "Denver, CO"
1. Forest Roofs (4.9★)
   701 Birch Street
2. Mike & Sons Roofing (4.8★)
   ...
```

Options: `--json`.

### `mcpscraper memory search <query>`

Semantic search across your mcp-memory vaults, dispatched through your mcpscraper.dev API key (no separate memory key needed).

```bash
$ mcpscraper memory search "roofing warranty terms"
[0.83] note:competitor-research/roofing-warranties.md
  Standard roofing warranty terms cover materials for 25-30 years...
```

### `mcpscraper memory list-vaults`

```bash
$ mcpscraper memory list-vaults
Ideas (2 notes, owner)
Inspiration (2 notes, owner)
Knowledge (3 notes, owner)
```

## Every command supports `--json`

```bash
$ mcpscraper map https://example.com --json
{
  "urls": ["https://example.com/", "https://example.com/about"]
}
```

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-sdk`](../scraper) · [`mcpscraper-memory-sdk`](../memory) · Python: [`mcpscraper-sdk`](../scraper-python) · [`mcpscraper-memory-sdk`](../memory-python)

Durable PAA harvests should wait at least 20 seconds between status checks and honor a longer returned polling interval. Keep the same job ID and retry key while the original work is running.

Release changes: [SDK 0.55.1 release notes](https://github.com/VilovietaSEO/mcpscraper-sdk/releases/tag/v0.55.1).

Artifact delivery may include optional `delivery.availableExports` handles. Use the
export artifact ID with `artifact_download`, `artifact_read` or `artifact_describe`
to generate Markdown from retained JSON without repeating acquisition. The
[on-demand export example](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/v0.55.0/examples/serp-on-demand-export.mjs)
shows the complete flow and preserves a retry key for uncertain search responses.

For page content, start `extract_site` directly; it discovers pages during extraction. Use `map_site_urls` when you need the URL inventory itself. See the [direct site-export example](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/v0.55.1/examples/site-export-direct.mjs) for retry keys, status and complete page reads.

Release changes: [SDK 0.56.0 release notes](https://github.com/VilovietaSEO/mcpscraper-sdk/releases/tag/v0.56.0).

## Reddit discovery and known threads

Use `reddit_trending` with `window:"year"` to discover past-year search candidates and
select relevant threads before collecting comments. Set `maxThreads` to bound the
number selected and `maxCommentsPerThread:20` for a per-thread capture limit.
Twenty is a request limit; inspect returned coverage because fewer accessible text
comments can produce a partial result. Publication dates are optional when unknown.

Pass a known Reddit thread URL directly to `reddit_thread` with `maxComments:20`;
it does not require a discovery call first. Trending returns ranked summaries and
questions; the thread tool returns full comment bodies. Preserve each operation's
retry key and exact inputs after an uncertain response.

The [past-year and direct-thread example](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/v0.56.0/examples/reddit-past-year.mjs)
shows both paths.

## Saved Maps reviews

Server 0.100.1 improves Maps discovery, review text and list collection through the existing interfaces. Use the exact name and location returned by discovery. Read the saved run and its review pages before considering a new acquisition. An explicit resume uses a fresh browser and reopens the profile and reviews; it retains saved review IDs. A new resume key authorizes a separately billed attempt, while repeating that key reads the same run.

## Consistent hosted MCP protocol

This release targets MCP Scraper 0.102.0 with 349 tools. Calls use protocol `2026-07-28` with matching routing headers and request metadata. Poll the returned job/run ID through its dedicated status tool; MCP Task handles are no longer supported. Lead enrichment cancellation uses `lead_list_enrich_cancel`. Update the SDK packages together.
