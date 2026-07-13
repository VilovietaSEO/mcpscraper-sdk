# Changelog

All notable changes to `mcpscraper-sdk` and `mcpscraper-memory-sdk` are documented here. Each entry notes which product version(s) it was verified against.

## [Unreleased]
- Initial scaffold: contracts/ (OpenAPI spec for mcp-scraper, tool manifest for mcp-memory), packages/scraper, packages/memory.

## mcpscraper-memory-sdk 0.9.0 / mcpscraper-sdk 0.10.0 / Python SDKs 0.7.0 / mcpscraper-cli 0.7.0
- Regenerated all Node, Python, CLI, and cURL bindings from the 157-tool MCP Scraper contract for the Meta media-buying release.
- Added `meta_ads_insights` to `connections.exportConnectedServiceData` / `connections.export_connected_service_data` for bounded daily account, campaign, ad-set, and ad reporting with inline-or-private-artifact delivery and resumable continuations.
- Added permission-aware connection inventory fields: verified `grantedPermissions`, `permissionVerification`, and per-tool `toolCapabilities` with required and missing OAuth grants. Unavailable tools remain discoverable in the inventory but are excluded from callable read/action lists.
- Expanded `describeServiceConnectionTool` / `describe_service_connection_tool` with exact required and missing permissions plus permission-specific blocked reasons, keeping the generated SDK aligned with the standalone MCP protocol surface outside Mastra.

## mcpscraper-memory-sdk 0.7.0 / mcpscraper-sdk 0.8.0 / Python SDKs 0.5.0 / mcpscraper-cli 0.5.0
- Regenerated the unified Node, Python, CLI, and cURL surfaces from the 156-tool MCP Scraper manifest: 71 MCP Scraper tools plus 85 mirrored memory tools.
- Added typed `connections.describeServiceConnectionTool` / `connections.describe_service_connection_tool` bindings so clients can discover the exact input schema and read/action classification for provider-native connected-service tools before calling them.
- Expanded connected-data exports to Resend with `resend_data`, `resend_emails`, `resend_received_emails`, `resend_logs`, `resend_contacts`, `resend_broadcasts`, and `resend_templates` datasets, including typed continuation and output enums.
- Expanded connection results with credential `transport`, provider/reconnect metadata, and permanently blocked administrative tool names without exposing credentials.
- Raised deterministic parity and package tests to require exact 156/156 tool-name and binding coverage across every generated surface.

## mcpscraper-memory-sdk 0.6.0 / mcpscraper-sdk 0.7.0 / Python SDKs 0.4.0 / mcpscraper-cli 0.4.0
- Regenerated the unified Node, Python, CLI, and cURL surfaces from the mcp-scraper `0.14.0` 155-tool manifest.
- Added typed `connections.exportConnectedServiceData` / `connections.export_connected_service_data` bindings for bounded Gmail, Google Calendar, and Zoom range exports with inline-or-private-artifact delivery and resumable continuations.
- Added typed `connections.renewConnectedDataDownload` / `connections.renew_connected_data_download` bindings for refreshing expiring private artifact download URLs.
- Added manifest-derived output contracts across the unified SDK so connected-data exports and all other schema-backed tools return generated TypeScript/Python output types instead of `unknown` or empty models.
- Updated the provider-neutral connection descriptions for GitHub's 27 reads and 20 gated actions; the top-level MCP catalog remains 155 tools.
- Raised deterministic parity and package tests to require exact 155/155 tool-name and binding coverage.

## mcpscraper-memory-sdk 0.5.0
- Added typed `executionMode` support for scheduled actions: create accepts `agent` or `connection_sync` (defaulting to `agent`), returns the stored mode, and list exposes the mode for every action. Aligned with the mcp-memory 1.8.0 scheduling contract.

## mcpscraper-memory-sdk 0.4.0 / mcpscraper-sdk 0.6.0 / Python SDKs 0.3.0 / mcpscraper-cli 0.3.0
- Regenerated the unified contract and every Node, Python, CLI, and cURL binding for all 153 live MCP tools.
- Added the connected-service surface: list and read tenant-owned OAuth connections, run explicitly allowlisted gated actions, send through Slack/Gmail/Calendar/Zoom, and bind exact connection tools to scheduled actions.
- Refreshed the direct Memory contract from 85 to 86 tools, adding schedule-default configuration and current scheduled-action/video schemas.
- Updated deterministic parity gates from 145 to 153 tools. Verified against mcp-scraper `0.11.0`.

## mcpscraper-sdk 0.5.0
- Added the `issues` value to `extractSite`'s `formats` enum and the resulting nullable `seoAudit` response object (31-key issues map, `linkSummary` internal/external link report, `pageMetrics`), reflecting mcp-scraper's new site-wide SEO audit.
- Added the nullable `imageAudit` response object (`rows` + `summary`) to `extractSite`; `formats: ["images"]` now performs the image audit on the synchronous path too (previously background-only).
- Added `inSitemap` (boolean|null) to `extractSite` page objects and `sitemapUrls` to its `spider` object; documented the background job's `seo-audit.json` artifact and `inSitemap` in `pages.jsonl` rows on `getExtractSiteStatus`.
- Contract bumped to 1.2.0 (additive only). Verified against mcp-scraper `0.8.0`.

## mcpscraper-memory-sdk 0.3.0 / mcpscraper-sdk 0.4.0 / Python SDKs 0.2.0 / mcpscraper-cli 0.2.0
- Added one canonical live-derived `contracts/mcp.tools.json` contract for all 145 unified MCP tools.
- Added generated, typed `McpToolsClient` namespaces with all 145 tools to both Node packages and both Python packages.
- Added `ScraperClient.tools` in Node and Python while preserving REST convenience APIs and direct 85-tool Memory clients.
- Added universal CLI discovery and invocation through `tools list`, `tools describe`, and `tools call`; all 145 wire names are reachable.
- Added a generated complete cURL catalog and deterministic live/Node/Python/CLI/cURL 145/145 release gates.
- Corrected the public REST operation count from 40 to 43.

## mcpscraper-cli 0.1.1
- Fixed npm-installed CLI execution by resolving the `.bin` symlink before checking the module entrypoint.
- Published the public CLI against `mcpscraper-sdk@0.3.0`.
- Removed the redundant direct memory SDK dependency; memory commands route through `mcpscraper-sdk`.
- Corrected Python installation documentation to use working GitHub source-package URLs until PyPI publishing is configured.

## mcpscraper-memory-sdk 0.2.0
- Expanded the generated client from 74 to 85 live memory tools.
- Added governed capture (`prepareMemoryWrite`, `validateMemoryWrite`, `memoryCapture`), canonical tag operations, vault contracts/routing, and memory graph backlinks/universe/path namespaces.
- Updated `libraryIngestTool` and `putTool` types to the live schemas from `mcpscraper-memory-tools@1.2.0` and verified against mcp-memory `1.6.0`.

## mcpscraper-sdk 0.3.0
- Updated `client.memoryTools` to the complete 85-tool contract and added typed `tags` and `graph` namespaces through `mcpscraper-memory-sdk@0.2.0`.

## mcpscraper-sdk 0.2.0
- Added `depositToVault`/`vaultName` to `extractUrl` and the `memory` response field (`VaultDepositResult`), reflecting mcp-scraper's scrape-to-vault feature.
- Added `POST /memory/mcp-call` to the contract and `client.memoryTools.*` to the SDK — all 74 memory.mcpscraper.dev tools, callable with only a scraper API key (reuses `mcpscraper-memory-sdk`'s generated namespace classes as a workspace dependency; no code duplicated).
- Verified against mcp-scraper `main` as of commit `b04db11` ("merge mcp-memory's 74 tools into the unified MCP surface") and `mcpscraper-memory-tools@1.1.0` (confirmed exact 74/74 tool-name parity against `contracts/memory.tools.json` — no changes needed there).
- `mcp-scraper-scheduler` (the new cron/automation worker mcp-memory's scheduling engine moved to) has no public API surface — confirmed via its own landing page copy — and is out of scope for this SDK.
