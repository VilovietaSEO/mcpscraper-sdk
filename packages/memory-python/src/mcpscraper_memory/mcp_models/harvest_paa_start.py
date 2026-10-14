from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class HarvestPaaStartInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    pages: Union[Annotated[int, Field(ge=1, le=2)], None] = Field(None, alias='pages', description='Organic result pages to capture. Default 1, maximum 2. Page 2 is captured when available before harvesting PAA on the original first page; it does not add a second PAA graph. Pagination output reports the pages actually captured.')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='The search topic, exactly as it should be searched, e.g. "best hvac company in Denver". Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.')
    location: Union[str, None] = Field(None, alias='location', description='Where Google should think the searcher is, e.g. "Denver, CO". Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.')
    max_questions: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='maxQuestions', description='PAA questions to extract. Default 30, maximum 100. Use 10 for quick probes and 100 for deep research. Billed per extracted question; unused hold refunded.')
    gl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='gl', description='Google country code inferred from location or user language.')
    hl: Union[str, None] = Field(None, alias='hl', description='Google interface/content language inferred from the user request.')
    device: Union[Literal['desktop', 'mobile'], None] = Field(None, alias='device', description='SERP device context. Use mobile only for mobile rankings.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required durable recovery identity for this logical harvest. Reuse this exact key only after an uncertain/lost response or while recovering the same job; never replace it merely because polling timed out.')
    serp_identity: Union[str, None] = Field(None, alias='serpIdentity', description='Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.')
    include_all_serp_features: Union[bool, None] = Field(None, alias='includeAllSerpFeatures', description='Capture every optional same-page SERP surface: local pack, forums, videos, AI Overview/AI Mode, and What People Are Saying.')
    include_local_pack: Union[bool, None] = Field(None, alias='includeLocalPack', description='Include Google local/map-pack businesses and merge their entity IDs.')
    include_forums: Union[bool, None] = Field(None, alias='includeForums', description='Include Discussions and Forums results.')
    include_videos: Union[bool, None] = Field(None, alias='includeVideos', description='Include video result names and URLs present on the original SERP.')
    include_ai_overview: Union[bool, None] = Field(None, alias='includeAiOverview', description='Include AI Overview and AI Mode text and citations when present.')
    include_what_people_saying: Union[bool, None] = Field(None, alias='includeWhatPeopleSaying', description='Include the What People Are Saying social surface when present.')


HarvestPaaStartOutputVariant1StatusVariant1 = TypedDict('HarvestPaaStartOutputVariant1StatusVariant1', {
    'state': Required[Literal['pending']],
    'terminal': Required[Literal[False]],
    'pollAfterSeconds': Required[Annotated[int, Field(ge=20, le=9007199254740991)]],
    'retryGuidance': Required[str],
})
HarvestPaaStartOutputVariant1StatusVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStartOutputVariant1StatusVariant2 = TypedDict('HarvestPaaStartOutputVariant1StatusVariant2', {
    'state': Required[Literal['running']],
    'terminal': Required[Literal[False]],
    'pollAfterSeconds': Required[Annotated[int, Field(ge=20, le=9007199254740991)]],
    'retryGuidance': Required[str],
})
HarvestPaaStartOutputVariant1StatusVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStartOutputVariant1StatusVariant3 = TypedDict('HarvestPaaStartOutputVariant1StatusVariant3', {
    'state': Required[Literal['done']],
    'terminal': Required[Literal[True]],
    'pollAfterSeconds': Required[None],
    'retryGuidance': Required[str],
})
HarvestPaaStartOutputVariant1StatusVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStartOutputVariant1StatusVariant4 = TypedDict('HarvestPaaStartOutputVariant1StatusVariant4', {
    'state': Required[Literal['failed']],
    'terminal': Required[Literal[True]],
    'pollAfterSeconds': Required[None],
    'retryGuidance': Required[str],
})
HarvestPaaStartOutputVariant1StatusVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStartOutputVariant1StatusVariant5 = TypedDict('HarvestPaaStartOutputVariant1StatusVariant5', {
    'state': Required[Literal['cancelled']],
    'terminal': Required[Literal[True]],
    'pollAfterSeconds': Required[None],
    'retryGuidance': Required[str],
})
HarvestPaaStartOutputVariant1StatusVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStartOutputVariant1Execution = TypedDict('HarvestPaaStartOutputVariant1Execution', {
    'state': Required[Literal['unknown']],
    'physicalOutcome': Required[Literal['unknown']],
    'holdState': Required[Literal['held', 'unconfirmed']],
    'retryGuidance': Required[str],
})
HarvestPaaStartOutputVariant1Execution.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class HarvestPaaStartOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    operation_id: str = Field(..., alias='operationId', description='')
    task_id: str = Field(..., alias='taskId', description='')
    status: Union[HarvestPaaStartOutputVariant1StatusVariant1, HarvestPaaStartOutputVariant1StatusVariant2, HarvestPaaStartOutputVariant1StatusVariant3, HarvestPaaStartOutputVariant1StatusVariant4, HarvestPaaStartOutputVariant1StatusVariant5] = Field(..., alias='status', description='')
    execution: Union[HarvestPaaStartOutputVariant1Execution, None] = Field(None, alias='execution', description='')
    replayed: bool = Field(..., alias='replayed', description='')
    status_tool: Literal['harvest_paa_status'] = Field(..., alias='statusTool', description='')


HarvestPaaStartOutputVariant2DeliveryArtifactsItem = TypedDict('HarvestPaaStartOutputVariant2DeliveryArtifactsItem', {
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
HarvestPaaStartOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStartOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('HarvestPaaStartOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
HarvestPaaStartOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStartOutputVariant2Delivery = TypedDict('HarvestPaaStartOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[HarvestPaaStartOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[HarvestPaaStartOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
HarvestPaaStartOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStartOutputVariant2RecoveryOperation = TypedDict('HarvestPaaStartOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
HarvestPaaStartOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStartOutputVariant2Recovery = TypedDict('HarvestPaaStartOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[HarvestPaaStartOutputVariant2RecoveryOperation],
})
HarvestPaaStartOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class HarvestPaaStartOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: HarvestPaaStartOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: HarvestPaaStartOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(HarvestPaaStartOutput).
HarvestPaaStartOutput = Union[HarvestPaaStartOutputVariant1, HarvestPaaStartOutputVariant2]

_HarvestPaaStartInputAdapter = TypeAdapter(HarvestPaaStartInput)
_HarvestPaaStartOutputAdapter = TypeAdapter(HarvestPaaStartOutput)