# mcpscraper-memory-sdk (Python)

Official Python client for the [memory.mcpscraper.dev](https://memory.mcpscraper.dev) hosted memory API — 74 tools across access/keys, channels, memory search/CRUD, tables, vaults, facts, schedule, webhooks, and video.

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

`client.access`, `client.capture`, `client.channels`, `client.facts`, `client.library`, `client.memory`, `client.recall`, `client.schedule`, `client.storage`, `client.tables`, `client.vaults`, `client.video`, `client.webhooks` — one method per tool, snake_case, typed with generated Pydantic models.

## Don't have a memory key?

If you already have an `mcpscraper.dev` API key and don't want to provision a separate `mk_...` memory key, use `mcpscraper-sdk`'s `ScraperClient.memory_tools` instead — it exposes this exact same set of 74 tools, dispatched through your scraper API key.

## Regenerating models

`src/mcpscraper_memory/models/` and `_generated_client.py` are generated from `../../contracts/memory.tools.json`. After editing the manifest, regenerate with:

```bash
python scripts/generate_models.py
```
