from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SearchSerpStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    job_id: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='jobId', description='The jobId returned by search_serp.')


SearchSerpStatusOutputVariant1PaginationVariant1 = TypedDict('SearchSerpStatusOutputVariant1PaginationVariant1', {
    'requestedPages': Required[Union[Literal[1], Literal[2]]],
    'capturedPages': Required[Union[Literal[1], Literal[2]]],
    'page2Status': Required[Literal['not_requested', 'not_attempted', 'captured', 'unavailable', 'failed']],
    'page1OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'page2OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failureCode': NotRequired[Literal['missing_next', 'invalid_next', 'empty_page', 'captcha', 'timeout', 'navigation_error', 'unsupported_driver']],
})
SearchSerpStatusOutputVariant1PaginationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1SerpCompletenessVariant1PaginationPageResultCountsItem = TypedDict('SearchSerpStatusOutputVariant1SerpCompletenessVariant1PaginationPageResultCountsItem', {
    'page': Required[Union[Literal[1], Literal[2]]],
    'resultCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
SearchSerpStatusOutputVariant1SerpCompletenessVariant1PaginationPageResultCountsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1SerpCompletenessVariant1Pagination = TypedDict('SearchSerpStatusOutputVariant1SerpCompletenessVariant1Pagination', {
    'status': Required[Literal['complete', 'incomplete']],
    'requestedPages': Required[Annotated[list[Union[Literal[1], Literal[2]]], Field(min_length=1, max_length=2)]],
    'attemptedPages': Required[Annotated[list[Union[Literal[1], Literal[2]]], Field(max_length=2)]],
    'capturedPages': Required[Annotated[list[Union[Literal[1], Literal[2]]], Field(max_length=2)]],
    'pageResultCounts': Required[Annotated[list[SearchSerpStatusOutputVariant1SerpCompletenessVariant1PaginationPageResultCountsItem], Field(max_length=2)]],
    'providerRequestCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failureCode': Required[Union[str, None]],
})
SearchSerpStatusOutputVariant1SerpCompletenessVariant1Pagination.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1SerpCompletenessVariant1Features = TypedDict('SearchSerpStatusOutputVariant1SerpCompletenessVariant1Features', {
    'localPack': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
    'forums': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
    'videos': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
    'aiOverview': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
    'whatPeopleSaying': Required[Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']],
})
SearchSerpStatusOutputVariant1SerpCompletenessVariant1Features.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1SerpCompletenessVariant1QueryIntegrity = TypedDict('SearchSerpStatusOutputVariant1SerpCompletenessVariant1QueryIntegrity', {
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
SearchSerpStatusOutputVariant1SerpCompletenessVariant1QueryIntegrity.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1SerpCompletenessVariant1 = TypedDict('SearchSerpStatusOutputVariant1SerpCompletenessVariant1', {
    'pagination': Required[SearchSerpStatusOutputVariant1SerpCompletenessVariant1Pagination],
    'features': Required[SearchSerpStatusOutputVariant1SerpCompletenessVariant1Features],
    'queryIntegrity': Required[SearchSerpStatusOutputVariant1SerpCompletenessVariant1QueryIntegrity],
    'failureStage': Required[Union[Literal['provider_transport', 'invalid_payload', 'serp_readiness', 'query_integrity', 'pagination', 'optional_feature_parsing', 'unknown'], None]],
})
SearchSerpStatusOutputVariant1SerpCompletenessVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1OrganicResultsItem = TypedDict('SearchSerpStatusOutputVariant1OrganicResultsItem', {
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
SearchSerpStatusOutputVariant1OrganicResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1LocalPackItem = TypedDict('SearchSerpStatusOutputVariant1LocalPackItem', {
    'position': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'name': Required[str],
    'rating': Required[Union[str, None]],
    'reviewCount': Required[Union[str, None]],
    'websiteUrl': Required[Union[str, None]],
})
SearchSerpStatusOutputVariant1LocalPackItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1AiOverviewVariant1CitationsItem = TypedDict('SearchSerpStatusOutputVariant1AiOverviewVariant1CitationsItem', {
    'text': Required[str],
    'href': Required[str],
    'rawUrl': Required[str],
    'resolvedUrl': Required[Union[str, None]],
    'linkType': Required[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': Required[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
})
SearchSerpStatusOutputVariant1AiOverviewVariant1CitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1AiOverviewVariant1 = TypedDict('SearchSerpStatusOutputVariant1AiOverviewVariant1', {
    'detected': Required[bool],
    'text': Required[Union[str, None]],
    'citations': Required[list[SearchSerpStatusOutputVariant1AiOverviewVariant1CitationsItem]],
    'expanded': Required[bool],
    'fullyExpanded': Required[bool],
    'sections': Required[list[str]],
    'shareUrl': NotRequired[Union[str, None]],
})
SearchSerpStatusOutputVariant1AiOverviewVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1AiModeVariant1CitationsItem = TypedDict('SearchSerpStatusOutputVariant1AiModeVariant1CitationsItem', {
    'text': Required[str],
    'href': Required[str],
})
SearchSerpStatusOutputVariant1AiModeVariant1CitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1AiModeVariant1 = TypedDict('SearchSerpStatusOutputVariant1AiModeVariant1', {
    'detected': Required[bool],
    'text': Required[Union[str, None]],
    'citations': Required[list[SearchSerpStatusOutputVariant1AiModeVariant1CitationsItem]],
})
SearchSerpStatusOutputVariant1AiModeVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1ForumsItem = TypedDict('SearchSerpStatusOutputVariant1ForumsItem', {
    'title': Required[str],
    'source': Required[str],
    'url': Required[str],
})
SearchSerpStatusOutputVariant1ForumsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1VideosItem = TypedDict('SearchSerpStatusOutputVariant1VideosItem', {
    'type': Required[str],
    'title': Required[str],
    'channel': Required[str],
    'platform': Required[str],
    'duration': Required[str],
    'url': Required[str],
})
SearchSerpStatusOutputVariant1VideosItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1PaaPreviewItem = TypedDict('SearchSerpStatusOutputVariant1PaaPreviewItem', {
    'question': Required[str],
    'answer': Required[Union[str, None]],
    'url': Required[Union[str, None]],
})
SearchSerpStatusOutputVariant1PaaPreviewItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1AdditionalSerpFeaturesItemItemsItem = TypedDict('SearchSerpStatusOutputVariant1AdditionalSerpFeaturesItemItemsItem', {
    'title': Required[Union[str, None]],
    'url': Required[Union[str, None]],
    'description': Required[Union[str, None]],
    'position': Required[Union[Union[float, int], None]],
})
SearchSerpStatusOutputVariant1AdditionalSerpFeaturesItemItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1AdditionalSerpFeaturesItem = TypedDict('SearchSerpStatusOutputVariant1AdditionalSerpFeaturesItem', {
    'name': Required[str],
    'attributes': Required[dict[str, Union[str, Union[float, int], bool, None]]],
    'items': Required[list[SearchSerpStatusOutputVariant1AdditionalSerpFeaturesItemItemsItem]],
})
SearchSerpStatusOutputVariant1AdditionalSerpFeaturesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1EntityIdsVariant1EntitiesItem = TypedDict('SearchSerpStatusOutputVariant1EntityIdsVariant1EntitiesItem', {
    'name': Required[str],
    'kgId': Required[Union[str, None]],
    'cid': Required[Union[str, None]],
    'gcid': Required[Union[str, None]],
})
SearchSerpStatusOutputVariant1EntityIdsVariant1EntitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1EntityIdsVariant1 = TypedDict('SearchSerpStatusOutputVariant1EntityIdsVariant1', {
    'entities': Required[list[SearchSerpStatusOutputVariant1EntityIdsVariant1EntitiesItem]],
    'kgIds': Required[list[str]],
    'cids': Required[list[str]],
    'gcids': Required[list[str]],
})
SearchSerpStatusOutputVariant1EntityIdsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant1PhaseTimingsVariant1 = TypedDict('SearchSerpStatusOutputVariant1PhaseTimingsVariant1', {
    'providerConnectMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'navigationMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'serpParseMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaExpansionMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'linkResolutionMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalServerMs': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
SearchSerpStatusOutputVariant1PhaseTimingsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SearchSerpStatusOutputVariant1(BaseModel):
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
    pagination: Union[SearchSerpStatusOutputVariant1PaginationVariant1, None] = Field(..., alias='pagination', description='')
    serp_completeness: Union[SearchSerpStatusOutputVariant1SerpCompletenessVariant1, None] = Field(..., alias='serpCompleteness', description='')
    organic_results: list[SearchSerpStatusOutputVariant1OrganicResultsItem] = Field(..., alias='organicResults', description='')
    local_pack: list[SearchSerpStatusOutputVariant1LocalPackItem] = Field(..., alias='localPack', description='')
    ai_overview: Union[SearchSerpStatusOutputVariant1AiOverviewVariant1, None] = Field(..., alias='aiOverview', description='')
    ai_mode: Union[SearchSerpStatusOutputVariant1AiModeVariant1, None] = Field(..., alias='aiMode', description='')
    forums: list[SearchSerpStatusOutputVariant1ForumsItem] = Field(..., alias='forums', description='')
    videos: list[SearchSerpStatusOutputVariant1VideosItem] = Field(..., alias='videos', description='')
    what_people_saying: list[dict[str, Any]] = Field(..., alias='whatPeopleSaying', description='')
    paa_preview: list[SearchSerpStatusOutputVariant1PaaPreviewItem] = Field(..., alias='paaPreview', description='')
    additional_serp_features: list[SearchSerpStatusOutputVariant1AdditionalSerpFeaturesItem] = Field(..., alias='additionalSerpFeatures', description='')
    feature_status: dict[str, Literal['observed_present', 'observed_absent', 'incomplete', 'not_requested', 'unknown', 'unsupported']] = Field(..., alias='featureStatus', description='')
    feature_pages: Annotated[list[dict[str, Any]], Field(max_length=2)] = Field(..., alias='featurePages', description='')
    entity_ids: Union[SearchSerpStatusOutputVariant1EntityIdsVariant1, None] = Field(..., alias='entityIds', description='')
    phase_timings: Union[SearchSerpStatusOutputVariant1PhaseTimingsVariant1, None] = Field(..., alias='phaseTimings', description='')
    duration_ms: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='durationMs', description='')
    attempt_count: Annotated[int, Field(ge=1, le=9007199254740991)] = Field(..., alias='attemptCount', description='')


SearchSerpStatusOutputVariant2DeliveryArtifactsItem = TypedDict('SearchSerpStatusOutputVariant2DeliveryArtifactsItem', {
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
SearchSerpStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SearchSerpStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SearchSerpStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant2Delivery = TypedDict('SearchSerpStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SearchSerpStatusOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SearchSerpStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SearchSerpStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant2RecoveryOperation = TypedDict('SearchSerpStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SearchSerpStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SearchSerpStatusOutputVariant2Recovery = TypedDict('SearchSerpStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SearchSerpStatusOutputVariant2RecoveryOperation],
})
SearchSerpStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SearchSerpStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SearchSerpStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SearchSerpStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SearchSerpStatusOutput).
SearchSerpStatusOutput = Union[SearchSerpStatusOutputVariant1, SearchSerpStatusOutputVariant2]

_SearchSerpStatusInputAdapter = TypeAdapter(SearchSerpStatusInput)
_SearchSerpStatusOutputAdapter = TypeAdapter(SearchSerpStatusOutput)