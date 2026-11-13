from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmCounterpartPreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    research_entity_id: str = Field(..., alias='researchEntityId', description='Stable Research entity identifier used only for explicit counterpart planning.')
    crm_entity_id: str = Field(..., alias='crmEntityId', description='Stable CRM entity identifier; it is distinct from any Research record identifier.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    ttl_minutes: Union[Annotated[int, Field(ge=5, le=1440)], None] = Field(None, alias='ttlMinutes', description='Bounded preview lifetime in minutes before the plan expires.')
    mode: Union[Literal['link_only'], None] = Field(None, alias='mode', description='Governed execution mode for this operation.')


CrmCounterpartPreviewOutputVariant1Variant1Plan = TypedDict('CrmCounterpartPreviewOutputVariant1Variant1Plan', {
    'planId': Required[str],
    'planHandle': Required[str],
    'digest': Required[str],
    'expiresAt': Required[str],
    'researchEntityId': Required[str],
    'crmEntityId': Required[str],
    'copiedFields': Required[list[Any]],
    'mode': Required[Literal['link_only']],
})
CrmCounterpartPreviewOutputVariant1Variant1Plan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmCounterpartPreviewOutputVariant1Variant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    plan: Union[CrmCounterpartPreviewOutputVariant1Variant1Plan, None] = Field(None, alias='plan', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmCounterpartPreviewOutputVariant1Variant2DeliveryArtifactsItem = TypedDict('CrmCounterpartPreviewOutputVariant1Variant2DeliveryArtifactsItem', {
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
CrmCounterpartPreviewOutputVariant1Variant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartPreviewOutputVariant1Variant2DeliveryStorageFailureVariant1 = TypedDict('CrmCounterpartPreviewOutputVariant1Variant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmCounterpartPreviewOutputVariant1Variant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartPreviewOutputVariant1Variant2Delivery = TypedDict('CrmCounterpartPreviewOutputVariant1Variant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmCounterpartPreviewOutputVariant1Variant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmCounterpartPreviewOutputVariant1Variant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmCounterpartPreviewOutputVariant1Variant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartPreviewOutputVariant1Variant2RecoveryOperation = TypedDict('CrmCounterpartPreviewOutputVariant1Variant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmCounterpartPreviewOutputVariant1Variant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartPreviewOutputVariant1Variant2Recovery = TypedDict('CrmCounterpartPreviewOutputVariant1Variant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmCounterpartPreviewOutputVariant1Variant2RecoveryOperation],
})
CrmCounterpartPreviewOutputVariant1Variant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmCounterpartPreviewOutputVariant1Variant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmCounterpartPreviewOutputVariant1Variant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmCounterpartPreviewOutputVariant1Variant2Recovery = Field(..., alias='recovery', description='')


CrmCounterpartPreviewOutputVariant1Variant3Operation = TypedDict('CrmCounterpartPreviewOutputVariant1Variant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmCounterpartPreviewOutputVariant1Variant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmCounterpartPreviewOutputVariant1Variant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmCounterpartPreviewOutputVariant1Variant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmCounterpartPreviewOutputVariant1).
CrmCounterpartPreviewOutputVariant1 = Union[CrmCounterpartPreviewOutputVariant1Variant2, CrmCounterpartPreviewOutputVariant1Variant3, CrmCounterpartPreviewOutputVariant1Variant1]


CrmCounterpartPreviewOutputVariant2DeliveryArtifactsItem = TypedDict('CrmCounterpartPreviewOutputVariant2DeliveryArtifactsItem', {
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
CrmCounterpartPreviewOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartPreviewOutputVariant2DeliveryAvailableExportsItem = TypedDict('CrmCounterpartPreviewOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CrmCounterpartPreviewOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartPreviewOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmCounterpartPreviewOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmCounterpartPreviewOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartPreviewOutputVariant2Delivery = TypedDict('CrmCounterpartPreviewOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmCounterpartPreviewOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CrmCounterpartPreviewOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmCounterpartPreviewOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmCounterpartPreviewOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartPreviewOutputVariant2RecoveryOperation = TypedDict('CrmCounterpartPreviewOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmCounterpartPreviewOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmCounterpartPreviewOutputVariant2Recovery = TypedDict('CrmCounterpartPreviewOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmCounterpartPreviewOutputVariant2RecoveryOperation],
})
CrmCounterpartPreviewOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmCounterpartPreviewOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmCounterpartPreviewOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmCounterpartPreviewOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmCounterpartPreviewOutput).
CrmCounterpartPreviewOutput = Union[CrmCounterpartPreviewOutputVariant2, CrmCounterpartPreviewOutputVariant1]

_CrmCounterpartPreviewInputAdapter = TypeAdapter(CrmCounterpartPreviewInput)
_CrmCounterpartPreviewOutputAdapter = TypeAdapter(CrmCounterpartPreviewOutput)