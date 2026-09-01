from typing import Any, Callable

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
from .direct_models.research_organization_capture import ResearchOrganizationCaptureInput, ResearchOrganizationCaptureOutput
from .direct_models.research_organization_get import ResearchOrganizationGetInput, ResearchOrganizationGetOutput
from .direct_models.research_organization_search import ResearchOrganizationSearchInput, ResearchOrganizationSearchOutput
from .direct_models.research_person_capture import ResearchPersonCaptureInput, ResearchPersonCaptureOutput
from .direct_models.research_person_get import ResearchPersonGetInput, ResearchPersonGetOutput
from .direct_models.research_person_search import ResearchPersonSearchInput, ResearchPersonSearchOutput


class AccessNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



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



class MemoryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



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



class WebhooksNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool
