# All 331 MCP tools with cURL

This catalog is generated from `contracts/mcp.tools.json`. Every listed tool is callable through the same JSON-RPC endpoint with an `MCP_SCRAPER_API_KEY`.

## List all tools

```bash
curl --retry 3 --retry-all-errors --retry-delay 1 https://mcpscraper.dev/mcp \
  -H "x-api-key: $MCP_SCRAPER_API_KEY" \
  -H "content-type: application/json" \
  -H "accept: application/json, text/event-stream" \
  --data '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

## Call any tool

Set `TOOL_NAME` and `TOOL_ARGS` to any entry below:

```bash
TOOL_NAME="memory-search"
TOOL_ARGS='{"query":"vault routing"}'

jq -n --arg name "$TOOL_NAME" --argjson args "$TOOL_ARGS" \
  '{jsonrpc:"2.0",id:1,method:"tools/call",params:{name:$name,arguments:$args}}' \
  | curl https://mcpscraper.dev/mcp \
      -H "x-api-key: $MCP_SCRAPER_API_KEY" \
      -H "content-type: application/json" \
      -H "accept: application/json, text/event-stream" \
      --data-binary @-
```

## Bulk connected-data export

Fetch a bounded Gmail, Google Calendar, Google Search Console, Zoom, Meta Marketing, or Resend range in one call. Provider pagination happens server-side; large results become private downloadable artifacts. Search Console supports `search_console_performance` across every accessible property. Meta supports `meta_ads_insights` for daily account, campaign, ad-set, and ad reporting across connected ad accounts. Resend supports the aggregate `resend_data` dataset plus sent mail, received mail, logs, contacts, broadcasts, and templates individually.

```bash
jq -n --arg connectionId "$CONNECTION_ID" \
  '{jsonrpc:"2.0",id:1,method:"tools/call",params:{name:"export_connected_service_data",arguments:{connectionId:$connectionId,dataset:"emails",lastDays:7}}}' \
  | curl https://mcpscraper.dev/mcp \
      -H "x-api-key: $MCP_SCRAPER_API_KEY" \
      -H "content-type: application/json" \
      -H "accept: application/json, text/event-stream" \
      --data-binary @-
```

For a fresh Search Console API extract, set `dataset` to `search_console_performance` and choose the requested range with `lastDays` or `from`/`to`. For persisted scheduled data, get the connection `tableName` from `list_service_connections`, inspect/filter it with `table-describe` and `table-query`, or call `export_search_console_table_data` for a private filtered JSONL artifact.

If a signed artifact URL expires, call `renew_connected_data_download` with the returned `artifactId`. If an export is partial, pass its complete `continuation` object unchanged on the next export call.

## Complete Gmail workflow

The selection receipt is immutable. Keep `selectionId`, `selectionSha256`, and `count` together, then reuse that exact receipt for preview/export or a reviewed Memory import. `gmail_import_status` only observes progress; call `gmail_import_to_memory` again with the same idempotency key when `nextAction` says to resume.

```bash
CONNECTION_ID="gmail_connection_id"
QUERY='has:attachment newer_than:30d'

call_tool() {
  jq -n --arg name "$1" --argjson args "$2" \
    '{jsonrpc:"2.0",id:1,method:"tools/call",params:{name:$name,arguments:$args}}' \
  | curl -sS https://mcpscraper.dev/mcp \
      -H "x-api-key: $MCP_SCRAPER_API_KEY" \
      -H "content-type: application/json" \
      -H "accept: application/json, text/event-stream" \
      --data-binary @-
}

