# Changelog

All notable changes to `mcpscraper-sdk` and `mcpscraper-memory-sdk` are documented here. Each entry notes which product version(s) it was verified against.

## [Unreleased]
- Initial scaffold: contracts/ (OpenAPI spec for mcp-scraper, tool manifest for mcp-memory), packages/scraper, packages/memory.

## mcpscraper-sdk 0.14.1
- Documented the six live Google Search Console API batch tools released with MCP Scraper 0.24.0, including exact read/action routing, bounded inputs, per-item receipts, destructive dry-run confirmation, and scheduled-agent availability.
- Clarified that provider-native batches use the existing schema-discovered connection bridge and do not require database persistence or regenerated SDK methods.

## mcpscraper-memory-sdk 0.13.0 / mcpscraper-sdk 0.14.0 / Python SDKs 0.11.0 / mcpscraper-cli 0.11.0
- Regenerated the complete 160-tool Node, Python, CLI, and cURL surfaces against MCP Scraper 0.23.0.
- Added typed `connections.exportSearchConsoleTableData` / `connections.export_search_console_table_data` methods for private, server-filtered JSONL downloads from scheduled Search Console tables.
- Documented the AI-safe workflow distinction: live API export for fresh data, `connection_sync` for scheduling, `tableName` plus table tools for persisted filtering, and the new export method for downloading filtered stored rows.

## mcpscraper-memory-sdk 0.12.0 / mcpscraper-sdk 0.13.0 / Python SDKs 0.10.0 / mcpscraper-cli 0.10.0
- Added `search_console_performance` to the generated Node, Python, and CLI connected-data export input, continuation, and output enums.
- Regenerated the rich 159-tool unified contract from MCP Scraper 0.21.5 without dropping output schemas.
- Added Search Console examples for immediate, scheduled, and private Memory delivery to the public SDK and cURL guidance.

## mcpscraper-memory-sdk 0.11.4 / mcpscraper-sdk 0.12.4 / mcpscraper-cli 0.9.3
- Regenerated the unified Node, Python-source, CLI, and cURL bindings from MCP Scraper 0.21.4's rich 159-tool manifest while preserving complete input and output schemas for SDK consumers.
- Added retry-safe Node and Python convenience methods for `POST /serp-intelligence/capture`: optional `idempotencyKey` / `idempotency_key` inputs plus `captureWithReceipt` / `capture_with_receipt` methods that expose the server-accepted key. The OpenAPI contract now documents the request/response headers and `409 idempotency_conflict` response.
- Corrected the capture response billing contract so `billing.creditsUsed` is required and removed body-only request/job identifiers that the endpoint does not return.
- Corrected page-snapshot inputs so callers must provide exactly one of `urls` or structured `targets`; structured targets now require a URL and reject unknown fields.
- Corrected `POST /serp-intelligence/capture` billing documentation: the service holds 14 Credits and settles to 4 for headless execution or 14 for headful escalation.
- Documented optional embedded page snapshots at 1 Credit per attempted URL, with requested capacity held up front and unused capacity refunded.

## mcpscraper-sdk 0.12.3
- Updated `POST /harvest/sync`'s `serpOnly` description to match MCP Scraper 0.21.3's adaptive SERP pricing: 4 credits when served headless (typical), 14 credits if a CAPTCHA/block forces a headful retry (overestimate refunded). No shape change — description-only.

## mcpscraper-memory-sdk 0.11.3 / mcpscraper-sdk 0.12.2 / Python SDKs 0.9.2 / mcpscraper-cli 0.9.2
- Regenerated the direct Memory and unified 159-tool Node, Python, CLI, and cURL bindings against mcp-memory 1.9.1 and MCP Scraper 0.21.2.
- Added current paid-plan scheduling access and machine-readable denial fields to the generated scheduled-action models while retaining the shared 75-Credit base charge and 1.5-times OpenRouter agent-usage policy.
- Reframed the legacy schedule entitlement operation as admin credential provisioning and historical-row recovery; its former enablement and quota inputs are now optional migration-only values.
- Removed the obsolete generated `not_enabled` / scheduling-subscription denial description from Python `create_scheduled_action`; creation now reports the current machine-readable plan or Credit denial returned by the live service.

## mcpscraper-memory-sdk 0.11.2 / mcpscraper-sdk 0.12.1 / Python SDKs 0.9.1 / mcpscraper-cli 0.9.1
- Regenerated every Node, Python, CLI, and cURL binding from the 159-tool MCP Scraper 0.21.0 contract and the live 87-tool mcp-memory 1.9.0 contract.
- Replaced the old Scheduled Actions subscription contract with the unified policy: 75 Credits per started run, plus agent model usage at 1.5 times OpenRouter's actual reported cost.
- Corrected public Credit-rate metadata to the production conversion of 100 milli-Credits per Credit and synchronized the documented scraper, browser, social, transcription, review, and video-analysis rates.
- Documented current integration charging accurately: OAuth connect and reconnect have no extra Credit cost; direct connected-service reads, enabled actions, and exports have no separate connection-operation debit; scheduled and separately metered tool work retain their published prices.

## mcpscraper-memory-sdk 0.11.1 / mcpscraper-sdk 0.12.0 / Python SDKs 0.9.0 / mcpscraper-cli 0.9.0
- Added the typed `web.checkSiteExport` / `web.check_site_export` binding — polls a background `extract_site`/`audit_site` job and returns `bundleUrl`/`bundleBytes` once the export zip is ready.
- `extract_site`/`audit_site` requests gain `downloadImages` — downloads every discovered image as a real file into the export bundle (under `images/<page>/`), not just image URLs/stats. OFF by default; implies `background` regardless of the `background` flag since a whole-site image download is too slow to run inline. Capped at 20 images/page and 500/site.
- Regenerated the unified Node, Python, CLI, and cURL surfaces from the 159-tool MCP Scraper 0.20.0 contract.
- Fixed a stale nested `node_modules/mcpscraper-memory-sdk` copy in `packages/scraper` that was shadowing the correct hoisted workspace version — this was also the actual root cause of the previously-flagged `meta_ad_creative_media` parity gap, not a separate bug.

## mcpscraper-memory-sdk 0.11.0
- Added the typed `memory.bulkDeleteNotes` binding — deletes notes in one vault matching ANDed column filters (path/title/kind/source/captured_at/created_at/updated_at/revision, with a right-anchored `prefix` op alongside `eq`/`neq`/`gt`/`gte`/`lt`/`lte`/`like`/`in`) plus an optional ORed tag match. Defaults to a dry-run preview (match count + up to 20 sample notes); `dryRun: false` is required to actually delete. Verified against mcp-memory 1.8.1.

## mcpscraper-memory-sdk 0.10.0 / mcpscraper-sdk 0.11.0 / Python SDKs 0.8.0 / mcpscraper-cli 0.8.0
- Added the typed `connections.metaAdCreativeMedia` / `connections.meta_ad_creative_media` binding for connected Meta ad images, videos, organic-post resolution, transcription handoff, and frame-analysis handoff.
- Preserved full MCP content results with `callToolResult` in Node and `call_tool_result` in Python so native image, audio, and embedded-resource blocks are available to SDK callers without breaking legacy parsed calls.
- Made the CLI save inline MCP media blocks to private local files and print safe paths/metadata instead of base64 payloads.
- Regenerated Node, Python, CLI, and cURL bindings from the 158-tool MCP Scraper 0.19.0 contract.

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
