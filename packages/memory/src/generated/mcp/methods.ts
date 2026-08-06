export type McpToolCallFn = (name: string, args: unknown) => Promise<unknown>

import * as SearchHarvestPaa from './tools/harvest_paa.js'
import * as SearchSearchSerp from './tools/search_serp.js'
import * as WebExtractUrl from './tools/extract_url.js'
import * as WebDiffPage from './tools/diff_page.js'
import * as WebMapSiteUrls from './tools/map_site_urls.js'
import * as WebMapWaybackSnapshots from './tools/map_wayback_snapshots.js'
import * as WebExtractSite from './tools/extract_site.js'
import * as WebAuditSite from './tools/audit_site.js'
import * as WebCheckSiteExport from './tools/check_site_export.js'
import * as WebArchiveRead from './tools/archive_read.js'
import * as YoutubeHarvest from './tools/youtube_harvest.js'
import * as YoutubeTranscribe from './tools/youtube_transcribe.js'
import * as FacebookPageIntel from './tools/facebook_page_intel.js'
import * as FacebookAdSearch from './tools/facebook_ad_search.js'
import * as FacebookAdTranscribe from './tools/facebook_ad_transcribe.js'
import * as FacebookVideoTranscribe from './tools/facebook_video_transcribe.js'
import * as RedditThread from './tools/reddit_thread.js'
import * as RedditTrending from './tools/reddit_trending.js'
import * as VideoFrameAnalysis from './tools/video_frame_analysis.js'
import * as VideoFrameAnalysisStatus from './tools/video_frame_analysis_status.js'
import * as VideoAnalyzeStart from './tools/video-analyze-start.js'
import * as VideoAnalyzeStatus from './tools/video-analyze-status.js'
import * as GoogleAdsSearch from './tools/google_ads_search.js'
import * as GoogleAdsPageIntel from './tools/google_ads_page_intel.js'
import * as GoogleAdsTranscribe from './tools/google_ads_transcribe.js'
import * as InstagramProfileContent from './tools/instagram_profile_content.js'
import * as InstagramMediaDownload from './tools/instagram_media_download.js'
import * as MapsPlaceIntel from './tools/maps_place_intel.js'
import * as MapsSearch from './tools/maps_search.js'
import * as ReviewsTrustpilotReviews from './tools/trustpilot_reviews.js'
import * as ReviewsG2Reviews from './tools/g2_reviews.js'
import * as CommonsSearchEntities from './tools/commons_search_entities.js'
import * as CommonsGetEntity from './tools/commons_get_entity.js'
import * as CommonsListNeedsLinks from './tools/commons_list_needs_links.js'
import * as CommonsPrepareEntity from './tools/commons_prepare_entity.js'
import * as CommonsValidateEntity from './tools/commons_validate_entity.js'
import * as CommonsSubmitEntity from './tools/commons_submit_entity.js'
import * as CommonsGetEntityLedger from './tools/commons_get_entity_ledger.js'
import * as CommonsSaveFilter from './tools/commons_save_filter.js'
import * as CommonsListFilters from './tools/commons_list_filters.js'
import * as CommonsClaimPublication from './tools/commons_claim_publication.js'
import * as CommonsGetEntityLinkset from './tools/commons_get_entity_linkset.js'
import * as CommonsGetPublication from './tools/commons_get_publication.js'
import * as CommonsPreparePublication from './tools/commons_prepare_publication.js'
import * as CommonsPublishEditorial from './tools/commons_publish_editorial.js'
import * as CommonsValidatePublication from './tools/commons_validate_publication.js'
import * as DirectoryRun from './tools/directory_workflow.js'
import * as DirectoryWorkflowStatus from './tools/directory_workflow_status.js'
import * as DirectoryGetLocalSourcebookContract from './tools/get-local-sourcebook-contract.js'
import * as DirectoryListLocalSourcebookTags from './tools/list-local-sourcebook-tags.js'
import * as DirectoryResolveLocalSourcebookTags from './tools/resolve-local-sourcebook-tags.js'
import * as DirectoryPrepareLocalSourcebookWrite from './tools/prepare-local-sourcebook-write.js'
import * as DirectoryValidateLocalSourcebookWrite from './tools/validate-local-sourcebook-write.js'
import * as DirectoryLocalSourcebookCapture from './tools/local-sourcebook-capture.js'
import * as DirectoryLocalSourcebookSubmissionStatus from './tools/local_sourcebook_submission_status.js'
import * as DirectoryLocalSourcebookRefresh from './tools/local_sourcebook_refresh.js'
import * as DirectoryLocationMarkets from './tools/location_markets.js'
import * as WorkflowsList from './tools/workflow_list.js'
import * as WorkflowsSuggest from './tools/workflow_suggest.js'
import * as WorkflowsRun from './tools/workflow_run.js'
import * as WorkflowsStep from './tools/workflow_step.js'
import * as WorkflowsStatus from './tools/workflow_status.js'
import * as WorkflowsArtifactRead from './tools/workflow_artifact_read.js'
import * as WorkflowsRankTracker from './tools/rank_tracker_workflow.js'
import * as WorkflowsQueryFanout from './tools/query_fanout_workflow.js'
import * as EditorialReadingRoomGuide from './tools/editorial_reading_room_guide.js'
import * as EditorialCreateReadingRoom from './tools/create_editorial_reading_room.js'
import * as EditorialRenewReadingRoomDownload from './tools/renew_editorial_reading_room_download.js'
import * as ArtifactsRead from './tools/report_artifact_read.js'
import * as ArtifactsGetArtifactTemplateExample from './tools/get_artifact_template_example.js'
import * as BillingCreditsInfo from './tools/credits_info.js'
import * as ConnectionsListServiceConnections from './tools/list_service_connections.js'
import * as ConnectionsTestServiceConnection from './tools/test_service_connection.js'
import * as ConnectionsSlackSendMessage from './tools/slack_send_message.js'
import * as ConnectionsGmailSendMessage from './tools/gmail_send_message.js'
import * as ConnectionsGmailSearchContacts from './tools/gmail_search_contacts.js'
import * as ConnectionsGoogleCalendarCreateEvent from './tools/google_calendar_create_event.js'
import * as ConnectionsZoomCreateMeeting from './tools/zoom_create_meeting.js'
import * as ConnectionsReadServiceConnection from './tools/read_service_connection.js'
import * as ConnectionsMetaAdCreativeMedia from './tools/meta_ad_creative_media.js'
import * as ConnectionsImportServiceConnectionToMemory from './tools/import_service_connection_to_memory.js'
import * as ConnectionsDescribeServiceConnectionTool from './tools/describe_service_connection_tool.js'
import * as ConnectionsExportConnectedServiceData from './tools/export_connected_service_data.js'
import * as ConnectionsExportSearchConsoleTableData from './tools/export_search_console_table_data.js'
import * as ConnectionsRenewConnectedDataDownload from './tools/renew_connected_data_download.js'
import * as ConnectionsCallServiceConnectionAction from './tools/call_service_connection_action.js'
import * as ConnectionsSetScheduledActionConnections from './tools/set_scheduled_action_connections.js'
import * as SerpIntelligenceSnapshot from './tools/capture_serp_snapshot.js'
import * as SerpIntelligencePageSnapshots from './tools/capture_serp_page_snapshots.js'
import * as BrowserProfileConnect from './tools/browser_profile_connect.js'
import * as BrowserProfileList from './tools/browser_profile_list.js'
import * as BrowserExtensionImport from './tools/browser_extension_import.js'
import * as BrowserExtensionList from './tools/browser_extension_list.js'
import * as BrowserExtensionDelete from './tools/browser_extension_delete.js'
import * as BrowserOpen from './tools/browser_open.js'
import * as BrowserScreenshot from './tools/browser_screenshot.js'
import * as BrowserRead from './tools/browser_read.js'
import * as BrowserLocate from './tools/browser_locate.js'
import * as BrowserGoto from './tools/browser_goto.js'
import * as BrowserClick from './tools/browser_click.js'
import * as BrowserType from './tools/browser_type.js'
import * as BrowserScroll from './tools/browser_scroll.js'
import * as BrowserPress from './tools/browser_press.js'
import * as BrowserReplayStart from './tools/browser_replay_start.js'
import * as BrowserReplayStop from './tools/browser_replay_stop.js'
import * as BrowserListReplays from './tools/browser_list_replays.js'
import * as BrowserReplayDownload from './tools/browser_replay_download.js'
import * as BrowserReplayMark from './tools/browser_replay_mark.js'
import * as BrowserReplayAnnotate from './tools/browser_replay_annotate.js'
import * as BrowserClose from './tools/browser_close.js'
import * as BrowserListSessions from './tools/browser_list_sessions.js'
import * as ScheduleListArtifactTemplates from './tools/list_artifact_templates.js'
import * as ScheduleGetArtifactTemplate from './tools/get_artifact_template.js'
import * as ScheduleCreateArtifactTemplate from './tools/create_artifact_template.js'
import * as ScheduleUpdateArtifactTemplate from './tools/update_artifact_template.js'
import * as ScheduleArchiveArtifactTemplate from './tools/archive_artifact_template.js'
import * as ScheduleListScheduledRuns from './tools/list_scheduled_runs.js'
import * as ScheduleGetScheduledRun from './tools/get_scheduled_run.js'
import * as ScheduleMarkScheduledRunOpened from './tools/mark_scheduled_run_opened.js'
import * as ScheduleMarkScheduledRunUnopened from './tools/mark_scheduled_run_unopened.js'
import * as ScheduleArchiveScheduledRun from './tools/archive_scheduled_run.js'
import * as ScheduleCreateScheduledRunViewLink from './tools/create_scheduled_run_view_link.js'
import * as ScheduleRevokeScheduledRunViewLink from './tools/revoke_scheduled_run_view_link.js'
import * as ScheduleCreateScheduledAction from './tools/create-scheduled-action.js'
import * as ScheduleUpdateScheduledAction from './tools/update-scheduled-action.js'
import * as ScheduleDeleteScheduledAction from './tools/delete-scheduled-action.js'
import * as ScheduleGetScheduleLink from './tools/get-schedule-link.js'
import * as ScheduleGetScheduleStatus from './tools/get-schedule-status.js'
import * as ScheduleListScheduledActions from './tools/list-scheduled-actions.js'
import * as SchedulePauseScheduledAction from './tools/pause-scheduled-action.js'
import * as ScheduleProposeScheduledAction from './tools/propose-scheduled-action.js'
import * as ScheduleResumeScheduledAction from './tools/resume-scheduled-action.js'
import * as ScheduleRevokeScheduleLink from './tools/revoke-schedule-link.js'
import * as ScheduleSetScheduleDefaults from './tools/set-schedule-defaults.js'
import * as ScheduleSetScheduleEntitlement from './tools/set-schedule-entitlement.js'
import * as AccessAcceptShare from './tools/access-accept-share.js'
import * as AccessApproveSender from './tools/access-approve-sender.js'
import * as AccessDeclineShare from './tools/access-decline-share.js'
import * as AccessGetChatLink from './tools/get-chat-link.js'
import * as AccessGetVaultAppLink from './tools/get-vault-app-link.js'
import * as AccessInboxSettings from './tools/access-inbox-settings.js'
import * as AccessInviteAccount from './tools/access-invite-account.js'
import * as AccessIssueKey from './tools/access-issue-key.js'
import * as AccessListApprovedSenders from './tools/access-list-approved-senders.js'
import * as AccessListKeys from './tools/access-list-keys.js'
import * as AccessNoteInbox from './tools/access-note-inbox.js'
import * as AccessRemoveApprovedSender from './tools/access-remove-approved-sender.js'
import * as AccessRevokeChatLink from './tools/revoke-chat-link.js'
import * as AccessRevokeKey from './tools/access-revoke-key.js'
import * as AccessRevokeShare from './tools/access-revoke-share.js'
import * as AccessRevokeVaultAppLink from './tools/revoke-vault-app-link.js'
import * as AccessSetAgentIdentity from './tools/set-agent-identity.js'
import * as AccessSetScope from './tools/access-set-scope.js'
import * as AccessShareNote from './tools/access-share-note.js'
import * as AccessShareVault from './tools/access-share-vault.js'
import * as AccessSwapVault from './tools/access-swap-vault.js'
import * as AccessSwitchAccount from './tools/access-switch-account.js'
import * as AccessUnlinkShare from './tools/access-unlink-share.js'
import * as CaptureMemoryCapture from './tools/memory-capture.js'
import * as CaptureMemoryQuestions from './tools/memory-questions.js'
import * as CapturePrepareMemoryWrite from './tools/prepare-memory-write.js'
import * as CaptureValidateMemoryWrite from './tools/validate-memory-write.js'
import * as ChannelsCreateChannel from './tools/create-channel.js'
import * as ChannelsGetMessageNote from './tools/get-message-note.js'
import * as ChannelsListChannelMembers from './tools/list-channel-members.js'
import * as ChannelsListChannelMessages from './tools/list-channel-messages.js'
import * as ChannelsMyMentions from './tools/my-mentions.js'
import * as ChannelsPollChannel from './tools/poll-channel.js'
import * as ChannelsPostMessage from './tools/post-message.js'
import * as ChannelsReactMessage from './tools/react-message.js'
import * as ChannelsRemoveChannelMember from './tools/remove-channel-member.js'
import * as ChannelsReplyMessage from './tools/reply-message.js'
import * as FactsHistory from './tools/fact-history.js'
import * as FactsRecordFact from './tools/record-fact.js'
import * as GraphMemoryBacklinks from './tools/memory-backlinks.js'
import * as GraphMemoryGraphPath from './tools/memory-graph-path.js'
import * as GraphMemoryGraphUniverse from './tools/memory-graph-universe.js'
import * as LibraryIngest from './tools/library-ingest.js'
import * as MemoryBulkDeleteNotes from './tools/bulk-delete-notes.js'
import * as MemoryDeleteNote from './tools/delete-note.js'
import * as MemoryExport from './tools/memory-export.js'
import * as MemoryGet from './tools/memory-get.js'
import * as MemoryList from './tools/memory-list.js'
import * as MemoryPut from './tools/memory-put.js'
import * as MemorySearch from './tools/memory-search.js'
import * as MemorySuggest from './tools/memory-suggest.js'
import * as MemoryUpload from './tools/memory-upload.js'
import * as RecallTemporalRecall from './tools/temporal-recall.js'
import * as StorageCostUsage from './tools/cost-usage.js'
import * as StorageUsage from './tools/storage-usage.js'
import * as TablesCreate from './tools/table-create.js'
import * as TablesDeleteRows from './tools/table-delete-rows.js'
import * as TablesDescribe from './tools/table-describe.js'
import * as TablesDrop from './tools/table-drop.js'
import * as TablesInsertRows from './tools/table-insert-rows.js'
import * as TablesList from './tools/table-list.js'
import * as TablesQuery from './tools/table-query.js'
import * as TagsListMemoryTags from './tools/list-memory-tags.js'
import * as TagsMergeMemoryTags from './tools/merge-memory-tags.js'
import * as TagsResolveMemoryTags from './tools/resolve-memory-tags.js'
import * as TagsUpsertMemoryTag from './tools/upsert-memory-tag.js'
import * as VaultsAddVault from './tools/add-vault.js'
import * as VaultsCreateSecureVault from './tools/create-secure-vault.js'
import * as VaultsDeleteVault from './tools/delete-vault.js'
import * as VaultsGetVaultContract from './tools/get-vault-contract.js'
import * as VaultsListSharedWithMe from './tools/list-shared-with-me.js'
import * as VaultsListVaults from './tools/list-vaults.js'
import * as VaultsProvisionDefaults from './tools/provision-defaults.js'
import * as VaultsRouteMemory from './tools/route-memory.js'
import * as WebhooksCreateWebhook from './tools/create-webhook.js'
import * as WebhooksListWebhooks from './tools/list-webhooks.js'
import * as WebhooksRevokeWebhook from './tools/revoke-webhook.js'
import * as ImagesProjectCreate from './tools/image_project_create.js'
import * as ImagesProjectList from './tools/image_project_list.js'
import * as ImagesFolderCreate from './tools/image_folder_create.js'
import * as ImagesFolderList from './tools/image_folder_list.js'
import * as ImagesAssetSave from './tools/image_asset_save.js'
import * as ImagesAssetGet from './tools/image_asset_get.js'
import * as ImagesAssetList from './tools/image_asset_list.js'
import * as ImagesAssetSearch from './tools/image_asset_search.js'
import * as ImagesAssetMove from './tools/image_asset_move.js'
import * as ImagesAssetDelete from './tools/image_asset_delete.js'
import * as AnalyticsCreateActivationDestination from './tools/analytics_create_activation_destination.js'
import * as AnalyticsCreateCampaignLink from './tools/analytics_create_campaign_link.js'
import * as AnalyticsCreateExport from './tools/analytics_create_export.js'
import * as AnalyticsCreateForm from './tools/analytics_create_form.js'
import * as AnalyticsGetAcquisition from './tools/analytics_get_acquisition.js'
import * as AnalyticsGetBusinessMetrics from './tools/analytics_get_business_metrics.js'
import * as AnalyticsGetChannelBreakdown from './tools/analytics_get_channel_breakdown.js'
import * as AnalyticsGetContent from './tools/analytics_get_content.js'
import * as AnalyticsGetConversions from './tools/analytics_get_conversions.js'
import * as AnalyticsGetDimensions from './tools/analytics_get_dimensions.js'
import * as AnalyticsGetEntitlement from './tools/analytics_get_entitlement.js'
import * as AnalyticsGetEvents from './tools/analytics_get_events.js'
import * as AnalyticsGetForecast from './tools/analytics_get_forecast.js'
import * as AnalyticsGetHealth from './tools/analytics_get_health.js'
import * as AnalyticsGetOverview from './tools/analytics_get_overview.js'
import * as AnalyticsGetPaths from './tools/analytics_get_paths.js'
import * as AnalyticsGetTimeseries from './tools/analytics_get_timeseries.js'
import * as AnalyticsImportCrmCsv from './tools/analytics_import_crm_csv.js'
import * as AnalyticsListActivationDestinations from './tools/analytics_list_activation_destinations.js'
import * as AnalyticsListCampaignLinks from './tools/analytics_list_campaign_links.js'
import * as AnalyticsListCrmImports from './tools/analytics_list_crm_imports.js'
import * as AnalyticsListForms from './tools/analytics_list_forms.js'
import * as AnalyticsListPixels from './tools/analytics_list_pixels.js'
import * as AnalyticsListSites from './tools/analytics_list_sites.js'

