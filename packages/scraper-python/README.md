# mcpscraper-sdk (Python)

Official Python client for the [mcpscraper.dev](https://mcpscraper.dev) REST API — SERP search, People-Also-Ask harvesting, single-page and whole-site extraction, YouTube, Facebook/Google Ads Transparency, Instagram, Reddit, video breakdown, Google Maps, and directory/rank-tracking workflows.

This is a thin HTTP client generated against [`../../contracts/scraper.openapi.yaml`](../../contracts/scraper.openapi.yaml), the public contract for the hosted API. It contains no scraping, proxy, or billing logic — only typed request/response plumbing over `requests`.

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
- `err.is_concurrency_limit_exceeded()` — `err.body` has `active`, `limit`, `retryable`.

## API surface

Core operations are flat on the client: `search_serp`, `harvest_paa`, `extract_url`, `map_site_urls`, `extract_site`, `audit_site`, `get_extract_site_status`, `list_jobs`, `get_job`, `get_history`, `get_ledger`.

Everything else is namespaced by product area, matching the OpenAPI spec's tags: `client.youtube`, `client.screenshot`, `client.facebook`, `client.google_ads`, `client.instagram`, `client.reddit`, `client.video`, `client.maps`, `client.directory`, `client.serp_intelligence`, `client.workflows`.

Typed Pydantic models for every request/response schema are available from `mcpscraper.models` if you want to construct or validate payloads explicitly — the client methods themselves accept plain keyword arguments/dicts and return parsed JSON.

## Scrape → memory vault

```python
page = client.extract_url(url="https://example.com/pricing", depositToVault=True, vaultName="competitors")
print(page["memory"])  # {"deposited": True, "vault": "competitors", "noteId": "...", "chunks": 4}
```

## Memory tools, using only this API key

`client.memory_tools.call_tool(name, args)` dispatches to any of the 74 memory.mcpscraper.dev tools through `POST /memory/mcp-call`, using only this mcpscraper.dev API key — no separate memory key needed:

```python
hits = client.memory_tools.call_tool("searchTool", {"query": "competitor pricing pages"})
vaults = client.memory_tools.call_tool("listVaultsTool")
```

See `contracts/memory.tools.json` in this repo (or the `mcpscraper-memory-sdk` Python package) for the full tool list and per-tool argument shapes — this is a generic `call_tool(name, args)` passthrough rather than one fully-typed method per tool. The Node.js SDK (`mcpscraper-sdk` on npm) has the fully typed, one-method-per-tool version if you need that level of ergonomics today.

## Regenerating models

`src/mcpscraper/models.py` is generated from the OpenAPI spec and checked in. After editing `../../contracts/scraper.openapi.yaml`, regenerate with:

```bash
uv run datamodel-codegen \
  --input ../../contracts/scraper.openapi.yaml \
  --input-file-type openapi \
  --output src/mcpscraper/models.py \
  --output-model-type pydantic_v2.BaseModel \
  --field-constraints \
  --use-schema-description \
  --target-python-version 3.10 \
  --disable-timestamp
```
