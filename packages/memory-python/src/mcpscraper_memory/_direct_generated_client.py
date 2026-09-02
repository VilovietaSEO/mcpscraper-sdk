from typing import Any, Callable

from .direct_models.access_accept_share import AccessAcceptShareInput, AccessAcceptShareOutput
from .direct_models.access_approve_sender import AccessApproveSenderInput, AccessApproveSenderOutput
from .direct_models.access_decline_share import AccessDeclineShareInput, AccessDeclineShareOutput
from .direct_models.access_inbox_settings import AccessInboxSettingsInput, AccessInboxSettingsOutput
from .direct_models.access_invite_account import AccessInviteAccountInput, AccessInviteAccountOutput
from .direct_models.access_issue_key import AccessIssueKeyInput, AccessIssueKeyOutput
from .direct_models.access_list_approved_senders import AccessListApprovedSendersInput, AccessListApprovedSendersOutput
from .direct_models.access_list_keys import AccessListKeysInput, AccessListKeysOutput
from .direct_models.access_note_inbox import AccessNoteInboxInput, AccessNoteInboxOutput
from .direct_models.access_remove_approved_sender import AccessRemoveApprovedSenderInput, AccessRemoveApprovedSenderOutput
from .direct_models.access_revoke_key import AccessRevokeKeyInput, AccessRevokeKeyOutput
from .direct_models.access_revoke_share import AccessRevokeShareInput, AccessRevokeShareOutput
from .direct_models.access_set_scope import AccessSetScopeInput, AccessSetScopeOutput
from .direct_models.access_share_note import AccessShareNoteInput, AccessShareNoteOutput
from .direct_models.access_share_vault import AccessShareVaultInput, AccessShareVaultOutput
from .direct_models.access_swap_vault import AccessSwapVaultInput, AccessSwapVaultOutput
from .direct_models.access_switch_account import AccessSwitchAccountInput, AccessSwitchAccountOutput
from .direct_models.access_unlink_share import AccessUnlinkShareInput, AccessUnlinkShareOutput
from .direct_models.assistant_context_packet_create import AssistantContextPacketCreateInput, AssistantContextPacketCreateOutput
from .direct_models.assistant_context_packet_get import AssistantContextPacketGetInput, AssistantContextPacketGetOutput
from .direct_models.assistant_context_packet_lifecycle import AssistantContextPacketLifecycleInput, AssistantContextPacketLifecycleOutput
from .direct_models.assistant_context_packet_list import AssistantContextPacketListInput, AssistantContextPacketListOutput
from .direct_models.assistant_context_packet_share_accept import AssistantContextPacketShareAcceptInput, AssistantContextPacketShareAcceptOutput
from .direct_models.crm_activity_append import CrmActivityAppendInput, CrmActivityAppendOutput
from .direct_models.crm_counterpart_apply import CrmCounterpartApplyInput, CrmCounterpartApplyOutput
from .direct_models.crm_counterpart_preview import CrmCounterpartPreviewInput, CrmCounterpartPreviewOutput
from .direct_models.crm_deal_transition import CrmDealTransitionInput, CrmDealTransitionOutput
from .direct_models.crm_deal_upsert import CrmDealUpsertInput, CrmDealUpsertOutput
from .direct_models.crm_duplicate_search import CrmDuplicateSearchInput, CrmDuplicateSearchOutput
from .direct_models.crm_import_apply import CrmImportApplyInput, CrmImportApplyOutput
from .direct_models.crm_import_preview import CrmImportPreviewInput, CrmImportPreviewOutput
from .direct_models.crm_merge_apply import CrmMergeApplyInput, CrmMergeApplyOutput
from .direct_models.crm_merge_preview import CrmMergePreviewInput, CrmMergePreviewOutput
from .direct_models.crm_organization_get import CrmOrganizationGetInput, CrmOrganizationGetOutput
from .direct_models.crm_organization_search import CrmOrganizationSearchInput, CrmOrganizationSearchOutput
from .direct_models.crm_organization_upsert import CrmOrganizationUpsertInput, CrmOrganizationUpsertOutput
from .direct_models.crm_person_get import CrmPersonGetInput, CrmPersonGetOutput
from .direct_models.crm_person_search import CrmPersonSearchInput, CrmPersonSearchOutput
from .direct_models.crm_person_upsert import CrmPersonUpsertInput, CrmPersonUpsertOutput
from .direct_models.crm_pipeline_list import CrmPipelineListInput, CrmPipelineListOutput
from .direct_models.crm_pipeline_upsert import CrmPipelineUpsertInput, CrmPipelineUpsertOutput
from .direct_models.crm_quality_list import CrmQualityListInput, CrmQualityListOutput
from .direct_models.crm_task_upsert import CrmTaskUpsertInput, CrmTaskUpsertOutput
from .direct_models.crm_work_search import CrmWorkSearchInput, CrmWorkSearchOutput
from .direct_models.library_ingest import LibraryIngestInput, LibraryIngestOutput
from .direct_models.memory_backlinks import MemoryBacklinksInput, MemoryBacklinksOutput
from .direct_models.memory_capture import MemoryCaptureInput, MemoryCaptureOutput
from .direct_models.memory_export import MemoryExportInput, MemoryExportOutput
from .direct_models.memory_get import MemoryGetInput, MemoryGetOutput
from .direct_models.memory_graph_path import MemoryGraphPathInput, MemoryGraphPathOutput
from .direct_models.memory_graph_universe import MemoryGraphUniverseInput, MemoryGraphUniverseOutput
from .direct_models.memory_list import MemoryListInput, MemoryListOutput
from .direct_models.memory_put import MemoryPutInput, MemoryPutOutput
from .direct_models.memory_questions import MemoryQuestionsInput, MemoryQuestionsOutput
from .direct_models.memory_search import MemorySearchInput, MemorySearchOutput
from .direct_models.memory_suggest import MemorySuggestInput, MemorySuggestOutput
from .direct_models.memory_upload import MemoryUploadInput, MemoryUploadOutput
from .direct_models.research_organization_capture import ResearchOrganizationCaptureInput, ResearchOrganizationCaptureOutput
from .direct_models.research_organization_get import ResearchOrganizationGetInput, ResearchOrganizationGetOutput
from .direct_models.research_organization_search import ResearchOrganizationSearchInput, ResearchOrganizationSearchOutput
from .direct_models.research_person_capture import ResearchPersonCaptureInput, ResearchPersonCaptureOutput
from .direct_models.research_person_get import ResearchPersonGetInput, ResearchPersonGetOutput
from .direct_models.research_person_search import ResearchPersonSearchInput, ResearchPersonSearchOutput
from .direct_models.storage_usage import StorageUsageInput, StorageUsageOutput
from .direct_models.video_analyze_start import VideoAnalyzeStartInput, VideoAnalyzeStartOutput
from .direct_models.video_analyze_status import VideoAnalyzeStatusInput, VideoAnalyzeStatusOutput


class AccessNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def accept_share(self, **kwargs: Any) -> AccessAcceptShareOutput:
        payload = AccessAcceptShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("acceptShareTool", payload)
        return AccessAcceptShareOutput.model_validate(result)

    def approve_sender(self, **kwargs: Any) -> AccessApproveSenderOutput:
        payload = AccessApproveSenderInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("approveSenderTool", payload)
        return AccessApproveSenderOutput.model_validate(result)

    def decline_share(self, **kwargs: Any) -> AccessDeclineShareOutput:
        payload = AccessDeclineShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("declineShareTool", payload)
        return AccessDeclineShareOutput.model_validate(result)

    def inbox_settings(self, **kwargs: Any) -> AccessInboxSettingsOutput:
        payload = AccessInboxSettingsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("inboxSettingsTool", payload)
        return AccessInboxSettingsOutput.model_validate(result)

    def invite_account(self, **kwargs: Any) -> AccessInviteAccountOutput:
        payload = AccessInviteAccountInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("inviteAccountTool", payload)
        return AccessInviteAccountOutput.model_validate(result)

    def issue_key(self, **kwargs: Any) -> AccessIssueKeyOutput:
        payload = AccessIssueKeyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("issueKeyTool", payload)
        return AccessIssueKeyOutput.model_validate(result)

    def list_approved_senders(self, **kwargs: Any) -> AccessListApprovedSendersOutput:
        payload = AccessListApprovedSendersInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listApprovedSendersTool", payload)
        return AccessListApprovedSendersOutput.model_validate(result)

    def list_keys(self, **kwargs: Any) -> AccessListKeysOutput:
        payload = AccessListKeysInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listKeysTool", payload)
        return AccessListKeysOutput.model_validate(result)

    def note_inbox(self, **kwargs: Any) -> AccessNoteInboxOutput:
        payload = AccessNoteInboxInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("noteInboxTool", payload)
        return AccessNoteInboxOutput.model_validate(result)

    def remove_approved_sender(self, **kwargs: Any) -> AccessRemoveApprovedSenderOutput:
        payload = AccessRemoveApprovedSenderInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("removeApprovedSenderTool", payload)
        return AccessRemoveApprovedSenderOutput.model_validate(result)

    def revoke_key(self, **kwargs: Any) -> AccessRevokeKeyOutput:
        payload = AccessRevokeKeyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeKeyTool", payload)
        return AccessRevokeKeyOutput.model_validate(result)

    def revoke_share(self, **kwargs: Any) -> AccessRevokeShareOutput:
        payload = AccessRevokeShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeShareTool", payload)
        return AccessRevokeShareOutput.model_validate(result)

    def set_scope(self, **kwargs: Any) -> AccessSetScopeOutput:
        payload = AccessSetScopeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("setScopeTool", payload)
        return AccessSetScopeOutput.model_validate(result)

    def share_note(self, **kwargs: Any) -> AccessShareNoteOutput:
        payload = AccessShareNoteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("shareNoteTool", payload)
        return AccessShareNoteOutput.model_validate(result)

    def share_vault(self, **kwargs: Any) -> AccessShareVaultOutput:
        payload = AccessShareVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("shareVaultTool", payload)
        return AccessShareVaultOutput.model_validate(result)

    def swap_vault(self, **kwargs: Any) -> AccessSwapVaultOutput:
        payload = AccessSwapVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("swapVaultTool", payload)
        return AccessSwapVaultOutput.model_validate(result)

    def switch_account(self, **kwargs: Any) -> AccessSwitchAccountOutput:
        payload = AccessSwitchAccountInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("switchAccountTool", payload)
        return AccessSwitchAccountOutput.model_validate(result)

    def unlink_share(self, **kwargs: Any) -> AccessUnlinkShareOutput:
        payload = AccessUnlinkShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("unlinkShareTool", payload)
        return AccessUnlinkShareOutput.model_validate(result)


class AssistantNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def context_packet_create(self, **kwargs: Any) -> AssistantContextPacketCreateOutput:
        payload = AssistantContextPacketCreateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_create", payload)
        return AssistantContextPacketCreateOutput.model_validate(result)

    def context_packet_get(self, **kwargs: Any) -> AssistantContextPacketGetOutput:
        payload = AssistantContextPacketGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_get", payload)
        return AssistantContextPacketGetOutput.model_validate(result)

    def context_packet_lifecycle(self, **kwargs: Any) -> AssistantContextPacketLifecycleOutput:
        payload = AssistantContextPacketLifecycleInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_lifecycle", payload)
        return AssistantContextPacketLifecycleOutput.model_validate(result)

    def context_packet_list(self, **kwargs: Any) -> AssistantContextPacketListOutput:
        payload = AssistantContextPacketListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_list", payload)
        return AssistantContextPacketListOutput.model_validate(result)

    def context_packet_share_accept(self, **kwargs: Any) -> AssistantContextPacketShareAcceptOutput:
        payload = AssistantContextPacketShareAcceptInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_share_accept", payload)
        return AssistantContextPacketShareAcceptOutput.model_validate(result)


class CaptureNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class ChannelsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class CrmNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def activity_append(self, **kwargs: Any) -> CrmActivityAppendOutput:
        payload = CrmActivityAppendInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmAppendCommunicationTool", payload)
        return CrmActivityAppendOutput.model_validate(result)

    def counterpart_apply(self, **kwargs: Any) -> CrmCounterpartApplyOutput:
        payload = CrmCounterpartApplyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmCounterpartApplyTool", payload)
        return CrmCounterpartApplyOutput.model_validate(result)

    def counterpart_preview(self, **kwargs: Any) -> CrmCounterpartPreviewOutput:
        payload = CrmCounterpartPreviewInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmCounterpartPreviewTool", payload)
        return CrmCounterpartPreviewOutput.model_validate(result)

    def deal_transition(self, **kwargs: Any) -> CrmDealTransitionOutput:
        payload = CrmDealTransitionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmDealTransitionTool", payload)
        return CrmDealTransitionOutput.model_validate(result)

    def deal_upsert(self, **kwargs: Any) -> CrmDealUpsertOutput:
        payload = CrmDealUpsertInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmDealUpsertTool", payload)
        return CrmDealUpsertOutput.model_validate(result)

    def duplicate_search(self, **kwargs: Any) -> CrmDuplicateSearchOutput:
        payload = CrmDuplicateSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmDuplicateSearchTool", payload)
        return CrmDuplicateSearchOutput.model_validate(result)

    def import_apply(self, **kwargs: Any) -> CrmImportApplyOutput:
        payload = CrmImportApplyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmImportApplyTool", payload)
        return CrmImportApplyOutput.model_validate(result)

    def import_preview(self, **kwargs: Any) -> CrmImportPreviewOutput:
        payload = CrmImportPreviewInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmImportPreviewTool", payload)
        return CrmImportPreviewOutput.model_validate(result)

    def merge_apply(self, **kwargs: Any) -> CrmMergeApplyOutput:
        payload = CrmMergeApplyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmMergeApplyTool", payload)
        return CrmMergeApplyOutput.model_validate(result)

    def merge_preview(self, **kwargs: Any) -> CrmMergePreviewOutput:
        payload = CrmMergePreviewInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmMergePreviewTool", payload)
        return CrmMergePreviewOutput.model_validate(result)

    def organization_get(self, **kwargs: Any) -> CrmOrganizationGetOutput:
        payload = CrmOrganizationGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmOrganizationGetTool", payload)
        return CrmOrganizationGetOutput.model_validate(result)

    def organization_search(self, **kwargs: Any) -> CrmOrganizationSearchOutput:
        payload = CrmOrganizationSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmOrganizationSearchTool", payload)
        return CrmOrganizationSearchOutput.model_validate(result)

    def person_get(self, **kwargs: Any) -> CrmPersonGetOutput:
        payload = CrmPersonGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmPersonGetTool", payload)
        return CrmPersonGetOutput.model_validate(result)

    def person_search(self, **kwargs: Any) -> CrmPersonSearchOutput:
        payload = CrmPersonSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmPersonSearchTool", payload)
        return CrmPersonSearchOutput.model_validate(result)

    def pipeline_list(self, **kwargs: Any) -> CrmPipelineListOutput:
        payload = CrmPipelineListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmPipelineListTool", payload)
        return CrmPipelineListOutput.model_validate(result)

    def pipeline_upsert(self, **kwargs: Any) -> CrmPipelineUpsertOutput:
        payload = CrmPipelineUpsertInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmPipelineUpsertTool", payload)
        return CrmPipelineUpsertOutput.model_validate(result)

    def quality_list(self, **kwargs: Any) -> CrmQualityListOutput:
        payload = CrmQualityListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmQualityListTool", payload)
        return CrmQualityListOutput.model_validate(result)

    def organization_upsert(self, **kwargs: Any) -> CrmOrganizationUpsertOutput:
        payload = CrmOrganizationUpsertInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmUpsertOrganizationTool", payload)
        return CrmOrganizationUpsertOutput.model_validate(result)

    def person_upsert(self, **kwargs: Any) -> CrmPersonUpsertOutput:
        payload = CrmPersonUpsertInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmUpsertPersonTool", payload)
        return CrmPersonUpsertOutput.model_validate(result)

    def task_upsert(self, **kwargs: Any) -> CrmTaskUpsertOutput:
        payload = CrmTaskUpsertInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmUpsertTaskTool", payload)
        return CrmTaskUpsertOutput.model_validate(result)

    def work_search(self, **kwargs: Any) -> CrmWorkSearchOutput:
        payload = CrmWorkSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("crmWorkSearchTool", payload)
        return CrmWorkSearchOutput.model_validate(result)


class FactsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class GraphNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class LibraryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def ingest(self, **kwargs: Any) -> LibraryIngestOutput:
        payload = LibraryIngestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("libraryIngestTool", payload)
        return LibraryIngestOutput.model_validate(result)


class MemoryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def export(self, **kwargs: Any) -> MemoryExportOutput:
        payload = MemoryExportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("exportTool", payload)
        return MemoryExportOutput.model_validate(result)

    def get(self, **kwargs: Any) -> MemoryGetOutput:
        payload = MemoryGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getTool", payload)
        return MemoryGetOutput.model_validate(result)

    def graph_path(self, **kwargs: Any) -> MemoryGraphPathOutput:
        payload = MemoryGraphPathInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("graphPathTool", payload)
        return MemoryGraphPathOutput.model_validate(result)

    def graph_universe(self, **kwargs: Any) -> MemoryGraphUniverseOutput:
        payload = MemoryGraphUniverseInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("graphUniverseTool", payload)
        return MemoryGraphUniverseOutput.model_validate(result)

    def list(self, **kwargs: Any) -> MemoryListOutput:
        payload = MemoryListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listTool", payload)
        return MemoryListOutput.model_validate(result)

    def capture(self, **kwargs: Any) -> MemoryCaptureOutput:
        payload = MemoryCaptureInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memoryCaptureTool", payload)
        return MemoryCaptureOutput.model_validate(result)

    def questions(self, **kwargs: Any) -> MemoryQuestionsOutput:
        payload = MemoryQuestionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memoryQuestionsTool", payload)
        return MemoryQuestionsOutput.model_validate(result)

    def backlinks(self, **kwargs: Any) -> MemoryBacklinksOutput:
        payload = MemoryBacklinksInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("noteBacklinksTool", payload)
        return MemoryBacklinksOutput.model_validate(result)

    def put(self, **kwargs: Any) -> MemoryPutOutput:
        payload = MemoryPutInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("putTool", payload)
        return MemoryPutOutput.model_validate(result)

    def search(self, **kwargs: Any) -> MemorySearchOutput:
        payload = MemorySearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("searchTool", payload)
        return MemorySearchOutput.model_validate(result)

    def suggest(self, **kwargs: Any) -> MemorySuggestOutput:
        payload = MemorySuggestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("suggestTool", payload)
        return MemorySuggestOutput.model_validate(result)

    def upload(self, **kwargs: Any) -> MemoryUploadOutput:
        payload = MemoryUploadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("uploadTool", payload)
        return MemoryUploadOutput.model_validate(result)


class RecallNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class ResearchNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def organization_capture(self, **kwargs: Any) -> ResearchOrganizationCaptureOutput:
        payload = ResearchOrganizationCaptureInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("researchOrganizationCaptureTool", payload)
        return ResearchOrganizationCaptureOutput.model_validate(result)

    def organization_get(self, **kwargs: Any) -> ResearchOrganizationGetOutput:
        payload = ResearchOrganizationGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("researchOrganizationGetTool", payload)
        return ResearchOrganizationGetOutput.model_validate(result)

    def organization_search(self, **kwargs: Any) -> ResearchOrganizationSearchOutput:
        payload = ResearchOrganizationSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("researchOrganizationSearchTool", payload)
        return ResearchOrganizationSearchOutput.model_validate(result)

    def person_capture(self, **kwargs: Any) -> ResearchPersonCaptureOutput:
        payload = ResearchPersonCaptureInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("researchPersonCaptureTool", payload)
        return ResearchPersonCaptureOutput.model_validate(result)

    def person_get(self, **kwargs: Any) -> ResearchPersonGetOutput:
        payload = ResearchPersonGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("researchPersonGetTool", payload)
        return ResearchPersonGetOutput.model_validate(result)

    def person_search(self, **kwargs: Any) -> ResearchPersonSearchOutput:
        payload = ResearchPersonSearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("researchPersonSearchTool", payload)
        return ResearchPersonSearchOutput.model_validate(result)


class ScheduleNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class StorageNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def usage(self, **kwargs: Any) -> StorageUsageOutput:
        payload = StorageUsageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("storageUsageTool", payload)
        return StorageUsageOutput.model_validate(result)


class TablesNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class TagsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class VaultsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class VideoNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def analyze_start(self, **kwargs: Any) -> VideoAnalyzeStartOutput:
        payload = VideoAnalyzeStartInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("videoAnalyzeStartTool", payload)
        return VideoAnalyzeStartOutput.model_validate(result)

    def analyze_status(self, **kwargs: Any) -> VideoAnalyzeStatusOutput:
        payload = VideoAnalyzeStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("videoAnalyzeStatusTool", payload)
        return VideoAnalyzeStatusOutput.model_validate(result)


class WebhooksNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool
