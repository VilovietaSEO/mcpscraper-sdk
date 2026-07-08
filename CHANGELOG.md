# Changelog

All notable changes to `mcpscraper-sdk` and `mcpscraper-memory-sdk` are documented here. Each entry notes which product version(s) it was verified against.

## [Unreleased]
- Initial scaffold: contracts/ (OpenAPI spec for mcp-scraper, tool manifest for mcp-memory), packages/scraper, packages/memory.

## mcpscraper-sdk 0.2.0
- Added `depositToVault`/`vaultName` to `extractUrl` and the `memory` response field (`VaultDepositResult`), reflecting mcp-scraper's scrape-to-vault feature.
- Added `POST /memory/mcp-call` to the contract and `client.memoryTools.*` to the SDK — all 74 memory.mcpscraper.dev tools, callable with only a scraper API key (reuses `mcpscraper-memory-sdk`'s generated namespace classes as a workspace dependency; no code duplicated).
- Verified against mcp-scraper `main` as of commit `b04db11` ("merge mcp-memory's 74 tools into the unified MCP surface") and `mcpscraper-memory-tools@1.1.0` (confirmed exact 74/74 tool-name parity against `contracts/memory.tools.json` — no changes needed there).
- `mcp-scraper-scheduler` (the new cron/automation worker mcp-memory's scheduling engine moved to) has no public API surface — confirmed via its own landing page copy — and is out of scope for this SDK.
