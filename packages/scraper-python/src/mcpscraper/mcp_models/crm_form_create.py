from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CrmFormCreateInputMappingCustomItem = TypedDict('CrmFormCreateInputMappingCustomItem', {
    'label': Required[Annotated[str, Field(min_length=1, max_length=80)]],
    'field': Required[Annotated[str, Field(min_length=1, max_length=200)]],
})
CrmFormCreateInputMappingCustomItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CrmFormCreateInputMapping = TypedDict('CrmFormCreateInputMapping', {
    'name': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'firstName': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'lastName': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'email': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'phone': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'company': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'message': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'submissionId': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'custom': NotRequired[Annotated[list[CrmFormCreateInputMappingCustomItem], Field(max_length=20)]],
})
CrmFormCreateInputMapping.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CrmFormCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Label identifying the form connection and its submission history.')
    mapping: CrmFormCreateInputMapping = Field(..., alias='mapping', description='Map CRM destination fields to existing input names or provider payload paths.')
    allowed_origins: Annotated[list[Annotated[str, Field(max_length=300)]], Field(min_length=1, max_length=10)] = Field(..., alias='allowedOrigins', description='Exact HTTPS website origins permitted to submit from a browser, without paths or trailing slashes.')
    relationship_type: Union[Literal['prospect', 'customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other'], None] = Field(None, alias='relationshipType', description='Relationship type for newly created contacts; existing contacts retain their managed fields.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Stable setup key; reuse unchanged arguments after an unknown result.')


class CrmFormCreateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    result: Union[dict[str, Any], None] = Field(None, alias='result', description='')


CrmFormCreateOutputVariant2DeliveryArtifactsItem = TypedDict('CrmFormCreateOutputVariant2DeliveryArtifactsItem', {
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
CrmFormCreateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormCreateOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmFormCreateOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmFormCreateOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormCreateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmFormCreateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmFormCreateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormCreateOutputVariant2Delivery = TypedDict('CrmFormCreateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmFormCreateOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmFormCreateOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmFormCreateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmFormCreateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormCreateOutputVariant2RecoveryOperation = TypedDict('CrmFormCreateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmFormCreateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormCreateOutputVariant2Recovery = TypedDict('CrmFormCreateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmFormCreateOutputVariant2RecoveryOperation],
})
CrmFormCreateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmFormCreateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmFormCreateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmFormCreateOutputVariant2Recovery = Field(..., alias='recovery', description='')


CrmFormCreateOutputVariant3Operation = TypedDict('CrmFormCreateOutputVariant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmFormCreateOutputVariant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmFormCreateOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmFormCreateOutputVariant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmFormCreateOutput).
CrmFormCreateOutput = Union[CrmFormCreateOutputVariant2, CrmFormCreateOutputVariant3, CrmFormCreateOutputVariant1]

_CrmFormCreateInputAdapter = TypeAdapter(CrmFormCreateInput)
_CrmFormCreateOutputAdapter = TypeAdapter(CrmFormCreateOutput)