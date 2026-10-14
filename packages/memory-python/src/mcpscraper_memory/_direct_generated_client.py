from typing import Any, Callable
from ._artifact_delivery import ArtifactDelivery, validate_tool_output

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
from .direct_models.archive_artifact_template import ArchiveArtifactTemplateInput, ArchiveArtifactTemplateOutput
from .direct_models.artifact_describe import ArtifactDescribeInput, ArtifactDescribeOutput
from .direct_models.artifact_download import ArtifactDownloadInput, ArtifactDownloadOutput
from .direct_models.artifact_read import ArtifactReadInput, ArtifactReadOutput
from .direct_models.create_artifact_template import CreateArtifactTemplateInput, CreateArtifactTemplateOutput
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
from .direct_models.get_artifact_template import GetArtifactTemplateInput, GetArtifactTemplateOutput
from .direct_models.library_ingest import LibraryIngestInput, LibraryIngestOutput
from .direct_models.list_artifact_templates import ListArtifactTemplatesInput, ListArtifactTemplatesOutput
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
from .direct_models.update_artifact_template import UpdateArtifactTemplateInput, UpdateArtifactTemplateOutput
from .direct_models.video_analyze_start import VideoAnalyzeStartInput, VideoAnalyzeStartOutput
from .direct_models.video_analyze_status import VideoAnalyzeStatusInput, VideoAnalyzeStatusOutput


class AccessNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def accept_share(self, **kwargs: Any) -> AccessAcceptShareOutput | ArtifactDelivery:
        payload = AccessAcceptShareInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("acceptShareTool", payload)
        return validate_tool_output(result, AccessAcceptShareOutput)

    def approve_sender(self, **kwargs: Any) -> AccessApproveSenderOutput | ArtifactDelivery:
        payload = AccessApproveSenderInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("approveSenderTool", payload)
        return validate_tool_output(result, AccessApproveSenderOutput)

    def decline_share(self, **kwargs: Any) -> AccessDeclineShareOutput | ArtifactDelivery:
        payload = AccessDeclineShareInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("declineShareTool", payload)
        return validate_tool_output(result, AccessDeclineShareOutput)

    def inbox_settings(self, **kwargs: Any) -> AccessInboxSettingsOutput | ArtifactDelivery:
        payload = AccessInboxSettingsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("inboxSettingsTool", payload)
        return validate_tool_output(result, AccessInboxSettingsOutput)

    def invite_account(self, **kwargs: Any) -> AccessInviteAccountOutput | ArtifactDelivery:
        payload = AccessInviteAccountInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("inviteAccountTool", payload)
        return validate_tool_output(result, AccessInviteAccountOutput)

    def issue_key(self, **kwargs: Any) -> AccessIssueKeyOutput | ArtifactDelivery:
        payload = AccessIssueKeyInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("issueKeyTool", payload)
        return validate_tool_output(result, AccessIssueKeyOutput)

    def list_approved_senders(self, **kwargs: Any) -> AccessListApprovedSendersOutput | ArtifactDelivery:
        payload = AccessListApprovedSendersInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("listApprovedSendersTool", payload)
        return validate_tool_output(result, AccessListApprovedSendersOutput)

    def list_keys(self, **kwargs: Any) -> AccessListKeysOutput | ArtifactDelivery:
        payload = AccessListKeysInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("listKeysTool", payload)
        return validate_tool_output(result, AccessListKeysOutput)

    def note_inbox(self, **kwargs: Any) -> AccessNoteInboxOutput | ArtifactDelivery:
        payload = AccessNoteInboxInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("noteInboxTool", payload)
        return validate_tool_output(result, AccessNoteInboxOutput)

    def remove_approved_sender(self, **kwargs: Any) -> AccessRemoveApprovedSenderOutput | ArtifactDelivery:
        payload = AccessRemoveApprovedSenderInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("removeApprovedSenderTool", payload)
        return validate_tool_output(result, AccessRemoveApprovedSenderOutput)

    def revoke_key(self, **kwargs: Any) -> AccessRevokeKeyOutput | ArtifactDelivery:
        payload = AccessRevokeKeyInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("revokeKeyTool", payload)
        return validate_tool_output(result, AccessRevokeKeyOutput)

    def revoke_share(self, **kwargs: Any) -> AccessRevokeShareOutput | ArtifactDelivery:
        payload = AccessRevokeShareInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("revokeShareTool", payload)
        return validate_tool_output(result, AccessRevokeShareOutput)

    def set_scope(self, **kwargs: Any) -> AccessSetScopeOutput | ArtifactDelivery:
        payload = AccessSetScopeInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("setScopeTool", payload)
        return validate_tool_output(result, AccessSetScopeOutput)

    def share_note(self, **kwargs: Any) -> AccessShareNoteOutput | ArtifactDelivery:
        payload = AccessShareNoteInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("shareNoteTool", payload)
        return validate_tool_output(result, AccessShareNoteOutput)

    def share_vault(self, **kwargs: Any) -> AccessShareVaultOutput | ArtifactDelivery:
        payload = AccessShareVaultInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("shareVaultTool", payload)
        return validate_tool_output(result, AccessShareVaultOutput)

    def swap_vault(self, **kwargs: Any) -> AccessSwapVaultOutput | ArtifactDelivery:
        payload = AccessSwapVaultInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("swapVaultTool", payload)
        return validate_tool_output(result, AccessSwapVaultOutput)

    def switch_account(self, **kwargs: Any) -> AccessSwitchAccountOutput | ArtifactDelivery:
        payload = AccessSwitchAccountInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("switchAccountTool", payload)
        return validate_tool_output(result, AccessSwitchAccountOutput)

    def unlink_share(self, **kwargs: Any) -> AccessUnlinkShareOutput | ArtifactDelivery:
        payload = AccessUnlinkShareInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("unlinkShareTool", payload)
        return validate_tool_output(result, AccessUnlinkShareOutput)


class ArtifactsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def archive_artifact_template(self, **kwargs: Any) -> ArchiveArtifactTemplateOutput | ArtifactDelivery:
        payload = ArchiveArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("archive_artifact_template", payload)
        return validate_tool_output(result, ArchiveArtifactTemplateOutput)

    def describe(self, **kwargs: Any) -> ArtifactDescribeOutput | ArtifactDelivery:
        payload = ArtifactDescribeInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("artifact_describe", payload)
        return validate_tool_output(result, ArtifactDescribeOutput)

    def download(self, **kwargs: Any) -> ArtifactDownloadOutput | ArtifactDelivery:
        payload = ArtifactDownloadInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("artifact_download", payload)
        return validate_tool_output(result, ArtifactDownloadOutput)

    def read(self, **kwargs: Any) -> ArtifactReadOutput | ArtifactDelivery:
        payload = ArtifactReadInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("artifact_read", payload)
        return validate_tool_output(result, ArtifactReadOutput)

    def create_artifact_template(self, **kwargs: Any) -> CreateArtifactTemplateOutput | ArtifactDelivery:
        payload = CreateArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("create_artifact_template", payload)
        return validate_tool_output(result, CreateArtifactTemplateOutput)

    def get_artifact_template(self, **kwargs: Any) -> GetArtifactTemplateOutput | ArtifactDelivery:
        payload = GetArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("get_artifact_template", payload)
        return validate_tool_output(result, GetArtifactTemplateOutput)

    def list_artifact_templates(self, **kwargs: Any) -> ListArtifactTemplatesOutput | ArtifactDelivery:
        payload = ListArtifactTemplatesInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("list_artifact_templates", payload)
        return validate_tool_output(result, ListArtifactTemplatesOutput)

    def update_artifact_template(self, **kwargs: Any) -> UpdateArtifactTemplateOutput | ArtifactDelivery:
        payload = UpdateArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("update_artifact_template", payload)
        return validate_tool_output(result, UpdateArtifactTemplateOutput)


class CaptureNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class ChannelsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class CrmNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def activity_append(self, **kwargs: Any) -> CrmActivityAppendOutput | ArtifactDelivery:
        payload = CrmActivityAppendInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmAppendCommunicationTool", payload)
        return validate_tool_output(result, CrmActivityAppendOutput)

    def counterpart_apply(self, **kwargs: Any) -> CrmCounterpartApplyOutput | ArtifactDelivery:
        payload = CrmCounterpartApplyInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmCounterpartApplyTool", payload)
        return validate_tool_output(result, CrmCounterpartApplyOutput)

    def counterpart_preview(self, **kwargs: Any) -> CrmCounterpartPreviewOutput | ArtifactDelivery:
        payload = CrmCounterpartPreviewInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmCounterpartPreviewTool", payload)
        return validate_tool_output(result, CrmCounterpartPreviewOutput)

    def deal_transition(self, **kwargs: Any) -> CrmDealTransitionOutput | ArtifactDelivery:
        payload = CrmDealTransitionInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmDealTransitionTool", payload)
        return validate_tool_output(result, CrmDealTransitionOutput)

    def deal_upsert(self, **kwargs: Any) -> CrmDealUpsertOutput | ArtifactDelivery:
        payload = CrmDealUpsertInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmDealUpsertTool", payload)
        return validate_tool_output(result, CrmDealUpsertOutput)

    def duplicate_search(self, **kwargs: Any) -> CrmDuplicateSearchOutput | ArtifactDelivery:
        payload = CrmDuplicateSearchInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmDuplicateSearchTool", payload)
        return validate_tool_output(result, CrmDuplicateSearchOutput)

    def import_apply(self, **kwargs: Any) -> CrmImportApplyOutput | ArtifactDelivery:
        payload = CrmImportApplyInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmImportApplyTool", payload)
        return validate_tool_output(result, CrmImportApplyOutput)

    def import_preview(self, **kwargs: Any) -> CrmImportPreviewOutput | ArtifactDelivery:
        payload = CrmImportPreviewInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmImportPreviewTool", payload)
        return validate_tool_output(result, CrmImportPreviewOutput)

    def merge_apply(self, **kwargs: Any) -> CrmMergeApplyOutput | ArtifactDelivery:
        payload = CrmMergeApplyInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmMergeApplyTool", payload)
        return validate_tool_output(result, CrmMergeApplyOutput)

    def merge_preview(self, **kwargs: Any) -> CrmMergePreviewOutput | ArtifactDelivery:
        payload = CrmMergePreviewInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmMergePreviewTool", payload)
        return validate_tool_output(result, CrmMergePreviewOutput)

    def organization_get(self, **kwargs: Any) -> CrmOrganizationGetOutput | ArtifactDelivery:
        payload = CrmOrganizationGetInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmOrganizationGetTool", payload)
        return validate_tool_output(result, CrmOrganizationGetOutput)

    def organization_search(self, **kwargs: Any) -> CrmOrganizationSearchOutput | ArtifactDelivery:
        payload = CrmOrganizationSearchInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmOrganizationSearchTool", payload)
        return validate_tool_output(result, CrmOrganizationSearchOutput)

    def person_get(self, **kwargs: Any) -> CrmPersonGetOutput | ArtifactDelivery:
        payload = CrmPersonGetInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmPersonGetTool", payload)
        return validate_tool_output(result, CrmPersonGetOutput)

    def person_search(self, **kwargs: Any) -> CrmPersonSearchOutput | ArtifactDelivery:
        payload = CrmPersonSearchInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmPersonSearchTool", payload)
        return validate_tool_output(result, CrmPersonSearchOutput)

    def pipeline_list(self, **kwargs: Any) -> CrmPipelineListOutput | ArtifactDelivery:
        payload = CrmPipelineListInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmPipelineListTool", payload)
        return validate_tool_output(result, CrmPipelineListOutput)

    def pipeline_upsert(self, **kwargs: Any) -> CrmPipelineUpsertOutput | ArtifactDelivery:
        payload = CrmPipelineUpsertInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmPipelineUpsertTool", payload)
        return validate_tool_output(result, CrmPipelineUpsertOutput)

    def quality_list(self, **kwargs: Any) -> CrmQualityListOutput | ArtifactDelivery:
        payload = CrmQualityListInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmQualityListTool", payload)
        return validate_tool_output(result, CrmQualityListOutput)

    def organization_upsert(self, **kwargs: Any) -> CrmOrganizationUpsertOutput | ArtifactDelivery:
        payload = CrmOrganizationUpsertInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmUpsertOrganizationTool", payload)
        return validate_tool_output(result, CrmOrganizationUpsertOutput)

    def person_upsert(self, **kwargs: Any) -> CrmPersonUpsertOutput | ArtifactDelivery:
        payload = CrmPersonUpsertInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmUpsertPersonTool", payload)
        return validate_tool_output(result, CrmPersonUpsertOutput)

    def task_upsert(self, **kwargs: Any) -> CrmTaskUpsertOutput | ArtifactDelivery:
        payload = CrmTaskUpsertInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmUpsertTaskTool", payload)
        return validate_tool_output(result, CrmTaskUpsertOutput)

    def work_search(self, **kwargs: Any) -> CrmWorkSearchOutput | ArtifactDelivery:
        payload = CrmWorkSearchInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("crmWorkSearchTool", payload)
        return validate_tool_output(result, CrmWorkSearchOutput)


class FactsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class FilesNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class GraphNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class ImagesNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class LibraryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def ingest(self, **kwargs: Any) -> LibraryIngestOutput | ArtifactDelivery:
        payload = LibraryIngestInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("libraryIngestTool", payload)
        return validate_tool_output(result, LibraryIngestOutput)


class MemoryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def export(self, **kwargs: Any) -> MemoryExportOutput | ArtifactDelivery:
        payload = MemoryExportInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("exportTool", payload)
        return validate_tool_output(result, MemoryExportOutput)

    def get(self, **kwargs: Any) -> MemoryGetOutput | ArtifactDelivery:
        payload = MemoryGetInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("getTool", payload)
        return validate_tool_output(result, MemoryGetOutput)

    def graph_path(self, **kwargs: Any) -> MemoryGraphPathOutput | ArtifactDelivery:
        payload = MemoryGraphPathInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("graphPathTool", payload)
        return validate_tool_output(result, MemoryGraphPathOutput)

    def graph_universe(self, **kwargs: Any) -> MemoryGraphUniverseOutput | ArtifactDelivery:
        payload = MemoryGraphUniverseInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("graphUniverseTool", payload)
        return validate_tool_output(result, MemoryGraphUniverseOutput)

    def list(self, **kwargs: Any) -> MemoryListOutput | ArtifactDelivery:
        payload = MemoryListInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("listTool", payload)
        return validate_tool_output(result, MemoryListOutput)

    def capture(self, **kwargs: Any) -> MemoryCaptureOutput | ArtifactDelivery:
        payload = MemoryCaptureInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("memoryCaptureTool", payload)
        return validate_tool_output(result, MemoryCaptureOutput)

    def questions(self, **kwargs: Any) -> MemoryQuestionsOutput | ArtifactDelivery:
        payload = MemoryQuestionsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("memoryQuestionsTool", payload)
        return validate_tool_output(result, MemoryQuestionsOutput)

    def backlinks(self, **kwargs: Any) -> MemoryBacklinksOutput | ArtifactDelivery:
        payload = MemoryBacklinksInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("noteBacklinksTool", payload)
        return validate_tool_output(result, MemoryBacklinksOutput)

    def put(self, **kwargs: Any) -> MemoryPutOutput | ArtifactDelivery:
        payload = MemoryPutInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("putTool", payload)
        return validate_tool_output(result, MemoryPutOutput)

    def search(self, **kwargs: Any) -> MemorySearchOutput | ArtifactDelivery:
        payload = MemorySearchInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("searchTool", payload)
        return validate_tool_output(result, MemorySearchOutput)

    def suggest(self, **kwargs: Any) -> MemorySuggestOutput | ArtifactDelivery:
        payload = MemorySuggestInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("suggestTool", payload)
        return validate_tool_output(result, MemorySuggestOutput)

    def upload(self, **kwargs: Any) -> MemoryUploadOutput | ArtifactDelivery:
        payload = MemoryUploadInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("uploadTool", payload)
        return validate_tool_output(result, MemoryUploadOutput)


class RecallNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class ResearchNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def organization_capture(self, **kwargs: Any) -> ResearchOrganizationCaptureOutput | ArtifactDelivery:
        payload = ResearchOrganizationCaptureInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("researchOrganizationCaptureTool", payload)
        return validate_tool_output(result, ResearchOrganizationCaptureOutput)

    def organization_get(self, **kwargs: Any) -> ResearchOrganizationGetOutput | ArtifactDelivery:
        payload = ResearchOrganizationGetInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("researchOrganizationGetTool", payload)
        return validate_tool_output(result, ResearchOrganizationGetOutput)

    def organization_search(self, **kwargs: Any) -> ResearchOrganizationSearchOutput | ArtifactDelivery:
        payload = ResearchOrganizationSearchInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("researchOrganizationSearchTool", payload)
        return validate_tool_output(result, ResearchOrganizationSearchOutput)

    def person_capture(self, **kwargs: Any) -> ResearchPersonCaptureOutput | ArtifactDelivery:
        payload = ResearchPersonCaptureInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("researchPersonCaptureTool", payload)
        return validate_tool_output(result, ResearchPersonCaptureOutput)

    def person_get(self, **kwargs: Any) -> ResearchPersonGetOutput | ArtifactDelivery:
        payload = ResearchPersonGetInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("researchPersonGetTool", payload)
        return validate_tool_output(result, ResearchPersonGetOutput)

    def person_search(self, **kwargs: Any) -> ResearchPersonSearchOutput | ArtifactDelivery:
        payload = ResearchPersonSearchInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("researchPersonSearchTool", payload)
        return validate_tool_output(result, ResearchPersonSearchOutput)


class StorageNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def usage(self, **kwargs: Any) -> StorageUsageOutput | ArtifactDelivery:
        payload = StorageUsageInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("storageUsageTool", payload)
        return validate_tool_output(result, StorageUsageOutput)


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

    def analyze_start(self, **kwargs: Any) -> VideoAnalyzeStartOutput | ArtifactDelivery:
        payload = VideoAnalyzeStartInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("videoAnalyzeStartTool", payload)
        return validate_tool_output(result, VideoAnalyzeStartOutput)

    def analyze_status(self, **kwargs: Any) -> VideoAnalyzeStatusOutput | ArtifactDelivery:
        payload = VideoAnalyzeStatusInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool("videoAnalyzeStatusTool", payload)
        return validate_tool_output(result, VideoAnalyzeStatusOutput)


class WebhooksNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool
