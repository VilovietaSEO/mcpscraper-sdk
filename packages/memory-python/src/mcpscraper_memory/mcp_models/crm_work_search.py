from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmWorkSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    entity_id: Union[str, None] = Field(None, alias='entityId', description='Optional stable CRM person or organization entity ID associated with the work record.')
    entity_ids: Union[Annotated[list[str], Field(min_length=1, max_length=10)], None] = Field(None, alias='entityIds', description='Optional stable CRM entity IDs that must all be associated with the work record.')
    work_id: Union[str, None] = Field(None, alias='workId', description='Optional exact canonical CRM activity, task, or deal work ID.')
    query: Union[Annotated[str, Field(min_length=1, max_length=300)], None] = Field(None, alias='query', description='Optional case-insensitive title search.')
    cursor: Union[Annotated[str, Field(min_length=1, max_length=2048)], None] = Field(None, alias='cursor', description='Opaque cursor returned by the previous crm-work-search page.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum work records to return before cursor pagination.')
    object_kind: Literal['activity', 'task', 'deal'] = Field(..., alias='objectKind', description='Search exactly one canonical CRM work kind.')
    task_statuses: Union[Annotated[list[Literal['todo', 'in_progress', 'blocked', 'done', 'cancelled']], Field(min_length=1, max_length=100)], None] = Field(None, alias='taskStatuses', description='Task-only statuses to include.')
    due_before: Union[str, None] = Field(None, alias='dueBefore', description='Task-only inclusive upper due-time bound.')
    due_after: Union[str, None] = Field(None, alias='dueAfter', description='Task-only inclusive lower due-time bound.')
    due_unscheduled: Union[bool, None] = Field(None, alias='dueUnscheduled', description='Task-only filter for records without a due date.')
    task_owner_id: Union[Annotated[str, Field(min_length=1, max_length=200)], None] = Field(None, alias='taskOwnerId', description='Task-only exact owner identifier.')
    deal_id: Union[str, None] = Field(None, alias='dealId', description='Task-only native CRM deal UUID.')
    pipeline_id: Union[str, None] = Field(None, alias='pipelineId', description='Deal-only native CRM pipeline UUID.')
    stage_ids: Union[Annotated[list[str], Field(min_length=1, max_length=100)], None] = Field(None, alias='stageIds', description='Deal-only native CRM stage UUIDs.')
    min_value: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(None, alias='minValue', description='Deal-only inclusive minimum value.')
    max_value: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(None, alias='maxValue', description='Deal-only inclusive maximum value.')


CrmWorkSearchOutputVariant1Variant1ItemsItemEntitiesItem = TypedDict('CrmWorkSearchOutputVariant1Variant1ItemsItemEntitiesItem', {
    'entityId': Required[str],
    'domain': Required[Literal['research_person', 'research_organization', 'crm_person', 'crm_organization']],
    'displayName': Required[str],
})
CrmWorkSearchOutputVariant1Variant1ItemsItemEntitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1Variant1ItemsItemDealStateVariant1 = TypedDict('CrmWorkSearchOutputVariant1Variant1ItemsItemDealStateVariant1', {
    'pipelineId': Required[str],
    'pipelineLabel': Required[str],
    'stageId': Required[str],
    'stageLabel': Required[str],
    'outcome': Required[Literal['open', 'won', 'lost']],
    'probability': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'fields': Required[dict[str, Any]],
})
CrmWorkSearchOutputVariant1Variant1ItemsItemDealStateVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1Variant1ItemsItem = TypedDict('CrmWorkSearchOutputVariant1Variant1ItemsItem', {
    'workId': Required[str],
    'objectKind': Required[Literal['activity', 'task', 'deal']],
    'noteId': Required[str],
    'vault': Required[Literal['Communication', 'Tasks', 'Deals']],
    'path': Required[str],
    'title': Required[str],
    'content': Required[str],
    'props': Required[dict[str, Any]],
    'entityIds': Required[list[str]],
    'entities': Required[list[CrmWorkSearchOutputVariant1Variant1ItemsItemEntitiesItem]],
    'revision': Required[Annotated[int, Field(ge=1)]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
    'dealState': Required[Union[CrmWorkSearchOutputVariant1Variant1ItemsItemDealStateVariant1, None]],
})
CrmWorkSearchOutputVariant1Variant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1Variant1PageInfo = TypedDict('CrmWorkSearchOutputVariant1Variant1PageInfo', {
    'endCursor': Required[Union[str, None]],
    'hasNextPage': Required[bool],
})
CrmWorkSearchOutputVariant1Variant1PageInfo.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmWorkSearchOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    items: Union[list[CrmWorkSearchOutputVariant1Variant1ItemsItem], None] = Field(None, alias='items', description='')
    page_info: Union[CrmWorkSearchOutputVariant1Variant1PageInfo, None] = Field(None, alias='pageInfo', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmWorkSearchOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('CrmWorkSearchOutputVariant1Variant2DeliveryArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Union[float, int]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'capabilities': Required[list[str]],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'downloadState': Required[Literal['available', 'local', 'unavailable']],
})
CrmWorkSearchOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('CrmWorkSearchOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmWorkSearchOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1Variant2Delivery = TypedDict('CrmWorkSearchOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmWorkSearchOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmWorkSearchOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmWorkSearchOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1Variant2RecoveryOperation = TypedDict('CrmWorkSearchOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmWorkSearchOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1Variant2Recovery = TypedDict('CrmWorkSearchOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmWorkSearchOutputVariant1Variant2RecoveryOperation],
})
CrmWorkSearchOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmWorkSearchOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmWorkSearchOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmWorkSearchOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


CrmWorkSearchOutputVariant1Variant3Operation = TypedDict('CrmWorkSearchOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmWorkSearchOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmWorkSearchOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmWorkSearchOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmWorkSearchOutputVariant1).
CrmWorkSearchOutputVariant1 = Union[CrmWorkSearchOutputVariant1Variant2, CrmWorkSearchOutputVariant1Variant3, CrmWorkSearchOutputVariant1Variant1]


CrmWorkSearchOutputVariant2DeliveryArtifactsItem = TypedDict('CrmWorkSearchOutputVariant2DeliveryArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Union[float, int]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'capabilities': Required[list[str]],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'downloadState': Required[Literal['available', 'local', 'unavailable']],
})
CrmWorkSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmWorkSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmWorkSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmWorkSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmWorkSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant2Delivery = TypedDict('CrmWorkSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmWorkSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmWorkSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmWorkSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmWorkSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant2RecoveryOperation = TypedDict('CrmWorkSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmWorkSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant2Recovery = TypedDict('CrmWorkSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmWorkSearchOutputVariant2RecoveryOperation],
})
CrmWorkSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmWorkSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmWorkSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmWorkSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmWorkSearchOutput).
CrmWorkSearchOutput = Union[CrmWorkSearchOutputVariant2, CrmWorkSearchOutputVariant1]

_CrmWorkSearchInputAdapter = TypeAdapter(CrmWorkSearchInput)
_CrmWorkSearchOutputAdapter = TypeAdapter(CrmWorkSearchOutput)