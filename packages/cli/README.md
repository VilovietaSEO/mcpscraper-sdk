# mcpscraper-cli

Command-line interface for [mcpscraper.dev](https://mcpscraper.dev) and [memory.mcpscraper.dev](https://memory.mcpscraper.dev).

[Release history](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/main/CHANGELOG.md)

The CLI provides friendly shortcuts for common operations plus universal discovery and invocation for every one of the 377 unified MCP tools, including provider-neutral X-Ray surveys, attribution-impact reporting, and truthful evidence-status operations.

## Install

```bash
npm install -g mcpscraper-cli
```

## Auth

```bash
export MCPSCRAPER_API_KEY=sk_live_your_key
```

or pass `--api-key <key>` on any command.

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
mcpscraper tools call list_scheduled_runs --args '{"view":"inbox","limit":30}' --json
mcpscraper tools call lead_list_enrich --args '{"idempotencyKey":"roofing-dallas-001","source":{"kind":"rows","rows":[{"Business":"White Rock Roofing","City":"Dallas","Website":"https://roofwhiterock.com"}]},"columnMap":{"name":"Business","city":"City","websiteUrl":"Website"},"defaultEntityType":"business","emailSearchFallback":"serp_snippets","peopleDiscovery":"owners","peopleQueryTemplates":["{business} owner of company {city}","{business} founder {city}"],"outputFormats":["csv","xlsx"]}' --json
mcpscraper tools call gmail_search_messages --args '{"connectionId":"gmail_conn_123","query":"has:attachment newer_than:30d","limit":25}' --json
mcpscraper tools call gmail_prepare_selection --args '{"connectionId":"gmail_conn_123","purpose":"memory_import","source":{"kind":"query","query":"has:attachment newer_than:30d"}}' --json
mcpscraper tools call gmail_import_status --args '{"ingestId":"opaque_ingest_id"}' --json
```

`tools list` contains exactly 377 manifest-backed names. `tools call` accepts any one of them. Tools marked destructive require `--yes`.

Integration connections are included with an active Starter plan or higher and have no extra connection-operation debit in this release. Scheduled occurrences cost 75 Credits; agent-mode runs also add 1.5 times OpenRouter's actual reported cost. Inspect the live policy with `mcpscraper tools call get-schedule-status --args '{}'`.

Current Google search pricing is 60 Credits per SERP search and 400 Credits plus 10 Credits per returned question for PAA. One optional concurrency pack adds two browser slots for $5/month; quantity n adds 2n browser slots.

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
mcpscraper export-read <job-id> --representation manifest
mcpscraper export-read <job-id> --representation html --page-id <page-id> --output page.html
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
