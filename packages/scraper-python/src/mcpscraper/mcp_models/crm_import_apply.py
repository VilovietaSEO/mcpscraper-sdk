from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmImportApplyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    import_id: str = Field(..., alias='importId', description='Owner-scoped governed CRM import plan identifier returned by preview.')
    plan_handle: Annotated[str, Field(min_length=1)] = Field(..., alias='planHandle', description='Owner-scoped opaque preview handle returned with the plan.')
    digest: Annotated[str, Field(min_length=64, max_length=64)] = Field(..., alias='digest', description='Exact SHA-256 digest returned by the preview; any changed input invalidates it.')
    confirmation_token: Annotated[str, Field(min_length=8)] = Field(..., alias='confirmationToken', description='Explicit confirmation token bound to the exact governed preview plan.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')


CrmImportApplyOutputVariant1Variant1Result = TypedDict('CrmImportApplyOutputVariant1Variant1Result', {
    'importId': Required[str],
    'status': Required[Literal['complete', 'partial', 'failed']],
    'applied': Required[int],
    'failed': Required[int],
    'entityIds': Required[list[str]],
})
CrmImportApplyOutputVariant1Variant1Result.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant1Variant1Receipt = TypedDict('CrmImportApplyOutputVariant1Variant1Receipt', {
    'receiptId': Required[str],
})
CrmImportApplyOutputVariant1Variant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmImportApplyOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    result: Union[CrmImportApplyOutputVariant1Variant1Result, None] = Field(None, alias='result', description='')
    receipt: Union[CrmImportApplyOutputVariant1Variant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmImportApplyOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('CrmImportApplyOutputVariant1Variant2DeliveryArtifactsItem', {
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
CrmImportApplyOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('CrmImportApplyOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmImportApplyOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant1Variant2Delivery = TypedDict('CrmImportApplyOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmImportApplyOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmImportApplyOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmImportApplyOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant1Variant2RecoveryOperation = TypedDict('CrmImportApplyOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmImportApplyOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant1Variant2Recovery = TypedDict('CrmImportApplyOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmImportApplyOutputVariant1Variant2RecoveryOperation],
})
CrmImportApplyOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmImportApplyOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmImportApplyOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmImportApplyOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


CrmImportApplyOutputVariant1Variant3Operation = TypedDict('CrmImportApplyOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmImportApplyOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmImportApplyOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmImportApplyOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmImportApplyOutputVariant1).
CrmImportApplyOutputVariant1 = Union[CrmImportApplyOutputVariant1Variant2, CrmImportApplyOutputVariant1Variant3, CrmImportApplyOutputVariant1Variant1]


CrmImportApplyOutputVariant2DeliveryArtifactsItem = TypedDict('CrmImportApplyOutputVariant2DeliveryArtifactsItem', {
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
CrmImportApplyOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmImportApplyOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmImportApplyOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmImportApplyOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmImportApplyOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant2Delivery = TypedDict('CrmImportApplyOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmImportApplyOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmImportApplyOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmImportApplyOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmImportApplyOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant2RecoveryOperation = TypedDict('CrmImportApplyOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmImportApplyOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmImportApplyOutputVariant2Recovery = TypedDict('CrmImportApplyOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmImportApplyOutputVariant2RecoveryOperation],
})
CrmImportApplyOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmImportApplyOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmImportApplyOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmImportApplyOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmImportApplyOutput).
CrmImportApplyOutput = Union[CrmImportApplyOutputVariant2, CrmImportApplyOutputVariant1]

_CrmImportApplyInputAdapter = TypeAdapter(CrmImportApplyInput)
_CrmImportApplyOutputAdapter = TypeAdapter(CrmImportApplyOutput)