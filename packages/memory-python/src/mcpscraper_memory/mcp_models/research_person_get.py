from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ResearchPersonGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    entity_id: str = Field(..., alias='entityId', description='Existing governed entity identifier for this relation or edit.')


ResearchPersonGetOutputVariant1Record = TypedDict('ResearchPersonGetOutputVariant1Record', {
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
ResearchPersonGetOutputVariant1Record.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonGetOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    record: Union[ResearchPersonGetOutputVariant1Record, None] = Field(None, alias='record', description='')
    aliases: Union[list[str], None] = Field(None, alias='aliases', description='')
    associations: Union[list[dict[str, Any]], None] = Field(None, alias='associations', description='')
    counterpart_entity_id: Union[Union[str, None], None] = Field(None, alias='counterpartEntityId', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ResearchPersonGetOutputVariant2DeliveryArtifactsItem = TypedDict('ResearchPersonGetOutputVariant2DeliveryArtifactsItem', {
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
ResearchPersonGetOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonGetOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ResearchPersonGetOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResearchPersonGetOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonGetOutputVariant2Delivery = TypedDict('ResearchPersonGetOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResearchPersonGetOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResearchPersonGetOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResearchPersonGetOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonGetOutputVariant2RecoveryOperation = TypedDict('ResearchPersonGetOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchPersonGetOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResearchPersonGetOutputVariant2Recovery = TypedDict('ResearchPersonGetOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResearchPersonGetOutputVariant2RecoveryOperation],
})
ResearchPersonGetOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonGetOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResearchPersonGetOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResearchPersonGetOutputVariant2Recovery = Field(..., alias='recovery', description='')


ResearchPersonGetOutputVariant3Operation = TypedDict('ResearchPersonGetOutputVariant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResearchPersonGetOutputVariant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResearchPersonGetOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[ResearchPersonGetOutputVariant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(ResearchPersonGetOutput).
ResearchPersonGetOutput = Union[ResearchPersonGetOutputVariant2, ResearchPersonGetOutputVariant3, ResearchPersonGetOutputVariant1]

_ResearchPersonGetInputAdapter = TypeAdapter(ResearchPersonGetInput)
_ResearchPersonGetOutputAdapter = TypeAdapter(ResearchPersonGetOutput)