from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmPersonSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='query', description='Text filter applied to the selected result inventory.')
    relationship_type: Union[Literal['prospect', 'customer', 'former_customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other'], None] = Field(None, alias='relationshipType', description='One managed relationship type used to filter CRM records.')
    relationship_status: Union[Literal['active', 'inactive', 'archived', 'merged'], None] = Field(None, alias='relationshipStatus', description='Operational relationship status independent of optional commercial lifecycle.')
    commercial_lifecycle: Union[Literal['lead', 'qualified', 'opportunity', 'customer', 'retained', 'churned', 'disqualified'], None] = Field(None, alias='commercialLifecycle', description='Optional commercial lifecycle; friends, coworkers, and other non-commercial relationships may leave it null.')
    relationship_owner_id: Union[Annotated[str, Field(max_length=300)], None] = Field(None, alias='relationshipOwnerId', description='Optional owner identifier responsible for the CRM relationship.')
    cursor: Union[str, None] = Field(None, alias='cursor', description='Opaque continuation cursor returned by the previous page; omit for the first page.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')


CrmPersonSearchOutputVariant1Variant1ItemsItem = TypedDict('CrmPersonSearchOutputVariant1Variant1ItemsItem', {
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
CrmPersonSearchOutputVariant1Variant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant1Variant1PageInfo = TypedDict('CrmPersonSearchOutputVariant1Variant1PageInfo', {
    'endCursor': Required[Union[str, None]],
    'hasNextPage': Required[bool],
})
CrmPersonSearchOutputVariant1Variant1PageInfo.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPersonSearchOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    items: Union[list[CrmPersonSearchOutputVariant1Variant1ItemsItem], None] = Field(None, alias='items', description='')
    page_info: Union[CrmPersonSearchOutputVariant1Variant1PageInfo, None] = Field(None, alias='pageInfo', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmPersonSearchOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('CrmPersonSearchOutputVariant1Variant2DeliveryArtifactsItem', {
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
CrmPersonSearchOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('CrmPersonSearchOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmPersonSearchOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant1Variant2Delivery = TypedDict('CrmPersonSearchOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmPersonSearchOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmPersonSearchOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmPersonSearchOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant1Variant2RecoveryOperation = TypedDict('CrmPersonSearchOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmPersonSearchOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant1Variant2Recovery = TypedDict('CrmPersonSearchOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmPersonSearchOutputVariant1Variant2RecoveryOperation],
})
CrmPersonSearchOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPersonSearchOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmPersonSearchOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmPersonSearchOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


CrmPersonSearchOutputVariant1Variant3Operation = TypedDict('CrmPersonSearchOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmPersonSearchOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPersonSearchOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmPersonSearchOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmPersonSearchOutputVariant1).
CrmPersonSearchOutputVariant1 = Union[CrmPersonSearchOutputVariant1Variant2, CrmPersonSearchOutputVariant1Variant3, CrmPersonSearchOutputVariant1Variant1]


CrmPersonSearchOutputVariant2DeliveryArtifactsItem = TypedDict('CrmPersonSearchOutputVariant2DeliveryArtifactsItem', {
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
CrmPersonSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmPersonSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmPersonSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmPersonSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmPersonSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant2Delivery = TypedDict('CrmPersonSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmPersonSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmPersonSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmPersonSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmPersonSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant2RecoveryOperation = TypedDict('CrmPersonSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmPersonSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPersonSearchOutputVariant2Recovery = TypedDict('CrmPersonSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmPersonSearchOutputVariant2RecoveryOperation],
})
CrmPersonSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPersonSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmPersonSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmPersonSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmPersonSearchOutput).
CrmPersonSearchOutput = Union[CrmPersonSearchOutputVariant2, CrmPersonSearchOutputVariant1]

_CrmPersonSearchInputAdapter = TypeAdapter(CrmPersonSearchInput)
_CrmPersonSearchOutputAdapter = TypeAdapter(CrmPersonSearchOutput)