export const MCP_TOOL_BINDINGS = [
  {
    "name": "harvest_paa",
    "category": "search",
    "methodName": "harvestPaa"
  },
  {
    "name": "search_serp",
    "category": "search",
    "methodName": "searchSerp"
  },
  {
    "name": "extract_url",
    "category": "web",
    "methodName": "extractUrl"
  },
  {
    "name": "diff_page",
    "category": "web",
    "methodName": "diffPage"
  },
  {
    "name": "map_site_urls",
    "category": "web",
    "methodName": "mapSiteUrls"
  },
  {
    "name": "map_wayback_snapshots",
    "category": "web",
    "methodName": "mapWaybackSnapshots"
  },
  {
    "name": "extract_site",
    "category": "web",
    "methodName": "extractSite"
  },
  {
    "name": "audit_site",
    "category": "web",
    "methodName": "auditSite"
  },
  {
    "name": "check_site_export",
    "category": "web",
    "methodName": "checkSiteExport"
  },
  {
    "name": "archive_read",
    "category": "web",
    "methodName": "archiveRead"
  },
  {
    "name": "youtube_harvest",
    "category": "youtube",
    "methodName": "harvest"
  },
  {
    "name": "youtube_transcribe",
    "category": "youtube",
    "methodName": "transcribe"
  },
  {
    "name": "facebook_page_intel",
    "category": "facebook",
    "methodName": "pageIntel"
  },
  {
    "name": "facebook_ad_search",
    "category": "facebook",
    "methodName": "adSearch"
  },
  {
    "name": "reddit_thread",
    "category": "reddit",
    "methodName": "thread"
  },
  {
    "name": "reddit_trending",
    "category": "reddit",
    "methodName": "trending"
  },
  {
    "name": "video_frame_analysis",
    "category": "video",
    "methodName": "frameAnalysis"
  },
  {
    "name": "video_frame_analysis_status",
    "category": "video",
    "methodName": "frameAnalysisStatus"
  },
  {
    "name": "facebook_ad_transcribe",
    "category": "facebook",
    "methodName": "adTranscribe"
  },
  {
    "name": "google_ads_search",
    "category": "googleAds",
    "methodName": "search"
  },
  {
    "name": "google_ads_page_intel",
    "category": "googleAds",
    "methodName": "pageIntel"
  },
  {
    "name": "google_ads_transcribe",
    "category": "googleAds",
    "methodName": "transcribe"
  },
  {
    "name": "facebook_video_transcribe",
    "category": "facebook",
    "methodName": "videoTranscribe"
  },
  {
    "name": "instagram_profile_content",
    "category": "instagram",
    "methodName": "profileContent"
  },
  {
    "name": "instagram_media_download",
    "category": "instagram",
    "methodName": "mediaDownload"
  },
  {
    "name": "maps_place_intel",
    "category": "maps",
    "methodName": "placeIntel"
  },
  {
    "name": "maps_search",
    "category": "maps",
    "methodName": "search"
  },
  {
    "name": "trustpilot_reviews",
    "category": "reviews",
    "methodName": "trustpilotReviews"
  },
  {
    "name": "g2_reviews",
    "category": "reviews",
    "methodName": "g2Reviews"
  },
  {
    "name": "commons_search_entities",
    "category": "commons",
    "methodName": "searchEntities"
  },
  {
    "name": "commons_get_entity",
    "category": "commons",
    "methodName": "getEntity"
  },
  {
    "name": "commons_list_needs_links",
    "category": "commons",
    "methodName": "listNeedsLinks"
  },
  {
    "name": "commons_prepare_entity",
    "category": "commons",
    "methodName": "prepareEntity"
  },
  {
    "name": "commons_validate_entity",
    "category": "commons",
    "methodName": "validateEntity"
  },
  {
    "name": "commons_submit_entity",
    "category": "commons",
    "methodName": "submitEntity"
  },
  {
    "name": "commons_get_entity_ledger",
    "category": "commons",
    "methodName": "getEntityLedger"
  },
  {
    "name": "commons_save_filter",
    "category": "commons",
    "methodName": "saveFilter"
  },
  {
    "name": "commons_list_filters",
    "category": "commons",
    "methodName": "listFilters"
  },
  {
    "name": "directory_workflow",
    "category": "directory",
    "methodName": "run"
  },
  {
    "name": "directory_workflow_status",
    "category": "directory",
    "methodName": "workflowStatus"
  },
  {
    "name": "get-local-sourcebook-contract",
    "category": "directory",
    "methodName": "getLocalSourcebookContract"
  },
  {
    "name": "list-local-sourcebook-tags",
    "category": "directory",
    "methodName": "listLocalSourcebookTags"
  },
  {
    "name": "resolve-local-sourcebook-tags",
    "category": "directory",
    "methodName": "resolveLocalSourcebookTags"
  },
  {
    "name": "prepare-local-sourcebook-write",
    "category": "directory",
    "methodName": "prepareLocalSourcebookWrite"
  },
  {
    "name": "validate-local-sourcebook-write",
    "category": "directory",
    "methodName": "validateLocalSourcebookWrite"
  },
  {
    "name": "local-sourcebook-capture",
    "category": "directory",
    "methodName": "localSourcebookCapture"
  },
  {
    "name": "local_sourcebook_submission_status",
    "category": "directory",
    "methodName": "localSourcebookSubmissionStatus"
  },
  {
    "name": "local_sourcebook_refresh",
    "category": "directory",
    "methodName": "localSourcebookRefresh"
  },
  {
    "name": "location_markets",
    "category": "directory",
    "methodName": "locationMarkets"
  },
  {
    "name": "workflow_list",
    "category": "workflows",
    "methodName": "list"
  },
  {
    "name": "workflow_suggest",
    "category": "workflows",
    "methodName": "suggest"
  },
  {
    "name": "workflow_run",
    "category": "workflows",
    "methodName": "run"
  },
  {
    "name": "workflow_step",
    "category": "workflows",
    "methodName": "step"
  },
  {
    "name": "workflow_status",
    "category": "workflows",
    "methodName": "status"
  },
  {
    "name": "workflow_artifact_read",
    "category": "workflows",
    "methodName": "artifactRead"
  },
  {
    "name": "editorial_reading_room_guide",
    "category": "editorial",
    "methodName": "readingRoomGuide"
  },
  {
    "name": "create_editorial_reading_room",
    "category": "editorial",
    "methodName": "createReadingRoom"
  },
  {
    "name": "renew_editorial_reading_room_download",
    "category": "editorial",
    "methodName": "renewReadingRoomDownload"
  },
  {
    "name": "report_artifact_read",
    "category": "artifacts",
    "methodName": "read"
  },
  {
    "name": "rank_tracker_workflow",
    "category": "workflows",
    "methodName": "rankTracker"
  },
  {
    "name": "credits_info",
    "category": "billing",
    "methodName": "creditsInfo"
  },
  {
    "name": "list_service_connections",
    "category": "connections",
    "methodName": "listServiceConnections"
  },
  {
    "name": "test_service_connection",
    "category": "connections",
    "methodName": "testServiceConnection"
  },
  {
    "name": "slack_send_message",
    "category": "connections",
    "methodName": "slackSendMessage"
  },
  {
    "name": "gmail_send_message",
    "category": "connections",
    "methodName": "gmailSendMessage"
  },
  {
    "name": "gmail_search_contacts",
    "category": "connections",
    "methodName": "gmailSearchContacts"
  },
  {
    "name": "google_calendar_create_event",
    "category": "connections",
    "methodName": "googleCalendarCreateEvent"
  },
  {
    "name": "zoom_create_meeting",
    "category": "connections",
    "methodName": "zoomCreateMeeting"
  },
  {
    "name": "read_service_connection",
    "category": "connections",
    "methodName": "readServiceConnection"
  },
  {
    "name": "meta_ad_creative_media",
    "category": "connections",
    "methodName": "metaAdCreativeMedia"
  },
  {
    "name": "import_service_connection_to_memory",
    "category": "connections",
    "methodName": "importServiceConnectionToMemory"
  },
  {
    "name": "describe_service_connection_tool",
    "category": "connections",
    "methodName": "describeServiceConnectionTool"
  },
  {
    "name": "export_connected_service_data",
    "category": "connections",
    "methodName": "exportConnectedServiceData"
  },
  {
    "name": "export_search_console_table_data",
    "category": "connections",
    "methodName": "exportSearchConsoleTableData"
  },
  {
    "name": "renew_connected_data_download",
    "category": "connections",
    "methodName": "renewConnectedDataDownload"
  },
  {
    "name": "call_service_connection_action",
    "category": "connections",
    "methodName": "callServiceConnectionAction"
  },
  {
    "name": "set_scheduled_action_connections",
    "category": "connections",
    "methodName": "setScheduledActionConnections"
  },
  {
    "name": "capture_serp_snapshot",
    "category": "serpIntelligence",
    "methodName": "snapshot"
  },
  {
    "name": "capture_serp_page_snapshots",
    "category": "serpIntelligence",
    "methodName": "pageSnapshots"
  },
  {
    "name": "browser_profile_connect",
    "category": "browser",
    "methodName": "profileConnect"
  },
  {
    "name": "browser_profile_list",
    "category": "browser",
    "methodName": "profileList"
  },
  {
    "name": "browser_extension_import",
    "category": "browser",
    "methodName": "extensionImport"
  },
  {
    "name": "browser_extension_list",
    "category": "browser",
    "methodName": "extensionList"
  },
  {
    "name": "browser_extension_delete",
    "category": "browser",
    "methodName": "extensionDelete"
  },
  {
    "name": "browser_open",
    "category": "browser",
    "methodName": "open"
  },
  {
    "name": "browser_screenshot",
    "category": "browser",
    "methodName": "screenshot"
  },
  {
    "name": "browser_read",
    "category": "browser",
    "methodName": "read"
  },
  {
    "name": "browser_locate",
    "category": "browser",
    "methodName": "locate"
  },
  {
    "name": "browser_goto",
    "category": "browser",
    "methodName": "goto"
  },
  {
    "name": "browser_click",
    "category": "browser",
    "methodName": "click"
  },
  {
    "name": "browser_type",
    "category": "browser",
    "methodName": "type"
  },
  {
    "name": "browser_scroll",
    "category": "browser",
    "methodName": "scroll"
  },
  {
    "name": "browser_press",
    "category": "browser",
    "methodName": "press"
  },
  {
    "name": "browser_replay_start",
    "category": "browser",
    "methodName": "replayStart"
  },
  {
    "name": "browser_replay_stop",
    "category": "browser",
    "methodName": "replayStop"
  },
  {
    "name": "browser_list_replays",
    "category": "browser",
    "methodName": "listReplays"
  },
  {
    "name": "browser_replay_download",
    "category": "browser",
    "methodName": "replayDownload"
  },
  {
    "name": "browser_replay_mark",
    "category": "browser",
    "methodName": "replayMark"
  },
  {
    "name": "browser_replay_annotate",
    "category": "browser",
    "methodName": "replayAnnotate"
  },
  {
    "name": "browser_close",
    "category": "browser",
    "methodName": "close"
  },
  {
    "name": "browser_list_sessions",
    "category": "browser",
    "methodName": "listSessions"
  },
  {
    "name": "query_fanout_workflow",
    "category": "workflows",
    "methodName": "queryFanout"
  },
  {
    "name": "list_artifact_templates",
    "category": "schedule",
    "methodName": "listArtifactTemplates"
  },
  {
    "name": "get_artifact_template",
    "category": "schedule",
    "methodName": "getArtifactTemplate"
  },
  {
    "name": "create_artifact_template",
    "category": "schedule",
    "methodName": "createArtifactTemplate"
  },
  {
    "name": "update_artifact_template",
    "category": "schedule",
    "methodName": "updateArtifactTemplate"
  },
  {
    "name": "archive_artifact_template",
    "category": "schedule",
    "methodName": "archiveArtifactTemplate"
  },
  {
    "name": "list_scheduled_runs",
    "category": "schedule",
    "methodName": "listScheduledRuns"
  },
  {
    "name": "get_scheduled_run",
    "category": "schedule",
    "methodName": "getScheduledRun"
  },
  {
    "name": "mark_scheduled_run_opened",
    "category": "schedule",
    "methodName": "markScheduledRunOpened"
  },
  {
    "name": "mark_scheduled_run_unopened",
    "category": "schedule",
    "methodName": "markScheduledRunUnopened"
  },
  {
    "name": "archive_scheduled_run",
    "category": "schedule",
    "methodName": "archiveScheduledRun"
  },
  {
    "name": "create_scheduled_run_view_link",
    "category": "schedule",
    "methodName": "createScheduledRunViewLink"
  },
  {
    "name": "revoke_scheduled_run_view_link",
    "category": "schedule",
    "methodName": "revokeScheduledRunViewLink"
  },
  {
    "name": "access-accept-share",
    "category": "access",
    "methodName": "acceptShare"
  },
  {
    "name": "access-approve-sender",
    "category": "access",
    "methodName": "approveSender"
  },
  {
    "name": "access-decline-share",
    "category": "access",
    "methodName": "declineShare"
  },
  {
    "name": "get-chat-link",
    "category": "access",
    "methodName": "getChatLink"
  },
  {
    "name": "get-vault-app-link",
    "category": "access",
    "methodName": "getVaultAppLink"
  },
  {
    "name": "access-inbox-settings",
    "category": "access",
    "methodName": "inboxSettings"
  },
  {
    "name": "access-invite-account",
    "category": "access",
    "methodName": "inviteAccount"
  },
  {
    "name": "access-issue-key",
    "category": "access",
    "methodName": "issueKey"
  },
  {
    "name": "access-list-approved-senders",
    "category": "access",
    "methodName": "listApprovedSenders"
  },
  {
    "name": "access-list-keys",
    "category": "access",
    "methodName": "listKeys"
  },
  {
    "name": "access-note-inbox",
    "category": "access",
    "methodName": "noteInbox"
  },
  {
    "name": "access-remove-approved-sender",
    "category": "access",
    "methodName": "removeApprovedSender"
  },
  {
    "name": "revoke-chat-link",
    "category": "access",
    "methodName": "revokeChatLink"
  },
  {
    "name": "access-revoke-key",
    "category": "access",
    "methodName": "revokeKey"
  },
  {
    "name": "access-revoke-share",
    "category": "access",
    "methodName": "revokeShare"
  },
  {
    "name": "revoke-vault-app-link",
    "category": "access",
    "methodName": "revokeVaultAppLink"
  },
  {
    "name": "set-agent-identity",
    "category": "access",
    "methodName": "setAgentIdentity"
  },
  {
    "name": "access-set-scope",
    "category": "access",
    "methodName": "setScope"
  },
  {
    "name": "access-share-note",
    "category": "access",
    "methodName": "shareNote"
  },
  {
    "name": "access-share-vault",
    "category": "access",
    "methodName": "shareVault"
  },
  {
    "name": "access-swap-vault",
    "category": "access",
    "methodName": "swapVault"
  },
  {
    "name": "access-switch-account",
    "category": "access",
    "methodName": "switchAccount"
  },
  {
    "name": "access-unlink-share",
    "category": "access",
    "methodName": "unlinkShare"
  },
  {
    "name": "memory-capture",
    "category": "capture",
    "methodName": "memoryCapture"
  },
  {
    "name": "memory-questions",
    "category": "capture",
    "methodName": "memoryQuestions"
  },
  {
    "name": "prepare-memory-write",
    "category": "capture",
    "methodName": "prepareMemoryWrite"
  },
  {
    "name": "validate-memory-write",
    "category": "capture",
    "methodName": "validateMemoryWrite"
  },
  {
    "name": "create-channel",
    "category": "channels",
    "methodName": "createChannel"
  },
  {
    "name": "get-message-note",
    "category": "channels",
    "methodName": "getMessageNote"
  },
  {
    "name": "list-channel-members",
    "category": "channels",
    "methodName": "listChannelMembers"
  },
  {
    "name": "list-channel-messages",
    "category": "channels",
    "methodName": "listChannelMessages"
  },
  {
    "name": "my-mentions",
    "category": "channels",
    "methodName": "myMentions"
  },
  {
    "name": "poll-channel",
    "category": "channels",
    "methodName": "pollChannel"
  },
  {
    "name": "post-message",
    "category": "channels",
    "methodName": "postMessage"
  },
  {
    "name": "react-message",
    "category": "channels",
    "methodName": "reactMessage"
  },
  {
    "name": "remove-channel-member",
    "category": "channels",
    "methodName": "removeChannelMember"
  },
  {
    "name": "reply-message",
    "category": "channels",
    "methodName": "replyMessage"
  },
  {
    "name": "fact-history",
    "category": "facts",
    "methodName": "history"
  },
  {
    "name": "record-fact",
    "category": "facts",
    "methodName": "recordFact"
  },
  {
    "name": "memory-backlinks",
    "category": "graph",
    "methodName": "memoryBacklinks"
  },
  {
    "name": "memory-graph-path",
    "category": "graph",
    "methodName": "memoryGraphPath"
  },
  {
    "name": "memory-graph-universe",
    "category": "graph",
    "methodName": "memoryGraphUniverse"
  },
  {
    "name": "library-ingest",
    "category": "library",
    "methodName": "ingest"
  },
  {
    "name": "bulk-delete-notes",
    "category": "memory",
    "methodName": "bulkDeleteNotes"
  },
  {
    "name": "delete-note",
    "category": "memory",
    "methodName": "deleteNote"
  },
  {
    "name": "memory-export",
    "category": "memory",
    "methodName": "export"
  },
  {
    "name": "memory-get",
    "category": "memory",
    "methodName": "get"
  },
  {
    "name": "memory-list",
    "category": "memory",
    "methodName": "list"
  },
  {
    "name": "memory-put",
    "category": "memory",
    "methodName": "put"
  },
  {
    "name": "memory-search",
    "category": "memory",
    "methodName": "search"
  },
  {
    "name": "memory-suggest",
    "category": "memory",
    "methodName": "suggest"
  },
  {
    "name": "memory-upload",
    "category": "memory",
    "methodName": "upload"
  },
  {
    "name": "temporal-recall",
    "category": "recall",
    "methodName": "temporalRecall"
  },
  {
    "name": "create-scheduled-action",
    "category": "schedule",
    "methodName": "createScheduledAction"
  },
  {
    "name": "update-scheduled-action",
    "category": "schedule",
    "methodName": "updateScheduledAction"
  },
  {
    "name": "delete-scheduled-action",
    "category": "schedule",
    "methodName": "deleteScheduledAction"
  },
  {
    "name": "get-schedule-link",
    "category": "schedule",
    "methodName": "getScheduleLink"
  },
  {
    "name": "get-schedule-status",
    "category": "schedule",
    "methodName": "getScheduleStatus"
  },
  {
    "name": "list-scheduled-actions",
    "category": "schedule",
    "methodName": "listScheduledActions"
  },
  {
    "name": "pause-scheduled-action",
    "category": "schedule",
    "methodName": "pauseScheduledAction"
  },
  {
    "name": "propose-scheduled-action",
    "category": "schedule",
    "methodName": "proposeScheduledAction"
  },
  {
    "name": "resume-scheduled-action",
    "category": "schedule",
    "methodName": "resumeScheduledAction"
  },
  {
    "name": "revoke-schedule-link",
    "category": "schedule",
    "methodName": "revokeScheduleLink"
  },
  {
    "name": "set-schedule-defaults",
    "category": "schedule",
    "methodName": "setScheduleDefaults"
  },
  {
    "name": "set-schedule-entitlement",
    "category": "schedule",
    "methodName": "setScheduleEntitlement"
  },
  {
    "name": "cost-usage",
    "category": "storage",
    "methodName": "costUsage"
  },
  {
    "name": "storage-usage",
    "category": "storage",
    "methodName": "usage"
  },
  {
    "name": "table-create",
    "category": "tables",
    "methodName": "create"
  },
  {
    "name": "table-delete-rows",
    "category": "tables",
    "methodName": "deleteRows"
  },
  {
    "name": "table-describe",
    "category": "tables",
    "methodName": "describe"
  },
  {
    "name": "table-drop",
    "category": "tables",
    "methodName": "drop"
  },
  {
    "name": "table-insert-rows",
    "category": "tables",
    "methodName": "insertRows"
  },
  {
    "name": "table-list",
    "category": "tables",
    "methodName": "list"
  },
  {
    "name": "table-query",
    "category": "tables",
    "methodName": "query"
  },
  {
    "name": "list-memory-tags",
    "category": "tags",
    "methodName": "listMemoryTags"
  },
  {
    "name": "merge-memory-tags",
    "category": "tags",
    "methodName": "mergeMemoryTags"
  },
  {
    "name": "resolve-memory-tags",
    "category": "tags",
    "methodName": "resolveMemoryTags"
  },
  {
    "name": "upsert-memory-tag",
    "category": "tags",
    "methodName": "upsertMemoryTag"
  },
  {
    "name": "add-vault",
    "category": "vaults",
    "methodName": "addVault"
  },
  {
    "name": "create-secure-vault",
    "category": "vaults",
    "methodName": "createSecureVault"
  },
  {
    "name": "delete-vault",
    "category": "vaults",
    "methodName": "deleteVault"
  },
  {
    "name": "get-vault-contract",
    "category": "vaults",
    "methodName": "getVaultContract"
  },
  {
    "name": "list-shared-with-me",
    "category": "vaults",
    "methodName": "listSharedWithMe"
  },
  {
    "name": "list-vaults",
    "category": "vaults",
    "methodName": "listVaults"
  },
  {
    "name": "provision-defaults",
    "category": "vaults",
    "methodName": "provisionDefaults"
  },
  {
    "name": "route-memory",
    "category": "vaults",
    "methodName": "routeMemory"
  },
  {
    "name": "video-analyze-start",
    "category": "video",
    "methodName": "analyzeStart"
  },
  {
    "name": "video-analyze-status",
    "category": "video",
    "methodName": "analyzeStatus"
  },
  {
    "name": "create-webhook",
    "category": "webhooks",
    "methodName": "createWebhook"
  },
  {
    "name": "list-webhooks",
    "category": "webhooks",
    "methodName": "listWebhooks"
  },
  {
    "name": "revoke-webhook",
    "category": "webhooks",
    "methodName": "revokeWebhook"
  },
  {
    "name": "image_project_create",
    "category": "images",
    "methodName": "projectCreate"
  },
  {
    "name": "image_project_list",
    "category": "images",
    "methodName": "projectList"
  },
  {
    "name": "image_folder_create",
    "category": "images",
    "methodName": "folderCreate"
  },
  {
    "name": "image_folder_list",
    "category": "images",
    "methodName": "folderList"
  },
  {
    "name": "image_asset_save",
    "category": "images",
    "methodName": "assetSave"
  },
  {
    "name": "image_asset_get",
    "category": "images",
    "methodName": "assetGet"
  },
  {
    "name": "image_asset_list",
    "category": "images",
    "methodName": "assetList"
  },
  {
    "name": "image_asset_search",
    "category": "images",
    "methodName": "assetSearch"
  },
  {
    "name": "image_asset_move",
    "category": "images",
    "methodName": "assetMove"
  },
  {
    "name": "image_asset_delete",
    "category": "images",
    "methodName": "assetDelete"
  },
  {
    "name": "analytics_create_activation_destination",
    "category": "analytics",
    "methodName": "createActivationDestination"
  },
  {
    "name": "analytics_create_campaign_link",
    "category": "analytics",
    "methodName": "createCampaignLink"
  },
  {
    "name": "analytics_create_export",
    "category": "analytics",
    "methodName": "createExport"
  },
  {
    "name": "analytics_create_form",
    "category": "analytics",
    "methodName": "createForm"
  },
  {
    "name": "analytics_get_acquisition",
    "category": "analytics",
    "methodName": "getAcquisition"
  },
  {
    "name": "analytics_get_business_metrics",
    "category": "analytics",
    "methodName": "getBusinessMetrics"
  },
  {
    "name": "analytics_get_channel_breakdown",
    "category": "analytics",
    "methodName": "getChannelBreakdown"
  },
  {
    "name": "analytics_get_content",
    "category": "analytics",
    "methodName": "getContent"
  },
  {
    "name": "analytics_get_conversions",
    "category": "analytics",
    "methodName": "getConversions"
  },
  {
    "name": "analytics_get_dimensions",
    "category": "analytics",
    "methodName": "getDimensions"
  },
  {
    "name": "analytics_get_entitlement",
    "category": "analytics",
    "methodName": "getEntitlement"
  },
  {
    "name": "analytics_get_events",
    "category": "analytics",
    "methodName": "getEvents"
  },
  {
    "name": "analytics_get_forecast",
    "category": "analytics",
    "methodName": "getForecast"
  },
  {
    "name": "analytics_get_health",
    "category": "analytics",
    "methodName": "getHealth"
  },
  {
    "name": "analytics_get_overview",
    "category": "analytics",
    "methodName": "getOverview"
  },
  {
    "name": "analytics_get_paths",
    "category": "analytics",
    "methodName": "getPaths"
  },
  {
    "name": "analytics_get_timeseries",
    "category": "analytics",
    "methodName": "getTimeseries"
  },
  {
    "name": "analytics_import_crm_csv",
    "category": "analytics",
    "methodName": "importCrmCsv"
  },
  {
    "name": "analytics_list_activation_destinations",
    "category": "analytics",
    "methodName": "listActivationDestinations"
  },
  {
    "name": "analytics_list_campaign_links",
    "category": "analytics",
    "methodName": "listCampaignLinks"
  },
  {
    "name": "analytics_list_crm_imports",
    "category": "analytics",
    "methodName": "listCrmImports"
  },
  {
    "name": "analytics_list_forms",
    "category": "analytics",
    "methodName": "listForms"
  },
  {
    "name": "analytics_list_pixels",
    "category": "analytics",
    "methodName": "listPixels"
  },
  {
    "name": "analytics_list_sites",
    "category": "analytics",
    "methodName": "listSites"
  },
  {
    "name": "commons_claim_publication",
    "category": "commons",
    "methodName": "claimPublication"
  },
  {
    "name": "commons_get_entity_linkset",
    "category": "commons",
    "methodName": "getEntityLinkset"
  },
  {
    "name": "commons_get_publication",
    "category": "commons",
    "methodName": "getPublication"
  },
  {
    "name": "commons_prepare_publication",
    "category": "commons",
    "methodName": "preparePublication"
  },
  {
    "name": "commons_publish_editorial",
    "category": "commons",
    "methodName": "publishEditorial"
  },
  {
    "name": "commons_validate_publication",
    "category": "commons",
    "methodName": "validatePublication"
  },
  {
    "name": "get_artifact_template_example",
    "category": "artifacts",
    "methodName": "getArtifactTemplateExample"
  }
] as const
export const MCP_TOOL_COUNT = MCP_TOOL_BINDINGS.length

