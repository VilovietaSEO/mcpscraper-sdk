from typing import Any

from .mcp_models.access_accept_share import AccessAcceptShareInput, AccessAcceptShareOutput
from .mcp_models.access_approve_sender import AccessApproveSenderInput, AccessApproveSenderOutput
from .mcp_models.access_decline_share import AccessDeclineShareInput, AccessDeclineShareOutput
from .mcp_models.access_inbox_settings import AccessInboxSettingsInput, AccessInboxSettingsOutput
from .mcp_models.access_invite_account import AccessInviteAccountInput, AccessInviteAccountOutput
from .mcp_models.access_issue_key import AccessIssueKeyInput, AccessIssueKeyOutput
from .mcp_models.access_list_approved_senders import AccessListApprovedSendersInput, AccessListApprovedSendersOutput
from .mcp_models.access_list_keys import AccessListKeysInput, AccessListKeysOutput
from .mcp_models.access_note_inbox import AccessNoteInboxInput, AccessNoteInboxOutput
from .mcp_models.access_remove_approved_sender import AccessRemoveApprovedSenderInput, AccessRemoveApprovedSenderOutput
from .mcp_models.access_revoke_key import AccessRevokeKeyInput, AccessRevokeKeyOutput
from .mcp_models.access_revoke_share import AccessRevokeShareInput, AccessRevokeShareOutput
from .mcp_models.access_set_scope import AccessSetScopeInput, AccessSetScopeOutput
from .mcp_models.access_share_note import AccessShareNoteInput, AccessShareNoteOutput
from .mcp_models.access_share_vault import AccessShareVaultInput, AccessShareVaultOutput
from .mcp_models.access_swap_vault import AccessSwapVaultInput, AccessSwapVaultOutput
from .mcp_models.access_switch_account import AccessSwitchAccountInput, AccessSwitchAccountOutput
from .mcp_models.access_unlink_share import AccessUnlinkShareInput, AccessUnlinkShareOutput
from .mcp_models.add_vault import AddVaultInput, AddVaultOutput
from .mcp_models.audit_site import AuditSiteInput, AuditSiteOutput
from .mcp_models.browser_click import BrowserClickInput, BrowserClickOutput
from .mcp_models.browser_close import BrowserCloseInput, BrowserCloseOutput
from .mcp_models.browser_extension_delete import BrowserExtensionDeleteInput, BrowserExtensionDeleteOutput
from .mcp_models.browser_extension_import import BrowserExtensionImportInput, BrowserExtensionImportOutput
from .mcp_models.browser_extension_list import BrowserExtensionListInput, BrowserExtensionListOutput
from .mcp_models.browser_goto import BrowserGotoInput, BrowserGotoOutput
from .mcp_models.browser_list_replays import BrowserListReplaysInput, BrowserListReplaysOutput
from .mcp_models.browser_list_sessions import BrowserListSessionsInput, BrowserListSessionsOutput
from .mcp_models.browser_locate import BrowserLocateInput, BrowserLocateOutput
from .mcp_models.browser_open import BrowserOpenInput, BrowserOpenOutput
from .mcp_models.browser_press import BrowserPressInput, BrowserPressOutput
from .mcp_models.browser_profile_connect import BrowserProfileConnectInput, BrowserProfileConnectOutput
from .mcp_models.browser_profile_list import BrowserProfileListInput, BrowserProfileListOutput
from .mcp_models.browser_read import BrowserReadInput, BrowserReadOutput
from .mcp_models.browser_replay_annotate import BrowserReplayAnnotateInput, BrowserReplayAnnotateOutput
from .mcp_models.browser_replay_download import BrowserReplayDownloadInput, BrowserReplayDownloadOutput
from .mcp_models.browser_replay_mark import BrowserReplayMarkInput, BrowserReplayMarkOutput
from .mcp_models.browser_replay_start import BrowserReplayStartInput, BrowserReplayStartOutput
from .mcp_models.browser_replay_stop import BrowserReplayStopInput, BrowserReplayStopOutput
from .mcp_models.browser_screenshot import BrowserScreenshotInput, BrowserScreenshotOutput
from .mcp_models.browser_scroll import BrowserScrollInput, BrowserScrollOutput
from .mcp_models.browser_type import BrowserTypeInput, BrowserTypeOutput
from .mcp_models.call_service_connection_action import CallServiceConnectionActionInput, CallServiceConnectionActionOutput
from .mcp_models.capture_serp_page_snapshots import CaptureSerpPageSnapshotsInput, CaptureSerpPageSnapshotsOutput
from .mcp_models.capture_serp_snapshot import CaptureSerpSnapshotInput, CaptureSerpSnapshotOutput
from .mcp_models.cost_usage import CostUsageInput, CostUsageOutput
from .mcp_models.create_channel import CreateChannelInput, CreateChannelOutput
from .mcp_models.create_scheduled_action import CreateScheduledActionInput, CreateScheduledActionOutput
from .mcp_models.create_secure_vault import CreateSecureVaultInput, CreateSecureVaultOutput
from .mcp_models.create_webhook import CreateWebhookInput, CreateWebhookOutput
from .mcp_models.credits_info import CreditsInfoInput, CreditsInfoOutput
from .mcp_models.delete_note import DeleteNoteInput, DeleteNoteOutput
from .mcp_models.delete_scheduled_action import DeleteScheduledActionInput, DeleteScheduledActionOutput
from .mcp_models.delete_vault import DeleteVaultInput, DeleteVaultOutput
from .mcp_models.diff_page import DiffPageInput, DiffPageOutput
from .mcp_models.directory_workflow import DirectoryWorkflowInput, DirectoryWorkflowOutput
from .mcp_models.export_connected_service_data import ExportConnectedServiceDataInput, ExportConnectedServiceDataOutput
from .mcp_models.extract_site import ExtractSiteInput, ExtractSiteOutput
from .mcp_models.extract_url import ExtractUrlInput, ExtractUrlOutput
from .mcp_models.facebook_ad_search import FacebookAdSearchInput, FacebookAdSearchOutput
from .mcp_models.facebook_ad_transcribe import FacebookAdTranscribeInput, FacebookAdTranscribeOutput
from .mcp_models.facebook_page_intel import FacebookPageIntelInput, FacebookPageIntelOutput
from .mcp_models.facebook_video_transcribe import FacebookVideoTranscribeInput, FacebookVideoTranscribeOutput
from .mcp_models.fact_history import FactHistoryInput, FactHistoryOutput
from .mcp_models.g2_reviews import G2ReviewsInput, G2ReviewsOutput
from .mcp_models.get_chat_link import GetChatLinkInput, GetChatLinkOutput
from .mcp_models.get_message_note import GetMessageNoteInput, GetMessageNoteOutput
from .mcp_models.get_schedule_link import GetScheduleLinkInput, GetScheduleLinkOutput
from .mcp_models.get_schedule_status import GetScheduleStatusInput, GetScheduleStatusOutput
from .mcp_models.get_vault_contract import GetVaultContractInput, GetVaultContractOutput
from .mcp_models.gmail_send_message import GmailSendMessageInput, GmailSendMessageOutput
from .mcp_models.google_ads_page_intel import GoogleAdsPageIntelInput, GoogleAdsPageIntelOutput
from .mcp_models.google_ads_search import GoogleAdsSearchInput, GoogleAdsSearchOutput
from .mcp_models.google_ads_transcribe import GoogleAdsTranscribeInput, GoogleAdsTranscribeOutput
from .mcp_models.google_calendar_create_event import GoogleCalendarCreateEventInput, GoogleCalendarCreateEventOutput
from .mcp_models.harvest_paa import HarvestPaaInput, HarvestPaaOutput
from .mcp_models.instagram_media_download import InstagramMediaDownloadInput, InstagramMediaDownloadOutput
from .mcp_models.instagram_profile_content import InstagramProfileContentInput, InstagramProfileContentOutput
from .mcp_models.library_ingest import LibraryIngestInput, LibraryIngestOutput
from .mcp_models.list_channel_members import ListChannelMembersInput, ListChannelMembersOutput
from .mcp_models.list_channel_messages import ListChannelMessagesInput, ListChannelMessagesOutput
from .mcp_models.list_memory_tags import ListMemoryTagsInput, ListMemoryTagsOutput
from .mcp_models.list_scheduled_actions import ListScheduledActionsInput, ListScheduledActionsOutput
from .mcp_models.list_service_connections import ListServiceConnectionsInput, ListServiceConnectionsOutput
from .mcp_models.list_shared_with_me import ListSharedWithMeInput, ListSharedWithMeOutput
from .mcp_models.list_vaults import ListVaultsInput, ListVaultsOutput
from .mcp_models.list_webhooks import ListWebhooksInput, ListWebhooksOutput
from .mcp_models.map_site_urls import MapSiteUrlsInput, MapSiteUrlsOutput
from .mcp_models.maps_place_intel import MapsPlaceIntelInput, MapsPlaceIntelOutput
from .mcp_models.maps_search import MapsSearchInput, MapsSearchOutput
from .mcp_models.memory_backlinks import MemoryBacklinksInput, MemoryBacklinksOutput
from .mcp_models.memory_capture import MemoryCaptureInput, MemoryCaptureOutput
from .mcp_models.memory_export import MemoryExportInput, MemoryExportOutput
from .mcp_models.memory_get import MemoryGetInput, MemoryGetOutput
from .mcp_models.memory_graph_path import MemoryGraphPathInput, MemoryGraphPathOutput
from .mcp_models.memory_graph_universe import MemoryGraphUniverseInput, MemoryGraphUniverseOutput
from .mcp_models.memory_list import MemoryListInput, MemoryListOutput
from .mcp_models.memory_put import MemoryPutInput, MemoryPutOutput
from .mcp_models.memory_questions import MemoryQuestionsInput, MemoryQuestionsOutput
from .mcp_models.memory_search import MemorySearchInput, MemorySearchOutput
from .mcp_models.memory_suggest import MemorySuggestInput, MemorySuggestOutput
from .mcp_models.memory_upload import MemoryUploadInput, MemoryUploadOutput
from .mcp_models.my_mentions import MyMentionsInput, MyMentionsOutput
from .mcp_models.pause_scheduled_action import PauseScheduledActionInput, PauseScheduledActionOutput
from .mcp_models.poll_channel import PollChannelInput, PollChannelOutput
from .mcp_models.post_message import PostMessageInput, PostMessageOutput
from .mcp_models.prepare_memory_write import PrepareMemoryWriteInput, PrepareMemoryWriteOutput
from .mcp_models.propose_scheduled_action import ProposeScheduledActionInput, ProposeScheduledActionOutput
from .mcp_models.provision_defaults import ProvisionDefaultsInput, ProvisionDefaultsOutput
from .mcp_models.query_fanout_workflow import QueryFanoutWorkflowInput, QueryFanoutWorkflowOutput
from .mcp_models.rank_tracker_workflow import RankTrackerWorkflowInput, RankTrackerWorkflowOutput
from .mcp_models.react_message import ReactMessageInput, ReactMessageOutput
from .mcp_models.read_service_connection import ReadServiceConnectionInput, ReadServiceConnectionOutput
from .mcp_models.record_fact import RecordFactInput, RecordFactOutput
from .mcp_models.reddit_thread import RedditThreadInput, RedditThreadOutput
from .mcp_models.remove_channel_member import RemoveChannelMemberInput, RemoveChannelMemberOutput
from .mcp_models.renew_connected_data_download import RenewConnectedDataDownloadInput, RenewConnectedDataDownloadOutput
from .mcp_models.reply_message import ReplyMessageInput, ReplyMessageOutput
from .mcp_models.report_artifact_read import ReportArtifactReadInput, ReportArtifactReadOutput
from .mcp_models.resolve_memory_tags import ResolveMemoryTagsInput, ResolveMemoryTagsOutput
from .mcp_models.resume_scheduled_action import ResumeScheduledActionInput, ResumeScheduledActionOutput
from .mcp_models.revoke_chat_link import RevokeChatLinkInput, RevokeChatLinkOutput
from .mcp_models.revoke_schedule_link import RevokeScheduleLinkInput, RevokeScheduleLinkOutput
from .mcp_models.revoke_webhook import RevokeWebhookInput, RevokeWebhookOutput
from .mcp_models.route_memory import RouteMemoryInput, RouteMemoryOutput
from .mcp_models.search_serp import SearchSerpInput, SearchSerpOutput
from .mcp_models.set_agent_identity import SetAgentIdentityInput, SetAgentIdentityOutput
from .mcp_models.set_schedule_entitlement import SetScheduleEntitlementInput, SetScheduleEntitlementOutput
from .mcp_models.set_scheduled_action_connections import SetScheduledActionConnectionsInput, SetScheduledActionConnectionsOutput
from .mcp_models.slack_send_message import SlackSendMessageInput, SlackSendMessageOutput
from .mcp_models.storage_usage import StorageUsageInput, StorageUsageOutput
from .mcp_models.table_create import TableCreateInput, TableCreateOutput
from .mcp_models.table_delete_rows import TableDeleteRowsInput, TableDeleteRowsOutput
from .mcp_models.table_describe import TableDescribeInput, TableDescribeOutput
from .mcp_models.table_drop import TableDropInput, TableDropOutput
from .mcp_models.table_insert_rows import TableInsertRowsInput, TableInsertRowsOutput
from .mcp_models.table_list import TableListInput, TableListOutput
from .mcp_models.table_query import TableQueryInput, TableQueryOutput
from .mcp_models.temporal_recall import TemporalRecallInput, TemporalRecallOutput
from .mcp_models.trustpilot_reviews import TrustpilotReviewsInput, TrustpilotReviewsOutput
from .mcp_models.upsert_memory_tag import UpsertMemoryTagInput, UpsertMemoryTagOutput
from .mcp_models.validate_memory_write import ValidateMemoryWriteInput, ValidateMemoryWriteOutput
from .mcp_models.video_analyze_start import VideoAnalyzeStartInput, VideoAnalyzeStartOutput
from .mcp_models.video_analyze_status import VideoAnalyzeStatusInput, VideoAnalyzeStatusOutput
from .mcp_models.video_frame_analysis import VideoFrameAnalysisInput, VideoFrameAnalysisOutput
from .mcp_models.video_frame_analysis_status import VideoFrameAnalysisStatusInput, VideoFrameAnalysisStatusOutput
from .mcp_models.workflow_artifact_read import WorkflowArtifactReadInput, WorkflowArtifactReadOutput
from .mcp_models.workflow_list import WorkflowListInput, WorkflowListOutput
from .mcp_models.workflow_run import WorkflowRunInput, WorkflowRunOutput
from .mcp_models.workflow_status import WorkflowStatusInput, WorkflowStatusOutput
from .mcp_models.workflow_step import WorkflowStepInput, WorkflowStepOutput
from .mcp_models.workflow_suggest import WorkflowSuggestInput, WorkflowSuggestOutput
from .mcp_models.youtube_harvest import YoutubeHarvestInput, YoutubeHarvestOutput
from .mcp_models.youtube_transcribe import YoutubeTranscribeInput, YoutubeTranscribeOutput
from .mcp_models.zoom_create_meeting import ZoomCreateMeetingInput, ZoomCreateMeetingOutput


