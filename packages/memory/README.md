# mcpscraper-memory-sdk

Official TypeScript/JavaScript clients for all 155 tools at [mcpscraper.dev](https://mcpscraper.dev) plus the direct 86-tool [memory.mcpscraper.dev](https://memory.mcpscraper.dev) API.

These are thin clients: `MemoryClient` calls the direct memory MCP with a memory Bearer key, while `McpToolsClient` calls the unified MCP with a scraper API key. No product logic lives in this package.

## Install

```bash
npm install mcpscraper-memory-sdk
```

For the complete unified surface, use the same `McpToolsClient` exported by every SDK package:

```ts
import { McpToolsClient } from 'mcpscraper-memory-sdk'

const tools = new McpToolsClient({ apiKey: process.env.MCP_SCRAPER_API_KEY! })
await tools.browser.listSessions()
await tools.memory.search({ query: 'q3 roadmap decisions' })
await tools.connections.exportConnectedServiceData({ connectionId: 'conn_123', lastDays: 7 })
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

`MemoryClient` retains the direct 86-tool memory namespaces. `McpToolsClient` is generated from [`contracts/mcp.tools.json`](../../contracts/mcp.tools.json) and contains all 155 tools across its generated namespaces.

Every method's input/output types are generated from the live tool schemas (see `src/generated/`, produced by `npm run generate` at the repo root from `contracts/memory.tools.json`) — no hand-maintained duplicate types to drift out of sync.

## Getting an API key

Issue one via the `access-issue-key` tool (or `client.access.issueKey(...)` once you have an initial key), or through the memory dashboard.

## Errors

All failures — HTTP-level, JSON-RPC-level, and MCP tool-level (`isError: true`) — surface as a single `MemoryApiError` with `httpStatus`, `rpcCode`, and `data`/`toolError` fields depending on where the failure occurred.

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-sdk`](../scraper) (Node, also reaches these 86 tools via `client.memoryTools` using only a scraper key) · [`mcpscraper-memory-sdk` Python source package](../memory-python) · [`mcpscraper-cli`](../cli)
