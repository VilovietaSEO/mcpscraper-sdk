from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class WorkflowStepInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    run_id: Annotated[str, Field(min_length=1)] = Field(..., alias='runId', description='Workflow run id returned by workflow_run/workflow_step/workflow_status. Advances the run by exactly one step.')


class WorkflowStepOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    run_id: str = Field(..., alias='runId', description='')
    run: Union[dict[str, Any], None] = Field(None, alias='run', description='')
    summary: Union[Union[dict[str, Any], None], None] = Field(None, alias='summary', description='')
    step: Union[dict[str, Any], None] = Field(None, alias='step', description='')
    next_step: Union[Union[dict[str, Any], None], None] = Field(None, alias='nextStep', description='')
    done: bool = Field(..., alias='done', description='')
    artifacts: list[dict[str, Any]] = Field(..., alias='artifacts', description='')


WorkflowStepOutputVariant2DeliveryArtifactsItem = TypedDict('WorkflowStepOutputVariant2DeliveryArtifactsItem', {
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
WorkflowStepOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowStepOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('WorkflowStepOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
WorkflowStepOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowStepOutputVariant2Delivery = TypedDict('WorkflowStepOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[WorkflowStepOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[WorkflowStepOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
WorkflowStepOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowStepOutputVariant2RecoveryOperation = TypedDict('WorkflowStepOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
WorkflowStepOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowStepOutputVariant2Recovery = TypedDict('WorkflowStepOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[WorkflowStepOutputVariant2RecoveryOperation],
})
WorkflowStepOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class WorkflowStepOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: WorkflowStepOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: WorkflowStepOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(WorkflowStepOutput).
WorkflowStepOutput = Union[WorkflowStepOutputVariant2, WorkflowStepOutputVariant1]

_WorkflowStepInputAdapter = TypeAdapter(WorkflowStepInput)
_WorkflowStepOutputAdapter = TypeAdapter(WorkflowStepOutput)