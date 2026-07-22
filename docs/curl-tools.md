# All 166 MCP tools with cURL

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

## Complete catalog (166)

## search

- `harvest_paa` — Google PAA + SERP Harvest
- `search_serp` — Google SERP Lookup

## web

- `extract_url` — Single URL Extract
- `diff_page` — Page Change Check
- `map_site_urls` — Site URL Map
- `extract_site` — Multi-Page Site Content Crawl
- `audit_site` — Technical SEO Audit
- `check_site_export` — Check Site Export

## youtube

- `youtube_harvest` — YouTube Video Harvest
- `youtube_transcribe` — YouTube Transcription

## facebook

- `facebook_page_intel` — Facebook Advertiser Ad Intel
- `facebook_ad_search` — Facebook Ad Library Search
- `facebook_ad_transcribe` — Facebook Ad Transcription
- `facebook_video_transcribe` — Facebook Organic Video Transcription

## reddit

- `reddit_thread` — Reddit Thread + Comments

## video

- `video_frame_analysis` — Video Breakdown (frame-by-frame + transcript)
- `video_frame_analysis_status` — Video Breakdown Status
- `video-analyze-start` — Start Video Breakdown
- `video-analyze-status` — Video Breakdown Status

## googleAds

- `google_ads_search` — Google Ads Transparency Search
- `google_ads_page_intel` — Google Ads Advertiser Intel
- `google_ads_transcribe` — Google Ad Video Transcription

## instagram

- `instagram_profile_content` — Instagram Profile Content Discovery
- `instagram_media_download` — Instagram Post/Reel Media Download

## maps

- `maps_place_intel` — Google Maps Business Profile Details
- `maps_search` — Google Maps Business Search

## reviews

- `trustpilot_reviews` — Trustpilot Review Harvest
- `g2_reviews` — G2 Review Harvest

## directory

- `directory_workflow` — Directory Workflow: Markets + Maps

## workflows

- `workflow_list` — Workflow Catalog
- `workflow_suggest` — Workflow Intent Router
- `workflow_run` — Run Workflow
- `workflow_step` — Advance Workflow Step
- `workflow_status` — Workflow Status
- `workflow_artifact_read` — Read Workflow Artifact
- `rank_tracker_workflow` — Rank Tracker Blueprint Builder
- `query_fanout_workflow` — Capture AI Search Fan-Out

## artifacts

- `report_artifact_read` — Read Report Artifact

## billing

- `credits_info` — MCP Scraper Credits & Costs

## connections

- `list_service_connections` — List Connected Services
- `test_service_connection` — Test Connected Service
- `slack_send_message` — Send Slack Message
- `gmail_send_message` — Send Gmail Message
- `google_calendar_create_event` — Create Calendar Event
- `zoom_create_meeting` — Create Zoom Meeting
- `read_service_connection` — Read Connected Service
- `meta_ad_creative_media` — View Meta Ad Creative Media
- `import_service_connection_to_memory` — Import Connected Service Snapshot to Memory
- `describe_service_connection_tool` — Describe Connected Service Tool
- `export_connected_service_data` — Export Connected Service Data
- `export_search_console_table_data` — Download Filtered Search Console Table Data
- `renew_connected_data_download` — Renew Connected Data Download
- `call_service_connection_action` — Run Connected Service Action
- `set_scheduled_action_connections` — Set Scheduled Action Connections
- `gmail_search_contacts` — Search Gmail Contacts

## serpIntelligence

- `capture_serp_snapshot` — SERP Intelligence Snapshot
- `capture_serp_page_snapshots` — SERP Intelligence Page Snapshots

## browser

- `browser_profile_connect` — Save a Site Login to a Profile
- `browser_profile_list` — List Saved Logins in a Profile
- `browser_extension_import` — Add Browser Extension
- `browser_extension_list` — List Browser Extensions
- `browser_extension_delete` — Remove Browser Extension
- `browser_open` — Open Browser Session
- `browser_screenshot` — See Page (Screenshot + Elements)
- `browser_read` — Read Page Text + Elements
- `browser_locate` — Locate DOM Targets
- `browser_goto` — Navigate To URL
- `browser_click` — Click
- `browser_type` — Type Text
- `browser_scroll` — Scroll
- `browser_press` — Press Keys
- `browser_replay_start` — Start Recording
- `browser_replay_stop` — Stop Recording
- `browser_list_replays` — List Replay Videos
- `browser_replay_download` — Download Replay MP4
- `browser_replay_mark` — Mark Replay Annotation
- `browser_replay_annotate` — Annotate Replay MP4
- `browser_close` — Close Browser Session
- `browser_list_sessions` — List Browser Sessions

## access

- `access-accept-share` — Accept Shared Note
- `access-approve-sender` — Approve Sender
- `access-decline-share` — Decline Shared Note
- `get-chat-link` — Get Chat Link
- `get-vault-app-link` — Get Vault App Link
- `access-inbox-settings` — Inbox Settings
- `access-invite-account` — Invite To Account
- `access-issue-key` — Issue API Key
- `access-list-approved-senders` — List Approved Senders
- `access-list-keys` — List API Keys
- `access-note-inbox` — Note Inbox
- `access-remove-approved-sender` — Remove Approved Sender
- `revoke-chat-link` — Revoke Chat Link
- `access-revoke-key` — Revoke API Key
- `access-revoke-share` — Revoke Note Share
- `revoke-vault-app-link` — Revoke Vault App Link
- `set-agent-identity` — Set Agent Identity
- `access-set-scope` — Set Key Scope / Plan
- `access-share-note` — Share Note
- `access-share-vault` — Share Vault Entitlement
- `access-swap-vault` — Swap Active Vault
- `access-switch-account` — Switch Active Account
- `access-unlink-share` — Unlink Shared Note

## capture

- `memory-capture` — Capture Governed Memory
- `memory-questions` — Daily Memory Questions
- `prepare-memory-write` — Prepare Memory Write
- `validate-memory-write` — Validate Memory Write

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

## facts

- `fact-history` — Fact History
- `record-fact` — Record Fact

## graph

- `memory-backlinks` — Memory Backlinks
- `memory-graph-path` — Memory Graph Path
- `memory-graph-universe` — Memory Graph Universe

## library

- `library-ingest` — Library Ingest

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

## recall

- `temporal-recall` — Temporal Memory Recall

## schedule

- `create-scheduled-action` — Create Scheduled Action
- `delete-scheduled-action` — Delete Scheduled Action
- `get-schedule-link` — Get Schedule Link
- `get-schedule-status` — Get Schedule Status
- `list-scheduled-actions` — List Scheduled Actions
- `pause-scheduled-action` — Pause Scheduled Action
- `propose-scheduled-action` — Propose Scheduled Action
- `resume-scheduled-action` — Resume Scheduled Action
- `revoke-schedule-link` — Revoke Schedule Link
- `set-schedule-defaults` — Set Schedule Defaults
- `set-schedule-entitlement` — Set Schedule Entitlement

## storage

- `cost-usage` — Cost & Usage
- `storage-usage` — Storage Usage

## tables

- `table-create` — Create Table
- `table-delete-rows` — Delete Table Rows
- `table-describe` — Describe Table
- `table-drop` — Drop Table
- `table-insert-rows` — Insert Table Rows
- `table-list` — List Tables
- `table-query` — Query Table

## tags

- `list-memory-tags` — List Memory Tags
- `resolve-memory-tags` — Resolve Memory Tags
- `upsert-memory-tag` — Upsert Memory Tag

## vaults

- `add-vault` — Add Vault
- `create-secure-vault` — Create Secure Vault
- `delete-vault` — Delete Vault
- `get-vault-contract` — Get Vault Contract
- `list-shared-with-me` — List Shared With Me
- `list-vaults` — List Vaults
- `provision-defaults` — Provision Default Vaults
- `route-memory` — Route Memory

## webhooks

- `create-webhook` — Create Webhook
- `list-webhooks` — List Webhooks
- `revoke-webhook` — Revoke Webhook
