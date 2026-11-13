from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class HarvestPaaInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    pages: Union[Annotated[int, Field(ge=1, le=2)], None] = Field(None, alias='pages', description='Organic result pages to capture. Default 1, maximum 2. Page 2 is captured when available before harvesting PAA on the original first page; it does not add a second PAA graph. Pagination output reports the pages actually captured.')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='The search topic, exactly as it should be searched, e.g. "best hvac company in Denver". Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.')
    location: Union[str, None] = Field(None, alias='location', description='Where Google should think the searcher is, e.g. "Denver, CO". Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.')
    max_questions: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='maxQuestions', description='PAA questions to extract. Default 30, maximum 100. Use 10 for quick probes and 100 for deep research. Billed per extracted question; unused hold refunded.')
    gl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='gl', description='Google country code inferred from location or user language.')
    hl: Union[str, None] = Field(None, alias='hl', description='Google interface/content language inferred from the user request.')
    device: Union[Literal['desktop', 'mobile'], None] = Field(None, alias='device', description='SERP device context. Use mobile only for mobile rankings.')
    idempotency_key: Union[Annotated[str, Field(min_length=8, max_length=200)], None] = Field(None, alias='idempotencyKey', description='Optional duplicate-start key. Reuse it only after an uncertain or lost response to the same logical call; use a new key for an intentional retry after a terminal failure. This is not the run identifier.')
    serp_identity: Union[str, None] = Field(None, alias='serpIdentity', description='Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.')
    include_all_serp_features: Union[bool, None] = Field(None, alias='includeAllSerpFeatures', description='Capture every optional same-page SERP surface: local pack, forums, videos, AI Overview/AI Mode, and What People Are Saying.')
    include_local_pack: Union[bool, None] = Field(None, alias='includeLocalPack', description='Include Google local/map-pack businesses and merge their entity IDs.')
    include_forums: Union[bool, None] = Field(None, alias='includeForums', description='Include Discussions and Forums results.')
    include_videos: Union[bool, None] = Field(None, alias='includeVideos', description='Include video result names and URLs present on the original SERP.')
    include_ai_overview: Union[bool, None] = Field(None, alias='includeAiOverview', description='Include AI Overview and AI Mode text and citations when present.')
    include_what_people_saying: Union[bool, None] = Field(None, alias='includeWhatPeopleSaying', description='Include the What People Are Saying social surface when present.')


