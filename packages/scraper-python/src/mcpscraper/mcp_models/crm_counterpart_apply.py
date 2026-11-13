from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmCounterpartApplyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    plan_id: str = Field(..., alias='planId', description='Exact owner-scoped counterpart plan identifier returned by crm-counterpart-preview; use its matching unexpired planHandle and digest.')
    plan_handle: Annotated[str, Field(min_length=1)] = Field(..., alias='planHandle', description='Owner-scoped opaque preview handle returned with the plan.')
    digest: Annotated[str, Field(min_length=64, max_length=64)] = Field(..., alias='digest', description='Exact SHA-256 digest returned by the preview; any changed input invalidates it.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')


CrmCounterpartApplyOutputVariant1Variant1Link = TypedDict('CrmCounterpartApplyOutputVariant1Variant1Link', {
    'linkId': Required[str],
    'subjectId': Required[str],
    'researchEntityId': Required[str],
    'crmEntityId': Required[str],
    'copiedFields': Required[list[Any]],
})
CrmCounterpartApplyOutputVariant1Variant1Link.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant1Variant1Receipt = TypedDict('CrmCounterpartApplyOutputVariant1Variant1Receipt', {
    'receiptId': Required[str],
})
CrmCounterpartApplyOutputVariant1Variant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmCounterpartApplyOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    link: Union[CrmCounterpartApplyOutputVariant1Variant1Link, None] = Field(None, alias='link', description='')
    receipt: Union[CrmCounterpartApplyOutputVariant1Variant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmCounterpartApplyOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('CrmCounterpartApplyOutputVariant1Variant2DeliveryArtifactsItem', {
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
CrmCounterpartApplyOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('CrmCounterpartApplyOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmCounterpartApplyOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant1Variant2Delivery = TypedDict('CrmCounterpartApplyOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmCounterpartApplyOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmCounterpartApplyOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmCounterpartApplyOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant1Variant2RecoveryOperation = TypedDict('CrmCounterpartApplyOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmCounterpartApplyOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant1Variant2Recovery = TypedDict('CrmCounterpartApplyOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmCounterpartApplyOutputVariant1Variant2RecoveryOperation],
})
CrmCounterpartApplyOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmCounterpartApplyOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmCounterpartApplyOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmCounterpartApplyOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


CrmCounterpartApplyOutputVariant1Variant3Operation = TypedDict('CrmCounterpartApplyOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmCounterpartApplyOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmCounterpartApplyOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmCounterpartApplyOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmCounterpartApplyOutputVariant1).
CrmCounterpartApplyOutputVariant1 = Union[CrmCounterpartApplyOutputVariant1Variant2, CrmCounterpartApplyOutputVariant1Variant3, CrmCounterpartApplyOutputVariant1Variant1]


CrmCounterpartApplyOutputVariant2DeliveryArtifactsItem = TypedDict('CrmCounterpartApplyOutputVariant2DeliveryArtifactsItem', {
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
CrmCounterpartApplyOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmCounterpartApplyOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmCounterpartApplyOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmCounterpartApplyOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmCounterpartApplyOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant2Delivery = TypedDict('CrmCounterpartApplyOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmCounterpartApplyOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmCounterpartApplyOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmCounterpartApplyOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmCounterpartApplyOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant2RecoveryOperation = TypedDict('CrmCounterpartApplyOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmCounterpartApplyOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartApplyOutputVariant2Recovery = TypedDict('CrmCounterpartApplyOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmCounterpartApplyOutputVariant2RecoveryOperation],
})
CrmCounterpartApplyOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmCounterpartApplyOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmCounterpartApplyOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmCounterpartApplyOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmCounterpartApplyOutput).
CrmCounterpartApplyOutput = Union[CrmCounterpartApplyOutputVariant2, CrmCounterpartApplyOutputVariant1]

_CrmCounterpartApplyInputAdapter = TypeAdapter(CrmCounterpartApplyInput)
_CrmCounterpartApplyOutputAdapter = TypeAdapter(CrmCounterpartApplyOutput)