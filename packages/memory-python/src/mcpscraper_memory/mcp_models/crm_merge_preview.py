from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmMergePreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    master_entity_id: str = Field(..., alias='masterEntityId', description='Stable CRM record selected as the surviving master in a merge preview.')
    duplicate_entity_id: str = Field(..., alias='duplicateEntityId', description='Stable CRM record selected as the duplicate candidate in a merge preview.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    ttl_minutes: Union[Annotated[int, Field(ge=5, le=1440)], None] = Field(None, alias='ttlMinutes', description='Bounded preview lifetime in minutes before the plan expires.')


CrmMergePreviewOutputVariant1Variant1Plan = TypedDict('CrmMergePreviewOutputVariant1Variant1Plan', {
    'mergeId': Required[str],
    'planHandle': Required[str],
    'digest': Required[str],
    'expiresAt': Required[str],
    'fieldConflicts': Required[list[dict[str, Any]]],
    'associationCount': Required[int],
    'preservesArchivedAlias': Required[Literal[True]],
    'deletesSourceHistory': Required[Literal[False]],
})
CrmMergePreviewOutputVariant1Variant1Plan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergePreviewOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    plan: Union[CrmMergePreviewOutputVariant1Variant1Plan, None] = Field(None, alias='plan', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmMergePreviewOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('CrmMergePreviewOutputVariant1Variant2DeliveryArtifactsItem', {
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
CrmMergePreviewOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergePreviewOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('CrmMergePreviewOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmMergePreviewOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergePreviewOutputVariant1Variant2Delivery = TypedDict('CrmMergePreviewOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmMergePreviewOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmMergePreviewOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmMergePreviewOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergePreviewOutputVariant1Variant2RecoveryOperation = TypedDict('CrmMergePreviewOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmMergePreviewOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergePreviewOutputVariant1Variant2Recovery = TypedDict('CrmMergePreviewOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmMergePreviewOutputVariant1Variant2RecoveryOperation],
})
CrmMergePreviewOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergePreviewOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmMergePreviewOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmMergePreviewOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


CrmMergePreviewOutputVariant1Variant3Operation = TypedDict('CrmMergePreviewOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmMergePreviewOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergePreviewOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmMergePreviewOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmMergePreviewOutputVariant1).
CrmMergePreviewOutputVariant1 = Union[CrmMergePreviewOutputVariant1Variant2, CrmMergePreviewOutputVariant1Variant3, CrmMergePreviewOutputVariant1Variant1]


CrmMergePreviewOutputVariant2DeliveryArtifactsItem = TypedDict('CrmMergePreviewOutputVariant2DeliveryArtifactsItem', {
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
CrmMergePreviewOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergePreviewOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmMergePreviewOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmMergePreviewOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergePreviewOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmMergePreviewOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmMergePreviewOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergePreviewOutputVariant2Delivery = TypedDict('CrmMergePreviewOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmMergePreviewOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmMergePreviewOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmMergePreviewOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmMergePreviewOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergePreviewOutputVariant2RecoveryOperation = TypedDict('CrmMergePreviewOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmMergePreviewOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergePreviewOutputVariant2Recovery = TypedDict('CrmMergePreviewOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmMergePreviewOutputVariant2RecoveryOperation],
})
CrmMergePreviewOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergePreviewOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmMergePreviewOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmMergePreviewOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmMergePreviewOutput).
CrmMergePreviewOutput = Union[CrmMergePreviewOutputVariant2, CrmMergePreviewOutputVariant1]

_CrmMergePreviewInputAdapter = TypeAdapter(CrmMergePreviewInput)
_CrmMergePreviewOutputAdapter = TypeAdapter(CrmMergePreviewOutput)