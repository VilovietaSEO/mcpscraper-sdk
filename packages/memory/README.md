# mcpscraper-memory-sdk

Official TypeScript/JavaScript client for [memory.mcpscraper.dev](https://memory.mcpscraper.dev) — a hosted, per-user, multi-vault memory API (notes, search, tables, channels, scheduled actions, and more).

This is a thin client: every method sends a JSON-RPC 2.0 `tools/call` request to `/mcp` with your Bearer API key and parses the response. No memory/vault logic lives in this package — see [`contracts/memory.tools.json`](../../contracts/memory.tools.json) for the full contract this client is generated from.

## Install

```bash
npm install mcpscraper-memory-sdk
```

## Quickstart

```ts
import { MemoryClient, MemoryApiError } from 'mcpscraper-memory-sdk'

const client = new MemoryClient({ apiKey: process.env.MCP_MEMORY_API_KEY! })

try {
  const results = await client.memory.search({ query: 'q3 roadmap decisions' })
  console.log(results.results)

  const note = await client.memory.get({ path: 'projects/q3-plan' })
  console.log(note)
} catch (err) {
  if (err instanceof MemoryApiError) {
    console.error('memory API error:', err.message, err.rpcCode, err.httpStatus)
  } else {
    throw err
  }
}
```

## Namespaces

Methods are grouped by category, matching [`contracts/memory.tools.json`](../../contracts/memory.tools.json): `client.memory` (get/list/put/search/suggest/export/upload/deleteNote), `client.vaults`, `client.access` (keys, shares, invites), `client.channels`, `client.tables`, `client.schedule`, `client.webhooks`, `client.facts`, `client.recall`, `client.storage`, `client.video`, `client.library`, `client.capture`.

Every method's input/output types are generated from the live tool schemas (see `src/generated/`, produced by `npm run generate` at the repo root from `contracts/memory.tools.json`) — no hand-maintained duplicate types to drift out of sync.

## Getting an API key

Issue one via the `access-issue-key` tool (or `client.access.issueKey(...)` once you have an initial key), or through the memory dashboard.

## Errors

All failures — HTTP-level, JSON-RPC-level, and MCP tool-level (`isError: true`) — surface as a single `MemoryApiError` with `httpStatus`, `rpcCode`, and `data`/`toolError` fields depending on where the failure occurred.

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-sdk`](../scraper) (Node, also reaches these 85 tools via `client.memoryTools` using only a scraper key) · [`mcpscraper-memory-sdk` Python source package](../memory-python) · [`mcpscraper-cli`](../cli)
