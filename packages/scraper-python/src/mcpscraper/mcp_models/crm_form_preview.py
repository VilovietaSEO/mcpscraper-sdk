from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CrmFormPreviewInputMappingCustomItem = TypedDict('CrmFormPreviewInputMappingCustomItem', {
    'label': Required[Annotated[str, Field(min_length=1, max_length=80)]],
    'field': Required[Annotated[str, Field(min_length=1, max_length=200)]],
})
CrmFormPreviewInputMappingCustomItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CrmFormPreviewInputMapping = TypedDict('CrmFormPreviewInputMapping', {
    'name': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'firstName': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'lastName': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'email': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'phone': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'company': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'message': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'submissionId': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'custom': NotRequired[Annotated[list[CrmFormPreviewInputMappingCustomItem], Field(max_length=20)]],
})
CrmFormPreviewInputMapping.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CrmFormPreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Label identifying the form connection and its submission history.')
    mapping: CrmFormPreviewInputMapping = Field(..., alias='mapping', description='Map CRM destination fields to existing input names or provider payload paths.')
    allowed_origins: Annotated[list[Annotated[str, Field(max_length=300)]], Field(min_length=1, max_length=10)] = Field(..., alias='allowedOrigins', description='Exact HTTPS website origins permitted to submit from a browser, without paths or trailing slashes.')
    relationship_type: Union[Literal['prospect', 'customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other'], None] = Field(None, alias='relationshipType', description='Relationship type for newly created contacts; existing contacts retain their managed fields.')
    sample: dict[str, Any] = Field(..., alias='sample', description='One synthetic submission using the actual field names or provider JSON structure.')


class CrmFormPreviewOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    result: Union[dict[str, Any], None] = Field(None, alias='result', description='')


CrmFormPreviewOutputVariant2DeliveryArtifactsItem = TypedDict('CrmFormPreviewOutputVariant2DeliveryArtifactsItem', {
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
CrmFormPreviewOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormPreviewOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmFormPreviewOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmFormPreviewOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormPreviewOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmFormPreviewOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmFormPreviewOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormPreviewOutputVariant2Delivery = TypedDict('CrmFormPreviewOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmFormPreviewOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmFormPreviewOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmFormPreviewOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmFormPreviewOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormPreviewOutputVariant2RecoveryOperation = TypedDict('CrmFormPreviewOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmFormPreviewOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmFormPreviewOutputVariant2Recovery = TypedDict('CrmFormPreviewOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmFormPreviewOutputVariant2RecoveryOperation],
})
CrmFormPreviewOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmFormPreviewOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmFormPreviewOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmFormPreviewOutputVariant2Recovery = Field(..., alias='recovery', description='')


CrmFormPreviewOutputVariant3Operation = TypedDict('CrmFormPreviewOutputVariant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmFormPreviewOutputVariant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmFormPreviewOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmFormPreviewOutputVariant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmFormPreviewOutput).
CrmFormPreviewOutput = Union[CrmFormPreviewOutputVariant2, CrmFormPreviewOutputVariant3, CrmFormPreviewOutputVariant1]

_CrmFormPreviewInputAdapter = TypeAdapter(CrmFormPreviewInput)
_CrmFormPreviewOutputAdapter = TypeAdapter(CrmFormPreviewOutput)