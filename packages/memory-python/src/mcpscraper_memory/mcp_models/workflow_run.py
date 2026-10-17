from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class WorkflowRunInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    workflow_id: Literal['directory', 'get-leads', 'agent-packet', 'local-competitive-audit', 'map-comparison', 'serp-comparison', 'paa-expansion-brief', 'ai-overview-language'] = Field(..., alias='workflowId', description='Workflow to run. Call workflow_list or workflow_suggest first when unsure.')
    input: Union[dict[str, Any], None] = Field(None, alias='input', description='Workflow-specific input object; shape depends on workflowId. Call workflow_list or workflow_suggest to see required fields.')
    webhook_url: Union[str, None] = Field(None, alias='webhookUrl', description='Optional HTTPS webhook to receive the completed hosted workflow run event.')


class WorkflowRunOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    workflow_id: str = Field(..., alias='workflowId', description='')
    input: dict[str, Any] = Field(..., alias='input', description='')
    run: Union[dict[str, Any], None] = Field(None, alias='run', description='')
    summary: Union[dict[str, Any], None] = Field(None, alias='summary', description='')
    step: Union[dict[str, Any], None] = Field(None, alias='step', description='')
    next_step: Union[Union[dict[str, Any], None], None] = Field(None, alias='nextStep', description='')
    done: Union[bool, None] = Field(None, alias='done', description='')
    artifacts: list[dict[str, Any]] = Field(..., alias='artifacts', description='')


WorkflowRunOutputVariant2DeliveryArtifactsItem = TypedDict('WorkflowRunOutputVariant2DeliveryArtifactsItem', {
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
WorkflowRunOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowRunOutputVariant2DeliveryAvailableExportsItem = TypedDict('WorkflowRunOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
WorkflowRunOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowRunOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('WorkflowRunOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
WorkflowRunOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowRunOutputVariant2Delivery = TypedDict('WorkflowRunOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[WorkflowRunOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[WorkflowRunOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[WorkflowRunOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
WorkflowRunOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowRunOutputVariant2RecoveryOperation = TypedDict('WorkflowRunOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
WorkflowRunOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowRunOutputVariant2Recovery = TypedDict('WorkflowRunOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[WorkflowRunOutputVariant2RecoveryOperation],
})
WorkflowRunOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class WorkflowRunOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: WorkflowRunOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: WorkflowRunOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(WorkflowRunOutput).
WorkflowRunOutput = Union[WorkflowRunOutputVariant2, WorkflowRunOutputVariant1]

_WorkflowRunInputAdapter = TypeAdapter(WorkflowRunInput)
_WorkflowRunOutputAdapter = TypeAdapter(WorkflowRunOutput)