export class SearchNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async harvestPaa(input: SearchHarvestPaa.Input): Promise<SearchHarvestPaa.Output> {
    return this.callTool('harvest_paa', input) as Promise<SearchHarvestPaa.Output>
  }

  async searchSerp(input: SearchSearchSerp.Input): Promise<SearchSearchSerp.Output> {
    return this.callTool('search_serp', input) as Promise<SearchSearchSerp.Output>
  }
}

export class WebNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async extractUrl(input: WebExtractUrl.Input): Promise<WebExtractUrl.Output> {
    return this.callTool('extract_url', input) as Promise<WebExtractUrl.Output>
  }

  async diffPage(input: WebDiffPage.Input): Promise<WebDiffPage.Output> {
    return this.callTool('diff_page', input) as Promise<WebDiffPage.Output>
  }

  async mapSiteUrls(input: WebMapSiteUrls.Input): Promise<WebMapSiteUrls.Output> {
    return this.callTool('map_site_urls', input) as Promise<WebMapSiteUrls.Output>
  }

  async mapWaybackSnapshots(input: WebMapWaybackSnapshots.Input): Promise<WebMapWaybackSnapshots.Output> {
    return this.callTool('map_wayback_snapshots', input) as Promise<WebMapWaybackSnapshots.Output>
  }

  async extractSite(input: WebExtractSite.Input): Promise<WebExtractSite.Output> {
    return this.callTool('extract_site', input) as Promise<WebExtractSite.Output>
  }

  async auditSite(input: WebAuditSite.Input): Promise<WebAuditSite.Output> {
    return this.callTool('audit_site', input) as Promise<WebAuditSite.Output>
  }

  async checkSiteExport(input: WebCheckSiteExport.Input): Promise<WebCheckSiteExport.Output> {
    return this.callTool('check_site_export', input) as Promise<WebCheckSiteExport.Output>
  }

  async archiveRead(input: WebArchiveRead.Input = {} as WebArchiveRead.Input): Promise<WebArchiveRead.Output> {
    return this.callTool('archive_read', input) as Promise<WebArchiveRead.Output>
  }
}

