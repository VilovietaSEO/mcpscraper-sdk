from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmWorkSearchInputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    api_key: Union[str, None] = Field(None, alias='apiKey', description='Caller API key. Omit when the MCP transport already authenticated this request.')
    session_id: Union[str, None] = Field(None, alias='sessionId', description='Optional MCP session identifier used for active account context.')
    entity_id: Union[str, None] = Field(None, alias='entityId', description='Optional stable CRM person or organization entity ID associated with the work record.')
    entity_ids: Union[Annotated[list[str], Field(min_length=1, max_length=10)], None] = Field(None, alias='entityIds', description='Optional stable CRM entity IDs that must all be associated with the work record.')
    work_id: Union[str, None] = Field(None, alias='workId', description='Optional exact canonical CRM activity, task, or deal work ID.')
    query: Union[Annotated[str, Field(min_length=1, max_length=300)], None] = Field(None, alias='query', description='Optional case-insensitive title search.')
    cursor: Union[Annotated[str, Field(min_length=1, max_length=2048)], None] = Field(None, alias='cursor', description='Opaque cursor returned by the previous crm-work-search page.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum work records to return before cursor pagination.')
    object_kind: Literal['activity'] = Field(..., alias='objectKind', description='Search only canonical CRM activity records.')


class CrmWorkSearchInputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    api_key: Union[str, None] = Field(None, alias='apiKey', description='Caller API key. Omit when the MCP transport already authenticated this request.')
    session_id: Union[str, None] = Field(None, alias='sessionId', description='Optional MCP session identifier used for active account context.')
    entity_id: Union[str, None] = Field(None, alias='entityId', description='Optional stable CRM person or organization entity ID associated with the work record.')
    entity_ids: Union[Annotated[list[str], Field(min_length=1, max_length=10)], None] = Field(None, alias='entityIds', description='Optional stable CRM entity IDs that must all be associated with the work record.')
    work_id: Union[str, None] = Field(None, alias='workId', description='Optional exact canonical CRM activity, task, or deal work ID.')
    query: Union[Annotated[str, Field(min_length=1, max_length=300)], None] = Field(None, alias='query', description='Optional case-insensitive title search.')
    cursor: Union[Annotated[str, Field(min_length=1, max_length=2048)], None] = Field(None, alias='cursor', description='Opaque cursor returned by the previous crm-work-search page.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum work records to return before cursor pagination.')
    object_kind: Literal['task'] = Field(..., alias='objectKind', description='Search only canonical Task records through the CRM lens.')
    task_statuses: Union[Annotated[list[Literal['todo', 'in_progress', 'blocked', 'done', 'cancelled']], Field(min_length=1, max_length=100)], None] = Field(None, alias='taskStatuses', description='Optional canonical Task statuses to include.')
    due_before: Union[str, None] = Field(None, alias='dueBefore', description='Inclusive upper due-time bound for canonical Tasks.')
    due_after: Union[str, None] = Field(None, alias='dueAfter', description='Inclusive lower due-time bound for canonical Tasks.')
    due_unscheduled: Union[bool, None] = Field(None, alias='dueUnscheduled', description='Set true to return only canonical Tasks without a due date.')
    task_owner_id: Union[Annotated[str, Field(min_length=1, max_length=200)], None] = Field(None, alias='taskOwnerId', description='Exact owner identifier stored on the canonical Task.')
    deal_id: Union[str, None] = Field(None, alias='dealId', description='Exact native CRM deal UUID linked from the canonical Task.')


class CrmWorkSearchInputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    api_key: Union[str, None] = Field(None, alias='apiKey', description='Caller API key. Omit when the MCP transport already authenticated this request.')
    session_id: Union[str, None] = Field(None, alias='sessionId', description='Optional MCP session identifier used for active account context.')
    entity_id: Union[str, None] = Field(None, alias='entityId', description='Optional stable CRM person or organization entity ID associated with the work record.')
    entity_ids: Union[Annotated[list[str], Field(min_length=1, max_length=10)], None] = Field(None, alias='entityIds', description='Optional stable CRM entity IDs that must all be associated with the work record.')
    work_id: Union[str, None] = Field(None, alias='workId', description='Optional exact canonical CRM activity, task, or deal work ID.')
    query: Union[Annotated[str, Field(min_length=1, max_length=300)], None] = Field(None, alias='query', description='Optional case-insensitive title search.')
    cursor: Union[Annotated[str, Field(min_length=1, max_length=2048)], None] = Field(None, alias='cursor', description='Opaque cursor returned by the previous crm-work-search page.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum work records to return before cursor pagination.')
    object_kind: Literal['deal'] = Field(..., alias='objectKind', description='Search only native CRM deal records.')
    pipeline_id: Union[str, None] = Field(None, alias='pipelineId', description='Optional exact native CRM pipeline UUID.')
    stage_ids: Union[Annotated[list[str], Field(min_length=1, max_length=100)], None] = Field(None, alias='stageIds', description='Optional native CRM stage UUIDs to include.')
    min_value: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(None, alias='minValue', description='Optional inclusive minimum deal value in the stored currency.')
    max_value: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(None, alias='maxValue', description='Optional inclusive maximum deal value in the stored currency.')


# Union schema: validate external payloads with TypeAdapter(CrmWorkSearchInput).
CrmWorkSearchInput = Union[CrmWorkSearchInputVariant1, CrmWorkSearchInputVariant2, CrmWorkSearchInputVariant3]


CrmWorkSearchOutputVariant1ItemsItemEntitiesItem = TypedDict('CrmWorkSearchOutputVariant1ItemsItemEntitiesItem', {
    'entityId': Required[str],
    'domain': Required[Literal['research_person', 'research_organization', 'crm_person', 'crm_organization']],
    'displayName': Required[str],
})
CrmWorkSearchOutputVariant1ItemsItemEntitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1ItemsItemDealStateVariant1 = TypedDict('CrmWorkSearchOutputVariant1ItemsItemDealStateVariant1', {
    'pipelineId': Required[str],
    'pipelineLabel': Required[str],
    'stageId': Required[str],
    'stageLabel': Required[str],
    'outcome': Required[Literal['open', 'won', 'lost']],
    'probability': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'fields': Required[dict[str, Any]],
})
CrmWorkSearchOutputVariant1ItemsItemDealStateVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1ItemsItem = TypedDict('CrmWorkSearchOutputVariant1ItemsItem', {
    'workId': Required[str],
    'objectKind': Required[Literal['activity', 'task', 'deal']],
    'noteId': Required[str],
    'vault': Required[Literal['Communication', 'Tasks', 'Deals']],
    'path': Required[str],
    'title': Required[str],
    'content': Required[str],
    'props': Required[dict[str, Any]],
    'entityIds': Required[list[str]],
    'entities': Required[list[CrmWorkSearchOutputVariant1ItemsItemEntitiesItem]],
    'revision': Required[Annotated[int, Field(ge=1)]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
    'dealState': Required[Union[CrmWorkSearchOutputVariant1ItemsItemDealStateVariant1, None]],
})
CrmWorkSearchOutputVariant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmWorkSearchOutputVariant1PageInfo = TypedDict('CrmWorkSearchOutputVariant1PageInfo', {
    'endCursor': Required[Union[str, None]],
    'hasNextPage': Required[bool],
})
CrmWorkSearchOutputVariant1PageInfo.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmWorkSearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    items: Union[list[CrmWorkSearchOutputVariant1ItemsItem], None] = Field(None, alias='items', description='')
    page_info: Union[CrmWorkSearchOutputVariant1PageInfo, None] = Field(None, alias='pageInfo', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


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