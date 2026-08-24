# Changelog

All notable changes to `mcpscraper-sdk` and `mcpscraper-memory-sdk` are documented here. Each entry notes which product version(s) it was verified against.

## 2026-08-23 — verified against mcp-scraper 0.63.1 / mcp-memory 1.18.1

### Added

- Added typed REST methods for direct site-export text and image reads, plus generated `site_export_read` and `site_export_image` bindings across Node, Python, CLI, and cURL surfaces.
- Added CLI `export-status`, `export-read`, and `export-image` commands; `crawl` now starts a durable export that defaults to complete JSON, acquired HTML, Markdown, and links with retry-safe idempotency.

### Changed

- Standardized REST and MCP transport timeouts at 300 seconds in the Node and Python clients and preserve the service's structured timeout/error envelope when it is available.
- Expanded extraction requests and models with HTML, media preservation, component warnings, detailed public error codes, and `refund_pending` settlement state.
- Regenerated the unified catalog at 254 tools: 153 MCP Scraper tools plus 101 mirrored Memory tools, with exact parity across every generated interface.
- Prepared `mcpscraper-memory-sdk` 0.30.0, `mcpscraper-sdk` 0.29.0, `mcpscraper-cli` 0.28.0, Python `mcpscraper-sdk` 0.28.0, and Python `mcpscraper-memory-sdk` 0.27.0.

### Fixed

- Added `site_export_format_unavailable` to the generated and runtime-safe public error enums so older exports report a detailed, non-retryable representation mismatch instead of being collapsed into a generic client error.
- Updated `mcpscraper-sdk` to resolve the current `mcpscraper-memory-sdk` workspace dependency; the stale nested 0.28.0 package silently removed five generated methods from the Node scraper surface.
- Made the public product count check derive its invariant from the canonical manifest instead of maintaining a second hardcoded tool total.

## 2026-08-21 — verified against mcp-scraper 0.62.0 / mcp-memory 1.18.1

### Added

- Added `idempotencyKey` to `extract_url`, `harvest_paa`, and `search_serp` across every generated surface.
- Added `commons_update_editorial_article`, `commons_get_proposal`, and `commons_host_image` to the unified catalog.

### Changed

