# mcpscraper-sdk (Python)

Official Python client for the [mcpscraper.dev](https://mcpscraper.dev) REST API — SERP search, People-Also-Ask harvesting, single-page and whole-site extraction, YouTube, Facebook/Google Ads Transparency, Instagram, Reddit, video breakdown, Google Maps, and directory/rank-tracking workflows.

[Release history](https://github.com/VilovietaSEO/mcpscraper-sdk/releases/tag/v0.58.0)

This is a thin HTTP client generated against [`../../contracts/scraper.openapi.generated.json`](../../contracts/scraper.openapi.generated.json), the complete public REST contract for the hosted API. It contains no scraping, proxy, or billing logic — only typed request/response plumbing over `requests`.

## Install

```bash
pip install mcpscraper-sdk
# or
uv add mcpscraper-sdk
```

## Usage

```python
from mcpscraper import ScraperClient, ScraperApiError

client = ScraperClient(api_key="sk_live_your_key")

serp = client.search_serp(query="roof repair Denver")

try:
    places = client.maps.search({"query": "roofers", "location": "Denver, CO"})
    print(places)
except ScraperApiError as err:
    if err.is_insufficient_balance():
        print(f"Need {err.body['required_credits']} credits, have {err.body['balance_credits']}. Top up: {err.body['topup_url']}")
    else:
        raise
```

## Errors

Every non-2xx response raises a `ScraperApiError` with `.status`, `.code`, and the raw response `.body`. Two cases have narrowing helpers:

- `err.is_insufficient_balance()` — `err.body` has `balance_credits`, `required_credits`, `topup_url`.
- `err.is_concurrency_limit_exceeded()` — `err.body` has `active`, `limit`, `retryable`, and pack upgrade details.
- `err.is_verification_challenge()` / `err.is_timeout()` — preserve actionable, vendor-neutral retry and charge details returned by the service.

Google Search light mode returns organic positions, URLs, titles, and descriptions for 20 Credits per delivered SERP page, or 35 Credits when the backup supplies the result. One-page full mode adds available same-page SERP features for 35 Credits. Both modes default to one page; an unfiltered two-page search costs 40 Credits when the normal provider returns both pages. Past-week and past-month searches return one page of organic results at 35 Credits; omit the date filter when requesting two pages. Unfiltered one-page light searches try the primary path twice, then one API fallback; an unfiltered one-page full search uses the feature-capable API directly. Date filters and saved search identities require one page. Combining either with two pages is rejected before acquisition or billing. Two-page searches return organic results without a backup provider. If page 2 cannot be delivered, an available page 1 is returned as partial and billed at the one-page rate. A 35-Credit-per-requested-page hold is settled after delivery. PAA costs 400 Credits plus 10 Credits per returned question. One optional concurrency pack adds two browser slots for $5/month; quantity `n` adds `2n` slots for `$5n` without changing the base plan.

## API surface

`client.tools` is the generated manifest-backed MCP surface, including provider-neutral X-Ray surveys, attribution-impact reporting, and truthful evidence-status operations, with one typed snake_case method per tool:

For durable PAA acquisition, call
`client.tools.other.harvest_paa_start(pages=2, ...)`, then poll its `job_id` with
`harvest_paa_status`. One page is the default. A second page contributes organic
results when available; all PAA questions still come from the preserved first
page. Pagination is nullable for older saved jobs.

Use `client.tools.call_tool_result(name, args)` when a multimodal tool must preserve its native MCP image, audio, or resource blocks. `call_tool(...)` remains the parsed, backward-compatible path.

```python
client.tools.search.search_serp(query="roof repair Denver")
client.tools.web.archive_read(
    url="https://github.com/octocat/Hello-World/archive/refs/heads/master.zip",
    path="Hello-World-master/README",
)
client.tools.web.archive_read(
    url="https://github.com/octocat/Hello-World/archive/refs/heads/master.zip",
    path_prefix="Hello-World-master/",
    max_entries=100,
    max_total_bytes=2_000_000,
)
method = client.tools.editorial.reading_room_guide(focus="workflow")
client.tools.memory.search(query="roofing warranty terms")
client.tools.connections.export_connected_service_data(
    connection_id="conn_123",
    dataset="resend_data",
    last_days=7,
)
templates = client.tools.artifacts.list_artifact_templates(status="active")
```

Lead enrichment is available through the same generated surface. Supply mapped rows directly, or call `client.tools.leads.import_(...)` first for CSV/TSV/XLSX input:

```python
job = client.tools.leads.enrich(
    idempotency_key="roofing-dallas-001",
    source={"kind": "rows", "rows": [{"Business": "White Rock Roofing", "City": "Dallas", "Website": "https://roofwhiterock.com"}]},
    column_map={"name": "Business", "city": "City", "websiteUrl": "Website"},
    default_entity_type="business",
    email_search_fallback="serp_snippets",
    people_discovery="owners",
    people_query_templates=["{business} owner of company {city}", "{business} founder {city}"],
    output_formats=["csv", "xlsx"],
)
```

The connected-data export performs bounded Gmail, Calendar, Google Search Console, Zoom, Meta Marketing, or Resend pagination server-side and returns small results inline or a private seven-day JSONL artifact. Use `search_console_performance` for bounded Search Analytics rows across every accessible property, and `meta_ads_insights` for daily account, campaign, ad-set, and ad reporting across connected Meta ad accounts. Resend can aggregate sent/received mail, logs, contacts, broadcasts, and templates with `resend_data`. Resume partial exports with the returned `continuation` object; renew an expired signed URL with `client.tools.connections.renew_connected_data_download(artifact_id="artifact_123")`. Use `list_service_connections` for verified grants and per-tool permission blockers, then `describe_service_connection_tool` for the exact provider-native schema before calling through the generic connection bridges.

Core operations are flat on the client: `search_serp`, `harvest_paa`, `extract_url`, `map_site_urls`, `extract_site`, `audit_site`, `get_extract_site_status`, `read_extract_site_export`, `read_extract_site_image`, `list_jobs`, `get_job`, `get_history`, `get_ledger`.

Everything else is namespaced by product area, matching the OpenAPI spec's tags: `client.youtube`, `client.screenshot`, `client.facebook`, `client.google_ads`, `client.instagram`, `client.reddit`, `client.video`, `client.maps`, `client.directory`, `client.serp_intelligence`, `client.workflows`.

Typed Pydantic models for every request/response schema are available from `mcpscraper.models` if you want to construct or validate payloads explicitly — the client methods themselves accept plain keyword arguments/dicts and return parsed JSON.

### Retry-safe SERP Intelligence captures

Pass a stable idempotency key when a capture may be retried. The regular method continues to return the response body; `capture_with_receipt` also returns the key accepted or generated by the server so it can be reused after a timeout or uncertain response:

```python
result = client.serp_intelligence.capture(
    {"query": "roofers near me"},
    idempotency_key="serp-run-2026-07-14-001",
)

receipt = client.serp_intelligence.capture_with_receipt({"query": "roofers near me"})
print(receipt["data"]["billing"]["creditsUsed"], receipt["idempotency_key"])
```

Reusing a key with the same body recovers the original debit and settlement. Reusing it with a different body raises `ScraperApiError` with status `409` and code `idempotency_conflict`.

## Scrape → memory vault

```python
page = client.extract_url(url="https://example.com/pricing", depositToVault=True, vaultName="competitors")
print(page["memory"])  # {"deposited": True, "vault": "competitors", "noteId": "...", "chunks": 4}
```

## Memory tools, using only this API key

`client.memory_tools.call_tool(name, args)` dispatches to supported Memory tools through the root `POST /memory/mcp-call` bridge, using the same MCP Scraper API key:

```python
hits = client.memory_tools.call_tool("searchTool", {"query": "competitor pricing pages"})
vaults = client.memory_tools.call_tool("listVaultsTool")
```

This generic compatibility bridge remains available, but new integrations should use `client.tools`, whose generated namespaces provide one typed method for every unified MCP tool.

## Regenerating models

`src/mcpscraper/models.py` is generated from the complete OpenAPI projection and checked in. From the repository root, update the server artifact, then regenerate Node and Python together:

```bash
npm run generate:rest
npm run verify:rest-contract
```

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-sdk` on npm](../scraper) (Node, full `memory_tools` typed surface) · [`mcpscraper-memory-sdk` on PyPI](https://pypi.org/project/mcpscraper-memory-sdk/) · [`mcpscraper-cli`](../cli)

Release changes: [SDK 0.55.1 release notes](https://github.com/VilovietaSEO/mcpscraper-sdk/releases/tag/v0.55.1).

## Client attribution and full results

Clients accept `client_attribution={"install_channel": ..., "ai_client": ..., "ai_model": ...}` and default to calling surface `sdk`. Set only known caller labels; unspecified labels stay unknown. `on_response` receives a metadata dictionary with `request_id` and `status` per response, and errors keep their own `request_id`. These options also apply to `McpToolsClient` and `MemoryClient`; labels are reporting declarations, not authorization.

Generated output unions return the matching model directly, preserving attributes such as `transcript_text`. Use `pydantic.TypeAdapter(Output)` when independently validating an output union. Large outputs may have `delivery`, `scope` and `recovery` instead of inline data. Preserve them, then use `tools.artifacts.describe`, `read_retained` (follow `next_offset` to None), or `download` with the artifact ID. The legacy `artifacts.read` method remains the report reader. `call_tool_result` preserves native content/resource links. Download URL expiry differs from retention; renew through `download` without rerunning acquisition. Use the returned capability for binary files.

Artifact delivery may include optional `delivery.availableExports` handles. Use the
export artifact ID with `artifact_download`, `artifact_read` or `artifact_describe`
to generate Markdown from retained JSON without repeating acquisition. The
[on-demand export example](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/v0.55.0/examples/serp-on-demand-export.mjs)
shows the complete flow and preserves a retry key for uncertain search responses.

For page content, start `extract_site` directly; it discovers pages during extraction. Use `map_site_urls` when you need the URL inventory itself. See the [direct site-export example](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/v0.55.1/examples/site-export-direct.mjs) for retry keys, status and complete page reads.

Release changes: [SDK 0.56.1 release notes](https://github.com/VilovietaSEO/mcpscraper-sdk/releases/tag/v0.56.1).

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

## Bug Reporting

Use `bug_reporting` to prepare a redacted draft from observed calls and errors. Review the returned report, then submit its exact `reportId` and `reviewToken` only when the user requests submission. Status returns the private receipt. The support team receives the report and verified account email. Drafts expire after one day; submitted reports after 365 days. See [the complete workflow](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/v0.57.0/examples/bug-reporting.mjs) and [release history](https://github.com/VilovietaSEO/mcpscraper-sdk/releases/tag/v0.57.0).

## Consistent hosted MCP protocol

This release targets MCP Scraper 0.102.0 with 349 tools. Calls use protocol `2026-07-28` with matching routing headers and request metadata. Poll the returned job/run ID through its dedicated status tool; MCP Task handles are no longer supported. Lead enrichment cancellation uses `lead_list_enrich_cancel`. Update the SDK packages together.
