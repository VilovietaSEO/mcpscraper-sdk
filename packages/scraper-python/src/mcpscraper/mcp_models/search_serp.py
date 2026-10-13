from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SearchSerpInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    mode: Union[Literal['light', 'full'], None] = Field(None, alias='mode', description='Light returns organic results. Full adds available same-page features for an unfiltered one-page search. Date-filtered, two-page, and browser-backup results contain organic listings only and mark rich features unsupported.')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='The search topic, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.')
    location: Union[str, None] = Field(None, alias='location', description='Compatibility field. Ordinary search ignores this. Include a place in query when needed.')
    gl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='gl', description='Compatibility field. Ordinary search uses its fixed default market.')
    hl: Union[str, None] = Field(None, alias='hl', description='Compatibility field. Ordinary search uses its fixed default language.')
    device: Union[Literal['desktop', 'mobile'], None] = Field(None, alias='device', description='Compatibility field. Ordinary search uses desktop results.')
    idempotency_key: Union[Annotated[str, Field(min_length=8, max_length=200)], None] = Field(None, alias='idempotencyKey', description='Retry key: reuse after a timeout to avoid re-billing. New key per search.')
    serp_identity: Union[str, None] = Field(None, alias='serpIdentity', description='Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.')
    pages: Union[Annotated[int, Field(ge=1, le=2)], None] = Field(None, alias='pages', description='One page by default. Set 2 only when the user explicitly requests two pages; two-page results include organic listings only; if page 2 is unavailable, page 1 is returned and billed when available.')
    recency: Union[Literal['week', 'month'], None] = Field(None, alias='recency', description='Limit Google results to the past week or past month. A date-filtered search uses the managed browser and returns organic listings only. It costs 35 Credits for one page or 70 Credits when two requested pages are delivered. Omit for unfiltered results.')


