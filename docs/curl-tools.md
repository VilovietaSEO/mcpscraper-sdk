# All 159 MCP tools with cURL

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

Search Console performance uses the same export contract: set `dataset` to `search_console_performance` and choose the requested range with `lastDays` or `from`/`to`.

If a signed artifact URL expires, call `renew_connected_data_download` with the returned `artifactId`. If an export is partial, pass its complete `continuation` object unchanged on the next export call.

## Complete catalog (159)

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
- `revoke-chat-link` — Revoke Chat Link
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

## web

- `audit_site` — Technical SEO Audit
- `check_site_export` — Check Site Export
- `diff_page` — Page Change Check
- `extract_site` — Multi-Page Site Content Crawl
- `extract_url` — Single URL Extract
- `map_site_urls` — Site URL Map

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

## connections

- `call_service_connection_action` — Run Connected Service Action
- `describe_service_connection_tool` — Describe Connected Service Tool
- `export_connected_service_data` — Export Connected Service Data
- `gmail_send_message` — Send Gmail Message
- `google_calendar_create_event` — Create Calendar Event
- `import_service_connection_to_memory` — Import Connected Service Snapshot to Memory
- `list_service_connections` — List Connected Services
- `meta_ad_creative_media` — View Meta Ad Creative Media
- `read_service_connection` — Read Connected Service
- `renew_connected_data_download` — Renew Connected Data Download
- `set_scheduled_action_connections` — Set Scheduled Action Connections
- `slack_send_message` — Send Slack Message
- `zoom_create_meeting` — Create Zoom Meeting

## serpIntelligence

- `capture_serp_page_snapshots` — SERP Intelligence Page Snapshots
- `capture_serp_snapshot` — SERP Intelligence Snapshot

## storage

- `cost-usage` — Cost & Usage
- `storage-usage` — Storage Usage

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
- `set-schedule-entitlement` — Set Schedule Entitlement

## webhooks

- `create-webhook` — Create Webhook
- `list-webhooks` — List Webhooks
- `revoke-webhook` — Revoke Webhook

## billing

- `credits_info` — MCP Scraper Credits & Costs

## memory

- `delete-note` — Delete Memory Note
- `memory-export` — Export Vault
- `memory-get` — Get Memory Note
- `memory-list` — List Memory Notes
- `memory-put` — Put Memory Note
- `memory-search` — Semantic Memory Search
- `memory-suggest` — Suggest Notes (typeahead)
- `memory-upload` — Upload Document to Vault

## directory

- `directory_workflow` — Directory Workflow: Markets + Maps

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

## googleAds

- `google_ads_page_intel` — Google Ads Advertiser Intel
- `google_ads_search` — Google Ads Transparency Search
- `google_ads_transcribe` — Google Ad Video Transcription

## search

- `harvest_paa` — Google PAA + SERP Harvest
- `search_serp` — Google SERP Lookup

## instagram

- `instagram_media_download` — Instagram Post/Reel Media Download
- `instagram_profile_content` — Instagram Profile Content Discovery

## library

- `library-ingest` — Library Ingest

## tags

- `list-memory-tags` — List Memory Tags
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

## artifacts

- `report_artifact_read` — Read Report Artifact

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
