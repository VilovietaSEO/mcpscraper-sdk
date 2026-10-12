from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmMergePreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    master_entity_id: str = Field(..., alias='masterEntityId', description='Stable CRM record selected as the surviving master in a merge preview.')
    duplicate_entity_id: str = Field(..., alias='duplicateEntityId', description='Stable CRM record selected as the duplicate candidate in a merge preview.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    ttl_minutes: Union[Annotated[int, Field(ge=5, le=1440)], None] = Field(None, alias='ttlMinutes', description='Bounded preview lifetime in minutes before the plan expires.')


CrmMergePreviewOutputVariant1Plan = TypedDict('CrmMergePreviewOutputVariant1Plan', {
    'mergeId': Required[str],
    'planHandle': Required[str],
    'digest': Required[str],
    'expiresAt': Required[str],
    'fieldConflicts': Required[list[dict[str, Any]]],
    'associationCount': Required[int],
    'preservesArchivedAlias': Required[Literal[True]],
    'deletesSourceHistory': Required[Literal[False]],
})
CrmMergePreviewOutputVariant1Plan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergePreviewOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    plan: Union[CrmMergePreviewOutputVariant1Plan, None] = Field(None, alias='plan', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


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


CrmMergePreviewOutputVariant3Operation = TypedDict('CrmMergePreviewOutputVariant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmMergePreviewOutputVariant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmMergePreviewOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmMergePreviewOutputVariant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmMergePreviewOutput).
CrmMergePreviewOutput = Union[CrmMergePreviewOutputVariant2, CrmMergePreviewOutputVariant3, CrmMergePreviewOutputVariant1]

_CrmMergePreviewInputAdapter = TypeAdapter(CrmMergePreviewInput)
_CrmMergePreviewOutputAdapter = TypeAdapter(CrmMergePreviewOutput)