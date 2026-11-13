from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmMergeApplyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    merge_id: str = Field(..., alias='mergeId', description='Owner-scoped merge plan identifier returned by merge preview.')
    plan_handle: Annotated[str, Field(min_length=1)] = Field(..., alias='planHandle', description='Owner-scoped opaque preview handle returned with the plan.')
    digest: Annotated[str, Field(min_length=64, max_length=64)] = Field(..., alias='digest', description='Exact SHA-256 digest returned by the preview; any changed input invalidates it.')
    owner_confirmation: Annotated[str, Field(min_length=8)] = Field(..., alias='ownerConfirmation', description='Explicit owner confirmation bound to the exact non-expired merge plan.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')


CrmMergeApplyOutputVariant1Variant1Result = TypedDict('CrmMergeApplyOutputVariant1Variant1Result', {
    'mergeId': Required[str],
    'masterEntityId': Required[str],
    'duplicateEntityId': Required[str],
    'status': Required[Literal['applied']],
    'receiptId': Required[str],
})
CrmMergeApplyOutputVariant1Variant1Result.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant1Variant1Receipt = TypedDict('CrmMergeApplyOutputVariant1Variant1Receipt', {
    'receiptId': Required[str],
})
CrmMergeApplyOutputVariant1Variant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergeApplyOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    result: Union[CrmMergeApplyOutputVariant1Variant1Result, None] = Field(None, alias='result', description='')
    receipt: Union[CrmMergeApplyOutputVariant1Variant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmMergeApplyOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('CrmMergeApplyOutputVariant1Variant2DeliveryArtifactsItem', {
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
CrmMergeApplyOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('CrmMergeApplyOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmMergeApplyOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant1Variant2Delivery = TypedDict('CrmMergeApplyOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmMergeApplyOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmMergeApplyOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmMergeApplyOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant1Variant2RecoveryOperation = TypedDict('CrmMergeApplyOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmMergeApplyOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant1Variant2Recovery = TypedDict('CrmMergeApplyOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmMergeApplyOutputVariant1Variant2RecoveryOperation],
})
CrmMergeApplyOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergeApplyOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmMergeApplyOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmMergeApplyOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


CrmMergeApplyOutputVariant1Variant3Operation = TypedDict('CrmMergeApplyOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmMergeApplyOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergeApplyOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmMergeApplyOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmMergeApplyOutputVariant1).
CrmMergeApplyOutputVariant1 = Union[CrmMergeApplyOutputVariant1Variant2, CrmMergeApplyOutputVariant1Variant3, CrmMergeApplyOutputVariant1Variant1]


CrmMergeApplyOutputVariant2DeliveryArtifactsItem = TypedDict('CrmMergeApplyOutputVariant2DeliveryArtifactsItem', {
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
CrmMergeApplyOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmMergeApplyOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmMergeApplyOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmMergeApplyOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmMergeApplyOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant2Delivery = TypedDict('CrmMergeApplyOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmMergeApplyOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmMergeApplyOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmMergeApplyOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmMergeApplyOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant2RecoveryOperation = TypedDict('CrmMergeApplyOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmMergeApplyOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmMergeApplyOutputVariant2Recovery = TypedDict('CrmMergeApplyOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmMergeApplyOutputVariant2RecoveryOperation],
})
CrmMergeApplyOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergeApplyOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmMergeApplyOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmMergeApplyOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmMergeApplyOutput).
CrmMergeApplyOutput = Union[CrmMergeApplyOutputVariant2, CrmMergeApplyOutputVariant1]

_CrmMergeApplyInputAdapter = TypeAdapter(CrmMergeApplyInput)
_CrmMergeApplyOutputAdapter = TypeAdapter(CrmMergeApplyOutput)