MCP_TOOL_BINDINGS = [{'name': 'harvest_paa', 'category': 'search', 'method_name': 'harvest_paa'}, {'name': 'search_serp', 'category': 'search', 'method_name': 'search_serp'}, {'name': 'extract_url', 'category': 'web', 'method_name': 'extract_url'}, {'name': 'diff_page', 'category': 'web', 'method_name': 'diff_page'}, {'name': 'map_site_urls', 'category': 'web', 'method_name': 'map_site_urls'}, {'name': 'extract_site', 'category': 'web', 'method_name': 'extract_site'}, {'name': 'audit_site', 'category': 'web', 'method_name': 'audit_site'}, {'name': 'youtube_harvest', 'category': 'youtube', 'method_name': 'harvest'}, {'name': 'youtube_transcribe', 'category': 'youtube', 'method_name': 'transcribe'}, {'name': 'facebook_page_intel', 'category': 'facebook', 'method_name': 'page_intel'}, {'name': 'facebook_ad_search', 'category': 'facebook', 'method_name': 'ad_search'}, {'name': 'reddit_thread', 'category': 'reddit', 'method_name': 'thread'}, {'name': 'video_frame_analysis', 'category': 'video', 'method_name': 'frame_analysis'}, {'name': 'video_frame_analysis_status', 'category': 'video', 'method_name': 'frame_analysis_status'}, {'name': 'facebook_ad_transcribe', 'category': 'facebook', 'method_name': 'ad_transcribe'}, {'name': 'google_ads_search', 'category': 'googleAds', 'method_name': 'search'}, {'name': 'google_ads_page_intel', 'category': 'googleAds', 'method_name': 'page_intel'}, {'name': 'google_ads_transcribe', 'category': 'googleAds', 'method_name': 'transcribe'}, {'name': 'facebook_video_transcribe', 'category': 'facebook', 'method_name': 'video_transcribe'}, {'name': 'instagram_profile_content', 'category': 'instagram', 'method_name': 'profile_content'}, {'name': 'instagram_media_download', 'category': 'instagram', 'method_name': 'media_download'}, {'name': 'maps_place_intel', 'category': 'maps', 'method_name': 'place_intel'}, {'name': 'maps_search', 'category': 'maps', 'method_name': 'search'}, {'name': 'trustpilot_reviews', 'category': 'reviews', 'method_name': 'trustpilot_reviews'}, {'name': 'g2_reviews', 'category': 'reviews', 'method_name': 'g2_reviews'}, {'name': 'directory_workflow', 'category': 'directory', 'method_name': 'run'}, {'name': 'workflow_list', 'category': 'workflows', 'method_name': 'list'}, {'name': 'workflow_suggest', 'category': 'workflows', 'method_name': 'suggest'}, {'name': 'workflow_run', 'category': 'workflows', 'method_name': 'run'}, {'name': 'workflow_step', 'category': 'workflows', 'method_name': 'step'}, {'name': 'workflow_status', 'category': 'workflows', 'method_name': 'status'}, {'name': 'workflow_artifact_read', 'category': 'workflows', 'method_name': 'artifact_read'}, {'name': 'report_artifact_read', 'category': 'artifacts', 'method_name': 'read'}, {'name': 'rank_tracker_workflow', 'category': 'workflows', 'method_name': 'rank_tracker'}, {'name': 'credits_info', 'category': 'billing', 'method_name': 'credits_info'}, {'name': 'list_service_connections', 'category': 'connections', 'method_name': 'list_service_connections'}, {'name': 'slack_send_message', 'category': 'connections', 'method_name': 'slack_send_message'}, {'name': 'gmail_send_message', 'category': 'connections', 'method_name': 'gmail_send_message'}, {'name': 'google_calendar_create_event', 'category': 'connections', 'method_name': 'google_calendar_create_event'}, {'name': 'zoom_create_meeting', 'category': 'connections', 'method_name': 'zoom_create_meeting'}, {'name': 'read_service_connection', 'category': 'connections', 'method_name': 'read_service_connection'}, {'name': 'call_service_connection_action', 'category': 'connections', 'method_name': 'call_service_connection_action'}, {'name': 'set_scheduled_action_connections', 'category': 'connections', 'method_name': 'set_scheduled_action_connections'}, {'name': 'capture_serp_snapshot', 'category': 'serpIntelligence', 'method_name': 'snapshot'}, {'name': 'capture_serp_page_snapshots', 'category': 'serpIntelligence', 'method_name': 'page_snapshots'}, {'name': 'browser_profile_connect', 'category': 'browser', 'method_name': 'profile_connect'}, {'name': 'browser_profile_list', 'category': 'browser', 'method_name': 'profile_list'}, {'name': 'browser_extension_import', 'category': 'browser', 'method_name': 'extension_import'}, {'name': 'browser_extension_list', 'category': 'browser', 'method_name': 'extension_list'}, {'name': 'browser_extension_delete', 'category': 'browser', 'method_name': 'extension_delete'}, {'name': 'browser_open', 'category': 'browser', 'method_name': 'open'}, {'name': 'browser_screenshot', 'category': 'browser', 'method_name': 'screenshot'}, {'name': 'browser_read', 'category': 'browser', 'method_name': 'read'}, {'name': 'browser_locate', 'category': 'browser', 'method_name': 'locate'}, {'name': 'browser_goto', 'category': 'browser', 'method_name': 'goto'}, {'name': 'browser_click', 'category': 'browser', 'method_name': 'click'}, {'name': 'browser_type', 'category': 'browser', 'method_name': 'type'}, {'name': 'browser_scroll', 'category': 'browser', 'method_name': 'scroll'}, {'name': 'browser_press', 'category': 'browser', 'method_name': 'press'}, {'name': 'browser_replay_start', 'category': 'browser', 'method_name': 'replay_start'}, {'name': 'browser_replay_stop', 'category': 'browser', 'method_name': 'replay_stop'}, {'name': 'browser_list_replays', 'category': 'browser', 'method_name': 'list_replays'}, {'name': 'browser_replay_download', 'category': 'browser', 'method_name': 'replay_download'}, {'name': 'browser_replay_mark', 'category': 'browser', 'method_name': 'replay_mark'}, {'name': 'browser_replay_annotate', 'category': 'browser', 'method_name': 'replay_annotate'}, {'name': 'browser_close', 'category': 'browser', 'method_name': 'close'}, {'name': 'browser_list_sessions', 'category': 'browser', 'method_name': 'list_sessions'}, {'name': 'query_fanout_workflow', 'category': 'workflows', 'method_name': 'query_fanout'}, {'name': 'access-accept-share', 'category': 'access', 'method_name': 'accept_share'}, {'name': 'access-approve-sender', 'category': 'access', 'method_name': 'approve_sender'}, {'name': 'access-decline-share', 'category': 'access', 'method_name': 'decline_share'}, {'name': 'get-chat-link', 'category': 'access', 'method_name': 'get_chat_link'}, {'name': 'access-inbox-settings', 'category': 'access', 'method_name': 'inbox_settings'}, {'name': 'access-invite-account', 'category': 'access', 'method_name': 'invite_account'}, {'name': 'access-issue-key', 'category': 'access', 'method_name': 'issue_key'}, {'name': 'access-list-approved-senders', 'category': 'access', 'method_name': 'list_approved_senders'}, {'name': 'access-list-keys', 'category': 'access', 'method_name': 'list_keys'}, {'name': 'access-note-inbox', 'category': 'access', 'method_name': 'note_inbox'}, {'name': 'access-remove-approved-sender', 'category': 'access', 'method_name': 'remove_approved_sender'}, {'name': 'revoke-chat-link', 'category': 'access', 'method_name': 'revoke_chat_link'}, {'name': 'access-revoke-key', 'category': 'access', 'method_name': 'revoke_key'}, {'name': 'access-revoke-share', 'category': 'access', 'method_name': 'revoke_share'}, {'name': 'set-agent-identity', 'category': 'access', 'method_name': 'set_agent_identity'}, {'name': 'access-set-scope', 'category': 'access', 'method_name': 'set_scope'}, {'name': 'access-share-note', 'category': 'access', 'method_name': 'share_note'}, {'name': 'access-share-vault', 'category': 'access', 'method_name': 'share_vault'}, {'name': 'access-swap-vault', 'category': 'access', 'method_name': 'swap_vault'}, {'name': 'access-switch-account', 'category': 'access', 'method_name': 'switch_account'}, {'name': 'access-unlink-share', 'category': 'access', 'method_name': 'unlink_share'}, {'name': 'memory-capture', 'category': 'capture', 'method_name': 'memory_capture'}, {'name': 'memory-questions', 'category': 'capture', 'method_name': 'memory_questions'}, {'name': 'prepare-memory-write', 'category': 'capture', 'method_name': 'prepare_memory_write'}, {'name': 'validate-memory-write', 'category': 'capture', 'method_name': 'validate_memory_write'}, {'name': 'create-channel', 'category': 'channels', 'method_name': 'create_channel'}, {'name': 'get-message-note', 'category': 'channels', 'method_name': 'get_message_note'}, {'name': 'list-channel-members', 'category': 'channels', 'method_name': 'list_channel_members'}, {'name': 'list-channel-messages', 'category': 'channels', 'method_name': 'list_channel_messages'}, {'name': 'my-mentions', 'category': 'channels', 'method_name': 'my_mentions'}, {'name': 'poll-channel', 'category': 'channels', 'method_name': 'poll_channel'}, {'name': 'post-message', 'category': 'channels', 'method_name': 'post_message'}, {'name': 'react-message', 'category': 'channels', 'method_name': 'react_message'}, {'name': 'remove-channel-member', 'category': 'channels', 'method_name': 'remove_channel_member'}, {'name': 'reply-message', 'category': 'channels', 'method_name': 'reply_message'}, {'name': 'fact-history', 'category': 'facts', 'method_name': 'history'}, {'name': 'record-fact', 'category': 'facts', 'method_name': 'record_fact'}, {'name': 'memory-backlinks', 'category': 'graph', 'method_name': 'memory_backlinks'}, {'name': 'memory-graph-path', 'category': 'graph', 'method_name': 'memory_graph_path'}, {'name': 'memory-graph-universe', 'category': 'graph', 'method_name': 'memory_graph_universe'}, {'name': 'library-ingest', 'category': 'library', 'method_name': 'ingest'}, {'name': 'delete-note', 'category': 'memory', 'method_name': 'delete_note'}, {'name': 'memory-export', 'category': 'memory', 'method_name': 'export'}, {'name': 'memory-get', 'category': 'memory', 'method_name': 'get'}, {'name': 'memory-list', 'category': 'memory', 'method_name': 'list'}, {'name': 'memory-put', 'category': 'memory', 'method_name': 'put'}, {'name': 'memory-search', 'category': 'memory', 'method_name': 'search'}, {'name': 'memory-suggest', 'category': 'memory', 'method_name': 'suggest'}, {'name': 'memory-upload', 'category': 'memory', 'method_name': 'upload'}, {'name': 'temporal-recall', 'category': 'recall', 'method_name': 'temporal_recall'}, {'name': 'create-scheduled-action', 'category': 'schedule', 'method_name': 'create_scheduled_action'}, {'name': 'delete-scheduled-action', 'category': 'schedule', 'method_name': 'delete_scheduled_action'}, {'name': 'get-schedule-link', 'category': 'schedule', 'method_name': 'get_schedule_link'}, {'name': 'get-schedule-status', 'category': 'schedule', 'method_name': 'get_schedule_status'}, {'name': 'list-scheduled-actions', 'category': 'schedule', 'method_name': 'list_scheduled_actions'}, {'name': 'pause-scheduled-action', 'category': 'schedule', 'method_name': 'pause_scheduled_action'}, {'name': 'propose-scheduled-action', 'category': 'schedule', 'method_name': 'propose_scheduled_action'}, {'name': 'resume-scheduled-action', 'category': 'schedule', 'method_name': 'resume_scheduled_action'}, {'name': 'revoke-schedule-link', 'category': 'schedule', 'method_name': 'revoke_schedule_link'}, {'name': 'set-schedule-entitlement', 'category': 'schedule', 'method_name': 'set_schedule_entitlement'}, {'name': 'cost-usage', 'category': 'storage', 'method_name': 'cost_usage'}, {'name': 'storage-usage', 'category': 'storage', 'method_name': 'usage'}, {'name': 'table-create', 'category': 'tables', 'method_name': 'create'}, {'name': 'table-delete-rows', 'category': 'tables', 'method_name': 'delete_rows'}, {'name': 'table-describe', 'category': 'tables', 'method_name': 'describe'}, {'name': 'table-drop', 'category': 'tables', 'method_name': 'drop'}, {'name': 'table-insert-rows', 'category': 'tables', 'method_name': 'insert_rows'}, {'name': 'table-list', 'category': 'tables', 'method_name': 'list'}, {'name': 'table-query', 'category': 'tables', 'method_name': 'query'}, {'name': 'list-memory-tags', 'category': 'tags', 'method_name': 'list_memory_tags'}, {'name': 'resolve-memory-tags', 'category': 'tags', 'method_name': 'resolve_memory_tags'}, {'name': 'upsert-memory-tag', 'category': 'tags', 'method_name': 'upsert_memory_tag'}, {'name': 'add-vault', 'category': 'vaults', 'method_name': 'add_vault'}, {'name': 'create-secure-vault', 'category': 'vaults', 'method_name': 'create_secure_vault'}, {'name': 'delete-vault', 'category': 'vaults', 'method_name': 'delete_vault'}, {'name': 'get-vault-contract', 'category': 'vaults', 'method_name': 'get_vault_contract'}, {'name': 'list-shared-with-me', 'category': 'vaults', 'method_name': 'list_shared_with_me'}, {'name': 'list-vaults', 'category': 'vaults', 'method_name': 'list_vaults'}, {'name': 'provision-defaults', 'category': 'vaults', 'method_name': 'provision_defaults'}, {'name': 'route-memory', 'category': 'vaults', 'method_name': 'route_memory'}, {'name': 'video-analyze-start', 'category': 'video', 'method_name': 'analyze_start'}, {'name': 'video-analyze-status', 'category': 'video', 'method_name': 'analyze_status'}, {'name': 'create-webhook', 'category': 'webhooks', 'method_name': 'create_webhook'}, {'name': 'list-webhooks', 'category': 'webhooks', 'method_name': 'list_webhooks'}, {'name': 'revoke-webhook', 'category': 'webhooks', 'method_name': 'revoke_webhook'}, {'name': 'export_connected_service_data', 'category': 'connections', 'method_name': 'export_connected_service_data'}, {'name': 'renew_connected_data_download', 'category': 'connections', 'method_name': 'renew_connected_data_download'}]
MCP_TOOL_COUNT = len(MCP_TOOL_BINDINGS)


class SearchNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def harvest_paa(self, **kwargs: Any) -> Any:
        payload = HarvestPaaInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("harvest_paa", payload)

    def search_serp(self, **kwargs: Any) -> Any:
        payload = SearchSerpInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("search_serp", payload)


class WebNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def extract_url(self, **kwargs: Any) -> Any:
        payload = ExtractUrlInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("extract_url", payload)

    def diff_page(self, **kwargs: Any) -> Any:
        payload = DiffPageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("diff_page", payload)

    def map_site_urls(self, **kwargs: Any) -> Any:
        payload = MapSiteUrlsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("map_site_urls", payload)

    def extract_site(self, **kwargs: Any) -> Any:
        payload = ExtractSiteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("extract_site", payload)

    def audit_site(self, **kwargs: Any) -> Any:
        payload = AuditSiteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("audit_site", payload)


class YoutubeNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def harvest(self, **kwargs: Any) -> Any:
        payload = YoutubeHarvestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("youtube_harvest", payload)

    def transcribe(self, **kwargs: Any) -> Any:
        payload = YoutubeTranscribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("youtube_transcribe", payload)


class FacebookNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def page_intel(self, **kwargs: Any) -> Any:
        payload = FacebookPageIntelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("facebook_page_intel", payload)

    def ad_search(self, **kwargs: Any) -> Any:
        payload = FacebookAdSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("facebook_ad_search", payload)

    def ad_transcribe(self, **kwargs: Any) -> Any:
        payload = FacebookAdTranscribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("facebook_ad_transcribe", payload)

    def video_transcribe(self, **kwargs: Any) -> Any:
        payload = FacebookVideoTranscribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("facebook_video_transcribe", payload)


class RedditNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def thread(self, **kwargs: Any) -> Any:
        payload = RedditThreadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("reddit_thread", payload)


class VideoNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def frame_analysis(self, **kwargs: Any) -> Any:
        payload = VideoFrameAnalysisInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("video_frame_analysis", payload)

    def frame_analysis_status(self, **kwargs: Any) -> Any:
        payload = VideoFrameAnalysisStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("video_frame_analysis_status", payload)

    def analyze_start(self, **kwargs: Any) -> VideoAnalyzeStartOutput:
        payload = VideoAnalyzeStartInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("video-analyze-start", payload)
        return VideoAnalyzeStartOutput.model_validate(result)

    def analyze_status(self, **kwargs: Any) -> VideoAnalyzeStatusOutput:
        payload = VideoAnalyzeStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("video-analyze-status", payload)
        return VideoAnalyzeStatusOutput.model_validate(result)


class GoogleAdsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def search(self, **kwargs: Any) -> Any:
        payload = GoogleAdsSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("google_ads_search", payload)

    def page_intel(self, **kwargs: Any) -> Any:
        payload = GoogleAdsPageIntelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("google_ads_page_intel", payload)

    def transcribe(self, **kwargs: Any) -> Any:
        payload = GoogleAdsTranscribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("google_ads_transcribe", payload)


class InstagramNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def profile_content(self, **kwargs: Any) -> Any:
        payload = InstagramProfileContentInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("instagram_profile_content", payload)

    def media_download(self, **kwargs: Any) -> Any:
        payload = InstagramMediaDownloadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("instagram_media_download", payload)


class MapsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def place_intel(self, **kwargs: Any) -> Any:
        payload = MapsPlaceIntelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("maps_place_intel", payload)

    def search(self, **kwargs: Any) -> Any:
        payload = MapsSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("maps_search", payload)


class ReviewsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def trustpilot_reviews(self, **kwargs: Any) -> Any:
        payload = TrustpilotReviewsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("trustpilot_reviews", payload)

    def g2_reviews(self, **kwargs: Any) -> Any:
        payload = G2ReviewsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("g2_reviews", payload)


class DirectoryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def run(self, **kwargs: Any) -> Any:
        payload = DirectoryWorkflowInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("directory_workflow", payload)


class WorkflowsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def list(self, **kwargs: Any) -> Any:
        payload = WorkflowListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("workflow_list", payload)

    def suggest(self, **kwargs: Any) -> Any:
        payload = WorkflowSuggestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("workflow_suggest", payload)

    def run(self, **kwargs: Any) -> Any:
        payload = WorkflowRunInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("workflow_run", payload)

    def step(self, **kwargs: Any) -> Any:
        payload = WorkflowStepInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("workflow_step", payload)

    def status(self, **kwargs: Any) -> Any:
        payload = WorkflowStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("workflow_status", payload)

    def artifact_read(self, **kwargs: Any) -> Any:
        payload = WorkflowArtifactReadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("workflow_artifact_read", payload)

    def rank_tracker(self, **kwargs: Any) -> Any:
        payload = RankTrackerWorkflowInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("rank_tracker_workflow", payload)

    def query_fanout(self, **kwargs: Any) -> Any:
        payload = QueryFanoutWorkflowInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("query_fanout_workflow", payload)


class ArtifactsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def read(self, **kwargs: Any) -> Any:
        payload = ReportArtifactReadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("report_artifact_read", payload)


class BillingNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def credits_info(self, **kwargs: Any) -> Any:
        payload = CreditsInfoInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("credits_info", payload)


class ConnectionsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def list_service_connections(self, **kwargs: Any) -> Any:
        payload = ListServiceConnectionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("list_service_connections", payload)

    def slack_send_message(self, **kwargs: Any) -> Any:
        payload = SlackSendMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("slack_send_message", payload)

    def gmail_send_message(self, **kwargs: Any) -> Any:
        payload = GmailSendMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("gmail_send_message", payload)

    def google_calendar_create_event(self, **kwargs: Any) -> Any:
        payload = GoogleCalendarCreateEventInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("google_calendar_create_event", payload)

    def zoom_create_meeting(self, **kwargs: Any) -> Any:
        payload = ZoomCreateMeetingInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("zoom_create_meeting", payload)

    def read_service_connection(self, **kwargs: Any) -> Any:
        payload = ReadServiceConnectionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("read_service_connection", payload)

    def call_service_connection_action(self, **kwargs: Any) -> Any:
        payload = CallServiceConnectionActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("call_service_connection_action", payload)

    def set_scheduled_action_connections(self, **kwargs: Any) -> Any:
        payload = SetScheduledActionConnectionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("set_scheduled_action_connections", payload)

    def export_connected_service_data(self, **kwargs: Any) -> Any:
        payload = ExportConnectedServiceDataInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("export_connected_service_data", payload)

    def renew_connected_data_download(self, **kwargs: Any) -> Any:
        payload = RenewConnectedDataDownloadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("renew_connected_data_download", payload)


class SerpIntelligenceNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def snapshot(self, **kwargs: Any) -> Any:
        payload = CaptureSerpSnapshotInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("capture_serp_snapshot", payload)

    def page_snapshots(self, **kwargs: Any) -> Any:
        payload = CaptureSerpPageSnapshotsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("capture_serp_page_snapshots", payload)


class BrowserNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def profile_connect(self, **kwargs: Any) -> Any:
        payload = BrowserProfileConnectInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_profile_connect", payload)

    def profile_list(self, **kwargs: Any) -> Any:
        payload = BrowserProfileListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_profile_list", payload)

    def extension_import(self, **kwargs: Any) -> Any:
        payload = BrowserExtensionImportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_extension_import", payload)

    def extension_list(self, **kwargs: Any) -> Any:
        payload = BrowserExtensionListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_extension_list", payload)

    def extension_delete(self, **kwargs: Any) -> Any:
        payload = BrowserExtensionDeleteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_extension_delete", payload)

    def open(self, **kwargs: Any) -> Any:
        payload = BrowserOpenInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_open", payload)

    def screenshot(self, **kwargs: Any) -> Any:
        payload = BrowserScreenshotInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_screenshot", payload)

    def read(self, **kwargs: Any) -> Any:
        payload = BrowserReadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_read", payload)

    def locate(self, **kwargs: Any) -> Any:
        payload = BrowserLocateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_locate", payload)

    def goto(self, **kwargs: Any) -> Any:
        payload = BrowserGotoInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_goto", payload)

    def click(self, **kwargs: Any) -> Any:
        payload = BrowserClickInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_click", payload)

    def type(self, **kwargs: Any) -> Any:
        payload = BrowserTypeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_type", payload)

    def scroll(self, **kwargs: Any) -> Any:
        payload = BrowserScrollInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_scroll", payload)

    def press(self, **kwargs: Any) -> Any:
        payload = BrowserPressInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_press", payload)

    def replay_start(self, **kwargs: Any) -> Any:
        payload = BrowserReplayStartInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_replay_start", payload)

    def replay_stop(self, **kwargs: Any) -> Any:
        payload = BrowserReplayStopInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_replay_stop", payload)

    def list_replays(self, **kwargs: Any) -> Any:
        payload = BrowserListReplaysInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_list_replays", payload)

    def replay_download(self, **kwargs: Any) -> Any:
        payload = BrowserReplayDownloadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_replay_download", payload)

    def replay_mark(self, **kwargs: Any) -> Any:
        payload = BrowserReplayMarkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_replay_mark", payload)

    def replay_annotate(self, **kwargs: Any) -> Any:
        payload = BrowserReplayAnnotateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_replay_annotate", payload)

    def close(self, **kwargs: Any) -> Any:
        payload = BrowserCloseInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_close", payload)

    def list_sessions(self, **kwargs: Any) -> Any:
        payload = BrowserListSessionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        return self._call_tool("browser_list_sessions", payload)


class AccessNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def accept_share(self, **kwargs: Any) -> AccessAcceptShareOutput:
        payload = AccessAcceptShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-accept-share", payload)
        return AccessAcceptShareOutput.model_validate(result)

    def approve_sender(self, **kwargs: Any) -> AccessApproveSenderOutput:
        payload = AccessApproveSenderInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-approve-sender", payload)
        return AccessApproveSenderOutput.model_validate(result)

    def decline_share(self, **kwargs: Any) -> AccessDeclineShareOutput:
        payload = AccessDeclineShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-decline-share", payload)
        return AccessDeclineShareOutput.model_validate(result)

    def get_chat_link(self, **kwargs: Any) -> GetChatLinkOutput:
        payload = GetChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-chat-link", payload)
        return GetChatLinkOutput.model_validate(result)

    def inbox_settings(self, **kwargs: Any) -> AccessInboxSettingsOutput:
        payload = AccessInboxSettingsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-inbox-settings", payload)
        return AccessInboxSettingsOutput.model_validate(result)

    def invite_account(self, **kwargs: Any) -> AccessInviteAccountOutput:
        payload = AccessInviteAccountInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-invite-account", payload)
        return AccessInviteAccountOutput.model_validate(result)

    def issue_key(self, **kwargs: Any) -> AccessIssueKeyOutput:
        payload = AccessIssueKeyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-issue-key", payload)
        return AccessIssueKeyOutput.model_validate(result)

    def list_approved_senders(self, **kwargs: Any) -> AccessListApprovedSendersOutput:
        payload = AccessListApprovedSendersInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-list-approved-senders", payload)
        return AccessListApprovedSendersOutput.model_validate(result)

    def list_keys(self, **kwargs: Any) -> AccessListKeysOutput:
        payload = AccessListKeysInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-list-keys", payload)
        return AccessListKeysOutput.model_validate(result)

    def note_inbox(self, **kwargs: Any) -> AccessNoteInboxOutput:
        payload = AccessNoteInboxInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-note-inbox", payload)
        return AccessNoteInboxOutput.model_validate(result)

    def remove_approved_sender(self, **kwargs: Any) -> AccessRemoveApprovedSenderOutput:
        payload = AccessRemoveApprovedSenderInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-remove-approved-sender", payload)
        return AccessRemoveApprovedSenderOutput.model_validate(result)

    def revoke_chat_link(self, **kwargs: Any) -> RevokeChatLinkOutput:
        payload = RevokeChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revoke-chat-link", payload)
        return RevokeChatLinkOutput.model_validate(result)

    def revoke_key(self, **kwargs: Any) -> AccessRevokeKeyOutput:
        payload = AccessRevokeKeyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-revoke-key", payload)
        return AccessRevokeKeyOutput.model_validate(result)

    def revoke_share(self, **kwargs: Any) -> AccessRevokeShareOutput:
        payload = AccessRevokeShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-revoke-share", payload)
        return AccessRevokeShareOutput.model_validate(result)

    def set_agent_identity(self, **kwargs: Any) -> SetAgentIdentityOutput:
        payload = SetAgentIdentityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("set-agent-identity", payload)
        return SetAgentIdentityOutput.model_validate(result)

    def set_scope(self, **kwargs: Any) -> AccessSetScopeOutput:
        payload = AccessSetScopeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-set-scope", payload)
        return AccessSetScopeOutput.model_validate(result)

    def share_note(self, **kwargs: Any) -> AccessShareNoteOutput:
        payload = AccessShareNoteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-share-note", payload)
        return AccessShareNoteOutput.model_validate(result)

    def share_vault(self, **kwargs: Any) -> AccessShareVaultOutput:
        payload = AccessShareVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-share-vault", payload)
        return AccessShareVaultOutput.model_validate(result)

    def swap_vault(self, **kwargs: Any) -> AccessSwapVaultOutput:
        payload = AccessSwapVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-swap-vault", payload)
        return AccessSwapVaultOutput.model_validate(result)

    def switch_account(self, **kwargs: Any) -> AccessSwitchAccountOutput:
        payload = AccessSwitchAccountInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-switch-account", payload)
        return AccessSwitchAccountOutput.model_validate(result)

    def unlink_share(self, **kwargs: Any) -> AccessUnlinkShareOutput:
        payload = AccessUnlinkShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-unlink-share", payload)
        return AccessUnlinkShareOutput.model_validate(result)


class CaptureNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def memory_capture(self, **kwargs: Any) -> MemoryCaptureOutput:
        payload = MemoryCaptureInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-capture", payload)
        return MemoryCaptureOutput.model_validate(result)

    def memory_questions(self, **kwargs: Any) -> MemoryQuestionsOutput:
        payload = MemoryQuestionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-questions", payload)
        return MemoryQuestionsOutput.model_validate(result)

    def prepare_memory_write(self, **kwargs: Any) -> PrepareMemoryWriteOutput:
        payload = PrepareMemoryWriteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("prepare-memory-write", payload)
        return PrepareMemoryWriteOutput.model_validate(result)

    def validate_memory_write(self, **kwargs: Any) -> ValidateMemoryWriteOutput:
        payload = ValidateMemoryWriteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("validate-memory-write", payload)
        return ValidateMemoryWriteOutput.model_validate(result)


class ChannelsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create_channel(self, **kwargs: Any) -> CreateChannelOutput:
        payload = CreateChannelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("create-channel", payload)
        return CreateChannelOutput.model_validate(result)

    def get_message_note(self, **kwargs: Any) -> GetMessageNoteOutput:
        payload = GetMessageNoteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-message-note", payload)
        return GetMessageNoteOutput.model_validate(result)

    def list_channel_members(self, **kwargs: Any) -> ListChannelMembersOutput:
        payload = ListChannelMembersInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-channel-members", payload)
        return ListChannelMembersOutput.model_validate(result)

    def list_channel_messages(self, **kwargs: Any) -> ListChannelMessagesOutput:
        payload = ListChannelMessagesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-channel-messages", payload)
        return ListChannelMessagesOutput.model_validate(result)

    def my_mentions(self, **kwargs: Any) -> MyMentionsOutput:
        payload = MyMentionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("my-mentions", payload)
        return MyMentionsOutput.model_validate(result)

    def poll_channel(self, **kwargs: Any) -> PollChannelOutput:
        payload = PollChannelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("poll-channel", payload)
        return PollChannelOutput.model_validate(result)

    def post_message(self, **kwargs: Any) -> PostMessageOutput:
        payload = PostMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("post-message", payload)
        return PostMessageOutput.model_validate(result)

    def react_message(self, **kwargs: Any) -> ReactMessageOutput:
        payload = ReactMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("react-message", payload)
        return ReactMessageOutput.model_validate(result)

    def remove_channel_member(self, **kwargs: Any) -> RemoveChannelMemberOutput:
        payload = RemoveChannelMemberInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("remove-channel-member", payload)
        return RemoveChannelMemberOutput.model_validate(result)

    def reply_message(self, **kwargs: Any) -> ReplyMessageOutput:
        payload = ReplyMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("reply-message", payload)
        return ReplyMessageOutput.model_validate(result)


class FactsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def history(self, **kwargs: Any) -> FactHistoryOutput:
        payload = FactHistoryInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("fact-history", payload)
        return FactHistoryOutput.model_validate(result)

    def record_fact(self, **kwargs: Any) -> RecordFactOutput:
        payload = RecordFactInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("record-fact", payload)
        return RecordFactOutput.model_validate(result)


class GraphNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def memory_backlinks(self, **kwargs: Any) -> MemoryBacklinksOutput:
        payload = MemoryBacklinksInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-backlinks", payload)
        return MemoryBacklinksOutput.model_validate(result)

    def memory_graph_path(self, **kwargs: Any) -> MemoryGraphPathOutput:
        payload = MemoryGraphPathInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-graph-path", payload)
        return MemoryGraphPathOutput.model_validate(result)

    def memory_graph_universe(self, **kwargs: Any) -> MemoryGraphUniverseOutput:
        payload = MemoryGraphUniverseInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-graph-universe", payload)
        return MemoryGraphUniverseOutput.model_validate(result)


class LibraryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def ingest(self, **kwargs: Any) -> LibraryIngestOutput:
        payload = LibraryIngestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("library-ingest", payload)
        return LibraryIngestOutput.model_validate(result)


class MemoryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def delete_note(self, **kwargs: Any) -> DeleteNoteOutput:
        payload = DeleteNoteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("delete-note", payload)
        return DeleteNoteOutput.model_validate(result)

    def export(self, **kwargs: Any) -> MemoryExportOutput:
        payload = MemoryExportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-export", payload)
        return MemoryExportOutput.model_validate(result)

    def get(self, **kwargs: Any) -> MemoryGetOutput:
        payload = MemoryGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-get", payload)
        return MemoryGetOutput.model_validate(result)

    def list(self, **kwargs: Any) -> MemoryListOutput:
        payload = MemoryListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-list", payload)
        return MemoryListOutput.model_validate(result)

    def put(self, **kwargs: Any) -> MemoryPutOutput:
        payload = MemoryPutInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-put", payload)
        return MemoryPutOutput.model_validate(result)

    def search(self, **kwargs: Any) -> MemorySearchOutput:
        payload = MemorySearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-search", payload)
        return MemorySearchOutput.model_validate(result)

    def suggest(self, **kwargs: Any) -> MemorySuggestOutput:
        payload = MemorySuggestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-suggest", payload)
        return MemorySuggestOutput.model_validate(result)

    def upload(self, **kwargs: Any) -> MemoryUploadOutput:
        payload = MemoryUploadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memory-upload", payload)
        return MemoryUploadOutput.model_validate(result)


class RecallNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def temporal_recall(self, **kwargs: Any) -> TemporalRecallOutput:
        payload = TemporalRecallInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("temporal-recall", payload)
        return TemporalRecallOutput.model_validate(result)


class ScheduleNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create_scheduled_action(self, **kwargs: Any) -> CreateScheduledActionOutput:
        payload = CreateScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("create-scheduled-action", payload)
        return CreateScheduledActionOutput.model_validate(result)

    def delete_scheduled_action(self, **kwargs: Any) -> DeleteScheduledActionOutput:
        payload = DeleteScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("delete-scheduled-action", payload)
        return DeleteScheduledActionOutput.model_validate(result)

    def get_schedule_link(self, **kwargs: Any) -> GetScheduleLinkOutput:
        payload = GetScheduleLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-schedule-link", payload)
        return GetScheduleLinkOutput.model_validate(result)

    def get_schedule_status(self, **kwargs: Any) -> GetScheduleStatusOutput:
        payload = GetScheduleStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-schedule-status", payload)
        return GetScheduleStatusOutput.model_validate(result)

    def list_scheduled_actions(self, **kwargs: Any) -> ListScheduledActionsOutput:
        payload = ListScheduledActionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-scheduled-actions", payload)
        return ListScheduledActionsOutput.model_validate(result)

    def pause_scheduled_action(self, **kwargs: Any) -> PauseScheduledActionOutput:
        payload = PauseScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("pause-scheduled-action", payload)
        return PauseScheduledActionOutput.model_validate(result)

    def propose_scheduled_action(self, **kwargs: Any) -> ProposeScheduledActionOutput:
        payload = ProposeScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("propose-scheduled-action", payload)
        return ProposeScheduledActionOutput.model_validate(result)

    def resume_scheduled_action(self, **kwargs: Any) -> ResumeScheduledActionOutput:
        payload = ResumeScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("resume-scheduled-action", payload)
        return ResumeScheduledActionOutput.model_validate(result)

    def revoke_schedule_link(self, **kwargs: Any) -> RevokeScheduleLinkOutput:
        payload = RevokeScheduleLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revoke-schedule-link", payload)
        return RevokeScheduleLinkOutput.model_validate(result)

    def set_schedule_entitlement(self, **kwargs: Any) -> SetScheduleEntitlementOutput:
        payload = SetScheduleEntitlementInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("set-schedule-entitlement", payload)
        return SetScheduleEntitlementOutput.model_validate(result)


class StorageNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def cost_usage(self, **kwargs: Any) -> CostUsageOutput:
        payload = CostUsageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("cost-usage", payload)
        return CostUsageOutput.model_validate(result)

    def usage(self, **kwargs: Any) -> StorageUsageOutput:
        payload = StorageUsageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("storage-usage", payload)
        return StorageUsageOutput.model_validate(result)


class TablesNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create(self, **kwargs: Any) -> TableCreateOutput:
        payload = TableCreateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("table-create", payload)
        return TableCreateOutput.model_validate(result)

    def delete_rows(self, **kwargs: Any) -> TableDeleteRowsOutput:
        payload = TableDeleteRowsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("table-delete-rows", payload)
        return TableDeleteRowsOutput.model_validate(result)

    def describe(self, **kwargs: Any) -> TableDescribeOutput:
        payload = TableDescribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("table-describe", payload)
        return TableDescribeOutput.model_validate(result)

    def drop(self, **kwargs: Any) -> TableDropOutput:
        payload = TableDropInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("table-drop", payload)
        return TableDropOutput.model_validate(result)

    def insert_rows(self, **kwargs: Any) -> TableInsertRowsOutput:
        payload = TableInsertRowsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("table-insert-rows", payload)
        return TableInsertRowsOutput.model_validate(result)

    def list(self, **kwargs: Any) -> TableListOutput:
        payload = TableListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("table-list", payload)
        return TableListOutput.model_validate(result)

    def query(self, **kwargs: Any) -> TableQueryOutput:
        payload = TableQueryInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("table-query", payload)
        return TableQueryOutput.model_validate(result)


class TagsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def list_memory_tags(self, **kwargs: Any) -> ListMemoryTagsOutput:
        payload = ListMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-memory-tags", payload)
        return ListMemoryTagsOutput.model_validate(result)

    def resolve_memory_tags(self, **kwargs: Any) -> ResolveMemoryTagsOutput:
        payload = ResolveMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("resolve-memory-tags", payload)
        return ResolveMemoryTagsOutput.model_validate(result)

    def upsert_memory_tag(self, **kwargs: Any) -> UpsertMemoryTagOutput:
        payload = UpsertMemoryTagInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("upsert-memory-tag", payload)
        return UpsertMemoryTagOutput.model_validate(result)


class VaultsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def add_vault(self, **kwargs: Any) -> AddVaultOutput:
        payload = AddVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("add-vault", payload)
        return AddVaultOutput.model_validate(result)

    def create_secure_vault(self, **kwargs: Any) -> CreateSecureVaultOutput:
        payload = CreateSecureVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("create-secure-vault", payload)
        return CreateSecureVaultOutput.model_validate(result)

    def delete_vault(self, **kwargs: Any) -> DeleteVaultOutput:
        payload = DeleteVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("delete-vault", payload)
        return DeleteVaultOutput.model_validate(result)

    def get_vault_contract(self, **kwargs: Any) -> GetVaultContractOutput:
        payload = GetVaultContractInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-vault-contract", payload)
        return GetVaultContractOutput.model_validate(result)

    def list_shared_with_me(self, **kwargs: Any) -> ListSharedWithMeOutput:
        payload = ListSharedWithMeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-shared-with-me", payload)
        return ListSharedWithMeOutput.model_validate(result)

    def list_vaults(self, **kwargs: Any) -> ListVaultsOutput:
        payload = ListVaultsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-vaults", payload)
        return ListVaultsOutput.model_validate(result)

    def provision_defaults(self, **kwargs: Any) -> ProvisionDefaultsOutput:
        payload = ProvisionDefaultsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("provision-defaults", payload)
        return ProvisionDefaultsOutput.model_validate(result)

    def route_memory(self, **kwargs: Any) -> RouteMemoryOutput:
        payload = RouteMemoryInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("route-memory", payload)
        return RouteMemoryOutput.model_validate(result)


class WebhooksNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create_webhook(self, **kwargs: Any) -> CreateWebhookOutput:
        payload = CreateWebhookInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("create-webhook", payload)
        return CreateWebhookOutput.model_validate(result)

    def list_webhooks(self, **kwargs: Any) -> ListWebhooksOutput:
        payload = ListWebhooksInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-webhooks", payload)
        return ListWebhooksOutput.model_validate(result)

    def revoke_webhook(self, **kwargs: Any) -> RevokeWebhookOutput:
        payload = RevokeWebhookInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revoke-webhook", payload)
        return RevokeWebhookOutput.model_validate(result)



class GeneratedMcpToolsClient:
    def __init__(self, call_tool):
        self.search = SearchNamespace(call_tool)
        self.web = WebNamespace(call_tool)
        self.youtube = YoutubeNamespace(call_tool)
        self.facebook = FacebookNamespace(call_tool)
        self.reddit = RedditNamespace(call_tool)
        self.video = VideoNamespace(call_tool)
        self.google_ads = GoogleAdsNamespace(call_tool)
        self.instagram = InstagramNamespace(call_tool)
        self.maps = MapsNamespace(call_tool)
        self.reviews = ReviewsNamespace(call_tool)
        self.directory = DirectoryNamespace(call_tool)
        self.workflows = WorkflowsNamespace(call_tool)
        self.artifacts = ArtifactsNamespace(call_tool)
        self.billing = BillingNamespace(call_tool)
        self.connections = ConnectionsNamespace(call_tool)
        self.serp_intelligence = SerpIntelligenceNamespace(call_tool)
        self.browser = BrowserNamespace(call_tool)
        self.access = AccessNamespace(call_tool)
        self.capture = CaptureNamespace(call_tool)
        self.channels = ChannelsNamespace(call_tool)
        self.facts = FactsNamespace(call_tool)
        self.graph = GraphNamespace(call_tool)
        self.library = LibraryNamespace(call_tool)
        self.memory = MemoryNamespace(call_tool)
        self.recall = RecallNamespace(call_tool)
        self.schedule = ScheduleNamespace(call_tool)
        self.storage = StorageNamespace(call_tool)
        self.tables = TablesNamespace(call_tool)
        self.tags = TagsNamespace(call_tool)
        self.vaults = VaultsNamespace(call_tool)
        self.webhooks = WebhooksNamespace(call_tool)
