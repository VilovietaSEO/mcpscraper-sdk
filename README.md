# mcpscraper-sdk

Official TypeScript/JavaScript client SDKs for [mcpscraper.dev](https://mcpscraper.dev) (web intelligence: SERP, PAA, site extraction, YouTube, Facebook/Google ads, Instagram, Maps, Reddit, video, directory workflows) and [memory.mcpscraper.dev](https://memory.mcpscraper.dev) (hosted per-user memory/vaults).

These are thin HTTP clients — they call the same hosted APIs that back the `mcp-scraper` and `mcpscraper-memory` MCP servers. No scraping, proxy, or billing logic lives in this repo; it's request/response plumbing only, licensed MIT.

## Packages

| Package | Talks to | Auth |
|---|---|---|
| [`mcpscraper-sdk`](./packages/scraper) | `mcpscraper.dev` REST API | `x-api-key` header |
| [`mcpscraper-memory-sdk`](./packages/memory) | `memory.mcpscraper.dev` `/mcp` (JSON-RPC) | `Authorization: Bearer mk_...` |

## Contracts

- [`contracts/scraper.openapi.yaml`](./contracts/scraper.openapi.yaml) — OpenAPI 3.1 spec for the mcp-scraper public REST contract. Source of truth for the `mcpscraper-sdk` package.
- [`contracts/memory.tools.json`](./contracts/memory.tools.json) — tool manifest for mcp-memory's MCP tool contract (name, description, input schema, output shape per tool). Source of truth for the `mcpscraper-memory-sdk` package.

Both are hand-maintained, independent of either product's internal implementation — they only change when a public-facing shape changes.

## Getting an API key

- mcp-scraper: `npx -y -p mcp-scraper@latest mcp-scraper-cli billing concurrency info` or see the [account dashboard](https://mcpscraper.dev).
- mcp-memory: issued via the `issue-key` MCP tool, or the memory dashboard.

## Development

```bash
npm install
npm run typecheck
npm run validate-contracts   # lints scraper.openapi.yaml, diffs memory.tools.json against live tools/list
npm run smoke-test           # live smoke test against prod using test/throwaway accounts
```
