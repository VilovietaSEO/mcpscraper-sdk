from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class WorkflowListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    include_recipes: Union[bool, None] = Field(None, alias='includeRecipes', description='Include high-level AI-facing recipes (market analysis, ICP research, CRO audits, content gaps, etc).')


WorkflowListOutputVariant1WorkflowsItem = TypedDict('WorkflowListOutputVariant1WorkflowsItem', {
    'id': Required[str],
    'title': Required[str],
    'description': Required[str],
})
WorkflowListOutputVariant1WorkflowsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowListOutputVariant1RecipesItem = TypedDict('WorkflowListOutputVariant1RecipesItem', {
    'id': Required[str],
    'title': Required[str],
    'description': Required[str],
    'primaryWorkflowId': Required[Union[str, None]],
    'recommendedTools': Required[list[str]],
    'requiredInputs': Required[list[str]],
    'optionalInputs': Required[list[str]],
    'produces': Required[list[str]],
    'runHint': Required[str],
})
WorkflowListOutputVariant1RecipesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class WorkflowListOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    workflows: list[WorkflowListOutputVariant1WorkflowsItem] = Field(..., alias='workflows', description='')
    recipes: list[WorkflowListOutputVariant1RecipesItem] = Field(..., alias='recipes', description='')


WorkflowListOutputVariant2DeliveryArtifactsItem = TypedDict('WorkflowListOutputVariant2DeliveryArtifactsItem', {
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
WorkflowListOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowListOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('WorkflowListOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
WorkflowListOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowListOutputVariant2Delivery = TypedDict('WorkflowListOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[WorkflowListOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[WorkflowListOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
WorkflowListOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowListOutputVariant2RecoveryOperation = TypedDict('WorkflowListOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
WorkflowListOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowListOutputVariant2Recovery = TypedDict('WorkflowListOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[WorkflowListOutputVariant2RecoveryOperation],
})
WorkflowListOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class WorkflowListOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: WorkflowListOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: WorkflowListOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(WorkflowListOutput).
WorkflowListOutput = Union[WorkflowListOutputVariant2, WorkflowListOutputVariant1]

_WorkflowListInputAdapter = TypeAdapter(WorkflowListInput)
_WorkflowListOutputAdapter = TypeAdapter(WorkflowListOutput)