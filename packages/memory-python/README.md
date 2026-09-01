# mcpscraper-memory-sdk (Python)

Official Python clients for all 363 unified [mcpscraper.dev](https://mcpscraper.dev) MCP tools plus the direct 121-tool [memory.mcpscraper.dev](https://memory.mcpscraper.dev) API.

This is a thin JSON-RPC client generated against [`../../contracts/memory.tools.json`](../../contracts/memory.tools.json), the public contract for the hosted API. It contains no product source — only typed request/response plumbing.

## Install

```bash
pip install mcpscraper-memory-sdk
```

## Usage

```python
from mcpscraper_memory import MemoryClient, MemoryApiError

client = MemoryClient(api_key="mk_your_key")

try:
    result = client.memory.search(query="competitor pricing pages")
    for hit in result.results or []:
        print(hit["source"], hit["score"])
except MemoryApiError as err:
    print(f"memory call failed: {err}")
```

## Namespaces

`client.access`, `client.capture`, `client.channels`, `client.facts`, `client.files`, `client.graph`, `client.library`, `client.memory`, `client.recall`, `client.schedule`, `client.storage`, `client.tables`, `client.tags`, `client.vaults`, `client.video`, `client.webhooks` — one method per tool, snake_case, typed with generated Pydantic models. Original Gmail attachment bytes saved to Memory are available through `client.files.file_asset_save(...)` and `client.files.file_asset_get(...)`.

Use `McpToolsClient(api_key="sk_...")` for all 363 unified tools, including the governed personal-assistant namespace; it has the same generated namespaces as every other SDK package. The ZIP reader is available as `client.web.archive_read(url=...)`, and the editorial workflow begins with `client.editorial.reading_room_guide(focus="workflow")`. Scheduled results and saved artifact templates are available under `client.schedule`; run IDs and cursors remain opaque. Bulk Gmail, Calendar, Zoom, Meta Marketing, and Resend exports are available through `client.connections.export_connected_service_data(...)`; select `meta_ads_insights` for daily account/campaign/ad-set/ad reporting or `resend_data` for the Resend aggregate, and renew expired artifact URLs with `client.connections.renew_connected_data_download(artifact_id="artifact_123")`.

Use `client.call_tool_result(name, args)` for native MCP image, audio, or resource blocks. The existing `call_tool` method keeps returning the parsed structured/text value.

## Don't have a memory key?

If you already have an `mcpscraper.dev` API key and don't want to provision a separate `mk_...` memory key, use `mcpscraper-sdk`'s `ScraperClient.memory_tools` instead — it exposes this exact same set of 121 tools, dispatched through your scraper API key.

## Regenerating models

`src/mcpscraper_memory/models/` and `_generated_client.py` are generated from `../../contracts/memory.tools.json`. After editing the manifest, regenerate with:

```bash
python scripts/generate_models.py
```

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-memory-sdk` on npm](../memory) (Node) · [`mcpscraper-sdk` on PyPI](https://pypi.org/project/mcpscraper-sdk/) (also reaches these 121 tools via a scraper key) · [`mcpscraper-cli`](../cli)
