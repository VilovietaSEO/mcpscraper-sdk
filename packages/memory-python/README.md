# mcpscraper-memory-sdk (Python)

Official Python clients for the unified [mcpscraper.dev](https://mcpscraper.dev) MCP catalog.
The direct Memory manifest remains checked for runtime compatibility.

[Release history](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/main/CHANGELOG.md)

This is a thin JSON-RPC client generated against [`../../contracts/memory.tools.json`](../../contracts/memory.tools.json), the public contract for the hosted API. It contains no product source — only typed request/response plumbing.

## Install

```bash
pip install mcpscraper-memory-sdk
```

## Usage

```python
import os
from mcpscraper_memory import MemoryClient, MemoryApiError

client = MemoryClient(api_key=os.environ["MCP_SCRAPER_API_KEY"])

try:
    result = client.memory.search(query="competitor pricing pages")
    for hit in result.results or []:
        print(hit["source"], hit["score"])
except MemoryApiError as err:
    print(f"memory call failed: {err}")
```

## Namespaces

`client.access`, `client.capture`, `client.channels`, `client.crm`, `client.facts`, `client.files`, `client.graph`, `client.library`, `client.memory`, `client.recall`, `client.research`, `client.artifacts`, `client.storage`, `client.tables`, `client.tags`, `client.vaults`, `client.video`, `client.webhooks` — one method per tool, snake_case, typed with generated Pydantic models. Use Research for sourced knowledge and CRM for an actual relationship; counterpart operations link records without copying fields. External CRM providers remain unavailable, with no setup or write wrapper. Original Gmail attachment bytes saved to Memory are available through `client.files.file_asset_save(...)` and `client.files.file_asset_get(...)`.

Use the same key with `McpToolsClient` for all unified scraper and Memory tools.

Use `client.call_tool_result(name, args)` for native MCP image, audio, or resource blocks. The existing `call_tool` method keeps returning the parsed structured/text value.

The unified MCP client accepts `pages=2` on
`client.other.harvest_paa_start(...)`. It keeps one page as the default, adds
page-two organic results when available, and expands PAA only on the preserved
first page. Poll the same job with `harvest_paa_status`; pagination remains
nullable for results saved under older contracts.

## Authentication

Set `MCP_SCRAPER_API_KEY` once. `MemoryClient`, `McpToolsClient`, and the scraper SDK all use that
same customer credential against `https://mcpscraper.dev/mcp`.

## Regenerating models

`src/mcpscraper_memory/models/` and `_generated_client.py` are generated from `../../contracts/memory.tools.json`. After editing the manifest, regenerate with:

```bash
python scripts/generate_models.py
```

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-memory-sdk` on npm](../memory) (Node) · [`mcpscraper-sdk` on PyPI](https://pypi.org/project/mcpscraper-sdk/) (also reaches these Memory tools via a scraper key) · [`mcpscraper-cli`](../cli)

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
