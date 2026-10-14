from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CrmPipelineListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



CrmPipelineListOutputVariant1PipelinesItemStagesItem = TypedDict('CrmPipelineListOutputVariant1PipelinesItemStagesItem', {
    'stageId': Required[str],
    'label': Required[str],
    'position': Required[Annotated[int, Field(ge=0)]],
    'outcome': Required[Literal['open', 'won', 'lost']],
    'probability': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'requiredFields': Required[list[str]],
    'allowedNextStageIds': Required[list[str]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
CrmPipelineListOutputVariant1PipelinesItemStagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineListOutputVariant1PipelinesItem = TypedDict('CrmPipelineListOutputVariant1PipelinesItem', {
    'pipelineId': Required[str],
    'label': Required[str],
    'version': Required[Annotated[int, Field(ge=1)]],
    'isDefault': Required[bool],
    'stages': Required[list[CrmPipelineListOutputVariant1PipelinesItemStagesItem]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
CrmPipelineListOutputVariant1PipelinesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPipelineListOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    pipelines: Union[list[CrmPipelineListOutputVariant1PipelinesItem], None] = Field(None, alias='pipelines', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmPipelineListOutputVariant2DeliveryArtifactsItem = TypedDict('CrmPipelineListOutputVariant2DeliveryArtifactsItem', {
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
CrmPipelineListOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineListOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmPipelineListOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmPipelineListOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineListOutputVariant2Delivery = TypedDict('CrmPipelineListOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmPipelineListOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmPipelineListOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmPipelineListOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineListOutputVariant2RecoveryOperation = TypedDict('CrmPipelineListOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmPipelineListOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineListOutputVariant2Recovery = TypedDict('CrmPipelineListOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmPipelineListOutputVariant2RecoveryOperation],
})
CrmPipelineListOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPipelineListOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmPipelineListOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmPipelineListOutputVariant2Recovery = Field(..., alias='recovery', description='')


CrmPipelineListOutputVariant3Operation = TypedDict('CrmPipelineListOutputVariant3Operation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmPipelineListOutputVariant3Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPipelineListOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    idempotency_key: Union[Annotated[str, Field(max_length=512)], None] = Field(None, alias='idempotencyKey', description='')
    operation: Union[CrmPipelineListOutputVariant3Operation, None] = Field(None, alias='operation', description='')
    error_code: str = Field(..., alias='error_code', description='')
    error_type: str = Field(..., alias='error_type', description='')
    message: str = Field(..., alias='message', description='')
    retryable: bool = Field(..., alias='retryable', description='')
    retry_after_seconds: Union[Union[float, int], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[str, None] = Field(None, alias='charge_status', description='')
    details: Union[dict[str, Any], None] = Field(None, alias='details', description='')


# Union schema: validate external payloads with TypeAdapter(CrmPipelineListOutput).
CrmPipelineListOutput = Union[CrmPipelineListOutputVariant2, CrmPipelineListOutputVariant3, CrmPipelineListOutputVariant1]

_CrmPipelineListInputAdapter = TypeAdapter(CrmPipelineListInput)
_CrmPipelineListOutputAdapter = TypeAdapter(CrmPipelineListOutput)