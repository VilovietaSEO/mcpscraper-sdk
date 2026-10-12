from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CrmPipelineUpsertInputStagesItem = TypedDict('CrmPipelineUpsertInputStagesItem', {
    'stageId': NotRequired[str],
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'outcome': Required[Literal['open', 'won', 'lost']],
    'probability': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'requiredFields': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=120)]], Field(max_length=100)]],
    'allowedNextStageIds': NotRequired[Annotated[list[str], Field(max_length=100)]],
})
CrmPipelineUpsertInputStagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CrmPipelineUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    pipeline_id: Union[str, None] = Field(None, alias='pipelineId', description='Existing owner-scoped pipeline UUID; omit to create a pipeline.')
    label: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='label', description='Human-readable pipeline label.')
    base_version: Annotated[int, Field(ge=0)] = Field(..., alias='baseVersion', description='Expected pipeline version for concurrency control; use 0 only when creating.')
    is_default: Union[bool, None] = Field(None, alias='isDefault', description='Whether this should become the owner default pipeline.')
    stages: Annotated[list[CrmPipelineUpsertInputStagesItem], Field(min_length=2, max_length=100)] = Field(..., alias='stages', description='Complete ordered stage definition for the pipeline.')


CrmPipelineUpsertOutputVariant1PipelineStagesItem = TypedDict('CrmPipelineUpsertOutputVariant1PipelineStagesItem', {
    'stageId': Required[str],
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'outcome': Required[Literal['open', 'won', 'lost']],
    'probability': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'requiredFields': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=120)]], Field(max_length=100)]],
    'allowedNextStageIds': NotRequired[Annotated[list[str], Field(max_length=100)]],
})
CrmPipelineUpsertOutputVariant1PipelineStagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineUpsertOutputVariant1Pipeline = TypedDict('CrmPipelineUpsertOutputVariant1Pipeline', {
    'pipelineId': Required[str],
    'version': Required[Annotated[int, Field(ge=1)]],
    'stages': Required[list[CrmPipelineUpsertOutputVariant1PipelineStagesItem]],
})
CrmPipelineUpsertOutputVariant1Pipeline.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPipelineUpsertOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    message: str = Field(..., alias='message', description='')
    pipeline: Union[CrmPipelineUpsertOutputVariant1Pipeline, None] = Field(None, alias='pipeline', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CrmPipelineUpsertOutputVariant2DeliveryArtifactsItem = TypedDict('CrmPipelineUpsertOutputVariant2DeliveryArtifactsItem', {
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
CrmPipelineUpsertOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineUpsertOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CrmPipelineUpsertOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CrmPipelineUpsertOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineUpsertOutputVariant2Delivery = TypedDict('CrmPipelineUpsertOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CrmPipelineUpsertOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CrmPipelineUpsertOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CrmPipelineUpsertOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineUpsertOutputVariant2RecoveryOperation = TypedDict('CrmPipelineUpsertOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CrmPipelineUpsertOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CrmPipelineUpsertOutputVariant2Recovery = TypedDict('CrmPipelineUpsertOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CrmPipelineUpsertOutputVariant2RecoveryOperation],
})
CrmPipelineUpsertOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CrmPipelineUpsertOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CrmPipelineUpsertOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CrmPipelineUpsertOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CrmPipelineUpsertOutput).
CrmPipelineUpsertOutput = Union[CrmPipelineUpsertOutputVariant2, CrmPipelineUpsertOutputVariant1]

_CrmPipelineUpsertInputAdapter = TypeAdapter(CrmPipelineUpsertInput)
_CrmPipelineUpsertOutputAdapter = TypeAdapter(CrmPipelineUpsertOutput)