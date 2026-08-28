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
from .mcp_models.analytics_apply_crm_pipeline_mapping import AnalyticsApplyCrmPipelineMappingInput, AnalyticsApplyCrmPipelineMappingOutput
from .mcp_models.analytics_approve_crm_provisioning import AnalyticsApproveCrmProvisioningInput, AnalyticsApproveCrmProvisioningOutput
from .mcp_models.analytics_archive_event_definition import AnalyticsArchiveEventDefinitionInput, AnalyticsArchiveEventDefinitionOutput
from .mcp_models.analytics_cancel_crm_sync import AnalyticsCancelCrmSyncInput, AnalyticsCancelCrmSyncOutput
from .mcp_models.analytics_commit_crm_import import AnalyticsCommitCrmImportInput, AnalyticsCommitCrmImportOutput
from .mcp_models.analytics_create_activation_destination import AnalyticsCreateActivationDestinationInput, AnalyticsCreateActivationDestinationOutput
from .mcp_models.analytics_create_campaign_link import AnalyticsCreateCampaignLinkInput, AnalyticsCreateCampaignLinkOutput
from .mcp_models.analytics_create_connection import AnalyticsCreateConnectionInput, AnalyticsCreateConnectionOutput
from .mcp_models.analytics_create_conversion_rule import AnalyticsCreateConversionRuleInput, AnalyticsCreateConversionRuleOutput
from .mcp_models.analytics_create_event_definition import AnalyticsCreateEventDefinitionInput, AnalyticsCreateEventDefinitionOutput
from .mcp_models.analytics_create_export import AnalyticsCreateExportInput, AnalyticsCreateExportOutput
from .mcp_models.analytics_create_form import AnalyticsCreateFormInput, AnalyticsCreateFormOutput
from .mcp_models.analytics_create_funnel import AnalyticsCreateFunnelInput, AnalyticsCreateFunnelOutput
from .mcp_models.analytics_create_lead_score import AnalyticsCreateLeadScoreInput, AnalyticsCreateLeadScoreOutput
from .mcp_models.analytics_create_prediction_target import AnalyticsCreatePredictionTargetInput, AnalyticsCreatePredictionTargetOutput
from .mcp_models.analytics_create_saved_view import AnalyticsCreateSavedViewInput, AnalyticsCreateSavedViewOutput
from .mcp_models.analytics_delete_privacy_subject import AnalyticsDeletePrivacySubjectInput, AnalyticsDeletePrivacySubjectOutput
from .mcp_models.analytics_delete_saved_view import AnalyticsDeleteSavedViewInput, AnalyticsDeleteSavedViewOutput
from .mcp_models.analytics_discover_activation_assets import AnalyticsDiscoverActivationAssetsInput, AnalyticsDiscoverActivationAssetsOutput
from .mcp_models.analytics_discover_crm_capabilities import AnalyticsDiscoverCrmCapabilitiesInput, AnalyticsDiscoverCrmCapabilitiesOutput
from .mcp_models.analytics_discover_crm_sync_objects import AnalyticsDiscoverCrmSyncObjectsInput, AnalyticsDiscoverCrmSyncObjectsOutput
from .mcp_models.analytics_export_crm_csv import AnalyticsExportCrmCsvInput, AnalyticsExportCrmCsvOutput
from .mcp_models.analytics_export_google_ads_csv import AnalyticsExportGoogleAdsCsvInput, AnalyticsExportGoogleAdsCsvOutput
from .mcp_models.analytics_export_meta_technical import AnalyticsExportMetaTechnicalInput, AnalyticsExportMetaTechnicalOutput
from .mcp_models.analytics_export_privacy_subject import AnalyticsExportPrivacySubjectInput, AnalyticsExportPrivacySubjectOutput
from .mcp_models.analytics_get_acquisition import AnalyticsGetAcquisitionInput, AnalyticsGetAcquisitionOutput
from .mcp_models.analytics_get_business_metrics import AnalyticsGetBusinessMetricsInput, AnalyticsGetBusinessMetricsOutput
from .mcp_models.analytics_get_candidate_coverage import AnalyticsGetCandidateCoverageInput, AnalyticsGetCandidateCoverageOutput
from .mcp_models.analytics_get_channel_breakdown import AnalyticsGetChannelBreakdownInput, AnalyticsGetChannelBreakdownOutput
from .mcp_models.analytics_get_consent_coverage import AnalyticsGetConsentCoverageInput, AnalyticsGetConsentCoverageOutput
from .mcp_models.analytics_get_content import AnalyticsGetContentInput, AnalyticsGetContentOutput
from .mcp_models.analytics_get_conversions import AnalyticsGetConversionsInput, AnalyticsGetConversionsOutput
from .mcp_models.analytics_get_coverage import AnalyticsGetCoverageInput, AnalyticsGetCoverageOutput
from .mcp_models.analytics_get_crm_sync_status import AnalyticsGetCrmSyncStatusInput, AnalyticsGetCrmSyncStatusOutput
from .mcp_models.analytics_get_dimensions import AnalyticsGetDimensionsInput, AnalyticsGetDimensionsOutput
from .mcp_models.analytics_get_entitlement import AnalyticsGetEntitlementInput, AnalyticsGetEntitlementOutput
from .mcp_models.analytics_get_events import AnalyticsGetEventsInput, AnalyticsGetEventsOutput
from .mcp_models.analytics_get_forecast import AnalyticsGetForecastInput, AnalyticsGetForecastOutput
from .mcp_models.analytics_get_funnel import AnalyticsGetFunnelInput, AnalyticsGetFunnelOutput
from .mcp_models.analytics_get_health import AnalyticsGetHealthInput, AnalyticsGetHealthOutput
from .mcp_models.analytics_get_onboarding_state import AnalyticsGetOnboardingStateInput, AnalyticsGetOnboardingStateOutput
from .mcp_models.analytics_get_overview import AnalyticsGetOverviewInput, AnalyticsGetOverviewOutput
from .mcp_models.analytics_get_paths import AnalyticsGetPathsInput, AnalyticsGetPathsOutput
from .mcp_models.analytics_get_person_journey import AnalyticsGetPersonJourneyInput, AnalyticsGetPersonJourneyOutput
from .mcp_models.analytics_get_prediction_eligibility import AnalyticsGetPredictionEligibilityInput, AnalyticsGetPredictionEligibilityOutput
from .mcp_models.analytics_get_session_timeline import AnalyticsGetSessionTimelineInput, AnalyticsGetSessionTimelineOutput
from .mcp_models.analytics_get_timeseries import AnalyticsGetTimeseriesInput, AnalyticsGetTimeseriesOutput
from .mcp_models.analytics_get_visitor_journey import AnalyticsGetVisitorJourneyInput, AnalyticsGetVisitorJourneyOutput
from .mcp_models.analytics_import_crm_csv import AnalyticsImportCrmCsvInput, AnalyticsImportCrmCsvOutput
from .mcp_models.analytics_list_activation_destinations import AnalyticsListActivationDestinationsInput, AnalyticsListActivationDestinationsOutput
from .mcp_models.analytics_list_activation_receipts import AnalyticsListActivationReceiptsInput, AnalyticsListActivationReceiptsOutput
from .mcp_models.analytics_list_campaign_links import AnalyticsListCampaignLinksInput, AnalyticsListCampaignLinksOutput
from .mcp_models.analytics_list_connections import AnalyticsListConnectionsInput, AnalyticsListConnectionsOutput
from .mcp_models.analytics_list_conversion_rules import AnalyticsListConversionRulesInput, AnalyticsListConversionRulesOutput
from .mcp_models.analytics_list_crm_capabilities import AnalyticsListCrmCapabilitiesInput, AnalyticsListCrmCapabilitiesOutput
from .mcp_models.analytics_list_crm_imports import AnalyticsListCrmImportsInput, AnalyticsListCrmImportsOutput
from .mcp_models.analytics_list_crm_outbound_policies import AnalyticsListCrmOutboundPoliciesInput, AnalyticsListCrmOutboundPoliciesOutput
from .mcp_models.analytics_list_crm_outbound_receipts import AnalyticsListCrmOutboundReceiptsInput, AnalyticsListCrmOutboundReceiptsOutput
from .mcp_models.analytics_list_event_definitions import AnalyticsListEventDefinitionsInput, AnalyticsListEventDefinitionsOutput
from .mcp_models.analytics_list_forms import AnalyticsListFormsInput, AnalyticsListFormsOutput
from .mcp_models.analytics_list_funnels import AnalyticsListFunnelsInput, AnalyticsListFunnelsOutput
from .mcp_models.analytics_list_inference_review import AnalyticsListInferenceReviewInput, AnalyticsListInferenceReviewOutput
from .mcp_models.analytics_list_journeys import AnalyticsListJourneysInput, AnalyticsListJourneysOutput
from .mcp_models.analytics_list_lead_scores import AnalyticsListLeadScoresInput, AnalyticsListLeadScoresOutput
from .mcp_models.analytics_list_namespace_sources import AnalyticsListNamespaceSourcesInput, AnalyticsListNamespaceSourcesOutput
from .mcp_models.analytics_list_pixels import AnalyticsListPixelsInput, AnalyticsListPixelsOutput
from .mcp_models.analytics_list_prediction_targets import AnalyticsListPredictionTargetsInput, AnalyticsListPredictionTargetsOutput
from .mcp_models.analytics_list_saved_views import AnalyticsListSavedViewsInput, AnalyticsListSavedViewsOutput
from .mcp_models.analytics_list_sessions import AnalyticsListSessionsInput, AnalyticsListSessionsOutput
from .mcp_models.analytics_list_sites import AnalyticsListSitesInput, AnalyticsListSitesOutput
from .mcp_models.analytics_list_visitors import AnalyticsListVisitorsInput, AnalyticsListVisitorsOutput
from .mcp_models.analytics_plan_crm_provisioning import AnalyticsPlanCrmProvisioningInput, AnalyticsPlanCrmProvisioningOutput
from .mcp_models.analytics_preview_crm_import import AnalyticsPreviewCrmImportInput, AnalyticsPreviewCrmImportOutput
from .mcp_models.analytics_reconcile_connection import AnalyticsReconcileConnectionInput, AnalyticsReconcileConnectionOutput
from .mcp_models.analytics_record_external_event import AnalyticsRecordExternalEventInput, AnalyticsRecordExternalEventOutput
from .mcp_models.analytics_retry_activation_delivery import AnalyticsRetryActivationDeliveryInput, AnalyticsRetryActivationDeliveryOutput
from .mcp_models.analytics_save_activation_mapping import AnalyticsSaveActivationMappingInput, AnalyticsSaveActivationMappingOutput
from .mcp_models.analytics_set_activation_automation import AnalyticsSetActivationAutomationInput, AnalyticsSetActivationAutomationOutput
from .mcp_models.analytics_start_crm_sync import AnalyticsStartCrmSyncInput, AnalyticsStartCrmSyncOutput
from .mcp_models.analytics_sync_crm_person import AnalyticsSyncCrmPersonInput, AnalyticsSyncCrmPersonOutput
from .mcp_models.analytics_test_activation_destination import AnalyticsTestActivationDestinationInput, AnalyticsTestActivationDestinationOutput
from .mcp_models.analytics_test_crm_provisioning import AnalyticsTestCrmProvisioningInput, AnalyticsTestCrmProvisioningOutput
from .mcp_models.analytics_test_crm_sync_mapping import AnalyticsTestCrmSyncMappingInput, AnalyticsTestCrmSyncMappingOutput
from .mcp_models.analytics_test_event_definition import AnalyticsTestEventDefinitionInput, AnalyticsTestEventDefinitionOutput
from .mcp_models.analytics_test_funnel import AnalyticsTestFunnelInput, AnalyticsTestFunnelOutput
from .mcp_models.analytics_update_crm_sync_schedule import AnalyticsUpdateCrmSyncScheduleInput, AnalyticsUpdateCrmSyncScheduleOutput
from .mcp_models.analytics_update_event_definition import AnalyticsUpdateEventDefinitionInput, AnalyticsUpdateEventDefinitionOutput
from .mcp_models.analytics_update_onboarding_preferences import AnalyticsUpdateOnboardingPreferencesInput, AnalyticsUpdateOnboardingPreferencesOutput
from .mcp_models.analytics_upsert_crm_outbound_policy import AnalyticsUpsertCrmOutboundPolicyInput, AnalyticsUpsertCrmOutboundPolicyOutput
from .mcp_models.analytics_validate_activation_mapping import AnalyticsValidateActivationMappingInput, AnalyticsValidateActivationMappingOutput
from .mcp_models.analytics_verify_live_event_definition import AnalyticsVerifyLiveEventDefinitionInput, AnalyticsVerifyLiveEventDefinitionOutput
from .mcp_models.analytics_withdraw_consent import AnalyticsWithdrawConsentInput, AnalyticsWithdrawConsentOutput
from .mcp_models.analyze_site_similarity import AnalyzeSiteSimilarityInput, AnalyzeSiteSimilarityOutput
from .mcp_models.archive_artifact_template import ArchiveArtifactTemplateInput, ArchiveArtifactTemplateOutput
from .mcp_models.archive_read import ArchiveReadInput, ArchiveReadOutput
from .mcp_models.archive_scheduled_run import ArchiveScheduledRunInput, ArchiveScheduledRunOutput
from .mcp_models.assistant_approval_decide import AssistantApprovalDecideInput, AssistantApprovalDecideOutput
from .mcp_models.assistant_approvals_list import AssistantApprovalsListInput, AssistantApprovalsListOutput
from .mcp_models.assistant_bulk_send import AssistantBulkSendInput, AssistantBulkSendOutput
from .mcp_models.assistant_command import AssistantCommandInput, AssistantCommandOutput
from .mcp_models.assistant_conversation_get import AssistantConversationGetInput, AssistantConversationGetOutput
from .mcp_models.assistant_execution_status import AssistantExecutionStatusInput, AssistantExecutionStatusOutput
from .mcp_models.assistant_grant_create import AssistantGrantCreateInput, AssistantGrantCreateOutput
from .mcp_models.assistant_grant_revoke import AssistantGrantRevokeInput, AssistantGrantRevokeOutput
from .mcp_models.assistant_grants_list import AssistantGrantsListInput, AssistantGrantsListOutput
from .mcp_models.assistant_message_send import AssistantMessageSendInput, AssistantMessageSendOutput
from .mcp_models.assistant_number_purchase import AssistantNumberPurchaseInput, AssistantNumberPurchaseOutput
from .mcp_models.assistant_number_release import AssistantNumberReleaseInput, AssistantNumberReleaseOutput
from .mcp_models.assistant_number_search import AssistantNumberSearchInput, AssistantNumberSearchOutput
from .mcp_models.assistant_number_status import AssistantNumberStatusInput, AssistantNumberStatusOutput
from .mcp_models.assistant_status import AssistantStatusInput, AssistantStatusOutput
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
from .mcp_models.bulk_delete_notes import BulkDeleteNotesInput, BulkDeleteNotesOutput
from .mcp_models.call_service_connection_action import CallServiceConnectionActionInput, CallServiceConnectionActionOutput
from .mcp_models.capture_serp_page_snapshots import CaptureSerpPageSnapshotsInput, CaptureSerpPageSnapshotsOutput
from .mcp_models.capture_serp_snapshot import CaptureSerpSnapshotInput, CaptureSerpSnapshotOutput
from .mcp_models.check_site_export import CheckSiteExportInput, CheckSiteExportOutput
from .mcp_models.commons_claim_publication import CommonsClaimPublicationInput, CommonsClaimPublicationOutput
from .mcp_models.commons_get_entity import CommonsGetEntityInput, CommonsGetEntityOutput
from .mcp_models.commons_get_entity_ledger import CommonsGetEntityLedgerInput, CommonsGetEntityLedgerOutput
from .mcp_models.commons_get_entity_linkset import CommonsGetEntityLinksetInput, CommonsGetEntityLinksetOutput
from .mcp_models.commons_get_proposal import CommonsGetProposalInput, CommonsGetProposalOutput
from .mcp_models.commons_get_publication import CommonsGetPublicationInput, CommonsGetPublicationOutput
from .mcp_models.commons_host_image import CommonsHostImageInput, CommonsHostImageOutput
from .mcp_models.commons_list_filters import CommonsListFiltersInput, CommonsListFiltersOutput
from .mcp_models.commons_list_needs_links import CommonsListNeedsLinksInput, CommonsListNeedsLinksOutput
from .mcp_models.commons_prepare_entity import CommonsPrepareEntityInput, CommonsPrepareEntityOutput
from .mcp_models.commons_prepare_publication import CommonsPreparePublicationInput, CommonsPreparePublicationOutput
from .mcp_models.commons_publish_editorial import CommonsPublishEditorialInput, CommonsPublishEditorialOutput
from .mcp_models.commons_save_filter import CommonsSaveFilterInput, CommonsSaveFilterOutput
from .mcp_models.commons_search_entities import CommonsSearchEntitiesInput, CommonsSearchEntitiesOutput
from .mcp_models.commons_submit_entity import CommonsSubmitEntityInput, CommonsSubmitEntityOutput
from .mcp_models.commons_update_editorial_article import CommonsUpdateEditorialArticleInput, CommonsUpdateEditorialArticleOutput
from .mcp_models.commons_validate_entity import CommonsValidateEntityInput, CommonsValidateEntityOutput
from .mcp_models.commons_validate_publication import CommonsValidatePublicationInput, CommonsValidatePublicationOutput
from .mcp_models.cost_usage import CostUsageInput, CostUsageOutput
from .mcp_models.create_artifact_template import CreateArtifactTemplateInput, CreateArtifactTemplateOutput
from .mcp_models.create_channel import CreateChannelInput, CreateChannelOutput
from .mcp_models.create_editorial_reading_room import CreateEditorialReadingRoomInput, CreateEditorialReadingRoomOutput
from .mcp_models.create_scheduled_action import CreateScheduledActionInput, CreateScheduledActionOutput
from .mcp_models.create_scheduled_run_view_link import CreateScheduledRunViewLinkInput, CreateScheduledRunViewLinkOutput
from .mcp_models.create_secure_vault import CreateSecureVaultInput, CreateSecureVaultOutput
from .mcp_models.create_webhook import CreateWebhookInput, CreateWebhookOutput
from .mcp_models.credits_info import CreditsInfoInput, CreditsInfoOutput
from .mcp_models.delete_note import DeleteNoteInput, DeleteNoteOutput
from .mcp_models.delete_scheduled_action import DeleteScheduledActionInput, DeleteScheduledActionOutput
from .mcp_models.delete_vault import DeleteVaultInput, DeleteVaultOutput
from .mcp_models.describe_service_connection_tool import DescribeServiceConnectionToolInput, DescribeServiceConnectionToolOutput
from .mcp_models.diff_page import DiffPageInput, DiffPageOutput
from .mcp_models.directory_workflow import DirectoryWorkflowInput, DirectoryWorkflowOutput
from .mcp_models.directory_workflow_status import DirectoryWorkflowStatusInput, DirectoryWorkflowStatusOutput
from .mcp_models.editorial_reading_room_guide import EditorialReadingRoomGuideInput, EditorialReadingRoomGuideOutput
from .mcp_models.export_connected_service_data import ExportConnectedServiceDataInput, ExportConnectedServiceDataOutput
from .mcp_models.export_search_console_table_data import ExportSearchConsoleTableDataInput, ExportSearchConsoleTableDataOutput
from .mcp_models.extract_site import ExtractSiteInput, ExtractSiteOutput
from .mcp_models.extract_url import ExtractUrlInput, ExtractUrlOutput
from .mcp_models.facebook_ad_search import FacebookAdSearchInput, FacebookAdSearchOutput
from .mcp_models.facebook_ad_transcribe import FacebookAdTranscribeInput, FacebookAdTranscribeOutput
from .mcp_models.facebook_page_intel import FacebookPageIntelInput, FacebookPageIntelOutput
from .mcp_models.facebook_video_transcribe import FacebookVideoTranscribeInput, FacebookVideoTranscribeOutput
from .mcp_models.fact_history import FactHistoryInput, FactHistoryOutput
from .mcp_models.g2_reviews import G2ReviewsInput, G2ReviewsOutput
from .mcp_models.get_artifact_template import GetArtifactTemplateInput, GetArtifactTemplateOutput
from .mcp_models.get_artifact_template_example import GetArtifactTemplateExampleInput, GetArtifactTemplateExampleOutput
from .mcp_models.get_chat_link import GetChatLinkInput, GetChatLinkOutput
from .mcp_models.get_local_sourcebook_contract import GetLocalSourcebookContractInput, GetLocalSourcebookContractOutput
from .mcp_models.get_message_note import GetMessageNoteInput, GetMessageNoteOutput
from .mcp_models.get_schedule_link import GetScheduleLinkInput, GetScheduleLinkOutput
from .mcp_models.get_schedule_status import GetScheduleStatusInput, GetScheduleStatusOutput
from .mcp_models.get_scheduled_run import GetScheduledRunInput, GetScheduledRunOutput
from .mcp_models.get_vault_app_link import GetVaultAppLinkInput, GetVaultAppLinkOutput
from .mcp_models.get_vault_contract import GetVaultContractInput, GetVaultContractOutput
from .mcp_models.gmail_bulk_delete_messages import GmailBulkDeleteMessagesInput, GmailBulkDeleteMessagesOutput
from .mcp_models.gmail_bulk_manage_messages import GmailBulkManageMessagesInput, GmailBulkManageMessagesOutput
from .mcp_models.gmail_export_selection import GmailExportSelectionInput, GmailExportSelectionOutput
from .mcp_models.gmail_get_attachment import GmailGetAttachmentInput, GmailGetAttachmentOutput
from .mcp_models.gmail_get_message import GmailGetMessageInput, GmailGetMessageOutput
from .mcp_models.gmail_import_status import GmailImportStatusInput, GmailImportStatusOutput
from .mcp_models.gmail_import_to_memory import GmailImportToMemoryInput, GmailImportToMemoryOutput
from .mcp_models.gmail_prepare_memory_import import GmailPrepareMemoryImportInput, GmailPrepareMemoryImportOutput
from .mcp_models.gmail_prepare_selection import GmailPrepareSelectionInput, GmailPrepareSelectionOutput
from .mcp_models.gmail_search_contacts import GmailSearchContactsInput, GmailSearchContactsOutput
from .mcp_models.gmail_search_messages import GmailSearchMessagesInput, GmailSearchMessagesOutput
from .mcp_models.gmail_send_message import GmailSendMessageInput, GmailSendMessageOutput
from .mcp_models.google_ads_page_intel import GoogleAdsPageIntelInput, GoogleAdsPageIntelOutput
from .mcp_models.google_ads_search import GoogleAdsSearchInput, GoogleAdsSearchOutput
from .mcp_models.google_ads_transcribe import GoogleAdsTranscribeInput, GoogleAdsTranscribeOutput
from .mcp_models.google_calendar_create_event import GoogleCalendarCreateEventInput, GoogleCalendarCreateEventOutput
from .mcp_models.harvest_paa import HarvestPaaInput, HarvestPaaOutput
from .mcp_models.harvest_paa_start import HarvestPaaStartInput, HarvestPaaStartOutput
from .mcp_models.harvest_paa_status import HarvestPaaStatusInput, HarvestPaaStatusOutput
from .mcp_models.image_asset_delete import ImageAssetDeleteInput, ImageAssetDeleteOutput
from .mcp_models.image_asset_get import ImageAssetGetInput, ImageAssetGetOutput
from .mcp_models.image_asset_list import ImageAssetListInput, ImageAssetListOutput
from .mcp_models.image_asset_move import ImageAssetMoveInput, ImageAssetMoveOutput
from .mcp_models.image_asset_save import ImageAssetSaveInput, ImageAssetSaveOutput
from .mcp_models.image_asset_search import ImageAssetSearchInput, ImageAssetSearchOutput
from .mcp_models.image_folder_create import ImageFolderCreateInput, ImageFolderCreateOutput
from .mcp_models.image_folder_list import ImageFolderListInput, ImageFolderListOutput
from .mcp_models.image_project_create import ImageProjectCreateInput, ImageProjectCreateOutput
from .mcp_models.image_project_list import ImageProjectListInput, ImageProjectListOutput
from .mcp_models.import_service_connection_to_memory import ImportServiceConnectionToMemoryInput, ImportServiceConnectionToMemoryOutput
from .mcp_models.instagram_media_download import InstagramMediaDownloadInput, InstagramMediaDownloadOutput
from .mcp_models.instagram_profile_content import InstagramProfileContentInput, InstagramProfileContentOutput
from .mcp_models.lead_list_enrich import LeadListEnrichInput, LeadListEnrichOutput
from .mcp_models.lead_list_enrich_status import LeadListEnrichStatusInput, LeadListEnrichStatusOutput
from .mcp_models.lead_list_import import LeadListImportInput, LeadListImportOutput
from .mcp_models.lead_list_upload_start import LeadListUploadStartInput, LeadListUploadStartOutput
from .mcp_models.library_ingest import LibraryIngestInput, LibraryIngestOutput
from .mcp_models.list_artifact_templates import ListArtifactTemplatesInput, ListArtifactTemplatesOutput
from .mcp_models.list_channel_members import ListChannelMembersInput, ListChannelMembersOutput
from .mcp_models.list_channel_messages import ListChannelMessagesInput, ListChannelMessagesOutput
from .mcp_models.list_local_sourcebook_tags import ListLocalSourcebookTagsInput, ListLocalSourcebookTagsOutput
from .mcp_models.list_memory_tags import ListMemoryTagsInput, ListMemoryTagsOutput
from .mcp_models.list_scheduled_actions import ListScheduledActionsInput, ListScheduledActionsOutput
from .mcp_models.list_scheduled_runs import ListScheduledRunsInput, ListScheduledRunsOutput
from .mcp_models.list_service_connections import ListServiceConnectionsInput, ListServiceConnectionsOutput
from .mcp_models.list_shared_with_me import ListSharedWithMeInput, ListSharedWithMeOutput
from .mcp_models.list_vaults import ListVaultsInput, ListVaultsOutput
from .mcp_models.list_webhooks import ListWebhooksInput, ListWebhooksOutput
from .mcp_models.local_sourcebook_capture import LocalSourcebookCaptureInput, LocalSourcebookCaptureOutput
from .mcp_models.local_sourcebook_refresh import LocalSourcebookRefreshInput, LocalSourcebookRefreshOutput
from .mcp_models.local_sourcebook_submission_status import LocalSourcebookSubmissionStatusInput, LocalSourcebookSubmissionStatusOutput
from .mcp_models.location_markets import LocationMarketsInput, LocationMarketsOutput
from .mcp_models.map_site_urls import MapSiteUrlsInput, MapSiteUrlsOutput
from .mcp_models.map_wayback_snapshots import MapWaybackSnapshotsInput, MapWaybackSnapshotsOutput
from .mcp_models.maps_place_intel import MapsPlaceIntelInput, MapsPlaceIntelOutput
from .mcp_models.maps_search import MapsSearchInput, MapsSearchOutput
from .mcp_models.mark_scheduled_run_opened import MarkScheduledRunOpenedInput, MarkScheduledRunOpenedOutput
from .mcp_models.mark_scheduled_run_unopened import MarkScheduledRunUnopenedInput, MarkScheduledRunUnopenedOutput
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
from .mcp_models.merge_memory_tags import MergeMemoryTagsInput, MergeMemoryTagsOutput
from .mcp_models.meta_ad_creative_media import MetaAdCreativeMediaInput, MetaAdCreativeMediaOutput
from .mcp_models.my_mentions import MyMentionsInput, MyMentionsOutput
from .mcp_models.pause_scheduled_action import PauseScheduledActionInput, PauseScheduledActionOutput
from .mcp_models.poll_channel import PollChannelInput, PollChannelOutput
from .mcp_models.post_message import PostMessageInput, PostMessageOutput
from .mcp_models.prepare_local_sourcebook_write import PrepareLocalSourcebookWriteInput, PrepareLocalSourcebookWriteOutput
from .mcp_models.prepare_memory_write import PrepareMemoryWriteInput, PrepareMemoryWriteOutput
from .mcp_models.propose_scheduled_action import ProposeScheduledActionInput, ProposeScheduledActionOutput
from .mcp_models.provision_defaults import ProvisionDefaultsInput, ProvisionDefaultsOutput
from .mcp_models.query_fanout_workflow import QueryFanoutWorkflowInput, QueryFanoutWorkflowOutput
from .mcp_models.rank_tracker_workflow import RankTrackerWorkflowInput, RankTrackerWorkflowOutput
from .mcp_models.react_message import ReactMessageInput, ReactMessageOutput
from .mcp_models.read_service_connection import ReadServiceConnectionInput, ReadServiceConnectionOutput
from .mcp_models.record_fact import RecordFactInput, RecordFactOutput
from .mcp_models.reddit_thread import RedditThreadInput, RedditThreadOutput
from .mcp_models.reddit_trending import RedditTrendingInput, RedditTrendingOutput
from .mcp_models.remove_channel_member import RemoveChannelMemberInput, RemoveChannelMemberOutput
from .mcp_models.renew_connected_data_download import RenewConnectedDataDownloadInput, RenewConnectedDataDownloadOutput
from .mcp_models.renew_editorial_reading_room_download import RenewEditorialReadingRoomDownloadInput, RenewEditorialReadingRoomDownloadOutput
from .mcp_models.reply_message import ReplyMessageInput, ReplyMessageOutput
from .mcp_models.report_artifact_read import ReportArtifactReadInput, ReportArtifactReadOutput
from .mcp_models.resolve_local_sourcebook_tags import ResolveLocalSourcebookTagsInput, ResolveLocalSourcebookTagsOutput
from .mcp_models.resolve_memory_tags import ResolveMemoryTagsInput, ResolveMemoryTagsOutput
from .mcp_models.resume_scheduled_action import ResumeScheduledActionInput, ResumeScheduledActionOutput
from .mcp_models.revoke_chat_link import RevokeChatLinkInput, RevokeChatLinkOutput
from .mcp_models.revoke_schedule_link import RevokeScheduleLinkInput, RevokeScheduleLinkOutput
from .mcp_models.revoke_scheduled_run_view_link import RevokeScheduledRunViewLinkInput, RevokeScheduledRunViewLinkOutput
from .mcp_models.revoke_vault_app_link import RevokeVaultAppLinkInput, RevokeVaultAppLinkOutput
from .mcp_models.revoke_webhook import RevokeWebhookInput, RevokeWebhookOutput
from .mcp_models.route_memory import RouteMemoryInput, RouteMemoryOutput
from .mcp_models.search_serp import SearchSerpInput, SearchSerpOutput
from .mcp_models.serp_identity_create import SerpIdentityCreateInput, SerpIdentityCreateOutput
from .mcp_models.serp_identity_delete import SerpIdentityDeleteInput, SerpIdentityDeleteOutput
from .mcp_models.serp_identity_list import SerpIdentityListInput, SerpIdentityListOutput
from .mcp_models.set_agent_identity import SetAgentIdentityInput, SetAgentIdentityOutput
from .mcp_models.set_schedule_defaults import SetScheduleDefaultsInput, SetScheduleDefaultsOutput
from .mcp_models.set_schedule_entitlement import SetScheduleEntitlementInput, SetScheduleEntitlementOutput
from .mcp_models.set_scheduled_action_connections import SetScheduledActionConnectionsInput, SetScheduledActionConnectionsOutput
from .mcp_models.site_export_image import SiteExportImageInput, SiteExportImageOutput
from .mcp_models.site_export_read import SiteExportReadInput, SiteExportReadOutput
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
from .mcp_models.test_service_connection import TestServiceConnectionInput, TestServiceConnectionOutput
from .mcp_models.trustpilot_reviews import TrustpilotReviewsInput, TrustpilotReviewsOutput
from .mcp_models.update_artifact_template import UpdateArtifactTemplateInput, UpdateArtifactTemplateOutput
from .mcp_models.update_scheduled_action import UpdateScheduledActionInput, UpdateScheduledActionOutput
from .mcp_models.upsert_memory_tag import UpsertMemoryTagInput, UpsertMemoryTagOutput
from .mcp_models.validate_local_sourcebook_write import ValidateLocalSourcebookWriteInput, ValidateLocalSourcebookWriteOutput
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