export class YoutubeNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async harvest(input: YoutubeHarvest.Input): Promise<YoutubeHarvest.Output> {
    return this.callTool('youtube_harvest', input) as Promise<YoutubeHarvest.Output>
  }

  async transcribe(input: YoutubeTranscribe.Input = {} as YoutubeTranscribe.Input): Promise<YoutubeTranscribe.Output> {
    return this.callTool('youtube_transcribe', input) as Promise<YoutubeTranscribe.Output>
  }
}

export class FacebookNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async pageIntel(input: FacebookPageIntel.Input = {} as FacebookPageIntel.Input): Promise<FacebookPageIntel.Output> {
    return this.callTool('facebook_page_intel', input) as Promise<FacebookPageIntel.Output>
  }

  async adSearch(input: FacebookAdSearch.Input): Promise<FacebookAdSearch.Output> {
    return this.callTool('facebook_ad_search', input) as Promise<FacebookAdSearch.Output>
  }

  async adTranscribe(input: FacebookAdTranscribe.Input): Promise<FacebookAdTranscribe.Output> {
    return this.callTool('facebook_ad_transcribe', input) as Promise<FacebookAdTranscribe.Output>
  }

  async videoTranscribe(input: FacebookVideoTranscribe.Input): Promise<FacebookVideoTranscribe.Output> {
    return this.callTool('facebook_video_transcribe', input) as Promise<FacebookVideoTranscribe.Output>
  }
}

export class RedditNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async thread(input: RedditThread.Input): Promise<RedditThread.Output> {
    return this.callTool('reddit_thread', input) as Promise<RedditThread.Output>
  }

  async trending(input: RedditTrending.Input): Promise<RedditTrending.Output> {
    return this.callTool('reddit_trending', input) as Promise<RedditTrending.Output>
  }
}

export class VideoNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async frameAnalysis(input: VideoFrameAnalysis.Input): Promise<VideoFrameAnalysis.Output> {
    return this.callTool('video_frame_analysis', input) as Promise<VideoFrameAnalysis.Output>
  }

  async frameAnalysisStatus(input: VideoFrameAnalysisStatus.Input): Promise<VideoFrameAnalysisStatus.Output> {
    return this.callTool('video_frame_analysis_status', input) as Promise<VideoFrameAnalysisStatus.Output>
  }

  async analyzeStart(input: VideoAnalyzeStart.Input): Promise<VideoAnalyzeStart.Output> {
    return this.callTool('video-analyze-start', input) as Promise<VideoAnalyzeStart.Output>
  }

  async analyzeStatus(input: VideoAnalyzeStatus.Input): Promise<VideoAnalyzeStatus.Output> {
    return this.callTool('video-analyze-status', input) as Promise<VideoAnalyzeStatus.Output>
  }
}

export class GoogleAdsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async search(input: GoogleAdsSearch.Input): Promise<GoogleAdsSearch.Output> {
    return this.callTool('google_ads_search', input) as Promise<GoogleAdsSearch.Output>
  }

  async pageIntel(input: GoogleAdsPageIntel.Input = {} as GoogleAdsPageIntel.Input): Promise<GoogleAdsPageIntel.Output> {
    return this.callTool('google_ads_page_intel', input) as Promise<GoogleAdsPageIntel.Output>
  }

  async transcribe(input: GoogleAdsTranscribe.Input): Promise<GoogleAdsTranscribe.Output> {
    return this.callTool('google_ads_transcribe', input) as Promise<GoogleAdsTranscribe.Output>
  }
}

export class InstagramNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async profileContent(input: InstagramProfileContent.Input = {} as InstagramProfileContent.Input): Promise<InstagramProfileContent.Output> {
    return this.callTool('instagram_profile_content', input) as Promise<InstagramProfileContent.Output>
  }

  async mediaDownload(input: InstagramMediaDownload.Input): Promise<InstagramMediaDownload.Output> {
    return this.callTool('instagram_media_download', input) as Promise<InstagramMediaDownload.Output>
  }
}

export class MapsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async placeIntel(input: MapsPlaceIntel.Input): Promise<MapsPlaceIntel.Output> {
    return this.callTool('maps_place_intel', input) as Promise<MapsPlaceIntel.Output>
  }

  async search(input: MapsSearch.Input): Promise<MapsSearch.Output> {
    return this.callTool('maps_search', input) as Promise<MapsSearch.Output>
  }
}

export class ReviewsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async trustpilotReviews(input: ReviewsTrustpilotReviews.Input): Promise<ReviewsTrustpilotReviews.Output> {
    return this.callTool('trustpilot_reviews', input) as Promise<ReviewsTrustpilotReviews.Output>
  }

  async g2Reviews(input: ReviewsG2Reviews.Input): Promise<ReviewsG2Reviews.Output> {
    return this.callTool('g2_reviews', input) as Promise<ReviewsG2Reviews.Output>
  }
}

