from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ResearchPersonSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='query', description='Text filter applied to the selected result inventory.')
    topic: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='topic', description='Research topic used to filter sourced records.')
    role: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='role', description='Optional sourced Research role to match on knowledge subjects; this is not a CRM relationship type.')
    cursor: Union[str, None] = Field(None, alias='cursor', description='Opaque continuation cursor returned by the previous page; omit for the first page.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')


ResearchPersonSearchOutputVariant1Variant1ItemsItem = TypedDict('ResearchPersonSearchOutputVariant1Variant1ItemsItem', {
    'entityId': Required[str],
    'domain': Required[Literal['research_person', 'research_organization', 'crm_person', 'crm_organization']],
    'entityKind': Required[Literal['person', 'organization']],
    'displayName': Required[str],
    'content': Required[str],
    'props': Required[dict[str, Any]],
    'relationshipStatus': Required[Union[Literal['active', 'inactive', 'archived', 'merged'], None]],
    'relationshipTypes': Required[list[Literal['prospect', 'customer', 'former_customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other']]],
    'commercialLifecycle': Required[Union[Literal['lead', 'qualified', 'opportunity', 'customer', 'retained', 'churned', 'disqualified'], None]],
    'relationshipOwnerId': Required[Union[str, None]],
    'topics': Required[list[str]],
    'researchRoles': Required[list[str]],
    'revision': Required[int],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
ResearchPersonSearchOutputVariant1Variant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant1Variant1PageInfo = TypedDict('ResearchPersonSearchOutputVariant1Variant1PageInfo', {
    'endCursor': Required[Union[str, None]],
    'hasNextPage': Required[bool],
})
ResearchPersonSearchOutputVariant1Variant1PageInfo.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonSearchOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    items: Union[list[ResearchPersonSearchOutputVariant1Variant1ItemsItem], None] = Field(None, alias='items', description='')
    page_info: Union[ResearchPersonSearchOutputVariant1Variant1PageInfo, None] = Field(None, alias='pageInfo', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ResearchPersonSearchOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('ResearchPersonSearchOutputVariant1Variant2DeliveryArtifactsItem', {
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
ResearchPersonSearchOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('ResearchPersonSearchOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResearchPersonSearchOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant1Variant2Delivery = TypedDict('ResearchPersonSearchOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResearchPersonSearchOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResearchPersonSearchOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResearchPersonSearchOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant1Variant2RecoveryOperation = TypedDict('ResearchPersonSearchOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchPersonSearchOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant1Variant2Recovery = TypedDict('ResearchPersonSearchOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResearchPersonSearchOutputVariant1Variant2RecoveryOperation],
})
ResearchPersonSearchOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonSearchOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResearchPersonSearchOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResearchPersonSearchOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


ResearchPersonSearchOutputVariant1Variant3Operation = TypedDict('ResearchPersonSearchOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchPersonSearchOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonSearchOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[ResearchPersonSearchOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(ResearchPersonSearchOutputVariant1).
ResearchPersonSearchOutputVariant1 = Union[ResearchPersonSearchOutputVariant1Variant2, ResearchPersonSearchOutputVariant1Variant3, ResearchPersonSearchOutputVariant1Variant1]


ResearchPersonSearchOutputVariant2DeliveryArtifactsItem = TypedDict('ResearchPersonSearchOutputVariant2DeliveryArtifactsItem', {
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
ResearchPersonSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('ResearchPersonSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ResearchPersonSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ResearchPersonSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResearchPersonSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant2Delivery = TypedDict('ResearchPersonSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResearchPersonSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ResearchPersonSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResearchPersonSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResearchPersonSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant2RecoveryOperation = TypedDict('ResearchPersonSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchPersonSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonSearchOutputVariant2Recovery = TypedDict('ResearchPersonSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResearchPersonSearchOutputVariant2RecoveryOperation],
})
ResearchPersonSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResearchPersonSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResearchPersonSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ResearchPersonSearchOutput).
ResearchPersonSearchOutput = Union[ResearchPersonSearchOutputVariant2, ResearchPersonSearchOutputVariant1]

_ResearchPersonSearchInputAdapter = TypeAdapter(ResearchPersonSearchInput)
_ResearchPersonSearchOutputAdapter = TypeAdapter(ResearchPersonSearchOutput)