SearchSerpOutputVariant1PaginationVariant1 = TypedDict('SearchSerpOutputVariant1PaginationVariant1', {
    'requestedPages': Required[Union[Literal[1], Literal[2]]],
    'capturedPages': Required[Union[Literal[1], Literal[2]]],
    'page2Status': Required[Literal['not_requested', 'not_attempted', 'captured', 'unavailable', 'failed']],
    'page1OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'page2OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failureCode': NotRequired[Literal['missing_next', 'invalid_next', 'empty_page', 'captcha', 'timeout', 'navigation_error', 'unsupported_driver']],
})
SearchSerpOutputVariant1PaginationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1SerpCompletenessVariant1PaginationPageResultCountsItem = TypedDict('SearchSerpOutputVariant1SerpCompletenessVariant1PaginationPageResultCountsItem', {
    'page': Required[Union[Literal[1], Literal[2]]],
    'resultCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
SearchSerpOutputVariant1SerpCompletenessVariant1PaginationPageResultCountsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1SerpCompletenessVariant1Pagination = TypedDict('SearchSerpOutputVariant1SerpCompletenessVariant1Pagination', {
    'status': Required[Literal['complete', 'incomplete']],
    'requestedPages': Required[Annotated[list[Union[Literal[1], Literal[2]]], Field(min_length=1, max_length=2)]],
    'attemptedPages': Required[Annotated[list[Union[Literal[1], Literal[2]]], Field(max_length=2)]],
    'capturedPages': Required[Annotated[list[Union[Literal[1], Literal[2]]], Field(max_length=2)]],
    'pageResultCounts': Required[Annotated[list[SearchSerpOutputVariant1SerpCompletenessVariant1PaginationPageResultCountsItem], Field(max_length=2)]],
    'providerRequestCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failureCode': Required[Union[str, None]],
})
SearchSerpOutputVariant1SerpCompletenessVariant1Pagination.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1SerpCompletenessVariant1Features = TypedDict('SearchSerpOutputVariant1SerpCompletenessVariant1Features', {
    'localPack': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
    'forums': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
    'videos': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
    'aiOverview': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
    'whatPeopleSaying': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
})
SearchSerpOutputVariant1SerpCompletenessVariant1Features.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1SerpCompletenessVariant1QueryIntegrity = TypedDict('SearchSerpOutputVariant1SerpCompletenessVariant1QueryIntegrity', {
    'status': Required[Literal['matched', 'unresolved_location', 'query_mismatch']],
    'queryHash': Required[str],
    'normalizedQueryTokens': Required[list[str]],
    'canonicalLocation': Required[Union[str, None]],
    'locationResolutionSource': Required[str],
    'locationAmbiguousCandidates': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'uulePresent': Required[bool],
    'uuleHash': Required[Union[str, None]],
    'outboundProviderMethod': Required[str],
    'finalQueryHash': Required[Union[str, None]],
})
SearchSerpOutputVariant1SerpCompletenessVariant1QueryIntegrity.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1SerpCompletenessVariant1 = TypedDict('SearchSerpOutputVariant1SerpCompletenessVariant1', {
    'pagination': Required[SearchSerpOutputVariant1SerpCompletenessVariant1Pagination],
    'features': Required[SearchSerpOutputVariant1SerpCompletenessVariant1Features],
    'queryIntegrity': Required[SearchSerpOutputVariant1SerpCompletenessVariant1QueryIntegrity],
    'failureStage': Required[Union[Literal['provider_transport', 'invalid_payload', 'serp_readiness', 'query_integrity', 'pagination', 'optional_feature_parsing', 'unknown'], None]],
})
SearchSerpOutputVariant1SerpCompletenessVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1OrganicResultsItem = TypedDict('SearchSerpOutputVariant1OrganicResultsItem', {
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
SearchSerpOutputVariant1OrganicResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1LocalPackItem = TypedDict('SearchSerpOutputVariant1LocalPackItem', {
    'position': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'name': Required[str],
    'rating': Required[Union[str, None]],
    'reviewCount': Required[Union[str, None]],
    'websiteUrl': Required[Union[str, None]],
})
SearchSerpOutputVariant1LocalPackItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1AiOverviewVariant1CitationsItem = TypedDict('SearchSerpOutputVariant1AiOverviewVariant1CitationsItem', {
    'text': Required[str],
    'href': Required[str],
    'rawUrl': Required[str],
    'resolvedUrl': Required[Union[str, None]],
    'linkType': Required[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': Required[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
})
SearchSerpOutputVariant1AiOverviewVariant1CitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1AiOverviewVariant1 = TypedDict('SearchSerpOutputVariant1AiOverviewVariant1', {
    'detected': Required[bool],
    'text': Required[Union[str, None]],
    'citations': Required[list[SearchSerpOutputVariant1AiOverviewVariant1CitationsItem]],
    'expanded': Required[bool],
    'fullyExpanded': Required[bool],
    'sections': Required[list[str]],
    'shareUrl': NotRequired[Union[str, None]],
})
SearchSerpOutputVariant1AiOverviewVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1AiModeVariant1CitationsItem = TypedDict('SearchSerpOutputVariant1AiModeVariant1CitationsItem', {
    'text': Required[str],
    'href': Required[str],
})
SearchSerpOutputVariant1AiModeVariant1CitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1AiModeVariant1 = TypedDict('SearchSerpOutputVariant1AiModeVariant1', {
    'detected': Required[bool],
    'text': Required[Union[str, None]],
    'citations': Required[list[SearchSerpOutputVariant1AiModeVariant1CitationsItem]],
})
SearchSerpOutputVariant1AiModeVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1ForumsItem = TypedDict('SearchSerpOutputVariant1ForumsItem', {
    'title': Required[str],
    'source': Required[str],
    'url': Required[str],
})
SearchSerpOutputVariant1ForumsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1VideosItem = TypedDict('SearchSerpOutputVariant1VideosItem', {
    'type': Required[str],
    'title': Required[str],
    'channel': Required[str],
    'platform': Required[str],
    'duration': Required[str],
    'url': Required[str],
})
SearchSerpOutputVariant1VideosItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1PaaPreviewItem = TypedDict('SearchSerpOutputVariant1PaaPreviewItem', {
    'question': Required[str],
    'answer': Required[Union[str, None]],
    'url': Required[Union[str, None]],
    'sourceTitle': NotRequired[Union[str, None]],
    'sourceName': NotRequired[Union[str, None]],
    'displayLink': NotRequired[Union[str, None]],
})
SearchSerpOutputVariant1PaaPreviewItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1AdditionalSerpFeaturesItemItemsItem = TypedDict('SearchSerpOutputVariant1AdditionalSerpFeaturesItemItemsItem', {
    'title': Required[Union[str, None]],
    'url': Required[Union[str, None]],
    'description': Required[Union[str, None]],
    'position': Required[Union[Union[float, int], None]],
})
SearchSerpOutputVariant1AdditionalSerpFeaturesItemItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1AdditionalSerpFeaturesItem = TypedDict('SearchSerpOutputVariant1AdditionalSerpFeaturesItem', {
    'name': Required[str],
    'attributes': Required[dict[str, Union[str, Union[float, int], bool, None]]],
    'items': Required[list[SearchSerpOutputVariant1AdditionalSerpFeaturesItemItemsItem]],
})
SearchSerpOutputVariant1AdditionalSerpFeaturesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1EntityIdsVariant1EntitiesItem = TypedDict('SearchSerpOutputVariant1EntityIdsVariant1EntitiesItem', {
    'name': Required[str],
    'kgId': Required[Union[str, None]],
    'cid': Required[Union[str, None]],
    'gcid': Required[Union[str, None]],
})
SearchSerpOutputVariant1EntityIdsVariant1EntitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1EntityIdsVariant1 = TypedDict('SearchSerpOutputVariant1EntityIdsVariant1', {
    'entities': Required[list[SearchSerpOutputVariant1EntityIdsVariant1EntitiesItem]],
    'kgIds': Required[list[str]],
    'cids': Required[list[str]],
    'gcids': Required[list[str]],
})
SearchSerpOutputVariant1EntityIdsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant1PhaseTimingsVariant1 = TypedDict('SearchSerpOutputVariant1PhaseTimingsVariant1', {
    'providerConnectMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'navigationMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'serpParseMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaExpansionMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'linkResolutionMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalServerMs': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
SearchSerpOutputVariant1PhaseTimingsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SearchSerpOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    mode: Literal['light', 'full'] = Field(..., alias='mode', description='')
    job_id: Union[str, None] = Field(..., alias='jobId', description='')
    status: Literal['pending', 'running', 'done'] = Field(..., alias='status', description='')
    status_tool: Union[str, None] = Field(..., alias='statusTool', description='')
    replayed: bool = Field(..., alias='replayed', description='')
    query: str = Field(..., alias='query', description='')
    location: Union[str, None] = Field(..., alias='location', description='')
    result_quality: Union[str, None] = Field(..., alias='resultQuality', description='')
    degraded_result: Union[bool, None] = Field(..., alias='degradedResult', description='')
    degradation_reasons: list[str] = Field(..., alias='degradationReasons', description='')
    retry_recommended: Union[bool, None] = Field(..., alias='retryRecommended', description='')
    pagination: Union[SearchSerpOutputVariant1PaginationVariant1, None] = Field(..., alias='pagination', description='')
    serp_completeness: Union[SearchSerpOutputVariant1SerpCompletenessVariant1, None] = Field(..., alias='serpCompleteness', description='')
    organic_results: list[SearchSerpOutputVariant1OrganicResultsItem] = Field(..., alias='organicResults', description='')
    local_pack: list[SearchSerpOutputVariant1LocalPackItem] = Field(..., alias='localPack', description='')
    ai_overview: Union[SearchSerpOutputVariant1AiOverviewVariant1, None] = Field(..., alias='aiOverview', description='')
    ai_mode: Union[SearchSerpOutputVariant1AiModeVariant1, None] = Field(..., alias='aiMode', description='')
    forums: list[SearchSerpOutputVariant1ForumsItem] = Field(..., alias='forums', description='')
    videos: list[SearchSerpOutputVariant1VideosItem] = Field(..., alias='videos', description='')
    what_people_saying: list[dict[str, Any]] = Field(..., alias='whatPeopleSaying', description='')
    paa_preview: list[SearchSerpOutputVariant1PaaPreviewItem] = Field(..., alias='paaPreview', description='')
    additional_serp_features: list[SearchSerpOutputVariant1AdditionalSerpFeaturesItem] = Field(..., alias='additionalSerpFeatures', description='')
    feature_status: dict[str, Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']] = Field(..., alias='featureStatus', description='')
    feature_pages: Annotated[list[dict[str, Any]], Field(max_length=2)] = Field(..., alias='featurePages', description='')
    entity_ids: Union[SearchSerpOutputVariant1EntityIdsVariant1, None] = Field(..., alias='entityIds', description='')
    phase_timings: Union[SearchSerpOutputVariant1PhaseTimingsVariant1, None] = Field(..., alias='phaseTimings', description='')
    duration_ms: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='durationMs', description='')
    attempt_count: Annotated[int, Field(ge=1, le=9007199254740991)] = Field(..., alias='attemptCount', description='')


SearchSerpOutputVariant2DeliveryArtifactsItem = TypedDict('SearchSerpOutputVariant2DeliveryArtifactsItem', {
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
SearchSerpOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SearchSerpOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SearchSerpOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant2Delivery = TypedDict('SearchSerpOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SearchSerpOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SearchSerpOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SearchSerpOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant2RecoveryOperation = TypedDict('SearchSerpOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SearchSerpOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpOutputVariant2Recovery = TypedDict('SearchSerpOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SearchSerpOutputVariant2RecoveryOperation],
})
SearchSerpOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SearchSerpOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SearchSerpOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SearchSerpOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SearchSerpOutput).
SearchSerpOutput = Union[SearchSerpOutputVariant1, SearchSerpOutputVariant2]

_SearchSerpInputAdapter = TypeAdapter(SearchSerpInput)
_SearchSerpOutputAdapter = TypeAdapter(SearchSerpOutput)