export class CommonsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async searchEntities(input: CommonsSearchEntities.Input = {} as CommonsSearchEntities.Input): Promise<CommonsSearchEntities.Output> {
    return this.callTool('commons_search_entities', input) as Promise<CommonsSearchEntities.Output>
  }

  async getEntity(input: CommonsGetEntity.Input): Promise<CommonsGetEntity.Output> {
    return this.callTool('commons_get_entity', input) as Promise<CommonsGetEntity.Output>
  }

  async listNeedsLinks(input: CommonsListNeedsLinks.Input = {} as CommonsListNeedsLinks.Input): Promise<CommonsListNeedsLinks.Output> {
    return this.callTool('commons_list_needs_links', input) as Promise<CommonsListNeedsLinks.Output>
  }

  async prepareEntity(input: CommonsPrepareEntity.Input): Promise<CommonsPrepareEntity.Output> {
    return this.callTool('commons_prepare_entity', input) as Promise<CommonsPrepareEntity.Output>
  }

  async validateEntity(input: CommonsValidateEntity.Input = {} as CommonsValidateEntity.Input): Promise<CommonsValidateEntity.Output> {
    return this.callTool('commons_validate_entity', input) as Promise<CommonsValidateEntity.Output>
  }

  async submitEntity(input: CommonsSubmitEntity.Input): Promise<CommonsSubmitEntity.Output> {
    return this.callTool('commons_submit_entity', input) as Promise<CommonsSubmitEntity.Output>
  }

  async getEntityLedger(input: CommonsGetEntityLedger.Input): Promise<CommonsGetEntityLedger.Output> {
    return this.callTool('commons_get_entity_ledger', input) as Promise<CommonsGetEntityLedger.Output>
  }

  async saveFilter(input: CommonsSaveFilter.Input): Promise<CommonsSaveFilter.Output> {
    return this.callTool('commons_save_filter', input) as Promise<CommonsSaveFilter.Output>
  }

  async listFilters(input: CommonsListFilters.Input = {} as CommonsListFilters.Input): Promise<CommonsListFilters.Output> {
    return this.callTool('commons_list_filters', input) as Promise<CommonsListFilters.Output>
  }

  async claimPublication(input: CommonsClaimPublication.Input): Promise<CommonsClaimPublication.Output> {
    return this.callTool('commons_claim_publication', input) as Promise<CommonsClaimPublication.Output>
  }

  async getEntityLinkset(input: CommonsGetEntityLinkset.Input): Promise<CommonsGetEntityLinkset.Output> {
    return this.callTool('commons_get_entity_linkset', input) as Promise<CommonsGetEntityLinkset.Output>
  }

  async getPublication(input: CommonsGetPublication.Input = {} as CommonsGetPublication.Input): Promise<CommonsGetPublication.Output> {
    return this.callTool('commons_get_publication', input) as Promise<CommonsGetPublication.Output>
  }

  async preparePublication(input: CommonsPreparePublication.Input): Promise<CommonsPreparePublication.Output> {
    return this.callTool('commons_prepare_publication', input) as Promise<CommonsPreparePublication.Output>
  }

  async publishEditorial(input: CommonsPublishEditorial.Input): Promise<CommonsPublishEditorial.Output> {
    return this.callTool('commons_publish_editorial', input) as Promise<CommonsPublishEditorial.Output>
  }

  async validatePublication(input: CommonsValidatePublication.Input): Promise<CommonsValidatePublication.Output> {
    return this.callTool('commons_validate_publication', input) as Promise<CommonsValidatePublication.Output>
  }
}

export class DirectoryNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async run(input: DirectoryRun.Input): Promise<DirectoryRun.Output> {
    return this.callTool('directory_workflow', input) as Promise<DirectoryRun.Output>
  }

  async workflowStatus(input: DirectoryWorkflowStatus.Input): Promise<DirectoryWorkflowStatus.Output> {
    return this.callTool('directory_workflow_status', input) as Promise<DirectoryWorkflowStatus.Output>
  }

  async getLocalSourcebookContract(input: DirectoryGetLocalSourcebookContract.Input = {} as DirectoryGetLocalSourcebookContract.Input): Promise<DirectoryGetLocalSourcebookContract.Output> {
    return this.callTool('get-local-sourcebook-contract', input) as Promise<DirectoryGetLocalSourcebookContract.Output>
  }

  async listLocalSourcebookTags(input: DirectoryListLocalSourcebookTags.Input = {} as DirectoryListLocalSourcebookTags.Input): Promise<DirectoryListLocalSourcebookTags.Output> {
    return this.callTool('list-local-sourcebook-tags', input) as Promise<DirectoryListLocalSourcebookTags.Output>
  }

  async resolveLocalSourcebookTags(input: DirectoryResolveLocalSourcebookTags.Input): Promise<DirectoryResolveLocalSourcebookTags.Output> {
    return this.callTool('resolve-local-sourcebook-tags', input) as Promise<DirectoryResolveLocalSourcebookTags.Output>
  }

  async prepareLocalSourcebookWrite(input: DirectoryPrepareLocalSourcebookWrite.Input): Promise<DirectoryPrepareLocalSourcebookWrite.Output> {
    return this.callTool('prepare-local-sourcebook-write', input) as Promise<DirectoryPrepareLocalSourcebookWrite.Output>
  }

  async validateLocalSourcebookWrite(input: DirectoryValidateLocalSourcebookWrite.Input): Promise<DirectoryValidateLocalSourcebookWrite.Output> {
    return this.callTool('validate-local-sourcebook-write', input) as Promise<DirectoryValidateLocalSourcebookWrite.Output>
  }

  async localSourcebookCapture(input: DirectoryLocalSourcebookCapture.Input): Promise<DirectoryLocalSourcebookCapture.Output> {
    return this.callTool('local-sourcebook-capture', input) as Promise<DirectoryLocalSourcebookCapture.Output>
  }

  async localSourcebookSubmissionStatus(input: DirectoryLocalSourcebookSubmissionStatus.Input): Promise<DirectoryLocalSourcebookSubmissionStatus.Output> {
    return this.callTool('local_sourcebook_submission_status', input) as Promise<DirectoryLocalSourcebookSubmissionStatus.Output>
  }

  async localSourcebookRefresh(input: DirectoryLocalSourcebookRefresh.Input): Promise<DirectoryLocalSourcebookRefresh.Output> {
    return this.callTool('local_sourcebook_refresh', input) as Promise<DirectoryLocalSourcebookRefresh.Output>
  }

  async locationMarkets(input: DirectoryLocationMarkets.Input = {} as DirectoryLocationMarkets.Input): Promise<DirectoryLocationMarkets.Output> {
    return this.callTool('location_markets', input) as Promise<DirectoryLocationMarkets.Output>
  }
}

export class WorkflowsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async list(input: WorkflowsList.Input = {} as WorkflowsList.Input): Promise<WorkflowsList.Output> {
    return this.callTool('workflow_list', input) as Promise<WorkflowsList.Output>
  }

  async suggest(input: WorkflowsSuggest.Input): Promise<WorkflowsSuggest.Output> {
    return this.callTool('workflow_suggest', input) as Promise<WorkflowsSuggest.Output>
  }

  async run(input: WorkflowsRun.Input): Promise<WorkflowsRun.Output> {
    return this.callTool('workflow_run', input) as Promise<WorkflowsRun.Output>
  }

  async step(input: WorkflowsStep.Input): Promise<WorkflowsStep.Output> {
    return this.callTool('workflow_step', input) as Promise<WorkflowsStep.Output>
  }

  async status(input: WorkflowsStatus.Input): Promise<WorkflowsStatus.Output> {
    return this.callTool('workflow_status', input) as Promise<WorkflowsStatus.Output>
  }

  async artifactRead(input: WorkflowsArtifactRead.Input): Promise<WorkflowsArtifactRead.Output> {
    return this.callTool('workflow_artifact_read', input) as Promise<WorkflowsArtifactRead.Output>
  }

  async rankTracker(input: WorkflowsRankTracker.Input = {} as WorkflowsRankTracker.Input): Promise<WorkflowsRankTracker.Output> {
    return this.callTool('rank_tracker_workflow', input) as Promise<WorkflowsRankTracker.Output>
  }

  async queryFanout(input: WorkflowsQueryFanout.Input): Promise<WorkflowsQueryFanout.Output> {
    return this.callTool('query_fanout_workflow', input) as Promise<WorkflowsQueryFanout.Output>
  }
}

export class EditorialNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async readingRoomGuide(input: EditorialReadingRoomGuide.Input = {} as EditorialReadingRoomGuide.Input): Promise<EditorialReadingRoomGuide.Output> {
    return this.callTool('editorial_reading_room_guide', input) as Promise<EditorialReadingRoomGuide.Output>
  }

  async createReadingRoom(input: EditorialCreateReadingRoom.Input): Promise<EditorialCreateReadingRoom.Output> {
    return this.callTool('create_editorial_reading_room', input) as Promise<EditorialCreateReadingRoom.Output>
  }

  async renewReadingRoomDownload(input: EditorialRenewReadingRoomDownload.Input): Promise<EditorialRenewReadingRoomDownload.Output> {
    return this.callTool('renew_editorial_reading_room_download', input) as Promise<EditorialRenewReadingRoomDownload.Output>
  }
}

export class ArtifactsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async read(input: ArtifactsRead.Input): Promise<ArtifactsRead.Output> {
    return this.callTool('report_artifact_read', input) as Promise<ArtifactsRead.Output>
  }

  async getArtifactTemplateExample(input: ArtifactsGetArtifactTemplateExample.Input): Promise<ArtifactsGetArtifactTemplateExample.Output> {
    return this.callTool('get_artifact_template_example', input) as Promise<ArtifactsGetArtifactTemplateExample.Output>
  }
}

export class BillingNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async creditsInfo(input: BillingCreditsInfo.Input = {} as BillingCreditsInfo.Input): Promise<BillingCreditsInfo.Output> {
    return this.callTool('credits_info', input) as Promise<BillingCreditsInfo.Output>
  }
}

export class ConnectionsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async listServiceConnections(input: ConnectionsListServiceConnections.Input = {} as ConnectionsListServiceConnections.Input): Promise<ConnectionsListServiceConnections.Output> {
    return this.callTool('list_service_connections', input) as Promise<ConnectionsListServiceConnections.Output>
  }

  async testServiceConnection(input: ConnectionsTestServiceConnection.Input): Promise<ConnectionsTestServiceConnection.Output> {
    return this.callTool('test_service_connection', input) as Promise<ConnectionsTestServiceConnection.Output>
  }

  async slackSendMessage(input: ConnectionsSlackSendMessage.Input): Promise<ConnectionsSlackSendMessage.Output> {
    return this.callTool('slack_send_message', input) as Promise<ConnectionsSlackSendMessage.Output>
  }

  async gmailSendMessage(input: ConnectionsGmailSendMessage.Input): Promise<ConnectionsGmailSendMessage.Output> {
    return this.callTool('gmail_send_message', input) as Promise<ConnectionsGmailSendMessage.Output>
  }

  async gmailSearchContacts(input: ConnectionsGmailSearchContacts.Input): Promise<ConnectionsGmailSearchContacts.Output> {
    return this.callTool('gmail_search_contacts', input) as Promise<ConnectionsGmailSearchContacts.Output>
  }

  async googleCalendarCreateEvent(input: ConnectionsGoogleCalendarCreateEvent.Input): Promise<ConnectionsGoogleCalendarCreateEvent.Output> {
    return this.callTool('google_calendar_create_event', input) as Promise<ConnectionsGoogleCalendarCreateEvent.Output>
  }

  async zoomCreateMeeting(input: ConnectionsZoomCreateMeeting.Input): Promise<ConnectionsZoomCreateMeeting.Output> {
    return this.callTool('zoom_create_meeting', input) as Promise<ConnectionsZoomCreateMeeting.Output>
  }

  async readServiceConnection(input: ConnectionsReadServiceConnection.Input): Promise<ConnectionsReadServiceConnection.Output> {
    return this.callTool('read_service_connection', input) as Promise<ConnectionsReadServiceConnection.Output>
  }

  async metaAdCreativeMedia(input: ConnectionsMetaAdCreativeMedia.Input): Promise<ConnectionsMetaAdCreativeMedia.Output> {
    return this.callTool('meta_ad_creative_media', input) as Promise<ConnectionsMetaAdCreativeMedia.Output>
  }

  async importServiceConnectionToMemory(input: ConnectionsImportServiceConnectionToMemory.Input): Promise<ConnectionsImportServiceConnectionToMemory.Output> {
    return this.callTool('import_service_connection_to_memory', input) as Promise<ConnectionsImportServiceConnectionToMemory.Output>
  }

  async describeServiceConnectionTool(input: ConnectionsDescribeServiceConnectionTool.Input): Promise<ConnectionsDescribeServiceConnectionTool.Output> {
    return this.callTool('describe_service_connection_tool', input) as Promise<ConnectionsDescribeServiceConnectionTool.Output>
  }

  async exportConnectedServiceData(input: ConnectionsExportConnectedServiceData.Input): Promise<ConnectionsExportConnectedServiceData.Output> {
    return this.callTool('export_connected_service_data', input) as Promise<ConnectionsExportConnectedServiceData.Output>
  }

  async exportSearchConsoleTableData(input: ConnectionsExportSearchConsoleTableData.Input): Promise<ConnectionsExportSearchConsoleTableData.Output> {
    return this.callTool('export_search_console_table_data', input) as Promise<ConnectionsExportSearchConsoleTableData.Output>
  }

  async renewConnectedDataDownload(input: ConnectionsRenewConnectedDataDownload.Input): Promise<ConnectionsRenewConnectedDataDownload.Output> {
    return this.callTool('renew_connected_data_download', input) as Promise<ConnectionsRenewConnectedDataDownload.Output>
  }

  async callServiceConnectionAction(input: ConnectionsCallServiceConnectionAction.Input): Promise<ConnectionsCallServiceConnectionAction.Output> {
    return this.callTool('call_service_connection_action', input) as Promise<ConnectionsCallServiceConnectionAction.Output>
  }

  async setScheduledActionConnections(input: ConnectionsSetScheduledActionConnections.Input): Promise<ConnectionsSetScheduledActionConnections.Output> {
    return this.callTool('set_scheduled_action_connections', input) as Promise<ConnectionsSetScheduledActionConnections.Output>
  }
}

