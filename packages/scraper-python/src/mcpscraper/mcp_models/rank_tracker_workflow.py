from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RankTrackerWorkflowInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    project_name: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='projectName', description='Optional name for the rank tracker project, client, or campaign.')
    target_domain: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='targetDomain', description='Primary domain to track in organic results, AI Overview citations, and PAA sources.')
    target_business_name: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='targetBusinessName', description='Primary Google Business Profile/brand name to match in Maps results, and the brand name looked for in assistant answers. Supply it when matching one business against Maps results or tracking ai_answers.')
    tracking_modes: Union[Annotated[list[Literal['maps', 'organic', 'ai_overview', 'paa', 'ai_answers']], Field(min_length=1, max_length=5)], None] = Field(None, alias='trackingModes', description='Rank tracker surfaces to build: maps, organic, ai_overview, paa, and ai_answers (whether ChatGPT, Gemini or Claude name the brand when asked a question). ai_answers is not in the default set.')
    prompts: Union[Annotated[list[Annotated[str, Field(min_length=3)]], Field(max_length=200)], None] = Field(None, alias='prompts', description='For ai_answers: the full-sentence questions to ask the assistants, e.g. "What is the best CRM for roofing companies?". Leave empty to derive questions from keywords downstream.')
    assistants: Union[Annotated[list[Literal['chatgpt', 'gemini', 'claude']], Field(min_length=1, max_length=3)], None] = Field(None, alias='assistants', description='For ai_answers: which assistants to ask. chatgpt and gemini need no sign-in; claude needs a saved signed-in profile.')
    runs_per_prompt: Union[Annotated[int, Field(ge=1, le=10)], None] = Field(None, alias='runsPerPrompt', description='For ai_answers: how many times each question is asked on each assistant in one requested batch. Answers vary between runs, so the mention rate is the share of runs that name the brand.')
    keywords: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(max_length=200)], None] = Field(None, alias='keywords', description='Seed keywords or service queries to track. Leave empty to derive from user input downstream.')
    locations: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(max_length=100)], None] = Field(None, alias='locations', description='Markets, cities, ZIPs, or service areas to track, e.g. "Denver, CO".')
    competitors: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(max_length=100)], None] = Field(None, alias='competitors', description='Optional competitor domains or business names to persist as comparison targets. For ai_answers, competitor names are looked for in each answer beside the target brand.')
    database: Union[Literal['postgres', 'neon', 'supabase', 'sqlite', 'mysql'], None] = Field(None, alias='database', description='Database family to target when generating migrations.')
    include_dashboard: Union[bool, None] = Field(None, alias='includeDashboard', description='Include dashboard/reporting requirements.')
    include_alerts: Union[bool, None] = Field(None, alias='includeAlerts', description='Include saved change findings when manually comparing rank movement and SERP features.')
    notes: Union[Annotated[str, Field(max_length=4000)], None] = Field(None, alias='notes', description='Extra product, client, stack, or hosting requirements.')


RankTrackerWorkflowOutputVariant1RecommendedToolsItem = TypedDict('RankTrackerWorkflowOutputVariant1RecommendedToolsItem', {
    'tool': Required[str],
    'purpose': Required[str],
})
RankTrackerWorkflowOutputVariant1RecommendedToolsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RankTrackerWorkflowOutputVariant1TablesItem = TypedDict('RankTrackerWorkflowOutputVariant1TablesItem', {
    'name': Required[str],
    'purpose': Required[str],
    'keyColumns': Required[list[str]],
})
RankTrackerWorkflowOutputVariant1TablesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RankTrackerWorkflowOutputVariant1StepsItem = TypedDict('RankTrackerWorkflowOutputVariant1StepsItem', {
    'name': Required[str],
    'purpose': Required[str],
    'modes': Required[list[Literal['maps', 'organic', 'ai_overview', 'paa', 'ai_answers']]],
    'recommendedTools': Required[list[str]],
})
RankTrackerWorkflowOutputVariant1StepsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RankTrackerWorkflowOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    project_name: str = Field(..., alias='projectName', description='')
    target_domain: Union[str, None] = Field(..., alias='targetDomain', description='')
    target_business_name: Union[str, None] = Field(..., alias='targetBusinessName', description='')
    tracking_modes: list[Literal['maps', 'organic', 'ai_overview', 'paa', 'ai_answers']] = Field(..., alias='trackingModes', description='')
    assistants: list[Literal['chatgpt', 'gemini', 'claude']] = Field(..., alias='assistants', description='')
    runs_per_prompt: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='runsPerPrompt', description='')
    database: str = Field(..., alias='database', description='')
    recommended_tools: list[RankTrackerWorkflowOutputVariant1RecommendedToolsItem] = Field(..., alias='recommendedTools', description='')
    tables: list[RankTrackerWorkflowOutputVariant1TablesItem] = Field(..., alias='tables', description='')
    steps: list[RankTrackerWorkflowOutputVariant1StepsItem] = Field(..., alias='steps', description='')
    metrics: list[str] = Field(..., alias='metrics', description='')
    implementation_prompt: str = Field(..., alias='implementationPrompt', description='')


RankTrackerWorkflowOutputVariant2DeliveryArtifactsItem = TypedDict('RankTrackerWorkflowOutputVariant2DeliveryArtifactsItem', {
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
RankTrackerWorkflowOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RankTrackerWorkflowOutputVariant2DeliveryAvailableExportsItem = TypedDict('RankTrackerWorkflowOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
RankTrackerWorkflowOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RankTrackerWorkflowOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RankTrackerWorkflowOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RankTrackerWorkflowOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RankTrackerWorkflowOutputVariant2Delivery = TypedDict('RankTrackerWorkflowOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RankTrackerWorkflowOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[RankTrackerWorkflowOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RankTrackerWorkflowOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RankTrackerWorkflowOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RankTrackerWorkflowOutputVariant2RecoveryOperation = TypedDict('RankTrackerWorkflowOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RankTrackerWorkflowOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RankTrackerWorkflowOutputVariant2Recovery = TypedDict('RankTrackerWorkflowOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RankTrackerWorkflowOutputVariant2RecoveryOperation],
})
RankTrackerWorkflowOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RankTrackerWorkflowOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RankTrackerWorkflowOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RankTrackerWorkflowOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RankTrackerWorkflowOutput).
RankTrackerWorkflowOutput = Union[RankTrackerWorkflowOutputVariant1, RankTrackerWorkflowOutputVariant2]

_RankTrackerWorkflowInputAdapter = TypeAdapter(RankTrackerWorkflowInput)
_RankTrackerWorkflowOutputAdapter = TypeAdapter(RankTrackerWorkflowOutput)