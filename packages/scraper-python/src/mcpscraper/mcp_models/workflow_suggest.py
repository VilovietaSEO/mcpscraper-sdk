from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class WorkflowSuggestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    goal: Annotated[str, Field(min_length=1)] = Field(..., alias='goal', description='The user goal or job to route, e.g. "market analysis for roofers in Tennessee", "ICP research for med spas", "CRO audit for this URL", or "brand design briefing".')
    query: Union[str, None] = Field(None, alias='query', description='Business category, niche, or Maps query when known.')
    keyword: Union[str, None] = Field(None, alias='keyword', description='Search keyword, audience problem, or content topic when known.')
    domain: Union[str, None] = Field(None, alias='domain', description='Target domain or brand domain when known.')
    url: Union[str, None] = Field(None, alias='url', description='Target URL when the workflow should inspect a specific page.')
    location: Union[str, None] = Field(None, alias='location', description='City/region/country for localized research, e.g. Denver, CO.')
    state: Union[str, None] = Field(None, alias='state', description='US state abbreviation or name for state-wide market research.')
    max_suggestions: Union[Annotated[int, Field(ge=1, le=8)], None] = Field(None, alias='maxSuggestions', description='Number of matching workflow recipes to return.')


WorkflowSuggestOutputVariant1SuggestionsItem = TypedDict('WorkflowSuggestOutputVariant1SuggestionsItem', {
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
WorkflowSuggestOutputVariant1SuggestionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class WorkflowSuggestOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    goal: str = Field(..., alias='goal', description='')
    suggestions: list[WorkflowSuggestOutputVariant1SuggestionsItem] = Field(..., alias='suggestions', description='')


WorkflowSuggestOutputVariant2DeliveryArtifactsItem = TypedDict('WorkflowSuggestOutputVariant2DeliveryArtifactsItem', {
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
WorkflowSuggestOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowSuggestOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('WorkflowSuggestOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
WorkflowSuggestOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowSuggestOutputVariant2Delivery = TypedDict('WorkflowSuggestOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[WorkflowSuggestOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[WorkflowSuggestOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
WorkflowSuggestOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowSuggestOutputVariant2RecoveryOperation = TypedDict('WorkflowSuggestOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
WorkflowSuggestOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


WorkflowSuggestOutputVariant2Recovery = TypedDict('WorkflowSuggestOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[WorkflowSuggestOutputVariant2RecoveryOperation],
})
WorkflowSuggestOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class WorkflowSuggestOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: WorkflowSuggestOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: WorkflowSuggestOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(WorkflowSuggestOutput).
WorkflowSuggestOutput = Union[WorkflowSuggestOutputVariant2, WorkflowSuggestOutputVariant1]

_WorkflowSuggestInputAdapter = TypeAdapter(WorkflowSuggestInput)
_WorkflowSuggestOutputAdapter = TypeAdapter(WorkflowSuggestOutput)