export class SerpIntelligenceNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async snapshot(input: SerpIntelligenceSnapshot.Input): Promise<SerpIntelligenceSnapshot.Output> {
    return this.callTool('capture_serp_snapshot', input) as Promise<SerpIntelligenceSnapshot.Output>
  }

  async pageSnapshots(input: SerpIntelligencePageSnapshots.Input = {} as SerpIntelligencePageSnapshots.Input): Promise<SerpIntelligencePageSnapshots.Output> {
    return this.callTool('capture_serp_page_snapshots', input) as Promise<SerpIntelligencePageSnapshots.Output>
  }
}

export class BrowserNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async profileConnect(input: BrowserProfileConnect.Input = {} as BrowserProfileConnect.Input): Promise<BrowserProfileConnect.Output> {
    return this.callTool('browser_profile_connect', input) as Promise<BrowserProfileConnect.Output>
  }

  async profileList(input: BrowserProfileList.Input = {} as BrowserProfileList.Input): Promise<BrowserProfileList.Output> {
    return this.callTool('browser_profile_list', input) as Promise<BrowserProfileList.Output>
  }

  async extensionImport(input: BrowserExtensionImport.Input): Promise<BrowserExtensionImport.Output> {
    return this.callTool('browser_extension_import', input) as Promise<BrowserExtensionImport.Output>
  }

  async extensionList(input: BrowserExtensionList.Input = {} as BrowserExtensionList.Input): Promise<BrowserExtensionList.Output> {
    return this.callTool('browser_extension_list', input) as Promise<BrowserExtensionList.Output>
  }

  async extensionDelete(input: BrowserExtensionDelete.Input): Promise<BrowserExtensionDelete.Output> {
    return this.callTool('browser_extension_delete', input) as Promise<BrowserExtensionDelete.Output>
  }

  async open(input: BrowserOpen.Input = {} as BrowserOpen.Input): Promise<BrowserOpen.Output> {
    return this.callTool('browser_open', input) as Promise<BrowserOpen.Output>
  }

  async screenshot(input: BrowserScreenshot.Input): Promise<BrowserScreenshot.Output> {
    return this.callTool('browser_screenshot', input) as Promise<BrowserScreenshot.Output>
  }

  async read(input: BrowserRead.Input): Promise<BrowserRead.Output> {
    return this.callTool('browser_read', input) as Promise<BrowserRead.Output>
  }

  async locate(input: BrowserLocate.Input): Promise<BrowserLocate.Output> {
    return this.callTool('browser_locate', input) as Promise<BrowserLocate.Output>
  }

  async goto(input: BrowserGoto.Input): Promise<BrowserGoto.Output> {
    return this.callTool('browser_goto', input) as Promise<BrowserGoto.Output>
  }

  async click(input: BrowserClick.Input): Promise<BrowserClick.Output> {
    return this.callTool('browser_click', input) as Promise<BrowserClick.Output>
  }

  async type(input: BrowserType.Input): Promise<BrowserType.Output> {
    return this.callTool('browser_type', input) as Promise<BrowserType.Output>
  }

  async scroll(input: BrowserScroll.Input): Promise<BrowserScroll.Output> {
    return this.callTool('browser_scroll', input) as Promise<BrowserScroll.Output>
  }

  async press(input: BrowserPress.Input): Promise<BrowserPress.Output> {
    return this.callTool('browser_press', input) as Promise<BrowserPress.Output>
  }

  async replayStart(input: BrowserReplayStart.Input): Promise<BrowserReplayStart.Output> {
    return this.callTool('browser_replay_start', input) as Promise<BrowserReplayStart.Output>
  }

  async replayStop(input: BrowserReplayStop.Input): Promise<BrowserReplayStop.Output> {
    return this.callTool('browser_replay_stop', input) as Promise<BrowserReplayStop.Output>
  }

  async listReplays(input: BrowserListReplays.Input): Promise<BrowserListReplays.Output> {
    return this.callTool('browser_list_replays', input) as Promise<BrowserListReplays.Output>
  }

  async replayDownload(input: BrowserReplayDownload.Input): Promise<BrowserReplayDownload.Output> {
    return this.callTool('browser_replay_download', input) as Promise<BrowserReplayDownload.Output>
  }

  async replayMark(input: BrowserReplayMark.Input): Promise<BrowserReplayMark.Output> {
    return this.callTool('browser_replay_mark', input) as Promise<BrowserReplayMark.Output>
  }

  async replayAnnotate(input: BrowserReplayAnnotate.Input): Promise<BrowserReplayAnnotate.Output> {
    return this.callTool('browser_replay_annotate', input) as Promise<BrowserReplayAnnotate.Output>
  }

  async close(input: BrowserClose.Input): Promise<BrowserClose.Output> {
    return this.callTool('browser_close', input) as Promise<BrowserClose.Output>
  }

  async listSessions(input: BrowserListSessions.Input = {} as BrowserListSessions.Input): Promise<BrowserListSessions.Output> {
    return this.callTool('browser_list_sessions', input) as Promise<BrowserListSessions.Output>
  }
}

export class ScheduleNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async listArtifactTemplates(input: ScheduleListArtifactTemplates.Input = {} as ScheduleListArtifactTemplates.Input): Promise<ScheduleListArtifactTemplates.Output> {
    return this.callTool('list_artifact_templates', input) as Promise<ScheduleListArtifactTemplates.Output>
  }

  async getArtifactTemplate(input: ScheduleGetArtifactTemplate.Input): Promise<ScheduleGetArtifactTemplate.Output> {
    return this.callTool('get_artifact_template', input) as Promise<ScheduleGetArtifactTemplate.Output>
  }

  async createArtifactTemplate(input: ScheduleCreateArtifactTemplate.Input = {} as ScheduleCreateArtifactTemplate.Input): Promise<ScheduleCreateArtifactTemplate.Output> {
    return this.callTool('create_artifact_template', input) as Promise<ScheduleCreateArtifactTemplate.Output>
  }

  async updateArtifactTemplate(input: ScheduleUpdateArtifactTemplate.Input): Promise<ScheduleUpdateArtifactTemplate.Output> {
    return this.callTool('update_artifact_template', input) as Promise<ScheduleUpdateArtifactTemplate.Output>
  }

  async archiveArtifactTemplate(input: ScheduleArchiveArtifactTemplate.Input): Promise<ScheduleArchiveArtifactTemplate.Output> {
    return this.callTool('archive_artifact_template', input) as Promise<ScheduleArchiveArtifactTemplate.Output>
  }

  async listScheduledRuns(input: ScheduleListScheduledRuns.Input = {} as ScheduleListScheduledRuns.Input): Promise<ScheduleListScheduledRuns.Output> {
    return this.callTool('list_scheduled_runs', input) as Promise<ScheduleListScheduledRuns.Output>
  }

  async getScheduledRun(input: ScheduleGetScheduledRun.Input): Promise<ScheduleGetScheduledRun.Output> {
    return this.callTool('get_scheduled_run', input) as Promise<ScheduleGetScheduledRun.Output>
  }

  async markScheduledRunOpened(input: ScheduleMarkScheduledRunOpened.Input): Promise<ScheduleMarkScheduledRunOpened.Output> {
    return this.callTool('mark_scheduled_run_opened', input) as Promise<ScheduleMarkScheduledRunOpened.Output>
  }

  async markScheduledRunUnopened(input: ScheduleMarkScheduledRunUnopened.Input): Promise<ScheduleMarkScheduledRunUnopened.Output> {
    return this.callTool('mark_scheduled_run_unopened', input) as Promise<ScheduleMarkScheduledRunUnopened.Output>
  }

  async archiveScheduledRun(input: ScheduleArchiveScheduledRun.Input): Promise<ScheduleArchiveScheduledRun.Output> {
    return this.callTool('archive_scheduled_run', input) as Promise<ScheduleArchiveScheduledRun.Output>
  }

  async createScheduledRunViewLink(input: ScheduleCreateScheduledRunViewLink.Input): Promise<ScheduleCreateScheduledRunViewLink.Output> {
    return this.callTool('create_scheduled_run_view_link', input) as Promise<ScheduleCreateScheduledRunViewLink.Output>
  }

  async revokeScheduledRunViewLink(input: ScheduleRevokeScheduledRunViewLink.Input): Promise<ScheduleRevokeScheduledRunViewLink.Output> {
    return this.callTool('revoke_scheduled_run_view_link', input) as Promise<ScheduleRevokeScheduledRunViewLink.Output>
  }

  async createScheduledAction(input: ScheduleCreateScheduledAction.Input): Promise<ScheduleCreateScheduledAction.Output> {
    return this.callTool('create-scheduled-action', input) as Promise<ScheduleCreateScheduledAction.Output>
  }

  async updateScheduledAction(input: ScheduleUpdateScheduledAction.Input): Promise<ScheduleUpdateScheduledAction.Output> {
    return this.callTool('update-scheduled-action', input) as Promise<ScheduleUpdateScheduledAction.Output>
  }

  async deleteScheduledAction(input: ScheduleDeleteScheduledAction.Input): Promise<ScheduleDeleteScheduledAction.Output> {
    return this.callTool('delete-scheduled-action', input) as Promise<ScheduleDeleteScheduledAction.Output>
  }

  async getScheduleLink(input: ScheduleGetScheduleLink.Input = {} as ScheduleGetScheduleLink.Input): Promise<ScheduleGetScheduleLink.Output> {
    return this.callTool('get-schedule-link', input) as Promise<ScheduleGetScheduleLink.Output>
  }

  async getScheduleStatus(input: ScheduleGetScheduleStatus.Input = {} as ScheduleGetScheduleStatus.Input): Promise<ScheduleGetScheduleStatus.Output> {
    return this.callTool('get-schedule-status', input) as Promise<ScheduleGetScheduleStatus.Output>
  }

  async listScheduledActions(input: ScheduleListScheduledActions.Input = {} as ScheduleListScheduledActions.Input): Promise<ScheduleListScheduledActions.Output> {
    return this.callTool('list-scheduled-actions', input) as Promise<ScheduleListScheduledActions.Output>
  }

  async pauseScheduledAction(input: SchedulePauseScheduledAction.Input): Promise<SchedulePauseScheduledAction.Output> {
    return this.callTool('pause-scheduled-action', input) as Promise<SchedulePauseScheduledAction.Output>
  }

  async proposeScheduledAction(input: ScheduleProposeScheduledAction.Input): Promise<ScheduleProposeScheduledAction.Output> {
    return this.callTool('propose-scheduled-action', input) as Promise<ScheduleProposeScheduledAction.Output>
  }

  async resumeScheduledAction(input: ScheduleResumeScheduledAction.Input): Promise<ScheduleResumeScheduledAction.Output> {
    return this.callTool('resume-scheduled-action', input) as Promise<ScheduleResumeScheduledAction.Output>
  }

  async revokeScheduleLink(input: ScheduleRevokeScheduleLink.Input = {} as ScheduleRevokeScheduleLink.Input): Promise<ScheduleRevokeScheduleLink.Output> {
    return this.callTool('revoke-schedule-link', input) as Promise<ScheduleRevokeScheduleLink.Output>
  }

  async setScheduleDefaults(input: ScheduleSetScheduleDefaults.Input): Promise<ScheduleSetScheduleDefaults.Output> {
    return this.callTool('set-schedule-defaults', input) as Promise<ScheduleSetScheduleDefaults.Output>
  }

  async setScheduleEntitlement(input: ScheduleSetScheduleEntitlement.Input): Promise<ScheduleSetScheduleEntitlement.Output> {
    return this.callTool('set-schedule-entitlement', input) as Promise<ScheduleSetScheduleEntitlement.Output>
  }
}

