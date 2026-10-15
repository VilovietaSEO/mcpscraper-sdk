# mcpscraper-memory-sdk

Official TypeScript/JavaScript clients for the unified MCP Scraper catalog. The direct
Memory manifest remains checked for runtime compatibility, but customer calls use the root MCP.

[Release history](https://github.com/VilovietaSEO/mcpscraper-sdk/blob/main/CHANGELOG.md)

Both `MemoryClient` and `McpToolsClient` call `https://mcpscraper.dev/mcp` with the same MCP Scraper
API key. No product logic lives in this package.

## Install

```bash
npm install mcpscraper-memory-sdk
```

For the complete unified surface, use the same `McpToolsClient` exported by every SDK package:

```ts
import { McpToolsClient } from 'mcpscraper-memory-sdk'

const tools = new McpToolsClient({ apiKey: process.env.MCP_SCRAPER_API_KEY! })
await tools.browser.listSessions()
await tools.web.archiveRead({
  url: 'https://github.com/octocat/Hello-World/archive/refs/heads/master.zip',
})
await tools.memory.search({ query: 'q3 roadmap decisions' })
await tools.connections.exportConnectedServiceData({ connectionId: 'conn_123', lastDays: 7 })
```

The unified connection namespace includes permission-aware provider inventory and `meta_ads_insights` bulk exports for daily account, campaign, ad-set, and ad reporting, with large results delivered as private artifacts.

OAuth connect/reconnect and direct connected-service operations do not currently have an extra connection-operation debit beyond the required paid plan.

## Quickstart

```ts
import { MemoryClient, MemoryApiError } from 'mcpscraper-memory-sdk'

const client = new MemoryClient({ apiKey: process.env.MCP_SCRAPER_API_KEY! })

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

`MemoryClient` preserves the established compatibility namespaces and maps them to public root tool
IDs. Research remains sourced knowledge; CRM remains actual relationships. External CRM providers
remain unavailable. Retired direct-key issue/scope methods fail explicitly. `McpToolsClient` contains
all unified tools.

Use `client.callToolResult(name, args)` when a tool can return native MCP image, audio, or resource content. It preserves the complete `content`, `structuredContent`, and `isError` result. The existing `callTool` method remains the convenient parsed JSON/text path.

The unified MCP client supports two-page PAA acquisition through
`client.other.harvestPaaStart({ pages: 2, ... })`. One page remains the default;
page two adds organic results when available and does not create another PAA
graph. Poll the returned job with `harvestPaaStatus` and treat pagination as
nullable for older saved jobs.

Every method's input/output types are generated from the live tool schemas (see `src/generated/`, produced by `npm run generate` at the repo root from `contracts/memory.tools.json`) — no hand-maintained duplicate types to drift out of sync.

## Getting an API key

Create or rotate the one MCP Scraper key at the account dashboard and expose it as
`MCP_SCRAPER_API_KEY`. Do not create a separate Memory key for new setup.

## Errors

All failures — HTTP-level, JSON-RPC-level, and MCP tool-level (`isError: true`) — surface as a single `MemoryApiError` with `httpStatus`, `rpcCode`, and `data`/`toolError` fields depending on where the failure occurred.

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-sdk`](../scraper) (Node, also reaches these Memory tools via `client.memoryTools` using only a scraper key) · [`mcpscraper-memory-sdk` on PyPI](https://pypi.org/project/mcpscraper-memory-sdk/) · [`mcpscraper-cli`](../cli)

Durable PAA harvests should wait at least 20 seconds between status checks and honor a longer returned polling interval. Keep the same job ID and retry key while the original work is running.

Release changes: [SDK 0.54.1 release notes](https://github.com/VilovietaSEO/mcpscraper-sdk/releases/tag/v0.54.1).

## Client attribution and full results

Clients accept `clientAttribution: { installChannel?, aiClient?, aiModel? }` and default to calling surface `sdk`. Set only known caller labels; unspecified labels stay unknown. `onResponse({ requestId, status })` receives per-response correlation without changing results, and errors keep their own `requestId`. These options also apply to `McpToolsClient` and `MemoryClient`; labels are reporting declarations, not authorization.

Large tool outputs may be delivery envelopes instead of inline domain values. Preserve `delivery`, `scope` and `recovery`, then use `tools.artifacts.describe`, `readRetained` (follow `nextOffset` to null), or `download` with the returned artifact ID. The legacy `artifacts.read` method remains the report reader. `callToolResult` preserves native content/resource links. Download URL expiry differs from artifact retention; renew a URL through `download` without rerunning acquisition. Use the returned capability for binary files.
