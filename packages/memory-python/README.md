# mcpscraper-memory-sdk (Python)

Official Python clients for the unified 375-tool [mcpscraper.dev](https://mcpscraper.dev) MCP catalog.
The direct 148-tool Memory manifest remains checked for runtime compatibility.

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

`client.access`, `client.capture`, `client.channels`, `client.crm`, `client.facts`, `client.files`, `client.graph`, `client.library`, `client.memory`, `client.recall`, `client.research`, `client.schedule`, `client.storage`, `client.tables`, `client.tags`, `client.vaults`, `client.video`, `client.webhooks` — one method per tool, snake_case, typed with generated Pydantic models. Use Research for sourced knowledge and CRM for an actual relationship; counterpart operations link records without copying fields. External CRM providers remain unavailable, with no setup or write wrapper. Original Gmail attachment bytes saved to Memory are available through `client.files.file_asset_save(...)` and `client.files.file_asset_get(...)`.

Use the same key with `McpToolsClient` for all 375 unified scraper and Memory tools.

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

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-memory-sdk` on npm](../memory) (Node) · [`mcpscraper-sdk` on PyPI](https://pypi.org/project/mcpscraper-sdk/) (also reaches these 148 tools via a scraper key) · [`mcpscraper-cli`](../cli)