export class AccessNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async acceptShare(input: AccessAcceptShare.Input): Promise<AccessAcceptShare.Output> {
    return this.callTool('access-accept-share', input) as Promise<AccessAcceptShare.Output>
  }

  async approveSender(input: AccessApproveSender.Input): Promise<AccessApproveSender.Output> {
    return this.callTool('access-approve-sender', input) as Promise<AccessApproveSender.Output>
  }

  async declineShare(input: AccessDeclineShare.Input): Promise<AccessDeclineShare.Output> {
    return this.callTool('access-decline-share', input) as Promise<AccessDeclineShare.Output>
  }

  async getChatLink(input: AccessGetChatLink.Input = {} as AccessGetChatLink.Input): Promise<AccessGetChatLink.Output> {
    return this.callTool('get-chat-link', input) as Promise<AccessGetChatLink.Output>
  }

  async getVaultAppLink(input: AccessGetVaultAppLink.Input = {} as AccessGetVaultAppLink.Input): Promise<AccessGetVaultAppLink.Output> {
    return this.callTool('get-vault-app-link', input) as Promise<AccessGetVaultAppLink.Output>
  }

  async inboxSettings(input: AccessInboxSettings.Input): Promise<AccessInboxSettings.Output> {
    return this.callTool('access-inbox-settings', input) as Promise<AccessInboxSettings.Output>
  }

  async inviteAccount(input: AccessInviteAccount.Input): Promise<AccessInviteAccount.Output> {
    return this.callTool('access-invite-account', input) as Promise<AccessInviteAccount.Output>
  }

  async issueKey(input: AccessIssueKey.Input): Promise<AccessIssueKey.Output> {
    return this.callTool('access-issue-key', input) as Promise<AccessIssueKey.Output>
  }

  async listApprovedSenders(input: AccessListApprovedSenders.Input = {} as AccessListApprovedSenders.Input): Promise<AccessListApprovedSenders.Output> {
    return this.callTool('access-list-approved-senders', input) as Promise<AccessListApprovedSenders.Output>
  }

  async listKeys(input: AccessListKeys.Input = {} as AccessListKeys.Input): Promise<AccessListKeys.Output> {
    return this.callTool('access-list-keys', input) as Promise<AccessListKeys.Output>
  }

  async noteInbox(input: AccessNoteInbox.Input = {} as AccessNoteInbox.Input): Promise<AccessNoteInbox.Output> {
    return this.callTool('access-note-inbox', input) as Promise<AccessNoteInbox.Output>
  }

  async removeApprovedSender(input: AccessRemoveApprovedSender.Input): Promise<AccessRemoveApprovedSender.Output> {
    return this.callTool('access-remove-approved-sender', input) as Promise<AccessRemoveApprovedSender.Output>
  }

  async revokeChatLink(input: AccessRevokeChatLink.Input = {} as AccessRevokeChatLink.Input): Promise<AccessRevokeChatLink.Output> {
    return this.callTool('revoke-chat-link', input) as Promise<AccessRevokeChatLink.Output>
  }

  async revokeKey(input: AccessRevokeKey.Input): Promise<AccessRevokeKey.Output> {
    return this.callTool('access-revoke-key', input) as Promise<AccessRevokeKey.Output>
  }

  async revokeShare(input: AccessRevokeShare.Input): Promise<AccessRevokeShare.Output> {
    return this.callTool('access-revoke-share', input) as Promise<AccessRevokeShare.Output>
  }

  async revokeVaultAppLink(input: AccessRevokeVaultAppLink.Input = {} as AccessRevokeVaultAppLink.Input): Promise<AccessRevokeVaultAppLink.Output> {
    return this.callTool('revoke-vault-app-link', input) as Promise<AccessRevokeVaultAppLink.Output>
  }

  async setAgentIdentity(input: AccessSetAgentIdentity.Input): Promise<AccessSetAgentIdentity.Output> {
    return this.callTool('set-agent-identity', input) as Promise<AccessSetAgentIdentity.Output>
  }

  async setScope(input: AccessSetScope.Input): Promise<AccessSetScope.Output> {
    return this.callTool('access-set-scope', input) as Promise<AccessSetScope.Output>
  }

  async shareNote(input: AccessShareNote.Input): Promise<AccessShareNote.Output> {
    return this.callTool('access-share-note', input) as Promise<AccessShareNote.Output>
  }

  async shareVault(input: AccessShareVault.Input): Promise<AccessShareVault.Output> {
    return this.callTool('access-share-vault', input) as Promise<AccessShareVault.Output>
  }

  async swapVault(input: AccessSwapVault.Input): Promise<AccessSwapVault.Output> {
    return this.callTool('access-swap-vault', input) as Promise<AccessSwapVault.Output>
  }

  async switchAccount(input: AccessSwitchAccount.Input = {} as AccessSwitchAccount.Input): Promise<AccessSwitchAccount.Output> {
    return this.callTool('access-switch-account', input) as Promise<AccessSwitchAccount.Output>
  }

  async unlinkShare(input: AccessUnlinkShare.Input): Promise<AccessUnlinkShare.Output> {
    return this.callTool('access-unlink-share', input) as Promise<AccessUnlinkShare.Output>
  }
}

export class CaptureNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async memoryCapture(input: CaptureMemoryCapture.Input): Promise<CaptureMemoryCapture.Output> {
    return this.callTool('memory-capture', input) as Promise<CaptureMemoryCapture.Output>
  }

  async memoryQuestions(input: CaptureMemoryQuestions.Input = {} as CaptureMemoryQuestions.Input): Promise<CaptureMemoryQuestions.Output> {
    return this.callTool('memory-questions', input) as Promise<CaptureMemoryQuestions.Output>
  }

  async prepareMemoryWrite(input: CapturePrepareMemoryWrite.Input): Promise<CapturePrepareMemoryWrite.Output> {
    return this.callTool('prepare-memory-write', input) as Promise<CapturePrepareMemoryWrite.Output>
  }

  async validateMemoryWrite(input: CaptureValidateMemoryWrite.Input): Promise<CaptureValidateMemoryWrite.Output> {
    return this.callTool('validate-memory-write', input) as Promise<CaptureValidateMemoryWrite.Output>
  }
}

export class ChannelsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async createChannel(input: ChannelsCreateChannel.Input): Promise<ChannelsCreateChannel.Output> {
    return this.callTool('create-channel', input) as Promise<ChannelsCreateChannel.Output>
  }

  async getMessageNote(input: ChannelsGetMessageNote.Input): Promise<ChannelsGetMessageNote.Output> {
    return this.callTool('get-message-note', input) as Promise<ChannelsGetMessageNote.Output>
  }

  async listChannelMembers(input: ChannelsListChannelMembers.Input): Promise<ChannelsListChannelMembers.Output> {
    return this.callTool('list-channel-members', input) as Promise<ChannelsListChannelMembers.Output>
  }

  async listChannelMessages(input: ChannelsListChannelMessages.Input): Promise<ChannelsListChannelMessages.Output> {
    return this.callTool('list-channel-messages', input) as Promise<ChannelsListChannelMessages.Output>
  }

  async myMentions(input: ChannelsMyMentions.Input = {} as ChannelsMyMentions.Input): Promise<ChannelsMyMentions.Output> {
    return this.callTool('my-mentions', input) as Promise<ChannelsMyMentions.Output>
  }

  async pollChannel(input: ChannelsPollChannel.Input): Promise<ChannelsPollChannel.Output> {
    return this.callTool('poll-channel', input) as Promise<ChannelsPollChannel.Output>
  }

  async postMessage(input: ChannelsPostMessage.Input): Promise<ChannelsPostMessage.Output> {
    return this.callTool('post-message', input) as Promise<ChannelsPostMessage.Output>
  }

  async reactMessage(input: ChannelsReactMessage.Input): Promise<ChannelsReactMessage.Output> {
    return this.callTool('react-message', input) as Promise<ChannelsReactMessage.Output>
  }

  async removeChannelMember(input: ChannelsRemoveChannelMember.Input): Promise<ChannelsRemoveChannelMember.Output> {
    return this.callTool('remove-channel-member', input) as Promise<ChannelsRemoveChannelMember.Output>
  }

  async replyMessage(input: ChannelsReplyMessage.Input): Promise<ChannelsReplyMessage.Output> {
    return this.callTool('reply-message', input) as Promise<ChannelsReplyMessage.Output>
  }
}

export class FactsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async history(input: FactsHistory.Input): Promise<FactsHistory.Output> {
    return this.callTool('fact-history', input) as Promise<FactsHistory.Output>
  }

  async recordFact(input: FactsRecordFact.Input): Promise<FactsRecordFact.Output> {
    return this.callTool('record-fact', input) as Promise<FactsRecordFact.Output>
  }
}

export class GraphNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async memoryBacklinks(input: GraphMemoryBacklinks.Input): Promise<GraphMemoryBacklinks.Output> {
    return this.callTool('memory-backlinks', input) as Promise<GraphMemoryBacklinks.Output>
  }

  async memoryGraphPath(input: GraphMemoryGraphPath.Input): Promise<GraphMemoryGraphPath.Output> {
    return this.callTool('memory-graph-path', input) as Promise<GraphMemoryGraphPath.Output>
  }

  async memoryGraphUniverse(input: GraphMemoryGraphUniverse.Input): Promise<GraphMemoryGraphUniverse.Output> {
    return this.callTool('memory-graph-universe', input) as Promise<GraphMemoryGraphUniverse.Output>
  }
}

export class LibraryNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async ingest(input: LibraryIngest.Input): Promise<LibraryIngest.Output> {
    return this.callTool('library-ingest', input) as Promise<LibraryIngest.Output>
  }
}

export class MemoryNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async bulkDeleteNotes(input: MemoryBulkDeleteNotes.Input = {} as MemoryBulkDeleteNotes.Input): Promise<MemoryBulkDeleteNotes.Output> {
    return this.callTool('bulk-delete-notes', input) as Promise<MemoryBulkDeleteNotes.Output>
  }

  async deleteNote(input: MemoryDeleteNote.Input = {} as MemoryDeleteNote.Input): Promise<MemoryDeleteNote.Output> {
    return this.callTool('delete-note', input) as Promise<MemoryDeleteNote.Output>
  }

  async export(input: MemoryExport.Input = {} as MemoryExport.Input): Promise<MemoryExport.Output> {
    return this.callTool('memory-export', input) as Promise<MemoryExport.Output>
  }

  async get(input: MemoryGet.Input = {} as MemoryGet.Input): Promise<MemoryGet.Output> {
    return this.callTool('memory-get', input) as Promise<MemoryGet.Output>
  }

  async list(input: MemoryList.Input = {} as MemoryList.Input): Promise<MemoryList.Output> {
    return this.callTool('memory-list', input) as Promise<MemoryList.Output>
  }

  async put(input: MemoryPut.Input): Promise<MemoryPut.Output> {
    return this.callTool('memory-put', input) as Promise<MemoryPut.Output>
  }

  async search(input: MemorySearch.Input): Promise<MemorySearch.Output> {
    return this.callTool('memory-search', input) as Promise<MemorySearch.Output>
  }

  async suggest(input: MemorySuggest.Input): Promise<MemorySuggest.Output> {
    return this.callTool('memory-suggest', input) as Promise<MemorySuggest.Output>
  }

  async upload(input: MemoryUpload.Input): Promise<MemoryUpload.Output> {
    return this.callTool('memory-upload', input) as Promise<MemoryUpload.Output>
  }
}

export class RecallNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async temporalRecall(input: RecallTemporalRecall.Input = {} as RecallTemporalRecall.Input): Promise<RecallTemporalRecall.Output> {
    return this.callTool('temporal-recall', input) as Promise<RecallTemporalRecall.Output>
  }
}

export class StorageNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async costUsage(input: StorageCostUsage.Input = {} as StorageCostUsage.Input): Promise<StorageCostUsage.Output> {
    return this.callTool('cost-usage', input) as Promise<StorageCostUsage.Output>
  }

  async usage(input: StorageUsage.Input = {} as StorageUsage.Input): Promise<StorageUsage.Output> {
    return this.callTool('storage-usage', input) as Promise<StorageUsage.Output>
  }
}

export class TablesNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async create(input: TablesCreate.Input): Promise<TablesCreate.Output> {
    return this.callTool('table-create', input) as Promise<TablesCreate.Output>
  }

  async deleteRows(input: TablesDeleteRows.Input): Promise<TablesDeleteRows.Output> {
    return this.callTool('table-delete-rows', input) as Promise<TablesDeleteRows.Output>
  }

  async describe(input: TablesDescribe.Input): Promise<TablesDescribe.Output> {
    return this.callTool('table-describe', input) as Promise<TablesDescribe.Output>
  }

  async drop(input: TablesDrop.Input): Promise<TablesDrop.Output> {
    return this.callTool('table-drop', input) as Promise<TablesDrop.Output>
  }

  async insertRows(input: TablesInsertRows.Input): Promise<TablesInsertRows.Output> {
    return this.callTool('table-insert-rows', input) as Promise<TablesInsertRows.Output>
  }

  async list(input: TablesList.Input = {} as TablesList.Input): Promise<TablesList.Output> {
    return this.callTool('table-list', input) as Promise<TablesList.Output>
  }

  async query(input: TablesQuery.Input): Promise<TablesQuery.Output> {
    return this.callTool('table-query', input) as Promise<TablesQuery.Output>
  }
}

export class TagsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async listMemoryTags(input: TagsListMemoryTags.Input = {} as TagsListMemoryTags.Input): Promise<TagsListMemoryTags.Output> {
    return this.callTool('list-memory-tags', input) as Promise<TagsListMemoryTags.Output>
  }

  async mergeMemoryTags(input: TagsMergeMemoryTags.Input): Promise<TagsMergeMemoryTags.Output> {
    return this.callTool('merge-memory-tags', input) as Promise<TagsMergeMemoryTags.Output>
  }

  async resolveMemoryTags(input: TagsResolveMemoryTags.Input): Promise<TagsResolveMemoryTags.Output> {
    return this.callTool('resolve-memory-tags', input) as Promise<TagsResolveMemoryTags.Output>
  }

  async upsertMemoryTag(input: TagsUpsertMemoryTag.Input): Promise<TagsUpsertMemoryTag.Output> {
    return this.callTool('upsert-memory-tag', input) as Promise<TagsUpsertMemoryTag.Output>
  }
}

