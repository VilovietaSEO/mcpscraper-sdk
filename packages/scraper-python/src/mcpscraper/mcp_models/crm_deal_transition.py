from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmDealTransitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    deal_id: str = Field(..., alias='dealId', description='Stable CRM deal or opportunity identifier.')
    pipeline_id: str = Field(..., alias='pipelineId', description='Exact CRM pipeline identifier selected from authorized tenant discovery.')
    target_stage_id: str = Field(..., alias='targetStageId', description='Governed destination stage identifier for this deal transition.')
    base_revision: Annotated[int, Field(ge=1)] = Field(..., alias='baseRevision', description='Last revision read by the caller; supply it to reject an update if the record changed meanwhile.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    fields: Union[dict[str, Any], None] = Field(None, alias='fields', description='Deal field values to apply during this stage transition, including values required by the destination stage.')


CrmDealTransitionOutputVariant1Variant1Record = TypedDict('CrmDealTransitionOutputVariant1Variant1Record', {
    'entityId': Required[str],
    'revision': Required[int],
    'noteId': NotRequired[str],
    'vault': NotRequired[str],
    'path': NotRequired[str],
    'associationIds': NotRequired[list[str]],
})
CrmDealTransitionOutputVariant1Variant1Record.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant1Variant1Receipt = TypedDict('CrmDealTransitionOutputVariant1Variant1Receipt', {
    'receiptId': Required[str],
    'replayed': NotRequired[bool],
})
CrmDealTransitionOutputVariant1Variant1Receipt.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmDealTransitionOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    record: Union[CrmDealTransitionOutputVariant1Variant1Record, None] = Field(None, alias='record', description='')
    receipt: Union[CrmDealTransitionOutputVariant1Variant1Receipt, None] = Field(None, alias='receipt', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmDealTransitionOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('CrmDealTransitionOutputVariant1Variant2DeliveryArtifactsItem', {
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
CrmDealTransitionOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('CrmDealTransitionOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmDealTransitionOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant1Variant2Delivery = TypedDict('CrmDealTransitionOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmDealTransitionOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmDealTransitionOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmDealTransitionOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant1Variant2RecoveryOperation = TypedDict('CrmDealTransitionOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmDealTransitionOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant1Variant2Recovery = TypedDict('CrmDealTransitionOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmDealTransitionOutputVariant1Variant2RecoveryOperation],
})
CrmDealTransitionOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmDealTransitionOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmDealTransitionOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmDealTransitionOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


CrmDealTransitionOutputVariant1Variant3Operation = TypedDict('CrmDealTransitionOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmDealTransitionOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmDealTransitionOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmDealTransitionOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmDealTransitionOutputVariant1).
CrmDealTransitionOutputVariant1 = Union[CrmDealTransitionOutputVariant1Variant2, CrmDealTransitionOutputVariant1Variant3, CrmDealTransitionOutputVariant1Variant1]


CrmDealTransitionOutputVariant2DeliveryArtifactsItem = TypedDict('CrmDealTransitionOutputVariant2DeliveryArtifactsItem', {
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
CrmDealTransitionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmDealTransitionOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmDealTransitionOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmDealTransitionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmDealTransitionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant2Delivery = TypedDict('CrmDealTransitionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmDealTransitionOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmDealTransitionOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmDealTransitionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmDealTransitionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant2RecoveryOperation = TypedDict('CrmDealTransitionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmDealTransitionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmDealTransitionOutputVariant2Recovery = TypedDict('CrmDealTransitionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmDealTransitionOutputVariant2RecoveryOperation],
})
CrmDealTransitionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmDealTransitionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmDealTransitionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmDealTransitionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmDealTransitionOutput).
CrmDealTransitionOutput = Union[CrmDealTransitionOutputVariant2, CrmDealTransitionOutputVariant1]

_CrmDealTransitionInputAdapter = TypeAdapter(CrmDealTransitionInput)
_CrmDealTransitionOutputAdapter = TypeAdapter(CrmDealTransitionOutput)