HarvestPaaOutputVariant1PaaLifecycleVariant1RetryBreakdown = TypedDict('HarvestPaaOutputVariant1PaaLifecycleVariant1RetryBreakdown', {
    'controlRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'browserRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'providerFallbacks': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'runtimeRecoveries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'idempotentReplays': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
HarvestPaaOutputVariant1PaaLifecycleVariant1RetryBreakdown.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1PaaLifecycleVariant1 = TypedDict('HarvestPaaOutputVariant1PaaLifecycleVariant1', {
    'requestedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'questionsFound': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'targetStatus': Required[Literal['met', 'not_met']],
    'discoveryStatus': Required[Literal['in_progress', 'target_reached', 'frontier_exhausted', 'no_paa_observed', 'interrupted', 'recovery_exhausted']],
    'materialStatus': Required[Literal['complete', 'partial']],
    'completionReason': Required[str],
    'automaticRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'retryBreakdown': Required[HarvestPaaOutputVariant1PaaLifecycleVariant1RetryBreakdown],
    'knownQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'processedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failedInteractions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'noGrowthConfirmations': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'visibleControls': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'eligibleControls': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'dispatchedInteractions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'confirmedInteractions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'unconfirmedInteractions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
HarvestPaaOutputVariant1PaaLifecycleVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1PhaseTimingsVariant1 = TypedDict('HarvestPaaOutputVariant1PhaseTimingsVariant1', {
    'providerConnectMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'navigationMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'serpParseMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaExpansionMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'linkResolutionMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalServerMs': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
HarvestPaaOutputVariant1PhaseTimingsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1PaginationVariant1 = TypedDict('HarvestPaaOutputVariant1PaginationVariant1', {
    'requestedPages': Required[Union[Literal[1], Literal[2]]],
    'capturedPages': Required[Union[Literal[1], Literal[2]]],
    'page2Status': Required[Literal['not_requested', 'not_attempted', 'captured', 'unavailable', 'failed']],
    'page1OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'page2OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failureCode': NotRequired[Literal['missing_next', 'invalid_next', 'empty_page', 'captcha', 'timeout', 'navigation_error', 'unsupported_driver']],
})
HarvestPaaOutputVariant1PaginationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1QuestionsItemSourcesItem = TypedDict('HarvestPaaOutputVariant1QuestionsItemSourcesItem', {
    'url': Required[str],
    'rawUrl': Required[str],
    'resolvedUrl': Required[Union[str, None]],
    'linkType': Required[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': Required[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
    'title': Required[Union[str, None]],
    'site': Required[Union[str, None]],
    'description': NotRequired[Union[str, None]],
})
HarvestPaaOutputVariant1QuestionsItemSourcesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1QuestionsItem = TypedDict('HarvestPaaOutputVariant1QuestionsItem', {
    'questionId': Required[str],
    'googleLinkId': Required[Union[str, None]],
    'googleEvidenceId': Required[Union[str, None]],
    'question': Required[str],
    'answer': Required[Union[str, None]],
    'answerExpansionIncomplete': NotRequired[bool],
    'sources': Required[list[HarvestPaaOutputVariant1QuestionsItemSourcesItem]],
    'sourceTitle': Required[Union[str, None]],
    'sourceSite': Required[Union[str, None]],
    'sourceUrl': Required[Union[str, None]],
})
HarvestPaaOutputVariant1QuestionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1OrganicResultsItem = TypedDict('HarvestPaaOutputVariant1OrganicResultsItem', {
    'position': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'sourcePage': NotRequired[Union[Literal[1], Literal[2]]],
    'title': Required[str],
    'url': Required[str],
    'rawUrl': Required[str],
    'resolvedUrl': Required[Union[str, None]],
    'linkType': Required[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': Required[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
    'domain': Required[str],
    'snippet': Required[Union[str, None]],
})
HarvestPaaOutputVariant1OrganicResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1AiOverviewVariant1CitationsItem = TypedDict('HarvestPaaOutputVariant1AiOverviewVariant1CitationsItem', {
    'text': Required[str],
    'href': Required[str],
    'rawUrl': Required[str],
    'resolvedUrl': Required[Union[str, None]],
    'linkType': Required[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': Required[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
})
HarvestPaaOutputVariant1AiOverviewVariant1CitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1AiOverviewVariant1 = TypedDict('HarvestPaaOutputVariant1AiOverviewVariant1', {
    'detected': Required[bool],
    'text': Required[Union[str, None]],
    'citations': Required[list[HarvestPaaOutputVariant1AiOverviewVariant1CitationsItem]],
    'expanded': Required[bool],
    'fullyExpanded': Required[bool],
    'sections': Required[list[str]],
    'shareUrl': NotRequired[Union[str, None]],
})
HarvestPaaOutputVariant1AiOverviewVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1EntityIdsVariant1EntitiesItem = TypedDict('HarvestPaaOutputVariant1EntityIdsVariant1EntitiesItem', {
    'name': Required[str],
    'kgId': Required[Union[str, None]],
    'cid': Required[Union[str, None]],
    'gcid': Required[Union[str, None]],
})
HarvestPaaOutputVariant1EntityIdsVariant1EntitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant1EntityIdsVariant1 = TypedDict('HarvestPaaOutputVariant1EntityIdsVariant1', {
    'entities': Required[list[HarvestPaaOutputVariant1EntityIdsVariant1EntitiesItem]],
    'kgIds': Required[list[str]],
    'cids': Required[list[str]],
    'gcids': Required[list[str]],
})
HarvestPaaOutputVariant1EntityIdsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class HarvestPaaOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    query: str = Field(..., alias='query', description='')
    location: Union[str, None] = Field(..., alias='location', description='')
    question_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='questionCount', description='')
    paa_incomplete_answers: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='paaIncompleteAnswers', description='')
    completion_status: Union[str, None] = Field(..., alias='completionStatus', description='')
    result_quality: Union[str, None] = Field(..., alias='resultQuality', description='')
    degraded_result: Union[bool, None] = Field(..., alias='degradedResult', description='')
    degradation_reasons: list[str] = Field(..., alias='degradationReasons', description='')
    retry_recommended: Union[bool, None] = Field(..., alias='retryRecommended', description='')
    paa_lifecycle: Union[HarvestPaaOutputVariant1PaaLifecycleVariant1, None] = Field(..., alias='paaLifecycle', description='')
    phase_timings: Union[HarvestPaaOutputVariant1PhaseTimingsVariant1, None] = Field(..., alias='phaseTimings', description='')
    pagination: Union[HarvestPaaOutputVariant1PaginationVariant1, None] = Field(..., alias='pagination', description='')
    questions: list[HarvestPaaOutputVariant1QuestionsItem] = Field(..., alias='questions', description='')
    organic_results: list[HarvestPaaOutputVariant1OrganicResultsItem] = Field(..., alias='organicResults', description='')
    ai_overview: Union[HarvestPaaOutputVariant1AiOverviewVariant1, None] = Field(..., alias='aiOverview', description='')
    entity_ids: Union[HarvestPaaOutputVariant1EntityIdsVariant1, None] = Field(..., alias='entityIds', description='')
    duration_ms: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(..., alias='durationMs', description='')


HarvestPaaOutputVariant2DeliveryArtifactsItem = TypedDict('HarvestPaaOutputVariant2DeliveryArtifactsItem', {
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
HarvestPaaOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant2DeliveryAvailableExportsItem = TypedDict('HarvestPaaOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
HarvestPaaOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('HarvestPaaOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
HarvestPaaOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant2Delivery = TypedDict('HarvestPaaOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[HarvestPaaOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[HarvestPaaOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[HarvestPaaOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
HarvestPaaOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant2RecoveryOperation = TypedDict('HarvestPaaOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
HarvestPaaOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaOutputVariant2Recovery = TypedDict('HarvestPaaOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[HarvestPaaOutputVariant2RecoveryOperation],
})
HarvestPaaOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class HarvestPaaOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: HarvestPaaOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: HarvestPaaOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(HarvestPaaOutput).
HarvestPaaOutput = Union[HarvestPaaOutputVariant1, HarvestPaaOutputVariant2]

_HarvestPaaInputAdapter = TypeAdapter(HarvestPaaInput)
_HarvestPaaOutputAdapter = TypeAdapter(HarvestPaaOutput)