export class VaultsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async addVault(input: VaultsAddVault.Input): Promise<VaultsAddVault.Output> {
    return this.callTool('add-vault', input) as Promise<VaultsAddVault.Output>
  }

  async createSecureVault(input: VaultsCreateSecureVault.Input): Promise<VaultsCreateSecureVault.Output> {
    return this.callTool('create-secure-vault', input) as Promise<VaultsCreateSecureVault.Output>
  }

  async deleteVault(input: VaultsDeleteVault.Input): Promise<VaultsDeleteVault.Output> {
    return this.callTool('delete-vault', input) as Promise<VaultsDeleteVault.Output>
  }

  async getVaultContract(input: VaultsGetVaultContract.Input): Promise<VaultsGetVaultContract.Output> {
    return this.callTool('get-vault-contract', input) as Promise<VaultsGetVaultContract.Output>
  }

  async listSharedWithMe(input: VaultsListSharedWithMe.Input = {} as VaultsListSharedWithMe.Input): Promise<VaultsListSharedWithMe.Output> {
    return this.callTool('list-shared-with-me', input) as Promise<VaultsListSharedWithMe.Output>
  }

  async listVaults(input: VaultsListVaults.Input = {} as VaultsListVaults.Input): Promise<VaultsListVaults.Output> {
    return this.callTool('list-vaults', input) as Promise<VaultsListVaults.Output>
  }

  async provisionDefaults(input: VaultsProvisionDefaults.Input): Promise<VaultsProvisionDefaults.Output> {
    return this.callTool('provision-defaults', input) as Promise<VaultsProvisionDefaults.Output>
  }

  async routeMemory(input: VaultsRouteMemory.Input): Promise<VaultsRouteMemory.Output> {
    return this.callTool('route-memory', input) as Promise<VaultsRouteMemory.Output>
  }
}

export class WebhooksNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async createWebhook(input: WebhooksCreateWebhook.Input = {} as WebhooksCreateWebhook.Input): Promise<WebhooksCreateWebhook.Output> {
    return this.callTool('create-webhook', input) as Promise<WebhooksCreateWebhook.Output>
  }

  async listWebhooks(input: WebhooksListWebhooks.Input = {} as WebhooksListWebhooks.Input): Promise<WebhooksListWebhooks.Output> {
    return this.callTool('list-webhooks', input) as Promise<WebhooksListWebhooks.Output>
  }

  async revokeWebhook(input: WebhooksRevokeWebhook.Input): Promise<WebhooksRevokeWebhook.Output> {
    return this.callTool('revoke-webhook', input) as Promise<WebhooksRevokeWebhook.Output>
  }
}

export class ImagesNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async projectCreate(input: ImagesProjectCreate.Input): Promise<ImagesProjectCreate.Output> {
    return this.callTool('image_project_create', input) as Promise<ImagesProjectCreate.Output>
  }

  async projectList(input: ImagesProjectList.Input = {} as ImagesProjectList.Input): Promise<ImagesProjectList.Output> {
    return this.callTool('image_project_list', input) as Promise<ImagesProjectList.Output>
  }

  async folderCreate(input: ImagesFolderCreate.Input): Promise<ImagesFolderCreate.Output> {
    return this.callTool('image_folder_create', input) as Promise<ImagesFolderCreate.Output>
  }

  async folderList(input: ImagesFolderList.Input): Promise<ImagesFolderList.Output> {
    return this.callTool('image_folder_list', input) as Promise<ImagesFolderList.Output>
  }

  async assetSave(input: ImagesAssetSave.Input): Promise<ImagesAssetSave.Output> {
    return this.callTool('image_asset_save', input) as Promise<ImagesAssetSave.Output>
  }

  async assetGet(input: ImagesAssetGet.Input): Promise<ImagesAssetGet.Output> {
    return this.callTool('image_asset_get', input) as Promise<ImagesAssetGet.Output>
  }

  async assetList(input: ImagesAssetList.Input = {} as ImagesAssetList.Input): Promise<ImagesAssetList.Output> {
    return this.callTool('image_asset_list', input) as Promise<ImagesAssetList.Output>
  }

  async assetSearch(input: ImagesAssetSearch.Input = {} as ImagesAssetSearch.Input): Promise<ImagesAssetSearch.Output> {
    return this.callTool('image_asset_search', input) as Promise<ImagesAssetSearch.Output>
  }

  async assetMove(input: ImagesAssetMove.Input): Promise<ImagesAssetMove.Output> {
    return this.callTool('image_asset_move', input) as Promise<ImagesAssetMove.Output>
  }

  async assetDelete(input: ImagesAssetDelete.Input): Promise<ImagesAssetDelete.Output> {
    return this.callTool('image_asset_delete', input) as Promise<ImagesAssetDelete.Output>
  }
}

export class AnalyticsNamespace {
  constructor(private readonly callTool: McpToolCallFn) {}

  async createActivationDestination(input: AnalyticsCreateActivationDestination.Input): Promise<AnalyticsCreateActivationDestination.Output> {
    return this.callTool('analytics_create_activation_destination', input) as Promise<AnalyticsCreateActivationDestination.Output>
  }

  async createCampaignLink(input: AnalyticsCreateCampaignLink.Input): Promise<AnalyticsCreateCampaignLink.Output> {
    return this.callTool('analytics_create_campaign_link', input) as Promise<AnalyticsCreateCampaignLink.Output>
  }

  async createExport(input: AnalyticsCreateExport.Input): Promise<AnalyticsCreateExport.Output> {
    return this.callTool('analytics_create_export', input) as Promise<AnalyticsCreateExport.Output>
  }

  async createForm(input: AnalyticsCreateForm.Input): Promise<AnalyticsCreateForm.Output> {
    return this.callTool('analytics_create_form', input) as Promise<AnalyticsCreateForm.Output>
  }

  async getAcquisition(input: AnalyticsGetAcquisition.Input): Promise<AnalyticsGetAcquisition.Output> {
    return this.callTool('analytics_get_acquisition', input) as Promise<AnalyticsGetAcquisition.Output>
  }

  async getBusinessMetrics(input: AnalyticsGetBusinessMetrics.Input): Promise<AnalyticsGetBusinessMetrics.Output> {
    return this.callTool('analytics_get_business_metrics', input) as Promise<AnalyticsGetBusinessMetrics.Output>
  }

  async getChannelBreakdown(input: AnalyticsGetChannelBreakdown.Input): Promise<AnalyticsGetChannelBreakdown.Output> {
    return this.callTool('analytics_get_channel_breakdown', input) as Promise<AnalyticsGetChannelBreakdown.Output>
  }

  async getContent(input: AnalyticsGetContent.Input): Promise<AnalyticsGetContent.Output> {
    return this.callTool('analytics_get_content', input) as Promise<AnalyticsGetContent.Output>
  }

  async getConversions(input: AnalyticsGetConversions.Input): Promise<AnalyticsGetConversions.Output> {
    return this.callTool('analytics_get_conversions', input) as Promise<AnalyticsGetConversions.Output>
  }

  async getDimensions(input: AnalyticsGetDimensions.Input): Promise<AnalyticsGetDimensions.Output> {
    return this.callTool('analytics_get_dimensions', input) as Promise<AnalyticsGetDimensions.Output>
  }

  async getEntitlement(input: AnalyticsGetEntitlement.Input = {} as AnalyticsGetEntitlement.Input): Promise<AnalyticsGetEntitlement.Output> {
    return this.callTool('analytics_get_entitlement', input) as Promise<AnalyticsGetEntitlement.Output>
  }

  async getEvents(input: AnalyticsGetEvents.Input): Promise<AnalyticsGetEvents.Output> {
    return this.callTool('analytics_get_events', input) as Promise<AnalyticsGetEvents.Output>
  }

  async getForecast(input: AnalyticsGetForecast.Input): Promise<AnalyticsGetForecast.Output> {
    return this.callTool('analytics_get_forecast', input) as Promise<AnalyticsGetForecast.Output>
  }

  async getHealth(input: AnalyticsGetHealth.Input): Promise<AnalyticsGetHealth.Output> {
    return this.callTool('analytics_get_health', input) as Promise<AnalyticsGetHealth.Output>
  }

  async getOverview(input: AnalyticsGetOverview.Input): Promise<AnalyticsGetOverview.Output> {
    return this.callTool('analytics_get_overview', input) as Promise<AnalyticsGetOverview.Output>
  }

  async getPaths(input: AnalyticsGetPaths.Input): Promise<AnalyticsGetPaths.Output> {
    return this.callTool('analytics_get_paths', input) as Promise<AnalyticsGetPaths.Output>
  }

  async getTimeseries(input: AnalyticsGetTimeseries.Input): Promise<AnalyticsGetTimeseries.Output> {
    return this.callTool('analytics_get_timeseries', input) as Promise<AnalyticsGetTimeseries.Output>
  }

  async importCrmCsv(input: AnalyticsImportCrmCsv.Input): Promise<AnalyticsImportCrmCsv.Output> {
    return this.callTool('analytics_import_crm_csv', input) as Promise<AnalyticsImportCrmCsv.Output>
  }

  async listActivationDestinations(input: AnalyticsListActivationDestinations.Input): Promise<AnalyticsListActivationDestinations.Output> {
    return this.callTool('analytics_list_activation_destinations', input) as Promise<AnalyticsListActivationDestinations.Output>
  }

  async listCampaignLinks(input: AnalyticsListCampaignLinks.Input): Promise<AnalyticsListCampaignLinks.Output> {
    return this.callTool('analytics_list_campaign_links', input) as Promise<AnalyticsListCampaignLinks.Output>
  }

  async listCrmImports(input: AnalyticsListCrmImports.Input): Promise<AnalyticsListCrmImports.Output> {
    return this.callTool('analytics_list_crm_imports', input) as Promise<AnalyticsListCrmImports.Output>
  }

  async listForms(input: AnalyticsListForms.Input): Promise<AnalyticsListForms.Output> {
    return this.callTool('analytics_list_forms', input) as Promise<AnalyticsListForms.Output>
  }

  async listPixels(input: AnalyticsListPixels.Input): Promise<AnalyticsListPixels.Output> {
    return this.callTool('analytics_list_pixels', input) as Promise<AnalyticsListPixels.Output>
  }

  async listSites(input: AnalyticsListSites.Input = {} as AnalyticsListSites.Input): Promise<AnalyticsListSites.Output> {
    return this.callTool('analytics_list_sites', input) as Promise<AnalyticsListSites.Output>
  }
}

export class GeneratedMcpToolsClient {
  readonly search: SearchNamespace
  readonly web: WebNamespace
  readonly youtube: YoutubeNamespace
  readonly facebook: FacebookNamespace
  readonly reddit: RedditNamespace
  readonly video: VideoNamespace
  readonly googleAds: GoogleAdsNamespace
  readonly instagram: InstagramNamespace
  readonly maps: MapsNamespace
  readonly reviews: ReviewsNamespace
  readonly commons: CommonsNamespace
  readonly directory: DirectoryNamespace
  readonly workflows: WorkflowsNamespace
  readonly editorial: EditorialNamespace
  readonly artifacts: ArtifactsNamespace
  readonly billing: BillingNamespace
  readonly connections: ConnectionsNamespace
  readonly serpIntelligence: SerpIntelligenceNamespace
  readonly browser: BrowserNamespace
  readonly schedule: ScheduleNamespace
  readonly access: AccessNamespace
  readonly capture: CaptureNamespace
  readonly channels: ChannelsNamespace
  readonly facts: FactsNamespace
  readonly graph: GraphNamespace
  readonly library: LibraryNamespace
  readonly memory: MemoryNamespace
  readonly recall: RecallNamespace
  readonly storage: StorageNamespace
  readonly tables: TablesNamespace
  readonly tags: TagsNamespace
  readonly vaults: VaultsNamespace
  readonly webhooks: WebhooksNamespace
  readonly images: ImagesNamespace
  readonly analytics: AnalyticsNamespace

  constructor(callTool: McpToolCallFn) {
    this.search = new SearchNamespace(callTool)
    this.web = new WebNamespace(callTool)
    this.youtube = new YoutubeNamespace(callTool)
    this.facebook = new FacebookNamespace(callTool)
    this.reddit = new RedditNamespace(callTool)
    this.video = new VideoNamespace(callTool)
    this.googleAds = new GoogleAdsNamespace(callTool)
    this.instagram = new InstagramNamespace(callTool)
    this.maps = new MapsNamespace(callTool)
    this.reviews = new ReviewsNamespace(callTool)
    this.commons = new CommonsNamespace(callTool)
    this.directory = new DirectoryNamespace(callTool)
    this.workflows = new WorkflowsNamespace(callTool)
    this.editorial = new EditorialNamespace(callTool)
    this.artifacts = new ArtifactsNamespace(callTool)
    this.billing = new BillingNamespace(callTool)
    this.connections = new ConnectionsNamespace(callTool)
    this.serpIntelligence = new SerpIntelligenceNamespace(callTool)
    this.browser = new BrowserNamespace(callTool)
    this.schedule = new ScheduleNamespace(callTool)
    this.access = new AccessNamespace(callTool)
    this.capture = new CaptureNamespace(callTool)
    this.channels = new ChannelsNamespace(callTool)
    this.facts = new FactsNamespace(callTool)
    this.graph = new GraphNamespace(callTool)
    this.library = new LibraryNamespace(callTool)
    this.memory = new MemoryNamespace(callTool)
    this.recall = new RecallNamespace(callTool)
    this.storage = new StorageNamespace(callTool)
    this.tables = new TablesNamespace(callTool)
    this.tags = new TagsNamespace(callTool)
    this.vaults = new VaultsNamespace(callTool)
    this.webhooks = new WebhooksNamespace(callTool)
    this.images = new ImagesNamespace(callTool)
    this.analytics = new AnalyticsNamespace(callTool)
  }
}