MCP_TOOL_BINDINGS = [{'name': 'access-accept-share', 'category': 'access', 'method_name': 'accept_share'}, {'name': 'access-approve-sender', 'category': 'access', 'method_name': 'approve_sender'}, {'name': 'access-decline-share', 'category': 'access', 'method_name': 'decline_share'}, {'name': 'access-inbox-settings', 'category': 'access', 'method_name': 'inbox_settings'}, {'name': 'access-invite-account', 'category': 'access', 'method_name': 'invite_account'}, {'name': 'access-issue-key', 'category': 'access', 'method_name': 'issue_key'}, {'name': 'access-list-approved-senders', 'category': 'access', 'method_name': 'list_approved_senders'}, {'name': 'access-list-keys', 'category': 'access', 'method_name': 'list_keys'}, {'name': 'access-note-inbox', 'category': 'access', 'method_name': 'note_inbox'}, {'name': 'access-remove-approved-sender', 'category': 'access', 'method_name': 'remove_approved_sender'}, {'name': 'access-revoke-key', 'category': 'access', 'method_name': 'revoke_key'}, {'name': 'access-revoke-share', 'category': 'access', 'method_name': 'revoke_share'}, {'name': 'access-set-scope', 'category': 'access', 'method_name': 'set_scope'}, {'name': 'access-share-note', 'category': 'access', 'method_name': 'share_note'}, {'name': 'access-share-vault', 'category': 'access', 'method_name': 'share_vault'}, {'name': 'access-swap-vault', 'category': 'access', 'method_name': 'swap_vault'}, {'name': 'access-switch-account', 'category': 'access', 'method_name': 'switch_account'}, {'name': 'access-unlink-share', 'category': 'access', 'method_name': 'unlink_share'}, {'name': 'add-vault', 'category': 'vaults', 'method_name': 'add_vault'}, {'name': 'analytics_apply_crm_pipeline_mapping', 'category': 'analytics', 'method_name': 'apply_crm_pipeline_mapping'}, {'name': 'analytics_approve_crm_provisioning', 'category': 'analytics', 'method_name': 'approve_crm_provisioning'}, {'name': 'analytics_archive_event_definition', 'category': 'analytics', 'method_name': 'archive_event_definition'}, {'name': 'analytics_cancel_crm_sync', 'category': 'analytics', 'method_name': 'cancel_crm_sync'}, {'name': 'analytics_commit_crm_import', 'category': 'analytics', 'method_name': 'commit_crm_import'}, {'name': 'analytics_create_activation_destination', 'category': 'analytics', 'method_name': 'create_activation_destination'}, {'name': 'analytics_create_campaign_link', 'category': 'analytics', 'method_name': 'create_campaign_link'}, {'name': 'analytics_create_connection', 'category': 'analytics', 'method_name': 'create_connection'}, {'name': 'analytics_create_conversion_rule', 'category': 'analytics', 'method_name': 'create_conversion_rule'}, {'name': 'analytics_create_event_definition', 'category': 'analytics', 'method_name': 'create_event_definition'}, {'name': 'analytics_create_export', 'category': 'analytics', 'method_name': 'create_export'}, {'name': 'analytics_create_form', 'category': 'analytics', 'method_name': 'create_form'}, {'name': 'analytics_create_funnel', 'category': 'analytics', 'method_name': 'create_funnel'}, {'name': 'analytics_create_lead_score', 'category': 'analytics', 'method_name': 'create_lead_score'}, {'name': 'analytics_create_prediction_target', 'category': 'analytics', 'method_name': 'create_prediction_target'}, {'name': 'analytics_create_saved_view', 'category': 'analytics', 'method_name': 'create_saved_view'}, {'name': 'analytics_delete_privacy_subject', 'category': 'analytics', 'method_name': 'delete_privacy_subject'}, {'name': 'analytics_delete_saved_view', 'category': 'analytics', 'method_name': 'delete_saved_view'}, {'name': 'analytics_discover_activation_assets', 'category': 'analytics', 'method_name': 'discover_activation_assets'}, {'name': 'analytics_discover_crm_capabilities', 'category': 'analytics', 'method_name': 'discover_crm_capabilities'}, {'name': 'analytics_discover_crm_sync_objects', 'category': 'analytics', 'method_name': 'discover_crm_sync_objects'}, {'name': 'analytics_export_crm_csv', 'category': 'analytics', 'method_name': 'export_crm_csv'}, {'name': 'analytics_export_google_ads_csv', 'category': 'analytics', 'method_name': 'export_google_ads_csv'}, {'name': 'analytics_export_meta_technical', 'category': 'analytics', 'method_name': 'export_meta_technical'}, {'name': 'analytics_export_privacy_subject', 'category': 'analytics', 'method_name': 'export_privacy_subject'}, {'name': 'analytics_get_acquisition', 'category': 'analytics', 'method_name': 'get_acquisition'}, {'name': 'analytics_get_business_metrics', 'category': 'analytics', 'method_name': 'get_business_metrics'}, {'name': 'analytics_get_candidate_coverage', 'category': 'analytics', 'method_name': 'get_candidate_coverage'}, {'name': 'analytics_get_channel_breakdown', 'category': 'analytics', 'method_name': 'get_channel_breakdown'}, {'name': 'analytics_get_consent_coverage', 'category': 'analytics', 'method_name': 'get_consent_coverage'}, {'name': 'analytics_get_content', 'category': 'analytics', 'method_name': 'get_content'}, {'name': 'analytics_get_conversions', 'category': 'analytics', 'method_name': 'get_conversions'}, {'name': 'analytics_get_coverage', 'category': 'analytics', 'method_name': 'get_coverage'}, {'name': 'analytics_get_crm_sync_status', 'category': 'analytics', 'method_name': 'get_crm_sync_status'}, {'name': 'analytics_get_dimensions', 'category': 'analytics', 'method_name': 'get_dimensions'}, {'name': 'analytics_get_entitlement', 'category': 'analytics', 'method_name': 'get_entitlement'}, {'name': 'analytics_get_events', 'category': 'analytics', 'method_name': 'get_events'}, {'name': 'analytics_get_forecast', 'category': 'analytics', 'method_name': 'get_forecast'}, {'name': 'analytics_get_funnel', 'category': 'analytics', 'method_name': 'get_funnel'}, {'name': 'analytics_get_health', 'category': 'analytics', 'method_name': 'get_health'}, {'name': 'analytics_get_onboarding_state', 'category': 'analytics', 'method_name': 'get_onboarding_state'}, {'name': 'analytics_get_overview', 'category': 'analytics', 'method_name': 'get_overview'}, {'name': 'analytics_get_paths', 'category': 'analytics', 'method_name': 'get_paths'}, {'name': 'analytics_get_person_journey', 'category': 'analytics', 'method_name': 'get_person_journey'}, {'name': 'analytics_get_prediction_eligibility', 'category': 'analytics', 'method_name': 'get_prediction_eligibility'}, {'name': 'analytics_get_session_timeline', 'category': 'analytics', 'method_name': 'get_session_timeline'}, {'name': 'analytics_get_timeseries', 'category': 'analytics', 'method_name': 'get_timeseries'}, {'name': 'analytics_get_visitor_journey', 'category': 'analytics', 'method_name': 'get_visitor_journey'}, {'name': 'analytics_import_crm_csv', 'category': 'analytics', 'method_name': 'import_crm_csv'}, {'name': 'analytics_list_activation_destinations', 'category': 'analytics', 'method_name': 'list_activation_destinations'}, {'name': 'analytics_list_activation_receipts', 'category': 'analytics', 'method_name': 'list_activation_receipts'}, {'name': 'analytics_list_campaign_links', 'category': 'analytics', 'method_name': 'list_campaign_links'}, {'name': 'analytics_list_connections', 'category': 'analytics', 'method_name': 'list_connections'}, {'name': 'analytics_list_conversion_rules', 'category': 'analytics', 'method_name': 'list_conversion_rules'}, {'name': 'analytics_list_crm_capabilities', 'category': 'analytics', 'method_name': 'list_crm_capabilities'}, {'name': 'analytics_list_crm_imports', 'category': 'analytics', 'method_name': 'list_crm_imports'}, {'name': 'analytics_list_crm_outbound_policies', 'category': 'analytics', 'method_name': 'list_crm_outbound_policies'}, {'name': 'analytics_list_crm_outbound_receipts', 'category': 'analytics', 'method_name': 'list_crm_outbound_receipts'}, {'name': 'analytics_list_event_definitions', 'category': 'analytics', 'method_name': 'list_event_definitions'}, {'name': 'analytics_list_forms', 'category': 'analytics', 'method_name': 'list_forms'}, {'name': 'analytics_list_funnels', 'category': 'analytics', 'method_name': 'list_funnels'}, {'name': 'analytics_list_inference_review', 'category': 'analytics', 'method_name': 'list_inference_review'}, {'name': 'analytics_list_journeys', 'category': 'analytics', 'method_name': 'list_journeys'}, {'name': 'analytics_list_lead_scores', 'category': 'analytics', 'method_name': 'list_lead_scores'}, {'name': 'analytics_list_namespace_sources', 'category': 'analytics', 'method_name': 'list_namespace_sources'}, {'name': 'analytics_list_pixels', 'category': 'analytics', 'method_name': 'list_pixels'}, {'name': 'analytics_list_prediction_targets', 'category': 'analytics', 'method_name': 'list_prediction_targets'}, {'name': 'analytics_list_saved_views', 'category': 'analytics', 'method_name': 'list_saved_views'}, {'name': 'analytics_list_sessions', 'category': 'analytics', 'method_name': 'list_sessions'}, {'name': 'analytics_list_sites', 'category': 'analytics', 'method_name': 'list_sites'}, {'name': 'analytics_list_visitors', 'category': 'analytics', 'method_name': 'list_visitors'}, {'name': 'analytics_plan_crm_provisioning', 'category': 'analytics', 'method_name': 'plan_crm_provisioning'}, {'name': 'analytics_preview_crm_import', 'category': 'analytics', 'method_name': 'preview_crm_import'}, {'name': 'analytics_reconcile_connection', 'category': 'analytics', 'method_name': 'reconcile_connection'}, {'name': 'analytics_record_external_event', 'category': 'analytics', 'method_name': 'record_external_event'}, {'name': 'analytics_retry_activation_delivery', 'category': 'analytics', 'method_name': 'retry_activation_delivery'}, {'name': 'analytics_save_activation_mapping', 'category': 'analytics', 'method_name': 'save_activation_mapping'}, {'name': 'analytics_set_activation_automation', 'category': 'analytics', 'method_name': 'set_activation_automation'}, {'name': 'analytics_start_crm_sync', 'category': 'analytics', 'method_name': 'start_crm_sync'}, {'name': 'analytics_sync_crm_person', 'category': 'analytics', 'method_name': 'sync_crm_person'}, {'name': 'analytics_test_activation_destination', 'category': 'analytics', 'method_name': 'test_activation_destination'}, {'name': 'analytics_test_crm_provisioning', 'category': 'analytics', 'method_name': 'test_crm_provisioning'}, {'name': 'analytics_test_crm_sync_mapping', 'category': 'analytics', 'method_name': 'test_crm_sync_mapping'}, {'name': 'analytics_test_event_definition', 'category': 'analytics', 'method_name': 'test_event_definition'}, {'name': 'analytics_test_funnel', 'category': 'analytics', 'method_name': 'test_funnel'}, {'name': 'analytics_update_crm_sync_schedule', 'category': 'analytics', 'method_name': 'update_crm_sync_schedule'}, {'name': 'analytics_update_event_definition', 'category': 'analytics', 'method_name': 'update_event_definition'}, {'name': 'analytics_update_onboarding_preferences', 'category': 'analytics', 'method_name': 'update_onboarding_preferences'}, {'name': 'analytics_upsert_crm_outbound_policy', 'category': 'analytics', 'method_name': 'upsert_crm_outbound_policy'}, {'name': 'analytics_validate_activation_mapping', 'category': 'analytics', 'method_name': 'validate_activation_mapping'}, {'name': 'analytics_verify_live_event_definition', 'category': 'analytics', 'method_name': 'verify_live_event_definition'}, {'name': 'analytics_withdraw_consent', 'category': 'analytics', 'method_name': 'withdraw_consent'}, {'name': 'analyze_site_similarity', 'category': 'web', 'method_name': 'analyze_site_similarity'}, {'name': 'archive_artifact_template', 'category': 'schedule', 'method_name': 'archive_artifact_template'}, {'name': 'archive_read', 'category': 'web', 'method_name': 'archive_read'}, {'name': 'archive_scheduled_run', 'category': 'schedule', 'method_name': 'archive_scheduled_run'}, {'name': 'assistant_approval_decide', 'category': 'assistant', 'method_name': 'approval_decide'}, {'name': 'assistant_approvals_list', 'category': 'assistant', 'method_name': 'approvals_list'}, {'name': 'assistant_bulk_send', 'category': 'assistant', 'method_name': 'bulk_send'}, {'name': 'assistant_command', 'category': 'assistant', 'method_name': 'command'}, {'name': 'assistant_conversation_get', 'category': 'assistant', 'method_name': 'conversation_get'}, {'name': 'assistant_execution_status', 'category': 'assistant', 'method_name': 'execution_status'}, {'name': 'assistant_grant_create', 'category': 'assistant', 'method_name': 'grant_create'}, {'name': 'assistant_grant_revoke', 'category': 'assistant', 'method_name': 'grant_revoke'}, {'name': 'assistant_grants_list', 'category': 'assistant', 'method_name': 'grants_list'}, {'name': 'assistant_message_send', 'category': 'assistant', 'method_name': 'message_send'}, {'name': 'assistant_number_purchase', 'category': 'assistant', 'method_name': 'number_purchase'}, {'name': 'assistant_number_release', 'category': 'assistant', 'method_name': 'number_release'}, {'name': 'assistant_number_search', 'category': 'assistant', 'method_name': 'number_search'}, {'name': 'assistant_number_status', 'category': 'assistant', 'method_name': 'number_status'}, {'name': 'assistant_status', 'category': 'assistant', 'method_name': 'status'}, {'name': 'audit_site', 'category': 'web', 'method_name': 'audit_site'}, {'name': 'browser_click', 'category': 'browser', 'method_name': 'click'}, {'name': 'browser_close', 'category': 'browser', 'method_name': 'close'}, {'name': 'browser_extension_delete', 'category': 'browser', 'method_name': 'extension_delete'}, {'name': 'browser_extension_import', 'category': 'browser', 'method_name': 'extension_import'}, {'name': 'browser_extension_list', 'category': 'browser', 'method_name': 'extension_list'}, {'name': 'browser_goto', 'category': 'browser', 'method_name': 'goto'}, {'name': 'browser_list_replays', 'category': 'browser', 'method_name': 'list_replays'}, {'name': 'browser_list_sessions', 'category': 'browser', 'method_name': 'list_sessions'}, {'name': 'browser_locate', 'category': 'browser', 'method_name': 'locate'}, {'name': 'browser_open', 'category': 'browser', 'method_name': 'open'}, {'name': 'browser_press', 'category': 'browser', 'method_name': 'press'}, {'name': 'browser_profile_connect', 'category': 'browser', 'method_name': 'profile_connect'}, {'name': 'browser_profile_list', 'category': 'browser', 'method_name': 'profile_list'}, {'name': 'browser_read', 'category': 'browser', 'method_name': 'read'}, {'name': 'browser_replay_annotate', 'category': 'browser', 'method_name': 'replay_annotate'}, {'name': 'browser_replay_download', 'category': 'browser', 'method_name': 'replay_download'}, {'name': 'browser_replay_mark', 'category': 'browser', 'method_name': 'replay_mark'}, {'name': 'browser_replay_start', 'category': 'browser', 'method_name': 'replay_start'}, {'name': 'browser_replay_stop', 'category': 'browser', 'method_name': 'replay_stop'}, {'name': 'browser_screenshot', 'category': 'browser', 'method_name': 'screenshot'}, {'name': 'browser_scroll', 'category': 'browser', 'method_name': 'scroll'}, {'name': 'browser_type', 'category': 'browser', 'method_name': 'type'}, {'name': 'bulk-delete-notes', 'category': 'memory', 'method_name': 'bulk_delete_notes'}, {'name': 'call_service_connection_action', 'category': 'connections', 'method_name': 'call_service_connection_action'}, {'name': 'capture_serp_page_snapshots', 'category': 'serpIntelligence', 'method_name': 'page_snapshots'}, {'name': 'capture_serp_snapshot', 'category': 'serpIntelligence', 'method_name': 'snapshot'}, {'name': 'check_site_export', 'category': 'web', 'method_name': 'check_site_export'}, {'name': 'commons_claim_publication', 'category': 'commons', 'method_name': 'claim_publication'}, {'name': 'commons_get_entity', 'category': 'commons', 'method_name': 'get_entity'}, {'name': 'commons_get_entity_ledger', 'category': 'commons', 'method_name': 'get_entity_ledger'}, {'name': 'commons_get_entity_linkset', 'category': 'commons', 'method_name': 'get_entity_linkset'}, {'name': 'commons_get_proposal', 'category': 'commons', 'method_name': 'get_proposal'}, {'name': 'commons_get_publication', 'category': 'commons', 'method_name': 'get_publication'}, {'name': 'commons_host_image', 'category': 'commons', 'method_name': 'host_image'}, {'name': 'commons_list_filters', 'category': 'commons', 'method_name': 'list_filters'}, {'name': 'commons_list_needs_links', 'category': 'commons', 'method_name': 'list_needs_links'}, {'name': 'commons_prepare_entity', 'category': 'commons', 'method_name': 'prepare_entity'}, {'name': 'commons_prepare_publication', 'category': 'commons', 'method_name': 'prepare_publication'}, {'name': 'commons_publish_editorial', 'category': 'commons', 'method_name': 'publish_editorial'}, {'name': 'commons_save_filter', 'category': 'commons', 'method_name': 'save_filter'}, {'name': 'commons_search_entities', 'category': 'commons', 'method_name': 'search_entities'}, {'name': 'commons_submit_entity', 'category': 'commons', 'method_name': 'submit_entity'}, {'name': 'commons_update_editorial_article', 'category': 'commons', 'method_name': 'update_editorial_article'}, {'name': 'commons_validate_entity', 'category': 'commons', 'method_name': 'validate_entity'}, {'name': 'commons_validate_publication', 'category': 'commons', 'method_name': 'validate_publication'}, {'name': 'cost-usage', 'category': 'storage', 'method_name': 'cost_usage'}, {'name': 'create_artifact_template', 'category': 'schedule', 'method_name': 'create_artifact_template'}, {'name': 'create_editorial_reading_room', 'category': 'editorial', 'method_name': 'create_reading_room'}, {'name': 'create_scheduled_run_view_link', 'category': 'schedule', 'method_name': 'create_scheduled_run_view_link'}, {'name': 'create-channel', 'category': 'channels', 'method_name': 'create_channel'}, {'name': 'create-scheduled-action', 'category': 'schedule', 'method_name': 'create_scheduled_action'}, {'name': 'create-secure-vault', 'category': 'vaults', 'method_name': 'create_secure_vault'}, {'name': 'create-webhook', 'category': 'webhooks', 'method_name': 'create_webhook'}, {'name': 'credits_info', 'category': 'billing', 'method_name': 'credits_info'}, {'name': 'delete-note', 'category': 'memory', 'method_name': 'delete_note'}, {'name': 'delete-scheduled-action', 'category': 'schedule', 'method_name': 'delete_scheduled_action'}, {'name': 'delete-vault', 'category': 'vaults', 'method_name': 'delete_vault'}, {'name': 'describe_service_connection_tool', 'category': 'connections', 'method_name': 'describe_service_connection_tool'}, {'name': 'diff_page', 'category': 'web', 'method_name': 'diff_page'}, {'name': 'directory_workflow', 'category': 'directory', 'method_name': 'run'}, {'name': 'directory_workflow_status', 'category': 'directory', 'method_name': 'workflow_status'}, {'name': 'editorial_reading_room_guide', 'category': 'editorial', 'method_name': 'reading_room_guide'}, {'name': 'export_connected_service_data', 'category': 'connections', 'method_name': 'export_connected_service_data'}, {'name': 'export_search_console_table_data', 'category': 'connections', 'method_name': 'export_search_console_table_data'}, {'name': 'extract_site', 'category': 'web', 'method_name': 'extract_site'}, {'name': 'extract_url', 'category': 'web', 'method_name': 'extract_url'}, {'name': 'facebook_ad_search', 'category': 'facebook', 'method_name': 'ad_search'}, {'name': 'facebook_ad_transcribe', 'category': 'facebook', 'method_name': 'ad_transcribe'}, {'name': 'facebook_page_intel', 'category': 'facebook', 'method_name': 'page_intel'}, {'name': 'facebook_video_transcribe', 'category': 'facebook', 'method_name': 'video_transcribe'}, {'name': 'fact-history', 'category': 'facts', 'method_name': 'history'}, {'name': 'g2_reviews', 'category': 'reviews', 'method_name': 'g2_reviews'}, {'name': 'get_artifact_template', 'category': 'schedule', 'method_name': 'get_artifact_template'}, {'name': 'get_artifact_template_example', 'category': 'artifacts', 'method_name': 'get_artifact_template_example'}, {'name': 'get_scheduled_run', 'category': 'schedule', 'method_name': 'get_scheduled_run'}, {'name': 'get-chat-link', 'category': 'access', 'method_name': 'get_chat_link'}, {'name': 'get-local-sourcebook-contract', 'category': 'directory', 'method_name': 'get_local_sourcebook_contract'}, {'name': 'get-message-note', 'category': 'channels', 'method_name': 'get_message_note'}, {'name': 'get-schedule-link', 'category': 'schedule', 'method_name': 'get_schedule_link'}, {'name': 'get-schedule-status', 'category': 'schedule', 'method_name': 'get_schedule_status'}, {'name': 'get-vault-app-link', 'category': 'access', 'method_name': 'get_vault_app_link'}, {'name': 'get-vault-contract', 'category': 'vaults', 'method_name': 'get_vault_contract'}, {'name': 'gmail_bulk_delete_messages', 'category': 'connections', 'method_name': 'gmail_bulk_delete_messages'}, {'name': 'gmail_bulk_manage_messages', 'category': 'connections', 'method_name': 'gmail_bulk_manage_messages'}, {'name': 'gmail_export_selection', 'category': 'connections', 'method_name': 'gmail_export_selection'}, {'name': 'gmail_get_attachment', 'category': 'connections', 'method_name': 'gmail_get_attachment'}, {'name': 'gmail_get_message', 'category': 'connections', 'method_name': 'gmail_get_message'}, {'name': 'gmail_import_status', 'category': 'connections', 'method_name': 'gmail_import_status'}, {'name': 'gmail_import_to_memory', 'category': 'connections', 'method_name': 'gmail_import_to_memory'}, {'name': 'gmail_prepare_memory_import', 'category': 'connections', 'method_name': 'gmail_prepare_memory_import'}, {'name': 'gmail_prepare_selection', 'category': 'connections', 'method_name': 'gmail_prepare_selection'}, {'name': 'gmail_search_contacts', 'category': 'connections', 'method_name': 'gmail_search_contacts'}, {'name': 'gmail_search_messages', 'category': 'connections', 'method_name': 'gmail_search_messages'}, {'name': 'gmail_send_message', 'category': 'connections', 'method_name': 'gmail_send_message'}, {'name': 'google_ads_page_intel', 'category': 'googleAds', 'method_name': 'page_intel'}, {'name': 'google_ads_search', 'category': 'googleAds', 'method_name': 'search'}, {'name': 'google_ads_transcribe', 'category': 'googleAds', 'method_name': 'transcribe'}, {'name': 'google_calendar_create_event', 'category': 'connections', 'method_name': 'google_calendar_create_event'}, {'name': 'harvest_paa', 'category': 'search', 'method_name': 'harvest_paa'}, {'name': 'harvest_paa_start', 'category': 'other', 'method_name': 'harvest_paa_start'}, {'name': 'harvest_paa_status', 'category': 'other', 'method_name': 'harvest_paa_status'}, {'name': 'image_asset_delete', 'category': 'images', 'method_name': 'asset_delete'}, {'name': 'image_asset_get', 'category': 'images', 'method_name': 'asset_get'}, {'name': 'image_asset_list', 'category': 'images', 'method_name': 'asset_list'}, {'name': 'image_asset_move', 'category': 'images', 'method_name': 'asset_move'}, {'name': 'image_asset_save', 'category': 'images', 'method_name': 'asset_save'}, {'name': 'image_asset_search', 'category': 'images', 'method_name': 'asset_search'}, {'name': 'image_folder_create', 'category': 'images', 'method_name': 'folder_create'}, {'name': 'image_folder_list', 'category': 'images', 'method_name': 'folder_list'}, {'name': 'image_project_create', 'category': 'images', 'method_name': 'project_create'}, {'name': 'image_project_list', 'category': 'images', 'method_name': 'project_list'}, {'name': 'import_service_connection_to_memory', 'category': 'connections', 'method_name': 'import_service_connection_to_memory'}, {'name': 'instagram_media_download', 'category': 'instagram', 'method_name': 'media_download'}, {'name': 'instagram_profile_content', 'category': 'instagram', 'method_name': 'profile_content'}, {'name': 'lead_list_enrich', 'category': 'leads', 'method_name': 'enrich'}, {'name': 'lead_list_enrich_status', 'category': 'leads', 'method_name': 'enrich_status'}, {'name': 'lead_list_import', 'category': 'leads', 'method_name': 'import_'}, {'name': 'lead_list_upload_start', 'category': 'leads', 'method_name': 'upload_start'}, {'name': 'library-ingest', 'category': 'library', 'method_name': 'ingest'}, {'name': 'list_artifact_templates', 'category': 'schedule', 'method_name': 'list_artifact_templates'}, {'name': 'list_scheduled_runs', 'category': 'schedule', 'method_name': 'list_scheduled_runs'}, {'name': 'list_service_connections', 'category': 'connections', 'method_name': 'list_service_connections'}, {'name': 'list-channel-members', 'category': 'channels', 'method_name': 'list_channel_members'}, {'name': 'list-channel-messages', 'category': 'channels', 'method_name': 'list_channel_messages'}, {'name': 'list-local-sourcebook-tags', 'category': 'directory', 'method_name': 'list_local_sourcebook_tags'}, {'name': 'list-memory-tags', 'category': 'tags', 'method_name': 'list_memory_tags'}, {'name': 'list-scheduled-actions', 'category': 'schedule', 'method_name': 'list_scheduled_actions'}, {'name': 'list-shared-with-me', 'category': 'vaults', 'method_name': 'list_shared_with_me'}, {'name': 'list-vaults', 'category': 'vaults', 'method_name': 'list_vaults'}, {'name': 'list-webhooks', 'category': 'webhooks', 'method_name': 'list_webhooks'}, {'name': 'local_sourcebook_refresh', 'category': 'directory', 'method_name': 'local_sourcebook_refresh'}, {'name': 'local_sourcebook_submission_status', 'category': 'directory', 'method_name': 'local_sourcebook_submission_status'}, {'name': 'local-sourcebook-capture', 'category': 'directory', 'method_name': 'local_sourcebook_capture'}, {'name': 'location_markets', 'category': 'directory', 'method_name': 'location_markets'}, {'name': 'map_site_urls', 'category': 'web', 'method_name': 'map_site_urls'}, {'name': 'map_wayback_snapshots', 'category': 'web', 'method_name': 'map_wayback_snapshots'}, {'name': 'maps_place_intel', 'category': 'maps', 'method_name': 'place_intel'}, {'name': 'maps_search', 'category': 'maps', 'method_name': 'search'}, {'name': 'mark_scheduled_run_opened', 'category': 'schedule', 'method_name': 'mark_scheduled_run_opened'}, {'name': 'mark_scheduled_run_unopened', 'category': 'schedule', 'method_name': 'mark_scheduled_run_unopened'}, {'name': 'memory-backlinks', 'category': 'graph', 'method_name': 'memory_backlinks'}, {'name': 'memory-capture', 'category': 'capture', 'method_name': 'memory_capture'}, {'name': 'memory-export', 'category': 'memory', 'method_name': 'export'}, {'name': 'memory-get', 'category': 'memory', 'method_name': 'get'}, {'name': 'memory-graph-path', 'category': 'graph', 'method_name': 'memory_graph_path'}, {'name': 'memory-graph-universe', 'category': 'graph', 'method_name': 'memory_graph_universe'}, {'name': 'memory-list', 'category': 'memory', 'method_name': 'list'}, {'name': 'memory-put', 'category': 'memory', 'method_name': 'put'}, {'name': 'memory-questions', 'category': 'capture', 'method_name': 'memory_questions'}, {'name': 'memory-search', 'category': 'memory', 'method_name': 'search'}, {'name': 'memory-suggest', 'category': 'memory', 'method_name': 'suggest'}, {'name': 'memory-upload', 'category': 'memory', 'method_name': 'upload'}, {'name': 'merge-memory-tags', 'category': 'tags', 'method_name': 'merge_memory_tags'}, {'name': 'meta_ad_creative_media', 'category': 'connections', 'method_name': 'meta_ad_creative_media'}, {'name': 'my-mentions', 'category': 'channels', 'method_name': 'my_mentions'}, {'name': 'pause-scheduled-action', 'category': 'schedule', 'method_name': 'pause_scheduled_action'}, {'name': 'poll-channel', 'category': 'channels', 'method_name': 'poll_channel'}, {'name': 'post-message', 'category': 'channels', 'method_name': 'post_message'}, {'name': 'prepare-local-sourcebook-write', 'category': 'directory', 'method_name': 'prepare_local_sourcebook_write'}, {'name': 'prepare-memory-write', 'category': 'capture', 'method_name': 'prepare_memory_write'}, {'name': 'propose-scheduled-action', 'category': 'schedule', 'method_name': 'propose_scheduled_action'}, {'name': 'provision-defaults', 'category': 'vaults', 'method_name': 'provision_defaults'}, {'name': 'query_fanout_workflow', 'category': 'workflows', 'method_name': 'query_fanout'}, {'name': 'rank_tracker_workflow', 'category': 'workflows', 'method_name': 'rank_tracker'}, {'name': 'react-message', 'category': 'channels', 'method_name': 'react_message'}, {'name': 'read_service_connection', 'category': 'connections', 'method_name': 'read_service_connection'}, {'name': 'record-fact', 'category': 'facts', 'method_name': 'record_fact'}, {'name': 'reddit_thread', 'category': 'reddit', 'method_name': 'thread'}, {'name': 'reddit_trending', 'category': 'reddit', 'method_name': 'trending'}, {'name': 'remove-channel-member', 'category': 'channels', 'method_name': 'remove_channel_member'}, {'name': 'renew_connected_data_download', 'category': 'connections', 'method_name': 'renew_connected_data_download'}, {'name': 'renew_editorial_reading_room_download', 'category': 'editorial', 'method_name': 'renew_reading_room_download'}, {'name': 'reply-message', 'category': 'channels', 'method_name': 'reply_message'}, {'name': 'report_artifact_read', 'category': 'artifacts', 'method_name': 'read'}, {'name': 'resolve-local-sourcebook-tags', 'category': 'directory', 'method_name': 'resolve_local_sourcebook_tags'}, {'name': 'resolve-memory-tags', 'category': 'tags', 'method_name': 'resolve_memory_tags'}, {'name': 'resume-scheduled-action', 'category': 'schedule', 'method_name': 'resume_scheduled_action'}, {'name': 'revoke_scheduled_run_view_link', 'category': 'schedule', 'method_name': 'revoke_scheduled_run_view_link'}, {'name': 'revoke-chat-link', 'category': 'access', 'method_name': 'revoke_chat_link'}, {'name': 'revoke-schedule-link', 'category': 'schedule', 'method_name': 'revoke_schedule_link'}, {'name': 'revoke-vault-app-link', 'category': 'access', 'method_name': 'revoke_vault_app_link'}, {'name': 'revoke-webhook', 'category': 'webhooks', 'method_name': 'revoke_webhook'}, {'name': 'route-memory', 'category': 'vaults', 'method_name': 'route_memory'}, {'name': 'search_serp', 'category': 'search', 'method_name': 'search_serp'}, {'name': 'serp_identity_create', 'category': 'search', 'method_name': 'serp_identity_create'}, {'name': 'serp_identity_delete', 'category': 'search', 'method_name': 'serp_identity_delete'}, {'name': 'serp_identity_list', 'category': 'search', 'method_name': 'serp_identity_list'}, {'name': 'set_scheduled_action_connections', 'category': 'connections', 'method_name': 'set_scheduled_action_connections'}, {'name': 'set-agent-identity', 'category': 'access', 'method_name': 'set_agent_identity'}, {'name': 'set-schedule-defaults', 'category': 'schedule', 'method_name': 'set_schedule_defaults'}, {'name': 'set-schedule-entitlement', 'category': 'schedule', 'method_name': 'set_schedule_entitlement'}, {'name': 'site_export_image', 'category': 'web', 'method_name': 'site_export_image'}, {'name': 'site_export_read', 'category': 'web', 'method_name': 'site_export_read'}, {'name': 'slack_send_message', 'category': 'connections', 'method_name': 'slack_send_message'}, {'name': 'storage-usage', 'category': 'storage', 'method_name': 'usage'}, {'name': 'table-create', 'category': 'tables', 'method_name': 'create'}, {'name': 'table-delete-rows', 'category': 'tables', 'method_name': 'delete_rows'}, {'name': 'table-describe', 'category': 'tables', 'method_name': 'describe'}, {'name': 'table-drop', 'category': 'tables', 'method_name': 'drop'}, {'name': 'table-insert-rows', 'category': 'tables', 'method_name': 'insert_rows'}, {'name': 'table-list', 'category': 'tables', 'method_name': 'list'}, {'name': 'table-query', 'category': 'tables', 'method_name': 'query'}, {'name': 'temporal-recall', 'category': 'recall', 'method_name': 'temporal_recall'}, {'name': 'test_service_connection', 'category': 'connections', 'method_name': 'test_service_connection'}, {'name': 'trustpilot_reviews', 'category': 'reviews', 'method_name': 'trustpilot_reviews'}, {'name': 'update_artifact_template', 'category': 'schedule', 'method_name': 'update_artifact_template'}, {'name': 'update-scheduled-action', 'category': 'schedule', 'method_name': 'update_scheduled_action'}, {'name': 'upsert-memory-tag', 'category': 'tags', 'method_name': 'upsert_memory_tag'}, {'name': 'validate-local-sourcebook-write', 'category': 'directory', 'method_name': 'validate_local_sourcebook_write'}, {'name': 'validate-memory-write', 'category': 'capture', 'method_name': 'validate_memory_write'}, {'name': 'video_frame_analysis', 'category': 'video', 'method_name': 'frame_analysis'}, {'name': 'video_frame_analysis_status', 'category': 'video', 'method_name': 'frame_analysis_status'}, {'name': 'video-analyze-start', 'category': 'video', 'method_name': 'analyze_start'}, {'name': 'video-analyze-status', 'category': 'video', 'method_name': 'analyze_status'}, {'name': 'workflow_artifact_read', 'category': 'workflows', 'method_name': 'artifact_read'}, {'name': 'workflow_list', 'category': 'workflows', 'method_name': 'list'}, {'name': 'workflow_run', 'category': 'workflows', 'method_name': 'run'}, {'name': 'workflow_status', 'category': 'workflows', 'method_name': 'status'}, {'name': 'workflow_step', 'category': 'workflows', 'method_name': 'step'}, {'name': 'workflow_suggest', 'category': 'workflows', 'method_name': 'suggest'}, {'name': 'youtube_harvest', 'category': 'youtube', 'method_name': 'harvest'}, {'name': 'youtube_transcribe', 'category': 'youtube', 'method_name': 'transcribe'}, {'name': 'zoom_create_meeting', 'category': 'connections', 'method_name': 'zoom_create_meeting'}]
MCP_TOOL_COUNT = len(MCP_TOOL_BINDINGS)


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

    def revoke_key(self, **kwargs: Any) -> AccessRevokeKeyOutput:
        payload = AccessRevokeKeyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-revoke-key", payload)
        return AccessRevokeKeyOutput.model_validate(result)

    def revoke_share(self, **kwargs: Any) -> AccessRevokeShareOutput:
        payload = AccessRevokeShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("access-revoke-share", payload)
        return AccessRevokeShareOutput.model_validate(result)

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

    def get_chat_link(self, **kwargs: Any) -> GetChatLinkOutput:
        payload = GetChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-chat-link", payload)
        return GetChatLinkOutput.model_validate(result)

    def get_vault_app_link(self, **kwargs: Any) -> GetVaultAppLinkOutput:
        payload = GetVaultAppLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-vault-app-link", payload)
        return GetVaultAppLinkOutput.model_validate(result)

    def revoke_chat_link(self, **kwargs: Any) -> RevokeChatLinkOutput:
        payload = RevokeChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revoke-chat-link", payload)
        return RevokeChatLinkOutput.model_validate(result)

    def revoke_vault_app_link(self, **kwargs: Any) -> RevokeVaultAppLinkOutput:
        payload = RevokeVaultAppLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revoke-vault-app-link", payload)
        return RevokeVaultAppLinkOutput.model_validate(result)

    def set_agent_identity(self, **kwargs: Any) -> SetAgentIdentityOutput:
        payload = SetAgentIdentityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("set-agent-identity", payload)
        return SetAgentIdentityOutput.model_validate(result)


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


class AnalyticsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def apply_crm_pipeline_mapping(self, **kwargs: Any) -> AnalyticsApplyCrmPipelineMappingOutput:
        payload = AnalyticsApplyCrmPipelineMappingInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_apply_crm_pipeline_mapping", payload)
        return AnalyticsApplyCrmPipelineMappingOutput.model_validate(result)

    def approve_crm_provisioning(self, **kwargs: Any) -> AnalyticsApproveCrmProvisioningOutput:
        payload = AnalyticsApproveCrmProvisioningInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_approve_crm_provisioning", payload)
        return AnalyticsApproveCrmProvisioningOutput.model_validate(result)

    def archive_event_definition(self, **kwargs: Any) -> AnalyticsArchiveEventDefinitionOutput:
        payload = AnalyticsArchiveEventDefinitionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_archive_event_definition", payload)
        return AnalyticsArchiveEventDefinitionOutput.model_validate(result)

    def cancel_crm_sync(self, **kwargs: Any) -> AnalyticsCancelCrmSyncOutput:
        payload = AnalyticsCancelCrmSyncInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_cancel_crm_sync", payload)
        return AnalyticsCancelCrmSyncOutput.model_validate(result)

    def commit_crm_import(self, **kwargs: Any) -> AnalyticsCommitCrmImportOutput:
        payload = AnalyticsCommitCrmImportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_commit_crm_import", payload)
        return AnalyticsCommitCrmImportOutput.model_validate(result)

    def create_activation_destination(self, **kwargs: Any) -> AnalyticsCreateActivationDestinationOutput:
        payload = AnalyticsCreateActivationDestinationInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_activation_destination", payload)
        return AnalyticsCreateActivationDestinationOutput.model_validate(result)

    def create_campaign_link(self, **kwargs: Any) -> AnalyticsCreateCampaignLinkOutput:
        payload = AnalyticsCreateCampaignLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_campaign_link", payload)
        return AnalyticsCreateCampaignLinkOutput.model_validate(result)

    def create_connection(self, **kwargs: Any) -> AnalyticsCreateConnectionOutput:
        payload = AnalyticsCreateConnectionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_connection", payload)
        return AnalyticsCreateConnectionOutput.model_validate(result)

    def create_conversion_rule(self, **kwargs: Any) -> AnalyticsCreateConversionRuleOutput:
        payload = AnalyticsCreateConversionRuleInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_conversion_rule", payload)
        return AnalyticsCreateConversionRuleOutput.model_validate(result)

    def create_event_definition(self, **kwargs: Any) -> AnalyticsCreateEventDefinitionOutput:
        payload = AnalyticsCreateEventDefinitionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_event_definition", payload)
        return AnalyticsCreateEventDefinitionOutput.model_validate(result)

    def create_export(self, **kwargs: Any) -> AnalyticsCreateExportOutput:
        payload = AnalyticsCreateExportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_export", payload)
        return AnalyticsCreateExportOutput.model_validate(result)

    def create_form(self, **kwargs: Any) -> AnalyticsCreateFormOutput:
        payload = AnalyticsCreateFormInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_form", payload)
        return AnalyticsCreateFormOutput.model_validate(result)

    def create_funnel(self, **kwargs: Any) -> AnalyticsCreateFunnelOutput:
        payload = AnalyticsCreateFunnelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_funnel", payload)
        return AnalyticsCreateFunnelOutput.model_validate(result)

    def create_lead_score(self, **kwargs: Any) -> AnalyticsCreateLeadScoreOutput:
        payload = AnalyticsCreateLeadScoreInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_lead_score", payload)
        return AnalyticsCreateLeadScoreOutput.model_validate(result)

    def create_prediction_target(self, **kwargs: Any) -> AnalyticsCreatePredictionTargetOutput:
        payload = AnalyticsCreatePredictionTargetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_prediction_target", payload)
        return AnalyticsCreatePredictionTargetOutput.model_validate(result)

    def create_saved_view(self, **kwargs: Any) -> AnalyticsCreateSavedViewOutput:
        payload = AnalyticsCreateSavedViewInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_create_saved_view", payload)
        return AnalyticsCreateSavedViewOutput.model_validate(result)

    def delete_privacy_subject(self, **kwargs: Any) -> AnalyticsDeletePrivacySubjectOutput:
        payload = AnalyticsDeletePrivacySubjectInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_delete_privacy_subject", payload)
        return AnalyticsDeletePrivacySubjectOutput.model_validate(result)

    def delete_saved_view(self, **kwargs: Any) -> AnalyticsDeleteSavedViewOutput:
        payload = AnalyticsDeleteSavedViewInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_delete_saved_view", payload)
        return AnalyticsDeleteSavedViewOutput.model_validate(result)

    def discover_activation_assets(self, **kwargs: Any) -> AnalyticsDiscoverActivationAssetsOutput:
        payload = AnalyticsDiscoverActivationAssetsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_discover_activation_assets", payload)
        return AnalyticsDiscoverActivationAssetsOutput.model_validate(result)

    def discover_crm_capabilities(self, **kwargs: Any) -> AnalyticsDiscoverCrmCapabilitiesOutput:
        payload = AnalyticsDiscoverCrmCapabilitiesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_discover_crm_capabilities", payload)
        return AnalyticsDiscoverCrmCapabilitiesOutput.model_validate(result)

    def discover_crm_sync_objects(self, **kwargs: Any) -> AnalyticsDiscoverCrmSyncObjectsOutput:
        payload = AnalyticsDiscoverCrmSyncObjectsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_discover_crm_sync_objects", payload)
        return AnalyticsDiscoverCrmSyncObjectsOutput.model_validate(result)

    def export_crm_csv(self, **kwargs: Any) -> AnalyticsExportCrmCsvOutput:
        payload = AnalyticsExportCrmCsvInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_export_crm_csv", payload)
        return AnalyticsExportCrmCsvOutput.model_validate(result)

    def export_google_ads_csv(self, **kwargs: Any) -> AnalyticsExportGoogleAdsCsvOutput:
        payload = AnalyticsExportGoogleAdsCsvInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_export_google_ads_csv", payload)
        return AnalyticsExportGoogleAdsCsvOutput.model_validate(result)

    def export_meta_technical(self, **kwargs: Any) -> AnalyticsExportMetaTechnicalOutput:
        payload = AnalyticsExportMetaTechnicalInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_export_meta_technical", payload)
        return AnalyticsExportMetaTechnicalOutput.model_validate(result)

    def export_privacy_subject(self, **kwargs: Any) -> AnalyticsExportPrivacySubjectOutput:
        payload = AnalyticsExportPrivacySubjectInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_export_privacy_subject", payload)
        return AnalyticsExportPrivacySubjectOutput.model_validate(result)

    def get_acquisition(self, **kwargs: Any) -> AnalyticsGetAcquisitionOutput:
        payload = AnalyticsGetAcquisitionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_acquisition", payload)
        return AnalyticsGetAcquisitionOutput.model_validate(result)

    def get_business_metrics(self, **kwargs: Any) -> AnalyticsGetBusinessMetricsOutput:
        payload = AnalyticsGetBusinessMetricsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_business_metrics", payload)
        return AnalyticsGetBusinessMetricsOutput.model_validate(result)

    def get_candidate_coverage(self, **kwargs: Any) -> AnalyticsGetCandidateCoverageOutput:
        payload = AnalyticsGetCandidateCoverageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_candidate_coverage", payload)
        return AnalyticsGetCandidateCoverageOutput.model_validate(result)

    def get_channel_breakdown(self, **kwargs: Any) -> AnalyticsGetChannelBreakdownOutput:
        payload = AnalyticsGetChannelBreakdownInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_channel_breakdown", payload)
        return AnalyticsGetChannelBreakdownOutput.model_validate(result)

    def get_consent_coverage(self, **kwargs: Any) -> AnalyticsGetConsentCoverageOutput:
        payload = AnalyticsGetConsentCoverageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_consent_coverage", payload)
        return AnalyticsGetConsentCoverageOutput.model_validate(result)

    def get_content(self, **kwargs: Any) -> AnalyticsGetContentOutput:
        payload = AnalyticsGetContentInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_content", payload)
        return AnalyticsGetContentOutput.model_validate(result)

    def get_conversions(self, **kwargs: Any) -> AnalyticsGetConversionsOutput:
        payload = AnalyticsGetConversionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_conversions", payload)
        return AnalyticsGetConversionsOutput.model_validate(result)

    def get_coverage(self, **kwargs: Any) -> AnalyticsGetCoverageOutput:
        payload = AnalyticsGetCoverageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_coverage", payload)
        return AnalyticsGetCoverageOutput.model_validate(result)

    def get_crm_sync_status(self, **kwargs: Any) -> AnalyticsGetCrmSyncStatusOutput:
        payload = AnalyticsGetCrmSyncStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_crm_sync_status", payload)
        return AnalyticsGetCrmSyncStatusOutput.model_validate(result)

    def get_dimensions(self, **kwargs: Any) -> AnalyticsGetDimensionsOutput:
        payload = AnalyticsGetDimensionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_dimensions", payload)
        return AnalyticsGetDimensionsOutput.model_validate(result)

    def get_entitlement(self, **kwargs: Any) -> AnalyticsGetEntitlementOutput:
        payload = AnalyticsGetEntitlementInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_entitlement", payload)
        return AnalyticsGetEntitlementOutput.model_validate(result)

    def get_events(self, **kwargs: Any) -> AnalyticsGetEventsOutput:
        payload = AnalyticsGetEventsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_events", payload)
        return AnalyticsGetEventsOutput.model_validate(result)

    def get_forecast(self, **kwargs: Any) -> AnalyticsGetForecastOutput:
        payload = AnalyticsGetForecastInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_forecast", payload)
        return AnalyticsGetForecastOutput.model_validate(result)

    def get_funnel(self, **kwargs: Any) -> AnalyticsGetFunnelOutput:
        payload = AnalyticsGetFunnelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_funnel", payload)
        return AnalyticsGetFunnelOutput.model_validate(result)

    def get_health(self, **kwargs: Any) -> AnalyticsGetHealthOutput:
        payload = AnalyticsGetHealthInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_health", payload)
        return AnalyticsGetHealthOutput.model_validate(result)

    def get_onboarding_state(self, **kwargs: Any) -> AnalyticsGetOnboardingStateOutput:
        payload = AnalyticsGetOnboardingStateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_onboarding_state", payload)
        return AnalyticsGetOnboardingStateOutput.model_validate(result)

    def get_overview(self, **kwargs: Any) -> AnalyticsGetOverviewOutput:
        payload = AnalyticsGetOverviewInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_overview", payload)
        return AnalyticsGetOverviewOutput.model_validate(result)

    def get_paths(self, **kwargs: Any) -> AnalyticsGetPathsOutput:
        payload = AnalyticsGetPathsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_paths", payload)
        return AnalyticsGetPathsOutput.model_validate(result)

    def get_person_journey(self, **kwargs: Any) -> AnalyticsGetPersonJourneyOutput:
        payload = AnalyticsGetPersonJourneyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_person_journey", payload)
        return AnalyticsGetPersonJourneyOutput.model_validate(result)

    def get_prediction_eligibility(self, **kwargs: Any) -> AnalyticsGetPredictionEligibilityOutput:
        payload = AnalyticsGetPredictionEligibilityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_prediction_eligibility", payload)
        return AnalyticsGetPredictionEligibilityOutput.model_validate(result)

    def get_session_timeline(self, **kwargs: Any) -> AnalyticsGetSessionTimelineOutput:
        payload = AnalyticsGetSessionTimelineInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_session_timeline", payload)
        return AnalyticsGetSessionTimelineOutput.model_validate(result)

    def get_timeseries(self, **kwargs: Any) -> AnalyticsGetTimeseriesOutput:
        payload = AnalyticsGetTimeseriesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_timeseries", payload)
        return AnalyticsGetTimeseriesOutput.model_validate(result)

    def get_visitor_journey(self, **kwargs: Any) -> AnalyticsGetVisitorJourneyOutput:
        payload = AnalyticsGetVisitorJourneyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_get_visitor_journey", payload)
        return AnalyticsGetVisitorJourneyOutput.model_validate(result)

    def import_crm_csv(self, **kwargs: Any) -> AnalyticsImportCrmCsvOutput:
        payload = AnalyticsImportCrmCsvInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_import_crm_csv", payload)
        return AnalyticsImportCrmCsvOutput.model_validate(result)

    def list_activation_destinations(self, **kwargs: Any) -> AnalyticsListActivationDestinationsOutput:
        payload = AnalyticsListActivationDestinationsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_activation_destinations", payload)
        return AnalyticsListActivationDestinationsOutput.model_validate(result)

    def list_activation_receipts(self, **kwargs: Any) -> AnalyticsListActivationReceiptsOutput:
        payload = AnalyticsListActivationReceiptsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_activation_receipts", payload)
        return AnalyticsListActivationReceiptsOutput.model_validate(result)

    def list_campaign_links(self, **kwargs: Any) -> AnalyticsListCampaignLinksOutput:
        payload = AnalyticsListCampaignLinksInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_campaign_links", payload)
        return AnalyticsListCampaignLinksOutput.model_validate(result)

    def list_connections(self, **kwargs: Any) -> AnalyticsListConnectionsOutput:
        payload = AnalyticsListConnectionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_connections", payload)
        return AnalyticsListConnectionsOutput.model_validate(result)

    def list_conversion_rules(self, **kwargs: Any) -> AnalyticsListConversionRulesOutput:
        payload = AnalyticsListConversionRulesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_conversion_rules", payload)
        return AnalyticsListConversionRulesOutput.model_validate(result)

    def list_crm_capabilities(self, **kwargs: Any) -> AnalyticsListCrmCapabilitiesOutput:
        payload = AnalyticsListCrmCapabilitiesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_crm_capabilities", payload)
        return AnalyticsListCrmCapabilitiesOutput.model_validate(result)

    def list_crm_imports(self, **kwargs: Any) -> AnalyticsListCrmImportsOutput:
        payload = AnalyticsListCrmImportsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_crm_imports", payload)
        return AnalyticsListCrmImportsOutput.model_validate(result)

    def list_crm_outbound_policies(self, **kwargs: Any) -> AnalyticsListCrmOutboundPoliciesOutput:
        payload = AnalyticsListCrmOutboundPoliciesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_crm_outbound_policies", payload)
        return AnalyticsListCrmOutboundPoliciesOutput.model_validate(result)

    def list_crm_outbound_receipts(self, **kwargs: Any) -> AnalyticsListCrmOutboundReceiptsOutput:
        payload = AnalyticsListCrmOutboundReceiptsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_crm_outbound_receipts", payload)
        return AnalyticsListCrmOutboundReceiptsOutput.model_validate(result)

    def list_event_definitions(self, **kwargs: Any) -> AnalyticsListEventDefinitionsOutput:
        payload = AnalyticsListEventDefinitionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_event_definitions", payload)
        return AnalyticsListEventDefinitionsOutput.model_validate(result)

    def list_forms(self, **kwargs: Any) -> AnalyticsListFormsOutput:
        payload = AnalyticsListFormsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_forms", payload)
        return AnalyticsListFormsOutput.model_validate(result)

    def list_funnels(self, **kwargs: Any) -> AnalyticsListFunnelsOutput:
        payload = AnalyticsListFunnelsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_funnels", payload)
        return AnalyticsListFunnelsOutput.model_validate(result)

    def list_inference_review(self, **kwargs: Any) -> AnalyticsListInferenceReviewOutput:
        payload = AnalyticsListInferenceReviewInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_inference_review", payload)
        return AnalyticsListInferenceReviewOutput.model_validate(result)

    def list_journeys(self, **kwargs: Any) -> AnalyticsListJourneysOutput:
        payload = AnalyticsListJourneysInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_journeys", payload)
        return AnalyticsListJourneysOutput.model_validate(result)

    def list_lead_scores(self, **kwargs: Any) -> AnalyticsListLeadScoresOutput:
        payload = AnalyticsListLeadScoresInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_lead_scores", payload)
        return AnalyticsListLeadScoresOutput.model_validate(result)

    def list_namespace_sources(self, **kwargs: Any) -> AnalyticsListNamespaceSourcesOutput:
        payload = AnalyticsListNamespaceSourcesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_namespace_sources", payload)
        return AnalyticsListNamespaceSourcesOutput.model_validate(result)

    def list_pixels(self, **kwargs: Any) -> AnalyticsListPixelsOutput:
        payload = AnalyticsListPixelsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_pixels", payload)
        return AnalyticsListPixelsOutput.model_validate(result)

    def list_prediction_targets(self, **kwargs: Any) -> AnalyticsListPredictionTargetsOutput:
        payload = AnalyticsListPredictionTargetsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_prediction_targets", payload)
        return AnalyticsListPredictionTargetsOutput.model_validate(result)

    def list_saved_views(self, **kwargs: Any) -> AnalyticsListSavedViewsOutput:
        payload = AnalyticsListSavedViewsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_saved_views", payload)
        return AnalyticsListSavedViewsOutput.model_validate(result)

    def list_sessions(self, **kwargs: Any) -> AnalyticsListSessionsOutput:
        payload = AnalyticsListSessionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_sessions", payload)
        return AnalyticsListSessionsOutput.model_validate(result)

    def list_sites(self, **kwargs: Any) -> AnalyticsListSitesOutput:
        payload = AnalyticsListSitesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_sites", payload)
        return AnalyticsListSitesOutput.model_validate(result)

    def list_visitors(self, **kwargs: Any) -> AnalyticsListVisitorsOutput:
        payload = AnalyticsListVisitorsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_list_visitors", payload)
        return AnalyticsListVisitorsOutput.model_validate(result)

    def plan_crm_provisioning(self, **kwargs: Any) -> AnalyticsPlanCrmProvisioningOutput:
        payload = AnalyticsPlanCrmProvisioningInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_plan_crm_provisioning", payload)
        return AnalyticsPlanCrmProvisioningOutput.model_validate(result)

    def preview_crm_import(self, **kwargs: Any) -> AnalyticsPreviewCrmImportOutput:
        payload = AnalyticsPreviewCrmImportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_preview_crm_import", payload)
        return AnalyticsPreviewCrmImportOutput.model_validate(result)

    def reconcile_connection(self, **kwargs: Any) -> AnalyticsReconcileConnectionOutput:
        payload = AnalyticsReconcileConnectionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_reconcile_connection", payload)
        return AnalyticsReconcileConnectionOutput.model_validate(result)

    def record_external_event(self, **kwargs: Any) -> AnalyticsRecordExternalEventOutput:
        payload = AnalyticsRecordExternalEventInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_record_external_event", payload)
        return AnalyticsRecordExternalEventOutput.model_validate(result)

    def retry_activation_delivery(self, **kwargs: Any) -> AnalyticsRetryActivationDeliveryOutput:
        payload = AnalyticsRetryActivationDeliveryInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_retry_activation_delivery", payload)
        return AnalyticsRetryActivationDeliveryOutput.model_validate(result)

    def save_activation_mapping(self, **kwargs: Any) -> AnalyticsSaveActivationMappingOutput:
        payload = AnalyticsSaveActivationMappingInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_save_activation_mapping", payload)
        return AnalyticsSaveActivationMappingOutput.model_validate(result)

    def set_activation_automation(self, **kwargs: Any) -> AnalyticsSetActivationAutomationOutput:
        payload = AnalyticsSetActivationAutomationInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_set_activation_automation", payload)
        return AnalyticsSetActivationAutomationOutput.model_validate(result)

    def start_crm_sync(self, **kwargs: Any) -> AnalyticsStartCrmSyncOutput:
        payload = AnalyticsStartCrmSyncInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_start_crm_sync", payload)
        return AnalyticsStartCrmSyncOutput.model_validate(result)

    def sync_crm_person(self, **kwargs: Any) -> AnalyticsSyncCrmPersonOutput:
        payload = AnalyticsSyncCrmPersonInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_sync_crm_person", payload)
        return AnalyticsSyncCrmPersonOutput.model_validate(result)

    def test_activation_destination(self, **kwargs: Any) -> AnalyticsTestActivationDestinationOutput:
        payload = AnalyticsTestActivationDestinationInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_test_activation_destination", payload)
        return AnalyticsTestActivationDestinationOutput.model_validate(result)

    def test_crm_provisioning(self, **kwargs: Any) -> AnalyticsTestCrmProvisioningOutput:
        payload = AnalyticsTestCrmProvisioningInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_test_crm_provisioning", payload)
        return AnalyticsTestCrmProvisioningOutput.model_validate(result)

    def test_crm_sync_mapping(self, **kwargs: Any) -> AnalyticsTestCrmSyncMappingOutput:
        payload = AnalyticsTestCrmSyncMappingInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_test_crm_sync_mapping", payload)
        return AnalyticsTestCrmSyncMappingOutput.model_validate(result)

    def test_event_definition(self, **kwargs: Any) -> AnalyticsTestEventDefinitionOutput:
        payload = AnalyticsTestEventDefinitionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_test_event_definition", payload)
        return AnalyticsTestEventDefinitionOutput.model_validate(result)

    def test_funnel(self, **kwargs: Any) -> AnalyticsTestFunnelOutput:
        payload = AnalyticsTestFunnelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_test_funnel", payload)
        return AnalyticsTestFunnelOutput.model_validate(result)

    def update_crm_sync_schedule(self, **kwargs: Any) -> AnalyticsUpdateCrmSyncScheduleOutput:
        payload = AnalyticsUpdateCrmSyncScheduleInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_update_crm_sync_schedule", payload)
        return AnalyticsUpdateCrmSyncScheduleOutput.model_validate(result)

    def update_event_definition(self, **kwargs: Any) -> AnalyticsUpdateEventDefinitionOutput:
        payload = AnalyticsUpdateEventDefinitionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_update_event_definition", payload)
        return AnalyticsUpdateEventDefinitionOutput.model_validate(result)

    def update_onboarding_preferences(self, **kwargs: Any) -> AnalyticsUpdateOnboardingPreferencesOutput:
        payload = AnalyticsUpdateOnboardingPreferencesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_update_onboarding_preferences", payload)
        return AnalyticsUpdateOnboardingPreferencesOutput.model_validate(result)

    def upsert_crm_outbound_policy(self, **kwargs: Any) -> AnalyticsUpsertCrmOutboundPolicyOutput:
        payload = AnalyticsUpsertCrmOutboundPolicyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_upsert_crm_outbound_policy", payload)
        return AnalyticsUpsertCrmOutboundPolicyOutput.model_validate(result)

    def validate_activation_mapping(self, **kwargs: Any) -> AnalyticsValidateActivationMappingOutput:
        payload = AnalyticsValidateActivationMappingInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_validate_activation_mapping", payload)
        return AnalyticsValidateActivationMappingOutput.model_validate(result)

    def verify_live_event_definition(self, **kwargs: Any) -> AnalyticsVerifyLiveEventDefinitionOutput:
        payload = AnalyticsVerifyLiveEventDefinitionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_verify_live_event_definition", payload)
        return AnalyticsVerifyLiveEventDefinitionOutput.model_validate(result)

    def withdraw_consent(self, **kwargs: Any) -> AnalyticsWithdrawConsentOutput:
        payload = AnalyticsWithdrawConsentInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analytics_withdraw_consent", payload)
        return AnalyticsWithdrawConsentOutput.model_validate(result)


class WebNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def analyze_site_similarity(self, **kwargs: Any) -> AnalyzeSiteSimilarityOutput:
        payload = AnalyzeSiteSimilarityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("analyze_site_similarity", payload)
        return AnalyzeSiteSimilarityOutput.model_validate(result)

    def archive_read(self, **kwargs: Any) -> ArchiveReadOutput:
        payload = ArchiveReadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("archive_read", payload)
        return ArchiveReadOutput.model_validate(result)

    def audit_site(self, **kwargs: Any) -> AuditSiteOutput:
        payload = AuditSiteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("audit_site", payload)
        return AuditSiteOutput.model_validate(result)

    def check_site_export(self, **kwargs: Any) -> CheckSiteExportOutput:
        payload = CheckSiteExportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("check_site_export", payload)
        return CheckSiteExportOutput.model_validate(result)

    def diff_page(self, **kwargs: Any) -> DiffPageOutput:
        payload = DiffPageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("diff_page", payload)
        return DiffPageOutput.model_validate(result)

    def extract_site(self, **kwargs: Any) -> ExtractSiteOutput:
        payload = ExtractSiteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("extract_site", payload)
        return ExtractSiteOutput.model_validate(result)

    def extract_url(self, **kwargs: Any) -> ExtractUrlOutput:
        payload = ExtractUrlInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("extract_url", payload)
        return ExtractUrlOutput.model_validate(result)

    def map_site_urls(self, **kwargs: Any) -> MapSiteUrlsOutput:
        payload = MapSiteUrlsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("map_site_urls", payload)
        return MapSiteUrlsOutput.model_validate(result)

    def map_wayback_snapshots(self, **kwargs: Any) -> MapWaybackSnapshotsOutput:
        payload = MapWaybackSnapshotsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("map_wayback_snapshots", payload)
        return MapWaybackSnapshotsOutput.model_validate(result)

    def site_export_image(self, **kwargs: Any) -> SiteExportImageOutput:
        payload = SiteExportImageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("site_export_image", payload)
        return SiteExportImageOutput.model_validate(result)

    def site_export_read(self, **kwargs: Any) -> SiteExportReadOutput:
        payload = SiteExportReadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("site_export_read", payload)
        return SiteExportReadOutput.model_validate(result)


class ScheduleNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def archive_artifact_template(self, **kwargs: Any) -> ArchiveArtifactTemplateOutput:
        payload = ArchiveArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("archive_artifact_template", payload)
        return ArchiveArtifactTemplateOutput.model_validate(result)

    def archive_scheduled_run(self, **kwargs: Any) -> ArchiveScheduledRunOutput:
        payload = ArchiveScheduledRunInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("archive_scheduled_run", payload)
        return ArchiveScheduledRunOutput.model_validate(result)

    def create_artifact_template(self, **kwargs: Any) -> CreateArtifactTemplateOutput:
        payload = CreateArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("create_artifact_template", payload)
        return CreateArtifactTemplateOutput.model_validate(result)

    def create_scheduled_run_view_link(self, **kwargs: Any) -> CreateScheduledRunViewLinkOutput:
        payload = CreateScheduledRunViewLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("create_scheduled_run_view_link", payload)
        return CreateScheduledRunViewLinkOutput.model_validate(result)

    def create_scheduled_action(self, **kwargs: Any) -> CreateScheduledActionOutput:
        payload = CreateScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("create-scheduled-action", payload)
        return CreateScheduledActionOutput.model_validate(result)

    def delete_scheduled_action(self, **kwargs: Any) -> DeleteScheduledActionOutput:
        payload = DeleteScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("delete-scheduled-action", payload)
        return DeleteScheduledActionOutput.model_validate(result)

    def get_artifact_template(self, **kwargs: Any) -> GetArtifactTemplateOutput:
        payload = GetArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get_artifact_template", payload)
        return GetArtifactTemplateOutput.model_validate(result)

    def get_scheduled_run(self, **kwargs: Any) -> GetScheduledRunOutput:
        payload = GetScheduledRunInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get_scheduled_run", payload)
        return GetScheduledRunOutput.model_validate(result)

    def get_schedule_link(self, **kwargs: Any) -> GetScheduleLinkOutput:
        payload = GetScheduleLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-schedule-link", payload)
        return GetScheduleLinkOutput.model_validate(result)

    def get_schedule_status(self, **kwargs: Any) -> GetScheduleStatusOutput:
        payload = GetScheduleStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-schedule-status", payload)
        return GetScheduleStatusOutput.model_validate(result)

    def list_artifact_templates(self, **kwargs: Any) -> ListArtifactTemplatesOutput:
        payload = ListArtifactTemplatesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list_artifact_templates", payload)
        return ListArtifactTemplatesOutput.model_validate(result)

    def list_scheduled_runs(self, **kwargs: Any) -> ListScheduledRunsOutput:
        payload = ListScheduledRunsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list_scheduled_runs", payload)
        return ListScheduledRunsOutput.model_validate(result)

    def list_scheduled_actions(self, **kwargs: Any) -> ListScheduledActionsOutput:
        payload = ListScheduledActionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-scheduled-actions", payload)
        return ListScheduledActionsOutput.model_validate(result)

    def mark_scheduled_run_opened(self, **kwargs: Any) -> MarkScheduledRunOpenedOutput:
        payload = MarkScheduledRunOpenedInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("mark_scheduled_run_opened", payload)
        return MarkScheduledRunOpenedOutput.model_validate(result)

    def mark_scheduled_run_unopened(self, **kwargs: Any) -> MarkScheduledRunUnopenedOutput:
        payload = MarkScheduledRunUnopenedInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("mark_scheduled_run_unopened", payload)
        return MarkScheduledRunUnopenedOutput.model_validate(result)

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

    def revoke_scheduled_run_view_link(self, **kwargs: Any) -> RevokeScheduledRunViewLinkOutput:
        payload = RevokeScheduledRunViewLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revoke_scheduled_run_view_link", payload)
        return RevokeScheduledRunViewLinkOutput.model_validate(result)

    def revoke_schedule_link(self, **kwargs: Any) -> RevokeScheduleLinkOutput:
        payload = RevokeScheduleLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revoke-schedule-link", payload)
        return RevokeScheduleLinkOutput.model_validate(result)

    def set_schedule_defaults(self, **kwargs: Any) -> SetScheduleDefaultsOutput:
        payload = SetScheduleDefaultsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("set-schedule-defaults", payload)
        return SetScheduleDefaultsOutput.model_validate(result)

    def set_schedule_entitlement(self, **kwargs: Any) -> SetScheduleEntitlementOutput:
        payload = SetScheduleEntitlementInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("set-schedule-entitlement", payload)
        return SetScheduleEntitlementOutput.model_validate(result)

    def update_artifact_template(self, **kwargs: Any) -> UpdateArtifactTemplateOutput:
        payload = UpdateArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("update_artifact_template", payload)
        return UpdateArtifactTemplateOutput.model_validate(result)

    def update_scheduled_action(self, **kwargs: Any) -> UpdateScheduledActionOutput:
        payload = UpdateScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("update-scheduled-action", payload)
        return UpdateScheduledActionOutput.model_validate(result)


class AssistantNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def approval_decide(self, **kwargs: Any) -> AssistantApprovalDecideOutput:
        payload = AssistantApprovalDecideInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_approval_decide", payload)
        return AssistantApprovalDecideOutput.model_validate(result)

    def approvals_list(self, **kwargs: Any) -> AssistantApprovalsListOutput:
        payload = AssistantApprovalsListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_approvals_list", payload)
        return AssistantApprovalsListOutput.model_validate(result)

    def bulk_send(self, **kwargs: Any) -> AssistantBulkSendOutput:
        payload = AssistantBulkSendInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_bulk_send", payload)
        return AssistantBulkSendOutput.model_validate(result)

    def command(self, **kwargs: Any) -> AssistantCommandOutput:
        payload = AssistantCommandInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_command", payload)
        return AssistantCommandOutput.model_validate(result)

    def conversation_get(self, **kwargs: Any) -> AssistantConversationGetOutput:
        payload = AssistantConversationGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_conversation_get", payload)
        return AssistantConversationGetOutput.model_validate(result)

    def execution_status(self, **kwargs: Any) -> AssistantExecutionStatusOutput:
        payload = AssistantExecutionStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_execution_status", payload)
        return AssistantExecutionStatusOutput.model_validate(result)

    def grant_create(self, **kwargs: Any) -> AssistantGrantCreateOutput:
        payload = AssistantGrantCreateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_grant_create", payload)
        return AssistantGrantCreateOutput.model_validate(result)

    def grant_revoke(self, **kwargs: Any) -> AssistantGrantRevokeOutput:
        payload = AssistantGrantRevokeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_grant_revoke", payload)
        return AssistantGrantRevokeOutput.model_validate(result)

    def grants_list(self, **kwargs: Any) -> AssistantGrantsListOutput:
        payload = AssistantGrantsListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_grants_list", payload)
        return AssistantGrantsListOutput.model_validate(result)

    def message_send(self, **kwargs: Any) -> AssistantMessageSendOutput:
        payload = AssistantMessageSendInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_message_send", payload)
        return AssistantMessageSendOutput.model_validate(result)

    def number_purchase(self, **kwargs: Any) -> AssistantNumberPurchaseOutput:
        payload = AssistantNumberPurchaseInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_number_purchase", payload)
        return AssistantNumberPurchaseOutput.model_validate(result)

    def number_release(self, **kwargs: Any) -> AssistantNumberReleaseOutput:
        payload = AssistantNumberReleaseInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_number_release", payload)
        return AssistantNumberReleaseOutput.model_validate(result)

    def number_search(self, **kwargs: Any) -> AssistantNumberSearchOutput:
        payload = AssistantNumberSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_number_search", payload)
        return AssistantNumberSearchOutput.model_validate(result)

    def number_status(self, **kwargs: Any) -> AssistantNumberStatusOutput:
        payload = AssistantNumberStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_number_status", payload)
        return AssistantNumberStatusOutput.model_validate(result)

    def status(self, **kwargs: Any) -> AssistantStatusOutput:
        payload = AssistantStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_status", payload)
        return AssistantStatusOutput.model_validate(result)


class BrowserNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def click(self, **kwargs: Any) -> BrowserClickOutput:
        payload = BrowserClickInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_click", payload)
        return BrowserClickOutput.model_validate(result)

    def close(self, **kwargs: Any) -> BrowserCloseOutput:
        payload = BrowserCloseInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_close", payload)
        return BrowserCloseOutput.model_validate(result)

    def extension_delete(self, **kwargs: Any) -> BrowserExtensionDeleteOutput:
        payload = BrowserExtensionDeleteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_extension_delete", payload)
        return BrowserExtensionDeleteOutput.model_validate(result)

    def extension_import(self, **kwargs: Any) -> BrowserExtensionImportOutput:
        payload = BrowserExtensionImportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_extension_import", payload)
        return BrowserExtensionImportOutput.model_validate(result)

    def extension_list(self, **kwargs: Any) -> BrowserExtensionListOutput:
        payload = BrowserExtensionListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_extension_list", payload)
        return BrowserExtensionListOutput.model_validate(result)

    def goto(self, **kwargs: Any) -> BrowserGotoOutput:
        payload = BrowserGotoInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_goto", payload)
        return BrowserGotoOutput.model_validate(result)

    def list_replays(self, **kwargs: Any) -> BrowserListReplaysOutput:
        payload = BrowserListReplaysInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_list_replays", payload)
        return BrowserListReplaysOutput.model_validate(result)

    def list_sessions(self, **kwargs: Any) -> BrowserListSessionsOutput:
        payload = BrowserListSessionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_list_sessions", payload)
        return BrowserListSessionsOutput.model_validate(result)

    def locate(self, **kwargs: Any) -> BrowserLocateOutput:
        payload = BrowserLocateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_locate", payload)
        return BrowserLocateOutput.model_validate(result)

    def open(self, **kwargs: Any) -> BrowserOpenOutput:
        payload = BrowserOpenInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_open", payload)
        return BrowserOpenOutput.model_validate(result)

    def press(self, **kwargs: Any) -> BrowserPressOutput:
        payload = BrowserPressInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_press", payload)
        return BrowserPressOutput.model_validate(result)

    def profile_connect(self, **kwargs: Any) -> BrowserProfileConnectOutput:
        payload = BrowserProfileConnectInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_profile_connect", payload)
        return BrowserProfileConnectOutput.model_validate(result)

    def profile_list(self, **kwargs: Any) -> BrowserProfileListOutput:
        payload = BrowserProfileListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_profile_list", payload)
        return BrowserProfileListOutput.model_validate(result)

    def read(self, **kwargs: Any) -> BrowserReadOutput:
        payload = BrowserReadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_read", payload)
        return BrowserReadOutput.model_validate(result)

    def replay_annotate(self, **kwargs: Any) -> BrowserReplayAnnotateOutput:
        payload = BrowserReplayAnnotateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_replay_annotate", payload)
        return BrowserReplayAnnotateOutput.model_validate(result)

    def replay_download(self, **kwargs: Any) -> BrowserReplayDownloadOutput:
        payload = BrowserReplayDownloadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_replay_download", payload)
        return BrowserReplayDownloadOutput.model_validate(result)

    def replay_mark(self, **kwargs: Any) -> BrowserReplayMarkOutput:
        payload = BrowserReplayMarkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_replay_mark", payload)
        return BrowserReplayMarkOutput.model_validate(result)

    def replay_start(self, **kwargs: Any) -> BrowserReplayStartOutput:
        payload = BrowserReplayStartInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_replay_start", payload)
        return BrowserReplayStartOutput.model_validate(result)

    def replay_stop(self, **kwargs: Any) -> BrowserReplayStopOutput:
        payload = BrowserReplayStopInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_replay_stop", payload)
        return BrowserReplayStopOutput.model_validate(result)

    def screenshot(self, **kwargs: Any) -> BrowserScreenshotOutput:
        payload = BrowserScreenshotInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_screenshot", payload)
        return BrowserScreenshotOutput.model_validate(result)

    def scroll(self, **kwargs: Any) -> BrowserScrollOutput:
        payload = BrowserScrollInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_scroll", payload)
        return BrowserScrollOutput.model_validate(result)

    def type(self, **kwargs: Any) -> BrowserTypeOutput:
        payload = BrowserTypeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("browser_type", payload)
        return BrowserTypeOutput.model_validate(result)


class MemoryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def bulk_delete_notes(self, **kwargs: Any) -> BulkDeleteNotesOutput:
        payload = BulkDeleteNotesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("bulk-delete-notes", payload)
        return BulkDeleteNotesOutput.model_validate(result)

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


class ConnectionsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def call_service_connection_action(self, **kwargs: Any) -> CallServiceConnectionActionOutput:
        payload = CallServiceConnectionActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("call_service_connection_action", payload)
        return CallServiceConnectionActionOutput.model_validate(result)

    def describe_service_connection_tool(self, **kwargs: Any) -> DescribeServiceConnectionToolOutput:
        payload = DescribeServiceConnectionToolInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("describe_service_connection_tool", payload)
        return DescribeServiceConnectionToolOutput.model_validate(result)

    def export_connected_service_data(self, **kwargs: Any) -> ExportConnectedServiceDataOutput:
        payload = ExportConnectedServiceDataInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("export_connected_service_data", payload)
        return ExportConnectedServiceDataOutput.model_validate(result)

    def export_search_console_table_data(self, **kwargs: Any) -> ExportSearchConsoleTableDataOutput:
        payload = ExportSearchConsoleTableDataInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("export_search_console_table_data", payload)
        return ExportSearchConsoleTableDataOutput.model_validate(result)

    def gmail_bulk_delete_messages(self, **kwargs: Any) -> GmailBulkDeleteMessagesOutput:
        payload = GmailBulkDeleteMessagesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_bulk_delete_messages", payload)
        return GmailBulkDeleteMessagesOutput.model_validate(result)

    def gmail_bulk_manage_messages(self, **kwargs: Any) -> GmailBulkManageMessagesOutput:
        payload = GmailBulkManageMessagesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_bulk_manage_messages", payload)
        return GmailBulkManageMessagesOutput.model_validate(result)

    def gmail_export_selection(self, **kwargs: Any) -> GmailExportSelectionOutput:
        payload = GmailExportSelectionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_export_selection", payload)
        return GmailExportSelectionOutput.model_validate(result)

    def gmail_get_attachment(self, **kwargs: Any) -> GmailGetAttachmentOutput:
        payload = GmailGetAttachmentInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_get_attachment", payload)
        return GmailGetAttachmentOutput.model_validate(result)

    def gmail_get_message(self, **kwargs: Any) -> GmailGetMessageOutput:
        payload = GmailGetMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_get_message", payload)
        return GmailGetMessageOutput.model_validate(result)

    def gmail_import_status(self, **kwargs: Any) -> GmailImportStatusOutput:
        payload = GmailImportStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_import_status", payload)
        return GmailImportStatusOutput.model_validate(result)

    def gmail_import_to_memory(self, **kwargs: Any) -> GmailImportToMemoryOutput:
        payload = GmailImportToMemoryInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_import_to_memory", payload)
        return GmailImportToMemoryOutput.model_validate(result)

    def gmail_prepare_memory_import(self, **kwargs: Any) -> GmailPrepareMemoryImportOutput:
        payload = GmailPrepareMemoryImportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_prepare_memory_import", payload)
        return GmailPrepareMemoryImportOutput.model_validate(result)

    def gmail_prepare_selection(self, **kwargs: Any) -> GmailPrepareSelectionOutput:
        payload = GmailPrepareSelectionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_prepare_selection", payload)
        return GmailPrepareSelectionOutput.model_validate(result)

    def gmail_search_contacts(self, **kwargs: Any) -> GmailSearchContactsOutput:
        payload = GmailSearchContactsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_search_contacts", payload)
        return GmailSearchContactsOutput.model_validate(result)

    def gmail_search_messages(self, **kwargs: Any) -> GmailSearchMessagesOutput:
        payload = GmailSearchMessagesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_search_messages", payload)
        return GmailSearchMessagesOutput.model_validate(result)

    def gmail_send_message(self, **kwargs: Any) -> GmailSendMessageOutput:
        payload = GmailSendMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("gmail_send_message", payload)
        return GmailSendMessageOutput.model_validate(result)

    def google_calendar_create_event(self, **kwargs: Any) -> GoogleCalendarCreateEventOutput:
        payload = GoogleCalendarCreateEventInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("google_calendar_create_event", payload)
        return GoogleCalendarCreateEventOutput.model_validate(result)

    def import_service_connection_to_memory(self, **kwargs: Any) -> ImportServiceConnectionToMemoryOutput:
        payload = ImportServiceConnectionToMemoryInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("import_service_connection_to_memory", payload)
        return ImportServiceConnectionToMemoryOutput.model_validate(result)

    def list_service_connections(self, **kwargs: Any) -> ListServiceConnectionsOutput:
        payload = ListServiceConnectionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list_service_connections", payload)
        return ListServiceConnectionsOutput.model_validate(result)

    def meta_ad_creative_media(self, **kwargs: Any) -> MetaAdCreativeMediaOutput:
        payload = MetaAdCreativeMediaInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("meta_ad_creative_media", payload)
        return MetaAdCreativeMediaOutput.model_validate(result)

    def read_service_connection(self, **kwargs: Any) -> ReadServiceConnectionOutput:
        payload = ReadServiceConnectionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("read_service_connection", payload)
        return ReadServiceConnectionOutput.model_validate(result)

    def renew_connected_data_download(self, **kwargs: Any) -> RenewConnectedDataDownloadOutput:
        payload = RenewConnectedDataDownloadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("renew_connected_data_download", payload)
        return RenewConnectedDataDownloadOutput.model_validate(result)

    def set_scheduled_action_connections(self, **kwargs: Any) -> SetScheduledActionConnectionsOutput:
        payload = SetScheduledActionConnectionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("set_scheduled_action_connections", payload)
        return SetScheduledActionConnectionsOutput.model_validate(result)

    def slack_send_message(self, **kwargs: Any) -> SlackSendMessageOutput:
        payload = SlackSendMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("slack_send_message", payload)
        return SlackSendMessageOutput.model_validate(result)

    def test_service_connection(self, **kwargs: Any) -> TestServiceConnectionOutput:
        payload = TestServiceConnectionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("test_service_connection", payload)
        return TestServiceConnectionOutput.model_validate(result)

    def zoom_create_meeting(self, **kwargs: Any) -> ZoomCreateMeetingOutput:
        payload = ZoomCreateMeetingInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("zoom_create_meeting", payload)
        return ZoomCreateMeetingOutput.model_validate(result)


class SerpIntelligenceNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def page_snapshots(self, **kwargs: Any) -> CaptureSerpPageSnapshotsOutput:
        payload = CaptureSerpPageSnapshotsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("capture_serp_page_snapshots", payload)
        return CaptureSerpPageSnapshotsOutput.model_validate(result)

    def snapshot(self, **kwargs: Any) -> CaptureSerpSnapshotOutput:
        payload = CaptureSerpSnapshotInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("capture_serp_snapshot", payload)
        return CaptureSerpSnapshotOutput.model_validate(result)


class CommonsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def claim_publication(self, **kwargs: Any) -> CommonsClaimPublicationOutput:
        payload = CommonsClaimPublicationInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_claim_publication", payload)
        return CommonsClaimPublicationOutput.model_validate(result)

    def get_entity(self, **kwargs: Any) -> CommonsGetEntityOutput:
        payload = CommonsGetEntityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_get_entity", payload)
        return CommonsGetEntityOutput.model_validate(result)

    def get_entity_ledger(self, **kwargs: Any) -> CommonsGetEntityLedgerOutput:
        payload = CommonsGetEntityLedgerInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_get_entity_ledger", payload)
        return CommonsGetEntityLedgerOutput.model_validate(result)

    def get_entity_linkset(self, **kwargs: Any) -> CommonsGetEntityLinksetOutput:
        payload = CommonsGetEntityLinksetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_get_entity_linkset", payload)
        return CommonsGetEntityLinksetOutput.model_validate(result)

    def get_proposal(self, **kwargs: Any) -> CommonsGetProposalOutput:
        payload = CommonsGetProposalInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_get_proposal", payload)
        return CommonsGetProposalOutput.model_validate(result)

    def get_publication(self, **kwargs: Any) -> CommonsGetPublicationOutput:
        payload = CommonsGetPublicationInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_get_publication", payload)
        return CommonsGetPublicationOutput.model_validate(result)

    def host_image(self, **kwargs: Any) -> CommonsHostImageOutput:
        payload = CommonsHostImageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_host_image", payload)
        return CommonsHostImageOutput.model_validate(result)

    def list_filters(self, **kwargs: Any) -> CommonsListFiltersOutput:
        payload = CommonsListFiltersInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_list_filters", payload)
        return CommonsListFiltersOutput.model_validate(result)

    def list_needs_links(self, **kwargs: Any) -> CommonsListNeedsLinksOutput:
        payload = CommonsListNeedsLinksInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_list_needs_links", payload)
        return CommonsListNeedsLinksOutput.model_validate(result)

    def prepare_entity(self, **kwargs: Any) -> CommonsPrepareEntityOutput:
        payload = CommonsPrepareEntityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_prepare_entity", payload)
        return CommonsPrepareEntityOutput.model_validate(result)

    def prepare_publication(self, **kwargs: Any) -> CommonsPreparePublicationOutput:
        payload = CommonsPreparePublicationInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_prepare_publication", payload)
        return CommonsPreparePublicationOutput.model_validate(result)

    def publish_editorial(self, **kwargs: Any) -> CommonsPublishEditorialOutput:
        payload = CommonsPublishEditorialInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_publish_editorial", payload)
        return CommonsPublishEditorialOutput.model_validate(result)

    def save_filter(self, **kwargs: Any) -> CommonsSaveFilterOutput:
        payload = CommonsSaveFilterInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_save_filter", payload)
        return CommonsSaveFilterOutput.model_validate(result)

    def search_entities(self, **kwargs: Any) -> CommonsSearchEntitiesOutput:
        payload = CommonsSearchEntitiesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_search_entities", payload)
        return CommonsSearchEntitiesOutput.model_validate(result)

    def submit_entity(self, **kwargs: Any) -> CommonsSubmitEntityOutput:
        payload = CommonsSubmitEntityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_submit_entity", payload)
        return CommonsSubmitEntityOutput.model_validate(result)

    def update_editorial_article(self, **kwargs: Any) -> CommonsUpdateEditorialArticleOutput:
        payload = CommonsUpdateEditorialArticleInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_update_editorial_article", payload)
        return CommonsUpdateEditorialArticleOutput.model_validate(result)

    def validate_entity(self, **kwargs: Any) -> CommonsValidateEntityOutput:
        payload = CommonsValidateEntityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_validate_entity", payload)
        return CommonsValidateEntityOutput.model_validate(result)

    def validate_publication(self, **kwargs: Any) -> CommonsValidatePublicationOutput:
        payload = CommonsValidatePublicationInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("commons_validate_publication", payload)
        return CommonsValidatePublicationOutput.model_validate(result)


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


class EditorialNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create_reading_room(self, **kwargs: Any) -> CreateEditorialReadingRoomOutput:
        payload = CreateEditorialReadingRoomInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("create_editorial_reading_room", payload)
        return CreateEditorialReadingRoomOutput.model_validate(result)

    def reading_room_guide(self, **kwargs: Any) -> EditorialReadingRoomGuideOutput:
        payload = EditorialReadingRoomGuideInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("editorial_reading_room_guide", payload)
        return EditorialReadingRoomGuideOutput.model_validate(result)

    def renew_reading_room_download(self, **kwargs: Any) -> RenewEditorialReadingRoomDownloadOutput:
        payload = RenewEditorialReadingRoomDownloadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("renew_editorial_reading_room_download", payload)
        return RenewEditorialReadingRoomDownloadOutput.model_validate(result)


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


class BillingNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def credits_info(self, **kwargs: Any) -> CreditsInfoOutput:
        payload = CreditsInfoInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("credits_info", payload)
        return CreditsInfoOutput.model_validate(result)


class DirectoryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def run(self, **kwargs: Any) -> DirectoryWorkflowOutput:
        payload = DirectoryWorkflowInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("directory_workflow", payload)
        return DirectoryWorkflowOutput.model_validate(result)

    def workflow_status(self, **kwargs: Any) -> DirectoryWorkflowStatusOutput:
        payload = DirectoryWorkflowStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("directory_workflow_status", payload)
        return DirectoryWorkflowStatusOutput.model_validate(result)

    def get_local_sourcebook_contract(self, **kwargs: Any) -> GetLocalSourcebookContractOutput:
        payload = GetLocalSourcebookContractInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get-local-sourcebook-contract", payload)
        return GetLocalSourcebookContractOutput.model_validate(result)

    def list_local_sourcebook_tags(self, **kwargs: Any) -> ListLocalSourcebookTagsOutput:
        payload = ListLocalSourcebookTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-local-sourcebook-tags", payload)
        return ListLocalSourcebookTagsOutput.model_validate(result)

    def local_sourcebook_refresh(self, **kwargs: Any) -> LocalSourcebookRefreshOutput:
        payload = LocalSourcebookRefreshInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("local_sourcebook_refresh", payload)
        return LocalSourcebookRefreshOutput.model_validate(result)

    def local_sourcebook_submission_status(self, **kwargs: Any) -> LocalSourcebookSubmissionStatusOutput:
        payload = LocalSourcebookSubmissionStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("local_sourcebook_submission_status", payload)
        return LocalSourcebookSubmissionStatusOutput.model_validate(result)

    def local_sourcebook_capture(self, **kwargs: Any) -> LocalSourcebookCaptureOutput:
        payload = LocalSourcebookCaptureInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("local-sourcebook-capture", payload)
        return LocalSourcebookCaptureOutput.model_validate(result)

    def location_markets(self, **kwargs: Any) -> LocationMarketsOutput:
        payload = LocationMarketsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("location_markets", payload)
        return LocationMarketsOutput.model_validate(result)

    def prepare_local_sourcebook_write(self, **kwargs: Any) -> PrepareLocalSourcebookWriteOutput:
        payload = PrepareLocalSourcebookWriteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("prepare-local-sourcebook-write", payload)
        return PrepareLocalSourcebookWriteOutput.model_validate(result)

    def resolve_local_sourcebook_tags(self, **kwargs: Any) -> ResolveLocalSourcebookTagsOutput:
        payload = ResolveLocalSourcebookTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("resolve-local-sourcebook-tags", payload)
        return ResolveLocalSourcebookTagsOutput.model_validate(result)

    def validate_local_sourcebook_write(self, **kwargs: Any) -> ValidateLocalSourcebookWriteOutput:
        payload = ValidateLocalSourcebookWriteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("validate-local-sourcebook-write", payload)
        return ValidateLocalSourcebookWriteOutput.model_validate(result)


class FacebookNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def ad_search(self, **kwargs: Any) -> FacebookAdSearchOutput:
        payload = FacebookAdSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("facebook_ad_search", payload)
        return FacebookAdSearchOutput.model_validate(result)

    def ad_transcribe(self, **kwargs: Any) -> FacebookAdTranscribeOutput:
        payload = FacebookAdTranscribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("facebook_ad_transcribe", payload)
        return FacebookAdTranscribeOutput.model_validate(result)

    def page_intel(self, **kwargs: Any) -> FacebookPageIntelOutput:
        payload = FacebookPageIntelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("facebook_page_intel", payload)
        return FacebookPageIntelOutput.model_validate(result)

    def video_transcribe(self, **kwargs: Any) -> FacebookVideoTranscribeOutput:
        payload = FacebookVideoTranscribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("facebook_video_transcribe", payload)
        return FacebookVideoTranscribeOutput.model_validate(result)


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


class ReviewsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def g2_reviews(self, **kwargs: Any) -> G2ReviewsOutput:
        payload = G2ReviewsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("g2_reviews", payload)
        return G2ReviewsOutput.model_validate(result)

    def trustpilot_reviews(self, **kwargs: Any) -> TrustpilotReviewsOutput:
        payload = TrustpilotReviewsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("trustpilot_reviews", payload)
        return TrustpilotReviewsOutput.model_validate(result)


class ArtifactsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def get_artifact_template_example(self, **kwargs: Any) -> GetArtifactTemplateExampleOutput:
        payload = GetArtifactTemplateExampleInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get_artifact_template_example", payload)
        return GetArtifactTemplateExampleOutput.model_validate(result)

    def read(self, **kwargs: Any) -> ReportArtifactReadOutput:
        payload = ReportArtifactReadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("report_artifact_read", payload)
        return ReportArtifactReadOutput.model_validate(result)


class GoogleAdsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def page_intel(self, **kwargs: Any) -> GoogleAdsPageIntelOutput:
        payload = GoogleAdsPageIntelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("google_ads_page_intel", payload)
        return GoogleAdsPageIntelOutput.model_validate(result)

    def search(self, **kwargs: Any) -> GoogleAdsSearchOutput:
        payload = GoogleAdsSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("google_ads_search", payload)
        return GoogleAdsSearchOutput.model_validate(result)

    def transcribe(self, **kwargs: Any) -> GoogleAdsTranscribeOutput:
        payload = GoogleAdsTranscribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("google_ads_transcribe", payload)
        return GoogleAdsTranscribeOutput.model_validate(result)


class SearchNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def harvest_paa(self, **kwargs: Any) -> HarvestPaaOutput:
        payload = HarvestPaaInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("harvest_paa", payload)
        return HarvestPaaOutput.model_validate(result)

    def search_serp(self, **kwargs: Any) -> SearchSerpOutput:
        payload = SearchSerpInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("search_serp", payload)
        return SearchSerpOutput.model_validate(result)

    def serp_identity_create(self, **kwargs: Any) -> SerpIdentityCreateOutput:
        payload = SerpIdentityCreateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("serp_identity_create", payload)
        return SerpIdentityCreateOutput.model_validate(result)

    def serp_identity_delete(self, **kwargs: Any) -> SerpIdentityDeleteOutput:
        payload = SerpIdentityDeleteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("serp_identity_delete", payload)
        return SerpIdentityDeleteOutput.model_validate(result)

    def serp_identity_list(self, **kwargs: Any) -> SerpIdentityListOutput:
        payload = SerpIdentityListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("serp_identity_list", payload)
        return SerpIdentityListOutput.model_validate(result)


class OtherNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def harvest_paa_start(self, **kwargs: Any) -> HarvestPaaStartOutput:
        payload = HarvestPaaStartInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("harvest_paa_start", payload)
        return HarvestPaaStartOutput.model_validate(result)

    def harvest_paa_status(self, **kwargs: Any) -> HarvestPaaStatusOutput:
        payload = HarvestPaaStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("harvest_paa_status", payload)
        return HarvestPaaStatusOutput.model_validate(result)


class ImagesNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def asset_delete(self, **kwargs: Any) -> ImageAssetDeleteOutput:
        payload = ImageAssetDeleteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_asset_delete", payload)
        return ImageAssetDeleteOutput.model_validate(result)

    def asset_get(self, **kwargs: Any) -> ImageAssetGetOutput:
        payload = ImageAssetGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_asset_get", payload)
        return ImageAssetGetOutput.model_validate(result)

    def asset_list(self, **kwargs: Any) -> ImageAssetListOutput:
        payload = ImageAssetListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_asset_list", payload)
        return ImageAssetListOutput.model_validate(result)

    def asset_move(self, **kwargs: Any) -> ImageAssetMoveOutput:
        payload = ImageAssetMoveInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_asset_move", payload)
        return ImageAssetMoveOutput.model_validate(result)

    def asset_save(self, **kwargs: Any) -> ImageAssetSaveOutput:
        payload = ImageAssetSaveInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_asset_save", payload)
        return ImageAssetSaveOutput.model_validate(result)

    def asset_search(self, **kwargs: Any) -> ImageAssetSearchOutput:
        payload = ImageAssetSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_asset_search", payload)
        return ImageAssetSearchOutput.model_validate(result)

    def folder_create(self, **kwargs: Any) -> ImageFolderCreateOutput:
        payload = ImageFolderCreateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_folder_create", payload)
        return ImageFolderCreateOutput.model_validate(result)

    def folder_list(self, **kwargs: Any) -> ImageFolderListOutput:
        payload = ImageFolderListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_folder_list", payload)
        return ImageFolderListOutput.model_validate(result)

    def project_create(self, **kwargs: Any) -> ImageProjectCreateOutput:
        payload = ImageProjectCreateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_project_create", payload)
        return ImageProjectCreateOutput.model_validate(result)

    def project_list(self, **kwargs: Any) -> ImageProjectListOutput:
        payload = ImageProjectListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("image_project_list", payload)
        return ImageProjectListOutput.model_validate(result)


class InstagramNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def media_download(self, **kwargs: Any) -> InstagramMediaDownloadOutput:
        payload = InstagramMediaDownloadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("instagram_media_download", payload)
        return InstagramMediaDownloadOutput.model_validate(result)

    def profile_content(self, **kwargs: Any) -> InstagramProfileContentOutput:
        payload = InstagramProfileContentInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("instagram_profile_content", payload)
        return InstagramProfileContentOutput.model_validate(result)


class LeadsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def enrich(self, **kwargs: Any) -> LeadListEnrichOutput:
        payload = LeadListEnrichInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("lead_list_enrich", payload)
        return LeadListEnrichOutput.model_validate(result)

    def enrich_status(self, **kwargs: Any) -> LeadListEnrichStatusOutput:
        payload = LeadListEnrichStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("lead_list_enrich_status", payload)
        return LeadListEnrichStatusOutput.model_validate(result)

    def import_(self, **kwargs: Any) -> LeadListImportOutput:
        payload = LeadListImportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("lead_list_import", payload)
        return LeadListImportOutput.model_validate(result)

    def upload_start(self, **kwargs: Any) -> LeadListUploadStartOutput:
        payload = LeadListUploadStartInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("lead_list_upload_start", payload)
        return LeadListUploadStartOutput.model_validate(result)


class LibraryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def ingest(self, **kwargs: Any) -> LibraryIngestOutput:
        payload = LibraryIngestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("library-ingest", payload)
        return LibraryIngestOutput.model_validate(result)


class TagsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def list_memory_tags(self, **kwargs: Any) -> ListMemoryTagsOutput:
        payload = ListMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list-memory-tags", payload)
        return ListMemoryTagsOutput.model_validate(result)

    def merge_memory_tags(self, **kwargs: Any) -> MergeMemoryTagsOutput:
        payload = MergeMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("merge-memory-tags", payload)
        return MergeMemoryTagsOutput.model_validate(result)

    def resolve_memory_tags(self, **kwargs: Any) -> ResolveMemoryTagsOutput:
        payload = ResolveMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("resolve-memory-tags", payload)
        return ResolveMemoryTagsOutput.model_validate(result)

    def upsert_memory_tag(self, **kwargs: Any) -> UpsertMemoryTagOutput:
        payload = UpsertMemoryTagInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("upsert-memory-tag", payload)
        return UpsertMemoryTagOutput.model_validate(result)


class MapsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def place_intel(self, **kwargs: Any) -> MapsPlaceIntelOutput:
        payload = MapsPlaceIntelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("maps_place_intel", payload)
        return MapsPlaceIntelOutput.model_validate(result)

    def search(self, **kwargs: Any) -> MapsSearchOutput:
        payload = MapsSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("maps_search", payload)
        return MapsSearchOutput.model_validate(result)


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


class WorkflowsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def query_fanout(self, **kwargs: Any) -> QueryFanoutWorkflowOutput:
        payload = QueryFanoutWorkflowInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("query_fanout_workflow", payload)
        return QueryFanoutWorkflowOutput.model_validate(result)

    def rank_tracker(self, **kwargs: Any) -> RankTrackerWorkflowOutput:
        payload = RankTrackerWorkflowInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("rank_tracker_workflow", payload)
        return RankTrackerWorkflowOutput.model_validate(result)

    def artifact_read(self, **kwargs: Any) -> WorkflowArtifactReadOutput:
        payload = WorkflowArtifactReadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("workflow_artifact_read", payload)
        return WorkflowArtifactReadOutput.model_validate(result)

    def list(self, **kwargs: Any) -> WorkflowListOutput:
        payload = WorkflowListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("workflow_list", payload)
        return WorkflowListOutput.model_validate(result)

    def run(self, **kwargs: Any) -> WorkflowRunOutput:
        payload = WorkflowRunInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("workflow_run", payload)
        return WorkflowRunOutput.model_validate(result)

    def status(self, **kwargs: Any) -> WorkflowStatusOutput:
        payload = WorkflowStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("workflow_status", payload)
        return WorkflowStatusOutput.model_validate(result)

    def step(self, **kwargs: Any) -> WorkflowStepOutput:
        payload = WorkflowStepInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("workflow_step", payload)
        return WorkflowStepOutput.model_validate(result)

    def suggest(self, **kwargs: Any) -> WorkflowSuggestOutput:
        payload = WorkflowSuggestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("workflow_suggest", payload)
        return WorkflowSuggestOutput.model_validate(result)


class RedditNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def thread(self, **kwargs: Any) -> RedditThreadOutput:
        payload = RedditThreadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("reddit_thread", payload)
        return RedditThreadOutput.model_validate(result)

    def trending(self, **kwargs: Any) -> RedditTrendingOutput:
        payload = RedditTrendingInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("reddit_trending", payload)
        return RedditTrendingOutput.model_validate(result)


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


class RecallNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def temporal_recall(self, **kwargs: Any) -> TemporalRecallOutput:
        payload = TemporalRecallInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("temporal-recall", payload)
        return TemporalRecallOutput.model_validate(result)


class VideoNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def frame_analysis(self, **kwargs: Any) -> VideoFrameAnalysisOutput:
        payload = VideoFrameAnalysisInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("video_frame_analysis", payload)
        return VideoFrameAnalysisOutput.model_validate(result)

    def frame_analysis_status(self, **kwargs: Any) -> VideoFrameAnalysisStatusOutput:
        payload = VideoFrameAnalysisStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("video_frame_analysis_status", payload)
        return VideoFrameAnalysisStatusOutput.model_validate(result)

    def analyze_start(self, **kwargs: Any) -> VideoAnalyzeStartOutput:
        payload = VideoAnalyzeStartInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("video-analyze-start", payload)
        return VideoAnalyzeStartOutput.model_validate(result)

    def analyze_status(self, **kwargs: Any) -> VideoAnalyzeStatusOutput:
        payload = VideoAnalyzeStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("video-analyze-status", payload)
        return VideoAnalyzeStatusOutput.model_validate(result)


class YoutubeNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def harvest(self, **kwargs: Any) -> YoutubeHarvestOutput:
        payload = YoutubeHarvestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("youtube_harvest", payload)
        return YoutubeHarvestOutput.model_validate(result)

    def transcribe(self, **kwargs: Any) -> YoutubeTranscribeOutput:
        payload = YoutubeTranscribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("youtube_transcribe", payload)
        return YoutubeTranscribeOutput.model_validate(result)



class GeneratedMcpToolsClient:
    def __init__(self, call_tool):
        self.access = AccessNamespace(call_tool)
        self.vaults = VaultsNamespace(call_tool)
        self.analytics = AnalyticsNamespace(call_tool)
        self.web = WebNamespace(call_tool)
        self.schedule = ScheduleNamespace(call_tool)
        self.assistant = AssistantNamespace(call_tool)
        self.browser = BrowserNamespace(call_tool)
        self.memory = MemoryNamespace(call_tool)
        self.connections = ConnectionsNamespace(call_tool)
        self.serp_intelligence = SerpIntelligenceNamespace(call_tool)
        self.commons = CommonsNamespace(call_tool)
        self.storage = StorageNamespace(call_tool)
        self.editorial = EditorialNamespace(call_tool)
        self.channels = ChannelsNamespace(call_tool)
        self.webhooks = WebhooksNamespace(call_tool)
        self.billing = BillingNamespace(call_tool)
        self.directory = DirectoryNamespace(call_tool)
        self.facebook = FacebookNamespace(call_tool)
        self.facts = FactsNamespace(call_tool)
        self.reviews = ReviewsNamespace(call_tool)
        self.artifacts = ArtifactsNamespace(call_tool)
        self.google_ads = GoogleAdsNamespace(call_tool)
        self.search = SearchNamespace(call_tool)
        self.other = OtherNamespace(call_tool)
        self.images = ImagesNamespace(call_tool)
        self.instagram = InstagramNamespace(call_tool)
        self.leads = LeadsNamespace(call_tool)
        self.library = LibraryNamespace(call_tool)
        self.tags = TagsNamespace(call_tool)
        self.maps = MapsNamespace(call_tool)
        self.graph = GraphNamespace(call_tool)
        self.capture = CaptureNamespace(call_tool)
        self.workflows = WorkflowsNamespace(call_tool)
        self.reddit = RedditNamespace(call_tool)
        self.tables = TablesNamespace(call_tool)
        self.recall = RecallNamespace(call_tool)
        self.video = VideoNamespace(call_tool)
        self.youtube = YoutubeNamespace(call_tool)