SEARCH=$(call_tool gmail_search_messages "$(jq -n --arg connectionId "$CONNECTION_ID" --arg query "$QUERY" '{connectionId:$connectionId,query:$query,limit:25}')")
SELECTION=$(call_tool gmail_prepare_selection "$(jq -n --arg connectionId "$CONNECTION_ID" --arg query "$QUERY" '{connectionId:$connectionId,purpose:"memory_import",source:{kind:"query",query:$query}}')")
# Parse the JSON tool result for selectionId, selectionSha256, and count before continuing.
# Prepare the reviewed route and attachment plan, then call gmail_import_to_memory with one stable idempotencyKey.
# If the result requests continuation, call gmail_import_to_memory again with the same importPlanId and key.
# Call gmail_import_status with the returned ingestId until its status is terminal.
```

A complete runnable Node example, including attachment preservation and resume/status handling, is checked in at `examples/gmail-complete-workflow.mjs`.

## Reversible Gmail bulk management

Use `gmail_prepare_selection` with `purpose:"mailbox_action"`, review its exact receipt, then call `gmail_bulk_manage_messages` with the unchanged receipt and a stable idempotency key. A runnable label add/remove example is checked in at `examples/gmail-bulk-manage.mjs`.

> **Permanent delete is separate and irreversible.** `gmail_bulk_delete_messages` requires the unchanged selection receipt, an idempotency key, and `confirmPermanentDelete:true`. Never use it for cleanup unless every selected message was created specifically as a disposable fixture.

## Complete catalog (331)

## access

- `access-accept-share` — Accept Shared Note
- `access-approve-sender` — Approve Sender
- `access-decline-share` — Decline Shared Note
- `access-inbox-settings` — Inbox Settings
- `access-invite-account` — Invite To Account
- `access-issue-key` — Issue API Key
- `access-list-approved-senders` — List Approved Senders
- `access-list-keys` — List API Keys
- `access-note-inbox` — Note Inbox
- `access-remove-approved-sender` — Remove Approved Sender
- `access-revoke-key` — Revoke API Key
- `access-revoke-share` — Revoke Note Share
- `access-set-scope` — Set Key Scope / Plan
- `access-share-note` — Share Note
- `access-share-vault` — Share Vault Entitlement
- `access-swap-vault` — Swap Active Vault
- `access-switch-account` — Switch Active Account
- `access-unlink-share` — Unlink Shared Note
- `get-chat-link` — Get Chat Link
- `get-vault-app-link` — Get Vault App Link
- `revoke-chat-link` — Revoke Chat Link
- `revoke-vault-app-link` — Revoke Vault App Link
- `set-agent-identity` — Set Agent Identity

## vaults

- `add-vault` — Add Vault
- `create-secure-vault` — Create Secure Vault
- `delete-vault` — Delete Vault
- `get-vault-contract` — Get Vault Contract
- `list-shared-with-me` — List Shared With Me
- `list-vaults` — List Vaults
- `provision-defaults` — Provision Default Vaults
- `route-memory` — Route Memory

## analytics

- `analytics_apply_crm_pipeline_mapping` — Push CRM Pipeline Event
- `analytics_approve_crm_provisioning` — Approve CRM Provisioning
- `analytics_archive_event_definition` — Archive Browser Event Definition
- `analytics_cancel_crm_sync` — Cancel CRM Synchronization
- `analytics_create_activation_destination` — Create Ad Activation Destination
- `analytics_create_campaign_link` — Create Campaign Link
- `analytics_create_connection` — Create X-Ray Connection
- `analytics_create_conversion_rule` — Create Conversion Rule
- `analytics_create_event_definition` — Create Browser Event Definition
- `analytics_create_export` — Create Analytics Export
- `analytics_create_form` — Create Pixel-linked Form
- `analytics_create_funnel` — Create Lead Funnel
- `analytics_create_lead_score` — Create Lead Score
- `analytics_create_prediction_target` — Create Prediction Target
- `analytics_create_saved_view` — Create Saved Analytics View
- `analytics_delete_privacy_subject` — Delete Privacy Subject
- `analytics_delete_saved_view` — Delete Saved Analytics View
- `analytics_discover_activation_assets` — Discover Ad Destination Assets
- `analytics_discover_crm_capabilities` — Discover CRM Capabilities
- `analytics_discover_crm_sync_objects` — Discover CRM Sync Objects
- `analytics_export_privacy_subject` — Export Privacy Subject
- `analytics_get_acquisition` — Analytics Acquisition
- `analytics_get_business_metrics` — Analytics Business Metrics
- `analytics_get_candidate_coverage` — Get Candidate Coverage
- `analytics_get_channel_breakdown` — Analytics Channel Breakdowns
- `analytics_get_consent_coverage` — Get Consent Coverage
- `analytics_get_content` — Analytics Content
- `analytics_get_conversions` — Analytics Conversions
- `analytics_get_coverage` — Get Attribution Coverage
- `analytics_get_crm_sync_status` — Get CRM Sync Status
- `analytics_get_dimensions` — Analytics Dimensions
- `analytics_get_entitlement` — Get X-Ray Pixel Access
- `analytics_get_events` — Analytics Events
- `analytics_get_forecast` — Analytics Forecast
- `analytics_get_funnel` — Get Lead Funnel Report
- `analytics_get_health` — Analytics Pixel Health
- `analytics_get_onboarding_state` — Get X-Ray Setup State
- `analytics_get_overview` — Analytics Overview
- `analytics_get_paths` — Analytics Conversion Paths
- `analytics_get_person_journey` — Get Person Journey
- `analytics_get_prediction_eligibility` — Get Prediction Eligibility
- `analytics_get_session_timeline` — Get Session Timeline
- `analytics_get_timeseries` — Analytics Timeseries
- `analytics_get_visitor_journey` — Get Visitor Journey
- `analytics_import_crm_csv` — Import CRM CSV
- `analytics_list_activation_destinations` — List Ad Activation Destinations
- `analytics_list_activation_receipts` — List Ad Activation Receipts
- `analytics_list_campaign_links` — List Campaign Links
- `analytics_list_connections` — List X-Ray Connections
- `analytics_list_conversion_rules` — List Conversion Rules
- `analytics_list_crm_capabilities` — List CRM Capabilities
- `analytics_list_crm_imports` — List CRM Imports
- `analytics_list_event_definitions` — List Browser Event Definitions
- `analytics_list_forms` — List Analytics Forms
- `analytics_list_funnels` — List Lead Funnels
- `analytics_list_inference_review` — List Inference Review
- `analytics_list_lead_scores` — List Lead Scores
- `analytics_list_namespace_sources` — List Identity Namespace Sources
- `analytics_list_pixels` — List Analytics Pixels
- `analytics_list_prediction_targets` — List Prediction Targets
- `analytics_list_saved_views` — List Saved Analytics Views
- `analytics_list_sessions` — List X-Ray Sessions
- `analytics_list_sites` — List Analytics Businesses
- `analytics_list_visitors` — List X-Ray Visitors
- `analytics_plan_crm_provisioning` — Plan CRM Provisioning
- `analytics_reconcile_connection` — Reconcile X-Ray Connection
- `analytics_record_external_event` — Record Server Event
- `analytics_retry_activation_delivery` — Retry Ad Activation Delivery
- `analytics_start_crm_sync` — Start Inbound CRM Synchronization
- `analytics_sync_crm_person` — Push Confirmed Person to CRM
- `analytics_test_activation_destination` — Test Ad Activation Destination
- `analytics_test_crm_provisioning` — Test CRM Provisioning
- `analytics_test_crm_sync_mapping` — Test CRM Sync Mapping
- `analytics_test_event_definition` — Test Browser Event Definition
- `analytics_test_funnel` — Test Lead Funnel
- `analytics_update_crm_sync_schedule` — Update CRM Sync Schedule
- `analytics_update_event_definition` — Update Browser Event Definition
- `analytics_update_onboarding_preferences` — Update X-Ray Setup Preferences
- `analytics_validate_activation_mapping` — Validate Activation Event Mapping
- `analytics_withdraw_consent` — Withdraw Analytics Consent
- `analytics_list_crm_outbound_policies` — List CRM Outbound Policies
- `analytics_list_crm_outbound_receipts` — List CRM Outbound Receipts
- `analytics_upsert_crm_outbound_policy` — Configure CRM Outbound Policy
- `analytics_list_journeys` — List X-Ray Journeys

## web

- `analyze_site_similarity` — Rendered Site Content Similarity
- `archive_read` — List or Read ZIP Archive
- `audit_site` — Technical SEO Audit
- `check_site_export` — Check Site Export
- `diff_page` — Page Change Check
- `extract_site` — Multi-Page Site Content Crawl
- `extract_url` — Single URL Extract
- `map_site_urls` — Site URL Map
- `map_wayback_snapshots` — Wayback Snapshot Inventory
- `site_export_image` — Read Site Export Image
- `site_export_read` — Read Site Export Page

## schedule

- `archive_artifact_template` — Archive Template
- `archive_scheduled_run` — Archive Scheduled Result
- `create_artifact_template` — Save Template
- `create_scheduled_run_view_link` — Create Scheduled Result View Link
- `create-scheduled-action` — Create Scheduled Action
- `delete-scheduled-action` — Delete Scheduled Action
- `get_artifact_template` — Get Template
- `get_scheduled_run` — Get Scheduled Result
- `get-schedule-link` — Get Schedule Link
- `get-schedule-status` — Get Schedule Status
- `list_artifact_templates` — Search Templates
- `list_scheduled_runs` — List Scheduled Results
- `list-scheduled-actions` — List Scheduled Actions
- `mark_scheduled_run_opened` — Mark Scheduled Result Opened
- `mark_scheduled_run_unopened` — Mark Scheduled Result Unopened
- `pause-scheduled-action` — Pause Scheduled Action
- `propose-scheduled-action` — Propose Scheduled Action
- `resume-scheduled-action` — Resume Scheduled Action
- `revoke_scheduled_run_view_link` — Revoke Scheduled Result View Link
- `revoke-schedule-link` — Revoke Schedule Link
- `set-schedule-defaults` — Set Schedule Defaults
- `set-schedule-entitlement` — Set Schedule Entitlement
- `update_artifact_template` — Update Template
- `update-scheduled-action` — Update Scheduled Action

## browser

- `browser_click` — Click
- `browser_close` — Close Browser Session
- `browser_extension_delete` — Remove Browser Extension
- `browser_extension_import` — Add Browser Extension
- `browser_extension_list` — List Browser Extensions
- `browser_goto` — Navigate To URL
- `browser_list_replays` — List Replay Videos
- `browser_list_sessions` — List Browser Sessions
- `browser_locate` — Locate DOM Targets
- `browser_open` — Open Browser Session
- `browser_press` — Press Keys
- `browser_profile_connect` — Save a Site Login to a Profile
- `browser_profile_list` — List Saved Logins in a Profile
- `browser_read` — Read Page Text + Elements
- `browser_replay_annotate` — Annotate Replay MP4
- `browser_replay_download` — Download Replay MP4
- `browser_replay_mark` — Mark Replay Annotation
- `browser_replay_start` — Start Recording
- `browser_replay_stop` — Stop Recording
- `browser_screenshot` — See Page (Screenshot + Elements)
- `browser_scroll` — Scroll
- `browser_type` — Type Text

## memory

- `bulk-delete-notes` — Bulk Delete Notes
- `delete-note` — Delete Memory Note
- `memory-export` — Export Vault
- `memory-get` — Get Memory Note
- `memory-list` — List Memory Notes
- `memory-put` — Put Memory Note
- `memory-search` — Hybrid Smart RAG Memory Search
- `memory-suggest` — Suggest Notes (typeahead)
- `memory-upload` — Upload Document to Vault

## connections

- `call_service_connection_action` — Run Connected Service Action
- `describe_service_connection_tool` — Describe Connected Service Tool
- `export_connected_service_data` — Export Connected Service Data
- `export_search_console_table_data` — Download Filtered Search Console Table Data
- `gmail_search_contacts` — Search Gmail Contacts
- `gmail_send_message` — Send Gmail Message
- `google_calendar_create_event` — Create Calendar Event
- `import_service_connection_to_memory` — Import Connected Service Snapshot to Memory
- `list_service_connections` — List Connected Services
- `meta_ad_creative_media` — View Meta Ad Creative Media
- `read_service_connection` — Read Connected Service
- `renew_connected_data_download` — Renew Connected Data Download
- `set_scheduled_action_connections` — Set Scheduled Action Connections
- `slack_send_message` — Send Slack Message
- `test_service_connection` — Test Connected Service
- `zoom_create_meeting` — Create Zoom Meeting
- `gmail_bulk_delete_messages` — Permanently Delete Gmail Messages
- `gmail_bulk_manage_messages` — Manage Gmail Messages in Bulk
- `gmail_export_selection` — Export Gmail Selection
- `gmail_get_attachment` — Open Gmail Attachment
- `gmail_get_message` — Read Full Gmail Message
- `gmail_import_status` — Get Gmail Memory Import Status
- `gmail_import_to_memory` — Import Gmail Selection to Memory
- `gmail_prepare_memory_import` — Plan Gmail Import to Memory
- `gmail_prepare_selection` — Prepare Gmail Selection
- `gmail_search_messages` — Search Gmail Messages

## serpIntelligence

- `capture_serp_page_snapshots` — SERP Intelligence Page Snapshots
- `capture_serp_snapshot` — SERP Intelligence Snapshot

## commons

- `commons_claim_publication` — Claim Transparent Commons Publication
- `commons_get_entity` — Transparent Commons Entity Lookup
- `commons_get_entity_ledger` — Transparent Commons Contribution Ledger
- `commons_get_entity_linkset` — Transparent Commons RFC 9264 Linkset
- `commons_get_proposal` — Transparent Commons Proposal Status
- `commons_get_publication` — Get Transparent Commons Publication
- `commons_host_image` — Host a Transparent Commons Image
- `commons_list_filters` — Transparent Commons List Saved Filters
- `commons_list_needs_links` — Transparent Commons Needs-Link Backlog
- `commons_prepare_entity` — Transparent Commons Prepare Entity
- `commons_prepare_publication` — Prepare Transparent Commons Publication
- `commons_publish_editorial` — Publish Transparent Commons Editorial Edition
- `commons_save_filter` — Transparent Commons Saved MCP Filter
- `commons_search_entities` — Transparent Commons Entity Search
- `commons_submit_entity` — Transparent Commons Governed Entity Write
- `commons_update_editorial_article` — Edit One Transparent Commons Article
- `commons_validate_entity` — Transparent Commons Validate Entity
- `commons_validate_publication` — Validate Transparent Commons Publication

## storage

- `cost-usage` — Cost & Usage
- `storage-usage` — Storage Usage

## editorial

- `create_editorial_reading_room` — Create Editorial Reading Room
- `editorial_reading_room_guide` — Editorial Reading Room Guide
- `renew_editorial_reading_room_download` — Renew Editorial Reading Room Download

## channels

- `create-channel` — Create Channel
- `get-message-note` — Get Message Attachment
- `list-channel-members` — List Channel Members
- `list-channel-messages` — List Channel Messages
- `my-mentions` — My Mentions
- `poll-channel` — Poll Channel
- `post-message` — Post Message
- `react-message` — React To Message
- `remove-channel-member` — Remove Channel Member
- `reply-message` — Reply To Message

## webhooks

- `create-webhook` — Create Webhook
- `list-webhooks` — List Webhooks
- `revoke-webhook` — Revoke Webhook

## billing

- `credits_info` — MCP Scraper Credits & Costs

## directory

- `directory_workflow` — Directory Workflow: Markets + Maps
- `directory_workflow_status` — Directory Workflow Status
- `get-local-sourcebook-contract` — Get Local Sourcebook Contract
- `list-local-sourcebook-tags` — List Local Sourcebook Tags
- `local_sourcebook_refresh` — Refresh a Local Sourcebook Listing
- `local_sourcebook_submission_status` — Local Sourcebook Submission Status
- `local-sourcebook-capture` — Capture Governed Local Sourcebook Listing
- `location_markets` — Hosted US Markets + ZIP Groups
- `prepare-local-sourcebook-write` — Prepare Local Sourcebook Write
- `resolve-local-sourcebook-tags` — Resolve Local Sourcebook Tags
- `validate-local-sourcebook-write` — Validate Local Sourcebook Write

## facebook

- `facebook_ad_search` — Facebook Ad Library Search
- `facebook_ad_transcribe` — Facebook Ad Transcription
- `facebook_page_intel` — Facebook Advertiser Ad Intel
- `facebook_video_transcribe` — Facebook Organic Video Transcription

## facts

- `fact-history` — Fact History
- `record-fact` — Record Fact

## reviews

- `g2_reviews` — G2 Review Harvest
- `trustpilot_reviews` — Trustpilot Review Harvest

## artifacts

- `get_artifact_template_example` — Preview Template Example
- `report_artifact_read` — Read Stored Artifact

## googleAds

- `google_ads_page_intel` — Google Ads Advertiser Intel
- `google_ads_search` — Google Ads Transparency Search
- `google_ads_transcribe` — Google Ad Video Transcription

## search

- `harvest_paa` — Google PAA + SERP Harvest
- `search_serp` — Google SERP Lookup
- `serp_identity_create` — Create and Take Over Persistent SERP Identity
- `serp_identity_delete` — Delete Persistent SERP Identity
- `serp_identity_list` — List Persistent SERP Identities

## images

- `image_asset_delete` — Delete Image Asset
- `image_asset_get` — Get Image Asset
- `image_asset_list` — List Image Assets
- `image_asset_move` — Move Image Asset
- `image_asset_save` — Save Image Asset
- `image_asset_search` — Search Image Assets
- `image_folder_create` — Create Image Folder
- `image_folder_list` — List Image Folders
- `image_project_create` — Create Image Project
- `image_project_list` — List Image Projects

## instagram

- `instagram_media_download` — Instagram Post/Reel Media Download
- `instagram_profile_content` — Instagram Profile Content Discovery

## leads

- `lead_list_enrich` — Enrich a Lead List
- `lead_list_enrich_status` — Lead List Enrichment Status
- `lead_list_import` — Import a Lead List
- `lead_list_upload_start` — Upload a Lead List

## library

- `library-ingest` — Library Ingest

## tags

- `list-memory-tags` — List Memory Tags
- `merge-memory-tags` — Merge Memory Tags
- `resolve-memory-tags` — Resolve Memory Tags
- `upsert-memory-tag` — Upsert Memory Tag

## maps

- `maps_place_intel` — Google Maps Business Profile Details
- `maps_search` — Google Maps Business Search

## graph

- `memory-backlinks` — Memory Backlinks
- `memory-graph-path` — Memory Graph Path
- `memory-graph-universe` — Memory Graph Universe

## capture

- `memory-capture` — Capture Governed Memory
- `memory-questions` — Daily Memory Questions
- `prepare-memory-write` — Prepare Memory Write
- `validate-memory-write` — Validate Memory Write

## workflows

- `query_fanout_workflow` — Capture AI Search Fan-Out
- `rank_tracker_workflow` — Rank Tracker Blueprint Builder
- `workflow_artifact_read` — Read Workflow Artifact
- `workflow_list` — Workflow Catalog
- `workflow_run` — Run Workflow
- `workflow_status` — Workflow Status
- `workflow_step` — Advance Workflow Step
- `workflow_suggest` — Workflow Intent Router

## reddit

- `reddit_thread` — Reddit Thread + Comments
- `reddit_trending` — Reddit Trending

## tables

- `table-create` — Create Table
- `table-delete-rows` — Delete Table Rows
- `table-describe` — Describe Table
- `table-drop` — Drop Table
- `table-insert-rows` — Insert Table Rows
- `table-list` — List Tables
- `table-query` — Query Table

## recall

- `temporal-recall` — Temporal Memory Recall

## video

- `video_frame_analysis` — Video Breakdown (frame-by-frame + transcript)
- `video_frame_analysis_status` — Video Breakdown Status
- `video-analyze-start` — Start Video Breakdown
- `video-analyze-status` — Video Breakdown Status

## youtube

- `youtube_harvest` — YouTube Video Harvest
- `youtube_transcribe` — YouTube Transcription

## other

- `harvest_paa_start` — Start Durable Google PAA Harvest
- `harvest_paa_status` — Check Durable Google PAA Harvest