- Refreshed the generated 252-tool MCP projection (was 249), updating the split to 151 MCP Scraper plus 101 mirrored Memory tools across the canonical manifest and every generated client, CLI catalog, and cURL catalog.
- Synced `extract_url` and `extract_site` descriptions with their real plain-fetch-first, browser-fallback-on-failure transport behavior.
- Synced `commons_submit_entity`'s description with its current governed-write workflow.
- Fixed a stale hardcoded tool count (`249`, and a separately stale `102` for the direct memory API's tool count in `packages/scraper-python/README.md`) across `README.md`, `packages/cli/README.md`, `packages/scraper/README.md`, `packages/scraper-python/README.md`, `packages/memory/README.md`, and `packages/memory-python/README.md`. The public-product-contract check's own count assertion (`scripts/check-public-product-contract.ts`) now derives its expected value from the manifest instead of hardcoding a second literal, so this class of drift can't silently reappear.
- Prepared `mcpscraper-memory-sdk` 0.29.0, `mcpscraper-sdk` 0.28.0, `mcpscraper-cli` 0.27.0, Python `mcpscraper-sdk` 0.27.0, and Python `mcpscraper-memory-sdk` 0.26.0.

### Note

This sync's `contracts/mcp.tools.json` source was generated locally from mcp-scraper's `codex/extract-transport-description-clarity` branch before it merged as [PR #189](https://github.com/VilovietaSEO/mcp-scraper/pull/189), so this SDK sync and that description-clarity work didn't need to happen twice. Confirmed zero diff in the tool schema/description source files between that generation point and the commit that actually merged (`b298a7ce`) and shipped as mcp-scraper 0.62.0 — this contract is accurate as published.

## 2026-08-14 — verified against mcp-scraper 0.55.0 / mcp-memory 1.17.2

### Added

- Added typed Node and Python public-error envelopes, verification-challenge and timeout helpers, and quantity-based concurrency pack and account models with actionable recovery details.
- Added a deterministic public-product convergence check covering TypeScript, Python, CLI, and cURL projections so tool inventory, search rates, concurrency packs, and vendor-neutral schemas cannot silently drift.

### Changed

- Refreshed the generated 249-tool MCP projection across the canonical manifest and generated clients while preserving the 148 MCP Scraper plus 101 mirrored Memory split.
- Updated public SDK and CLI documentation to the current 60-Credit SERP rate, 400 Credits plus 10 Credits per returned PAA question, and $5/month two-browser concurrency packs whose quantity scales slots and price linearly.
- Replaced an infrastructure-specific connected-service transport value with the stable `managed_oauth` public category across generated contracts and bindings.
- Prepared `mcpscraper-memory-sdk` 0.28.0, `mcpscraper-sdk` 0.27.0, `mcpscraper-cli` 0.26.0, and Python `mcpscraper-sdk` 0.26.0; Python `mcpscraper-memory-sdk` remains 0.25.3 because its packaged direct-Memory contract did not change.

## 2026-08-14 — verified against mcp-scraper 0.54.2 / mcp-memory 1.17.2

### Added

- Added typed bindings for the three persistent SERP identity tools and synchronized the unified catalog from 246 to 249 tools.

### Changed

- Regenerated Node, Python, CLI, and cURL contracts for the managed Google SERP/PAA transport, unchanged-query location semantics, same-page SERP feature flags, and current Maps descriptions accumulated through MCP Scraper 0.54.2.
- Updated `reddit_trending` with week, 30-day, and all-time discovery, exact quoted phrases, and the managed Google discovery contract; updated `reddit_thread` with canonical URLs and explicit normal/old Reddit retrieval sources.
- Prepared `mcpscraper-memory-sdk` 0.27.3, `mcpscraper-sdk` 0.26.3, `mcpscraper-cli` 0.25.3, and both Python packages 0.25.3.

## 2026-08-11 — verified against mcp-scraper 0.52.3 / mcp-memory 1.17.2

### Fixed

- Regenerated every unified client and catalog after the server removed the remaining anti-bot infrastructure brand from `browser_screenshot`; direct Memory bindings remain contract-identical.
- Prepared `mcpscraper-memory-sdk` 0.27.2, `mcpscraper-sdk` 0.26.2, `mcpscraper-cli` 0.25.2, and both Python packages 0.25.2.

## 2026-08-11 — verified against mcp-scraper 0.52.2 / mcp-memory 1.17.2

### Changed

- Regenerated all 246 unified MCP bindings and all 114 direct Memory bindings so embedded descriptions require hybrid Smart RAG before inventory tools for ordinary discovery; tool names and schemas are unchanged.
- Added a durable release-history link to every packaged README so npm and PyPI consumers can inspect the audience-specific SDK changelog.
- Prepared `mcpscraper-memory-sdk` 0.27.1, `mcpscraper-sdk` 0.26.1, `mcpscraper-cli` 0.25.1, and both Python packages 0.25.1.

### Fixed

- Closed the description-only contract gap left by the MCP Scraper 0.52.1 release, which updated the live servers without regenerating the SDK, CLI, and Python contract surfaces that embed tool guidance.

## 2026-08-10 — verified against mcp-scraper 0.52.0 / mcp-memory 1.15.0

### Added

- Added typed Node, Python, CLI, and cURL inputs for opt-in Google Maps listing-photo collection, owner/all scopes, bounded gallery traversal, inline image previews, and owner-scoped archives.
- Added typed website-media preservation controls and outputs for rendered/lazy-loaded media, completeness evidence, logo candidates, proof images, structured-data logos, and provenance-ranked brand colors.
- Synchronized the direct 114-tool Memory clients with the live artifact-template contract, including registered preset metadata and renderer-specific create/update inputs.

### Changed

- Regenerated all 246 unified MCP bindings from MCP Scraper 0.52.0, including contract drift accumulated since the SDK's 0.49.0 snapshot while preserving the existing tool count and method namespaces; the direct Memory surface remains at 114 tools.
- Prepared `mcpscraper-memory-sdk` 0.27.0, `mcpscraper-sdk` 0.26.0, `mcpscraper-cli` 0.25.0, and both Python packages 0.25.0.

## 2026-08-05 — verified against mcp-scraper 0.49.0 / mcp-memory 1.15.0

### Added

- Added typed Node, Python, CLI, and cURL bindings for `commons_get_entity_linkset`, including its read-only annotations and governed RFC 9264 input/output contract.
- Caught every generated client up to the full 246-tool MCP Scraper catalog, including Transparent Commons publications, X-Ray analytics, registered artifact-template examples, and the current image and scheduled-result schemas.

### Changed

- Added first-class `analytics` and `artifacts` SDK namespaces for the newly synchronized tools instead of leaving them in the fallback category.
- Prepared `mcpscraper-memory-sdk` 0.26.3, `mcpscraper-sdk` 0.25.3, `mcpscraper-cli` 0.24.3, and both Python packages 0.24.3.

## 2026-08-04 — verified against mcp-scraper 0.45.0 / mcp-memory 1.15.0

### Added

- Added governed Schema.org `LocalBusiness` subtype selection to the Local Sourcebook prepare, validate, and capture bindings for Node, Python, and the CLI contract catalog.

### Changed

- Documented the fixed 10-Credit create and 2-Credit edit prices for Local Sourcebook and Transparent Commons writes, including free validation, idempotent retry protection, and included Sourcebook acquisition.
- Prepared `mcpscraper-memory-sdk` 0.26.2, `mcpscraper-sdk` 0.25.2, `mcpscraper-cli` 0.24.2, and both Python packages 0.24.2.

## 2026-08-04 — verified against mcp-scraper 0.44.2 / mcp-memory 1.15.0

### Changed

- Updated the Local Sourcebook v2 write contract so subscribers provide only business identity and canonical tags; generated Node, Python, CLI, and cURL bindings no longer expose owner-authored listing payloads, submission revisions, or direct public-claim edits.
- Documented evidence-compiled automatic publication and refresh behavior across the generated contract surfaces.
- Prepared `mcpscraper-memory-sdk` 0.26.1, `mcpscraper-sdk` 0.25.1, `mcpscraper-cli` 0.24.1, and both Python packages 0.24.1.

## 2026-08-04 — verified against mcp-scraper 0.44.1 / mcp-memory 1.15.0

### Added

- Generated TypeScript, Python, CLI, and cURL bindings for the complete Local Sourcebook contract/tag/prepare/validate/capture/status/refresh workflow and all nine Transparent Commons search, entity, proposal, ledger, and filter tools.
- Added typed image project, folder, and asset namespaces from the direct Memory and unified MCP catalogs.

### Fixed

- Updated the live MCP manifest and drift readers to parse Streamable HTTP event-stream responses as well as plain JSON.

### Changed

- Regenerated every public client surface from the live 215-tool MCP Scraper 0.44.1 contract and the direct 114-tool Memory contract.
- Prepared `mcpscraper-memory-sdk` 0.26.0, `mcpscraper-sdk` 0.25.0, `mcpscraper-cli` 0.24.0, and both Python packages 0.24.0.

## 2026-07-30 — verified against mcp-scraper 0.42.0 / mcp-memory 1.15.0

### Added

- Generated TypeScript, Python, CLI, and cURL bindings for the Scheduled Results Inbox and versioned artifact-template contracts: template list/get/create/version/archive, cross-automation run list/get/open/unopen/archive, and scoped run-artifact view-link create/revoke.
- Added schema-derived `artifactSelection` support to scheduled-action create/update clients. `{mode:"none"}` disables only rendered HTML; `{mode:"saved_template"}` pins one exact immutable template version.

### Changed

- Expanded the direct hosted Memory contract to 102 tools and the unified MCP contract to 188 tools, with deterministic regeneration and parity checks for every public surface.
- Prepared `mcpscraper-memory-sdk` 0.25.0, `mcpscraper-sdk` 0.24.0, `mcpscraper-cli` 0.23.0, and both Python packages 0.23.0.

## 2026-07-30 — verified against mcp-scraper 0.40.3

### Security

- Node and Python scraper clients now collapse every server-side 5xx response into the first-party `service_unavailable` contract. Upstream service names, provider URLs, organization/account billing state, and unreviewed infrastructure diagnostics cannot escape through `ScraperApiError`, even if a future backend route misses its own sanitizer.
- Prepared `mcpscraper-sdk` 0.23.1 and Python `mcpscraper-sdk` 0.22.1. The CLI's existing `^0.23.0` dependency accepts the hardened Node client without a separate CLI release.

## 2026-07-28 — verified against mcp-scraper 0.39.0 / mcp-memory 1.13.0

### Added

- Typed `editorial.createReadingRoom`, `editorial.readingRoomGuide`, and `editorial.renewReadingRoomDownload` Node bindings, with matching Python, CLI, and cURL surfaces. Agents can first retrieve the editorial method, then render a source-grounded edition as a private hosted HTML artifact or a non-overwriting local stdio file.

### Changed

- Regenerated the canonical unified contract and every generated client from MCP Scraper 0.39.0: 175 tools total, split between 85 MCP Scraper tools and 90 mirrored Memory tools.
- Prepared `mcpscraper-memory-sdk` 0.24.0, `mcpscraper-sdk` 0.23.0, `mcpscraper-cli` 0.22.0, and both Python packages 0.22.0.

## 2026-07-28 — verified against mcp-scraper 0.38.0 / mcp-memory 1.13.0

### Added

- Typed `web.archiveRead` (Node) and `web.archive_read` (Python) bindings for the new `archive_read` MCP tool. It lists bounded public ZIP files, reads selected UTF-8 entries with byte-window continuation, and can preserve the complete selected file in the tenant Library vault.
- Runnable Node, Python, CLI, and cURL examples covering ZIP listing, selected-file reading, and opt-in Library deposit.

### Changed

- Regenerated the canonical unified contract and every generated client from MCP Scraper 0.38.0: 172 tools total, split between 82 scraper/browser/workflow/connection tools and 90 mirrored Memory tools.
- Prepared `mcpscraper-memory-sdk` 0.23.0, `mcpscraper-sdk` 0.22.0, `mcpscraper-cli` 0.21.0, and both Python packages 0.21.0.

## [2026-07-28] - verified against mcp-scraper 0.37.0 / mcp-memory 1.13.0

### Added

- `merge-memory-tags` in the unified MCP contract and the generated TypeScript, Python, and CLI clients. It collapses a duplicate tag into the canonical one across an account, retagging every note and recording the retired spelling as an alias.
- SDK category/legacyId mappings for `update-scheduled-action` and `list-scheduled-action-runs`, which shipped in mcp-memory but had no mapping here, so the memory manifest could not be regenerated at all until now.

### Changed

- Regenerated the unified contract from mcp-scraper 0.37.0 (previously 0.34.1) — 165 to 171 tools, memory 89 to 92. Catching up three product releases changed `search_serp`'s output contract, which now requires `resultQuality`, `degradedResult`, `degradationReasons`, and `retryRecommended`.
- The unified-bindings test now asserts against the contract's own tool count rather than a frozen literal, which had been failing since the catalog grew past 165.

## 2026-07-27 — verified against mcp-scraper 0.35.0

- Regenerated the complete 170-tool Node, Python, CLI, and cURL surfaces, including typed `web.mapWaybackSnapshots`, `directory.workflowStatus`, and `directory.locationMarkets` methods.
- Updated connected-service guidance and schemas for authenticated Zoom transcript export, server-side Gmail MIME construction, required Calendar invitees/context, and required Zoom agendas.
- Preserved the accepted Google location contract: direct egress remains the default while location supplies UULE and missing city text; optional configured-proxy controls remain available.
- Run SDK TypeScript generators, validators, and tests through Node's `--import tsx` hook so managed sandboxes do not fail on the `tsx` CLI's Unix IPC socket.
- Prepared `mcpscraper-sdk` and `mcpscraper-memory-sdk` 0.21.0, `mcpscraper-cli` 0.19.0, and both Python packages 0.19.0.

## 2026-07-24 — verified against mcp-scraper 0.34.0

- `search_serp` (and the REST `/harvest/sync` body) gains an optional `recency` window (`day`|`week`|`month`|`year`) that applies Google's past-day/week/month/year time filter. Omit for all-time.
- `reddit_trending` catches up to its live shape: added the `window` (`week`|`month`) input, raised `maxThreads` to a 40 max / 20 default (scrape-all), and the response now carries `candidatesFound`, `partial`, and `searchQuery` (was `searchUrl`). Fresh MCP client model files were generated for it (the contract had been 166 tools / one release behind; now 167).
- Added the `/reddit/trending` path to the REST OpenAPI contract (it had never been documented).
- Fixed the unified-manifest sync check, which still hardcoded `165` despite the prior "count-agnostic" pass — it now derives the expected count from the manifest itself.
- Regenerated all clients (167 tools). Published `mcpscraper-sdk` 0.20.0, `mcpscraper-memory-sdk` 0.20.0, `mcpscraper-cli` 0.18.0, Python packages 0.18.0.

## 2026-07-23 — verified against mcp-scraper 0.33.5

- Public output schemas no longer document internal diagnostic fields (per-attempt execution detail). The typed contract is leaner; response payloads are otherwise unchanged.
- Made the tool-catalog sync **count-agnostic** — adding a tool no longer requires editing hardcoded counts across the generators, parity scripts, and tests, and an unmapped tool now falls back to an `other` category with a warning instead of failing the sync.
- Regenerated all clients (166 tools). Published `mcpscraper-sdk` 0.19.0, `mcpscraper-memory-sdk` 0.19.0, `mcpscraper-cli` 0.17.0, Python packages 0.17.0.

## 2026-07-22 — verified against mcp-scraper 0.33.4

- `proxyMode` on the search and maps tools now exposes `configured` and `none` only; a prior geo-targeted option was removed upstream. Regenerated the MCP contract, OpenAPI, and all clients.
- Tightened tool and field descriptions across the contract to state intent without internal routing detail.
- Corrected two fields to match the live API: a diagnostic session-id output field is now `browserSessionId`, and a non-existent fallback flag was removed from the crawl endpoints.
- Refreshed the catalog to 166 unified tools (77 MCP Scraper + 89 memory), including the new `gmail_search_contacts`.
- Published: `mcpscraper-sdk` 0.18.0, `mcpscraper-memory-sdk` 0.18.0, `mcpscraper-cli` 0.16.0, Python packages 0.16.0.

## 2026-07-22 — verified against mcp-scraper 0.32.0

- `maps_search` gains an optional `includeServices` input and its `proxyMode` default is now `none`; regenerated the MCP contract, OpenAPI, and all clients (scraper `0.17.0`, memory `0.17.0`, cli `0.15.0`, python packages `0.15.0`).
- Reconciled a pre-existing CLI version drift (`CLI_VERSION` was `0.13.0` while `package.json` was `0.14.0`).

## 2026-07-21 — runtime 0.31.0 (Vault Taxonomy v2)
- `contracts/mcp.tools.json` resynced from mcp-scraper 0.31.0's generated manifest (165 tools): 16-vault taxonomy (new Organizations vault, Examples and Inspirations and Communication renames with permanent aliases), required/recommended vault primitives, Inbox naming, richer output schemas.
- `contracts/memory.tools.json` resynced from live memory.mcpscraper.dev (89 tools) with the same taxonomy.
- Regenerated unified MCP clients (TS/Python/CLI) and direct-memory clients; typed outputs now parse where the runtime publishes structured schemas (e.g. `search_serp`), so results are pydantic models rather than raw dicts in Python.
- Published: `mcpscraper-memory-sdk` 0.16.0, `mcpscraper-cli` 0.14.0; Python packages tagged 0.14.0. `mcpscraper-sdk` (TS scraper REST client) unchanged.

## Python SDKs 0.13.1
- Published both Python SDKs to PyPI and changed the public installation guidance from GitHub source URLs to `pip install` packages.

## mcpscraper-memory-sdk 0.15.1
- Ensure the published package builds its declared `dist` entrypoints during `prepack`; 0.15.0 is deprecated because its tarball omitted them.

## mcpscraper-memory-sdk 0.15.0 / mcpscraper-sdk 0.16.0 / Python SDKs 0.13.0 / mcpscraper-cli 0.13.0
- Regenerated the direct 89-tool Memory and complete 165-tool MCP Scraper Node, Python, CLI, and cURL clients from the live mcp-memory 1.10.0 and MCP Scraper 0.28.0 contracts.
- Added typed `access.getVaultAppLink` / `access.get_vault_app_link` and `access.revokeVaultAppLink` / `access.revoke_vault_app_link` bindings for the independent mobile Vault App link lifecycle.

## mcpscraper-sdk 0.15.1 / mcpscraper-cli 0.12.1
- Added mandatory prepack builds so published npm tarballs always include the declared `dist` entrypoints.
- Replaced and deprecated the incomplete `mcpscraper-sdk` 0.15.0 and `mcpscraper-cli` 0.12.0 tarballs.

## mcpscraper-memory-sdk 0.14.0 / mcpscraper-sdk 0.15.0 / Python SDKs 0.12.0 / mcpscraper-cli 0.12.0
- Regenerated the complete 163-tool Node, Python, CLI, and cURL surfaces for MCP Scraper 0.26.0, including the typed `connections.testServiceConnection` / `connections.test_service_connection` health check and the current 87-tool Memory contract.
- Updated SDK validation and public inventory copy to the canonical split of 76 scraper/browser/workflow/billing/connection tools plus 87 Memory tools.

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
- Updated `POST /harvest/sync`'s `serpOnly` description to match MCP Scraper 0.21.3's adaptive SERP pricing: 4 credits when served headless (typical), 14 credits if a block forces a fallback retry (overestimate refunded). No shape change — description-only.

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
