from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class WorkflowArtifactReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    run_id: Annotated[str, Field(min_length=1)] = Field(..., alias='runId', description='Workflow run id returned by workflow_run, workflow_step, or workflow_status. Use only a returned runId; do not construct one yourself.')
    artifact_id: Annotated[str, Field(min_length=1)] = Field(..., alias='artifactId', description='Artifact id from the run artifact list returned by workflow_run, workflow_step, or workflow_status. Use only a returned artifactId; do not construct one yourself.')
    max_bytes: Union[Annotated[int, Field(ge=1000, le=1000000)], None] = Field(None, alias='maxBytes', description='Maximum bytes of artifact text to return inline.')


class WorkflowArtifactReadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    run_id: str = Field(..., alias='runId', description='')
    artifact_id: str = Field(..., alias='artifactId', description='')
    content_type: str = Field(..., alias='contentType', description='')
    bytes: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='bytes', description='')
    truncated: bool = Field(..., alias='truncated', description='')
    text: str = Field(..., alias='text', description='')


WorkflowArtifactReadOutputVariant2DeliveryArtifactsItem = TypedDict('WorkflowArtifactReadOutputVariant2DeliveryArtifactsItem', {
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
WorkflowArtifactReadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowArtifactReadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('WorkflowArtifactReadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
WorkflowArtifactReadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowArtifactReadOutputVariant2Delivery = TypedDict('WorkflowArtifactReadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[WorkflowArtifactReadOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[WorkflowArtifactReadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
WorkflowArtifactReadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowArtifactReadOutputVariant2RecoveryOperation = TypedDict('WorkflowArtifactReadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
WorkflowArtifactReadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowArtifactReadOutputVariant2Recovery = TypedDict('WorkflowArtifactReadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[WorkflowArtifactReadOutputVariant2RecoveryOperation],
})
WorkflowArtifactReadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class WorkflowArtifactReadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: WorkflowArtifactReadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: WorkflowArtifactReadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(WorkflowArtifactReadOutput).
WorkflowArtifactReadOutput = Union[WorkflowArtifactReadOutputVariant1, WorkflowArtifactReadOutputVariant2]

_WorkflowArtifactReadInputAdapter = TypeAdapter(WorkflowArtifactReadInput)
_WorkflowArtifactReadOutputAdapter = TypeAdapter(WorkflowArtifactReadOutput)