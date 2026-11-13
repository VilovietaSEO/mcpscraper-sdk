from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ResearchOrganizationSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='query', description='Text filter applied to the selected result inventory.')
    topic: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='topic', description='Research topic used to filter sourced records.')
    role: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='role', description='Optional sourced Research role to match on knowledge subjects; this is not a CRM relationship type.')
    cursor: Union[str, None] = Field(None, alias='cursor', description='Opaque continuation cursor returned by the previous page; omit for the first page.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')


ResearchOrganizationSearchOutputVariant1Variant1ItemsItem = TypedDict('ResearchOrganizationSearchOutputVariant1Variant1ItemsItem', {
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
ResearchOrganizationSearchOutputVariant1Variant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant1Variant1PageInfo = TypedDict('ResearchOrganizationSearchOutputVariant1Variant1PageInfo', {
    'endCursor': Required[Union[str, None]],
    'hasNextPage': Required[bool],
})
ResearchOrganizationSearchOutputVariant1Variant1PageInfo.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchOrganizationSearchOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    items: Union[list[ResearchOrganizationSearchOutputVariant1Variant1ItemsItem], None] = Field(None, alias='items', description='')
    page_info: Union[ResearchOrganizationSearchOutputVariant1Variant1PageInfo, None] = Field(None, alias='pageInfo', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ResearchOrganizationSearchOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('ResearchOrganizationSearchOutputVariant1Variant2DeliveryArtifactsItem', {
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
ResearchOrganizationSearchOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('ResearchOrganizationSearchOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResearchOrganizationSearchOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant1Variant2Delivery = TypedDict('ResearchOrganizationSearchOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResearchOrganizationSearchOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResearchOrganizationSearchOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResearchOrganizationSearchOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant1Variant2RecoveryOperation = TypedDict('ResearchOrganizationSearchOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchOrganizationSearchOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant1Variant2Recovery = TypedDict('ResearchOrganizationSearchOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResearchOrganizationSearchOutputVariant1Variant2RecoveryOperation],
})
ResearchOrganizationSearchOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchOrganizationSearchOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResearchOrganizationSearchOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResearchOrganizationSearchOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


ResearchOrganizationSearchOutputVariant1Variant3Operation = TypedDict('ResearchOrganizationSearchOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchOrganizationSearchOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchOrganizationSearchOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[ResearchOrganizationSearchOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(ResearchOrganizationSearchOutputVariant1).
ResearchOrganizationSearchOutputVariant1 = Union[ResearchOrganizationSearchOutputVariant1Variant2, ResearchOrganizationSearchOutputVariant1Variant3, ResearchOrganizationSearchOutputVariant1Variant1]


ResearchOrganizationSearchOutputVariant2DeliveryArtifactsItem = TypedDict('ResearchOrganizationSearchOutputVariant2DeliveryArtifactsItem', {
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
ResearchOrganizationSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('ResearchOrganizationSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ResearchOrganizationSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ResearchOrganizationSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResearchOrganizationSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant2Delivery = TypedDict('ResearchOrganizationSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResearchOrganizationSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ResearchOrganizationSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResearchOrganizationSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResearchOrganizationSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant2RecoveryOperation = TypedDict('ResearchOrganizationSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchOrganizationSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchOrganizationSearchOutputVariant2Recovery = TypedDict('ResearchOrganizationSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResearchOrganizationSearchOutputVariant2RecoveryOperation],
})
ResearchOrganizationSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchOrganizationSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResearchOrganizationSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResearchOrganizationSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ResearchOrganizationSearchOutput).
ResearchOrganizationSearchOutput = Union[ResearchOrganizationSearchOutputVariant2, ResearchOrganizationSearchOutputVariant1]

_ResearchOrganizationSearchInputAdapter = TypeAdapter(ResearchOrganizationSearchInput)
_ResearchOrganizationSearchOutputAdapter = TypeAdapter(ResearchOrganizationSearchOutput)