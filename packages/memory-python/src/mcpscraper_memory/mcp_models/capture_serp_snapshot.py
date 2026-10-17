from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CaptureSerpSnapshotInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Search topic to capture, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.')
    location: Union[str, None] = Field(None, alias='location', description='Where Google should think the searcher is. Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.')
    gl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='gl', description='Google country code inferred from the requested market.')
    hl: Union[str, None] = Field(None, alias='hl', description='Google interface/content language inferred from the user request.')
    device: Union[Literal['desktop', 'mobile'], None] = Field(None, alias='device', description='SERP device context. Use mobile only for mobile rankings/evidence.')
    pages: Union[Annotated[int, Field(ge=1, le=2)], None] = Field(None, alias='pages', description='Google result pages to capture. Use 2 only for deeper ranking evidence.')
    include_page_snapshots: Union[bool, None] = Field(None, alias='includePageSnapshots', description='Also capture ranking-page snapshots for selected SERP URLs. Each attempted snapshot adds 1 Credit.')
    page_snapshot_limit: Union[Annotated[int, Field(ge=0, le=10)], None] = Field(None, alias='pageSnapshotLimit', description='Maximum ranking-page snapshots when includePageSnapshots is true. This capacity is held up front and unused capacity is refunded.')


CaptureSerpSnapshotOutputVariant1ArtifactsItemHeadingsItem = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemHeadingsItem', {
    'level': Required[Annotated[int, Field(ge=1, le=6)]],
    'text': Required[str],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemHeadingsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItemArtifact = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemArtifact', {
    'htmlBlobUrl': NotRequired[Union[str, None]],
    'textBlobUrl': NotRequired[Union[str, None]],
    'markdownBlobUrl': NotRequired[Union[str, None]],
    'screenshotBlobUrl': NotRequired[Union[str, None]],
    'contentSha256': NotRequired[Union[str, None]],
    'capturedAt': NotRequired[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemArtifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItemErrorVariant1 = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemErrorVariant1', {
    'code': Required[Literal['invalid_url', 'timeout', 'capture_failed']],
    'message': Required[str],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemErrorVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItemLinkCounts = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemLinkCounts', {
    'wordCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'internalLinkCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'externalLinkCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalLinkCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemLinkCounts.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItemHashes = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemHashes', {
    'htmlSha256': Required[Union[str, None]],
    'markdownSha256': Required[Union[str, None]],
    'textSha256': Required[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemHashes.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItemContent = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemContent', {
    'html': Required[Union[str, None]],
    'markdown': Required[Union[str, None]],
    'text': Required[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemContent.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsUrlValidation = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsUrlValidation', {
    'passed': Required[bool],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsUrlValidation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsBrowserFallback = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsBrowserFallback', {
    'configured': Required[bool],
    'used': Required[bool],
    'boundedByTimeoutMs': Required[Annotated[Union[float, int], Field(ge=0)]],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsBrowserFallback.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsContent = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsContent', {
    'htmlIncluded': Required[bool],
    'markdownIncluded': Required[bool],
    'textIncluded': Required[bool],
    'maxContentChars': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'truncated': Required[bool],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsContent.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnostics = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnostics', {
    'requestedAt': Required[str],
    'completedAt': Required[str],
    'durationMs': Required[Annotated[Union[float, int], Field(ge=0)]],
    'urlValidation': Required[CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsUrlValidation],
    'browserFallback': Required[CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsBrowserFallback],
    'content': Required[CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnosticsContent],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnostics.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1ArtifactsItem = TypedDict('CaptureSerpSnapshotOutputVariant1ArtifactsItem', {
    'url': NotRequired[str],
    'requestedUrl': NotRequired[str],
    'finalUrl': NotRequired[Union[str, None]],
    'sourceKind': NotRequired[Literal['organic', 'ai_citation', 'local_pack_website', 'configured_target', 'site_subject']],
    'sourcePosition': NotRequired[Union[Annotated[int, Field(ge=1, le=9007199254740991)], None]],
    'status': NotRequired[Literal['captured', 'skipped', 'failed']],
    'fetchedVia': NotRequired[Union[Literal['fetch', 'headless', 'browser', 'mcp'], None]],
    'httpStatus': NotRequired[Union[Annotated[int, Field(ge=100, le=599)], None]],
    'contentType': NotRequired[Union[str, None]],
    'title': NotRequired[Union[str, None]],
    'canonicalUrl': NotRequired[Union[str, None]],
    'metaDescription': NotRequired[Union[str, None]],
    'headings': NotRequired[list[CaptureSerpSnapshotOutputVariant1ArtifactsItemHeadingsItem]],
    'artifact': NotRequired[CaptureSerpSnapshotOutputVariant1ArtifactsItemArtifact],
    'error': NotRequired[Union[CaptureSerpSnapshotOutputVariant1ArtifactsItemErrorVariant1, None]],
    'schemaTypes': NotRequired[list[str]],
    'wordCount': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'linkCounts': NotRequired[CaptureSerpSnapshotOutputVariant1ArtifactsItemLinkCounts],
    'hashes': NotRequired[CaptureSerpSnapshotOutputVariant1ArtifactsItemHashes],
    'content': NotRequired[CaptureSerpSnapshotOutputVariant1ArtifactsItemContent],
    'diagnostics': NotRequired[CaptureSerpSnapshotOutputVariant1ArtifactsItemDiagnostics],
})
CaptureSerpSnapshotOutputVariant1ArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1BillingVariant1 = TypedDict('CaptureSerpSnapshotOutputVariant1BillingVariant1', {
    'creditsUsed': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
    'requestId': Required[Union[str, None]],
    'jobId': Required[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1BillingVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PhaseTimings = TypedDict('CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PhaseTimings', {
    'providerConnectMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'navigationMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'serpParseMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'paaExpansionMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'linkResolutionMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'totalServerMs': Required[Annotated[Union[float, int], Field(ge=0)]],
})
CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PhaseTimings.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Pagination = TypedDict('CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Pagination', {
    'requestedPages': Required[Union[Literal[1], Literal[2]]],
    'capturedPages': Required[Union[Literal[1], Literal[2]]],
    'page2Status': Required[Literal['not_requested', 'not_attempted', 'captured', 'unavailable', 'failed']],
    'page1OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'page2OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failureCode': NotRequired[Literal['missing_next', 'invalid_next', 'empty_page', 'captcha', 'timeout', 'navigation_error', 'unsupported_driver']],
})
CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Pagination.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Completeness = TypedDict('CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Completeness', {
    'paaWithoutAnswer': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaWithoutSource': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaIncompleteAnswers': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaAnswersRecovered': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'aioShareCaptured': Required[Union[bool, None]],
    'paaRequested': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaReturned': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaUnique': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Completeness.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Interruption = TypedDict('CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Interruption', {
    'code': Required[Literal['browser_session_interrupted', 'request_aborted', 'timeout']],
})
CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Interruption.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1WarningsItem = TypedDict('CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1WarningsItem', {
    'code': Required[Literal['short_videos_captcha_skipped', 'paa_partial']],
    'surface': Required[Literal['short_videos', 'paa']],
    'retryable': Required[bool],
})
CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1WarningsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Links = TypedDict('CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Links', {
    'linkCandidatesObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'plainLinksObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'googleUrlRedirectsObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'googleGotoRedirectsObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'redirectsResolved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'redirectsUnresolved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'redirectsRejected': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'resolverNonGoogleRequestsObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaSourcesPreserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'aiOverviewLabelValidated': Required[bool],
})
CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Links.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PaaLifecycleRetryBreakdown = TypedDict('CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PaaLifecycleRetryBreakdown', {
    'controlRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'browserRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'providerFallbacks': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'runtimeRecoveries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'idempotentReplays': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PaaLifecycleRetryBreakdown.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PaaLifecycle = TypedDict('CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PaaLifecycle', {
    'requestedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'questionsFound': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'targetStatus': Required[Literal['met', 'not_met']],
    'discoveryStatus': Required[Literal['in_progress', 'target_reached', 'frontier_exhausted', 'no_paa_observed', 'interrupted', 'recovery_exhausted']],
    'materialStatus': Required[Literal['complete', 'partial']],
    'automaticRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'retryBreakdown': Required[CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PaaLifecycleRetryBreakdown],
    'knownQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'processedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failedInteractions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'noGrowthConfirmations': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'visibleControls': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'eligibleControls': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'dispatchedInteractions': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'confirmedInteractions': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'unconfirmedInteractions': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PaaLifecycle.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1 = TypedDict('CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1', {
    'completionStatus': Required[Literal['paa_found', 'no_paa', 'serp_only']],
    'problem': NotRequired[None],
    'resultQuality': NotRequired[Literal['complete', 'partial', 'degraded']],
    'degradedResult': NotRequired[bool],
    'degradationReasons': NotRequired[list[Literal['empty_primary_serp', 'page_two_missing']]],
    'retryRecommended': NotRequired[bool],
    'noPaaObserved': NotRequired[bool],
    'phaseTimings': NotRequired[CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PhaseTimings],
    'pagination': NotRequired[CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Pagination],
    'completeness': NotRequired[CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Completeness],
    'interruption': NotRequired[CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Interruption],
    'warnings': NotRequired[list[CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1WarningsItem]],
    'links': NotRequired[CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1Links],
    'paaLifecycle': NotRequired[CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1PaaLifecycle],
})
CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultAiOverviewCitationsItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultAiOverviewCitationsItem', {
    'text': Required[str],
    'href': Required[str],
    'rawUrl': NotRequired[str],
    'resolvedUrl': NotRequired[Union[str, None]],
    'linkType': NotRequired[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': NotRequired[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
})
CaptureSerpSnapshotOutputVariant1HarvestResultAiOverviewCitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultAiOverview = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultAiOverview', {
    'detected': Required[bool],
    'text': Required[Union[str, None]],
    'citations': Required[list[CaptureSerpSnapshotOutputVariant1HarvestResultAiOverviewCitationsItem]],
    'expanded': NotRequired[bool],
    'fullyExpanded': NotRequired[bool],
    'sections': NotRequired[list[str]],
    'shareUrl': NotRequired[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultAiOverview.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultAiModeCitationsItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultAiModeCitationsItem', {
    'text': Required[str],
    'href': Required[str],
    'rawUrl': NotRequired[str],
    'resolvedUrl': NotRequired[Union[str, None]],
    'linkType': NotRequired[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': NotRequired[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
})
CaptureSerpSnapshotOutputVariant1HarvestResultAiModeCitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultAiMode = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultAiMode', {
    'detected': Required[bool],
    'text': Required[Union[str, None]],
    'citations': Required[list[CaptureSerpSnapshotOutputVariant1HarvestResultAiModeCitationsItem]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultAiMode.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultFlatItemSourcesItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultFlatItemSourcesItem', {
    'url': Required[str],
    'rawUrl': NotRequired[str],
    'resolvedUrl': NotRequired[Union[str, None]],
    'linkType': NotRequired[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': NotRequired[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
    'title': Required[Union[str, None]],
    'site': Required[Union[str, None]],
    'description': NotRequired[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultFlatItemSourcesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultFlatItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultFlatItem', {
    'seed_query': Required[str],
    'question_id': Required[str],
    'google_link_id': Required[str],
    'google_evidence_id': Required[str],
    'question': Required[str],
    'answer': Required[str],
    'answerExpansionIncomplete': NotRequired[bool],
    'source_title': Required[str],
    'source_site': Required[str],
    'source_cite': Required[str],
    'sources': Required[list[CaptureSerpSnapshotOutputVariant1HarvestResultFlatItemSourcesItem]],
    'depth': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'parent_question': Required[str],
    'extracted_at': Required[str],
})
CaptureSerpSnapshotOutputVariant1HarvestResultFlatItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultVideosItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultVideosItem', {
    'type': Required[Literal['video', 'short_video']],
    'title': Required[str],
    'channel': Required[str],
    'platform': Required[str],
    'duration': Required[str],
    'url': Required[str],
})
CaptureSerpSnapshotOutputVariant1HarvestResultVideosItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultForumsItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultForumsItem', {
    'title': Required[str],
    'source': Required[str],
    'url': Required[str],
})
CaptureSerpSnapshotOutputVariant1HarvestResultForumsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultOrganicResultsItemInlineRatingVariant1 = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultOrganicResultsItemInlineRatingVariant1', {
    'value': Required[str],
    'count': Required[str],
})
CaptureSerpSnapshotOutputVariant1HarvestResultOrganicResultsItemInlineRatingVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultOrganicResultsItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultOrganicResultsItem', {
    'position': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'title': Required[str],
    'url': Required[str],
    'rawUrl': NotRequired[str],
    'resolvedUrl': NotRequired[Union[str, None]],
    'linkType': NotRequired[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': NotRequired[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
    'sourcePage': NotRequired[Union[Literal[1], Literal[2]]],
    'domain': Required[str],
    'cite': Required[Union[str, None]],
    'snippet': Required[Union[str, None]],
    'isRedditStyle': Required[bool],
    'inlineRating': Required[Union[CaptureSerpSnapshotOutputVariant1HarvestResultOrganicResultsItemInlineRatingVariant1, None]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultOrganicResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultLocalPackItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultLocalPackItem', {
    'position': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'name': Required[str],
    'cid': NotRequired[Union[str, None]],
    'rating': NotRequired[Union[str, None]],
    'reviewCount': NotRequired[Union[str, None]],
    'metadata': NotRequired[list[str]],
    'websiteUrl': NotRequired[Union[str, None]],
    'directionsUrl': NotRequired[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultLocalPackItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultEntityIdsEntitiesItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultEntityIdsEntitiesItem', {
    'name': Required[str],
    'kgId': Required[Union[str, None]],
    'cid': Required[Union[str, None]],
    'gcid': Required[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultEntityIdsEntitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultEntityIds = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultEntityIds', {
    'entities': Required[list[CaptureSerpSnapshotOutputVariant1HarvestResultEntityIdsEntitiesItem]],
    'kgIds': Required[list[str]],
    'cids': Required[list[str]],
    'gcids': Required[list[str]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultEntityIds.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultStats = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultStats', {
    'seed': Required[str],
    'totalQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'maxDepthReached': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'durationMs': Required[Annotated[Union[float, int], Field(ge=0)]],
    'errorCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultStats.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPhaseTimings = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPhaseTimings', {
    'providerConnectMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'navigationMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'serpParseMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'paaExpansionMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'linkResolutionMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'totalServerMs': Required[Annotated[Union[float, int], Field(ge=0)]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPhaseTimings.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPagination = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPagination', {
    'requestedPages': Required[Union[Literal[1], Literal[2]]],
    'capturedPages': Required[Union[Literal[1], Literal[2]]],
    'page2Status': Required[Literal['not_requested', 'not_attempted', 'captured', 'unavailable', 'failed']],
    'page1OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'page2OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failureCode': NotRequired[Literal['missing_next', 'invalid_next', 'empty_page', 'captcha', 'timeout', 'navigation_error', 'unsupported_driver']],
})
CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPagination.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsCompleteness = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsCompleteness', {
    'paaWithoutAnswer': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaWithoutSource': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaIncompleteAnswers': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaAnswersRecovered': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'aioShareCaptured': Required[Union[bool, None]],
    'paaRequested': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaReturned': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaUnique': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsCompleteness.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsInterruption = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsInterruption', {
    'code': Required[Literal['browser_session_interrupted', 'request_aborted', 'timeout']],
})
CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsInterruption.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsWarningsItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsWarningsItem', {
    'code': Required[Literal['short_videos_captcha_skipped', 'paa_partial']],
    'surface': Required[Literal['short_videos', 'paa']],
    'retryable': Required[bool],
})
CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsWarningsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsLinks = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsLinks', {
    'linkCandidatesObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'plainLinksObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'googleUrlRedirectsObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'googleGotoRedirectsObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'redirectsResolved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'redirectsUnresolved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'redirectsRejected': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'resolverNonGoogleRequestsObserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaSourcesPreserved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'aiOverviewLabelValidated': Required[bool],
})
CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsLinks.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPaaLifecycleRetryBreakdown = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPaaLifecycleRetryBreakdown', {
    'controlRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'browserRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'providerFallbacks': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'runtimeRecoveries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'idempotentReplays': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPaaLifecycleRetryBreakdown.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPaaLifecycle = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPaaLifecycle', {
    'requestedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'questionsFound': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'targetStatus': Required[Literal['met', 'not_met']],
    'discoveryStatus': Required[Literal['in_progress', 'target_reached', 'frontier_exhausted', 'no_paa_observed', 'interrupted', 'recovery_exhausted']],
    'materialStatus': Required[Literal['complete', 'partial']],
    'automaticRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'retryBreakdown': Required[CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPaaLifecycleRetryBreakdown],
    'knownQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'processedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failedInteractions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'noGrowthConfirmations': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'visibleControls': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'eligibleControls': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'dispatchedInteractions': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'confirmedInteractions': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'unconfirmedInteractions': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPaaLifecycle.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultDiagnostics = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultDiagnostics', {
    'completionStatus': Required[Literal['paa_found', 'no_paa', 'serp_only']],
    'problem': NotRequired[None],
    'resultQuality': NotRequired[Literal['complete', 'partial', 'degraded']],
    'degradedResult': NotRequired[bool],
    'degradationReasons': NotRequired[list[Literal['empty_primary_serp', 'page_two_missing']]],
    'retryRecommended': NotRequired[bool],
    'noPaaObserved': NotRequired[bool],
    'phaseTimings': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPhaseTimings],
    'pagination': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPagination],
    'completeness': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsCompleteness],
    'interruption': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsInterruption],
    'warnings': NotRequired[list[CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsWarningsItem]],
    'links': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsLinks],
    'paaLifecycle': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultDiagnosticsPaaLifecycle],
})
CaptureSerpSnapshotOutputVariant1HarvestResultDiagnostics.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResultWhatPeopleSayingItem = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResultWhatPeopleSayingItem', {
    'type': Required[Literal['reddit', 'facebook', 'instagram', 'tiktok', 'youtube', 'news', 'unknown']],
    'title': Required[str],
    'url': Required[str],
    'source': Required[str],
    'platform': Required[str],
    'popularComment': Required[Union[str, None]],
    'engagement': Required[str],
    'date': Required[str],
    'duration': Required[Union[str, None]],
    'authorNote': Required[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1HarvestResultWhatPeopleSayingItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1HarvestResult = TypedDict('CaptureSerpSnapshotOutputVariant1HarvestResult', {
    'seed': NotRequired[str],
    'location': NotRequired[Union[str, None]],
    'extractedAt': NotRequired[str],
    'totalQuestions': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'surface': NotRequired[Literal['web', 'aim', 'unknown']],
    'aiOverview': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultAiOverview],
    'aiMode': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultAiMode],
    'tree': NotRequired[list[Any]],
    'flat': NotRequired[list[CaptureSerpSnapshotOutputVariant1HarvestResultFlatItem]],
    'videos': NotRequired[list[CaptureSerpSnapshotOutputVariant1HarvestResultVideosItem]],
    'forums': NotRequired[list[CaptureSerpSnapshotOutputVariant1HarvestResultForumsItem]],
    'organicResults': NotRequired[list[CaptureSerpSnapshotOutputVariant1HarvestResultOrganicResultsItem]],
    'localPack': NotRequired[list[CaptureSerpSnapshotOutputVariant1HarvestResultLocalPackItem]],
    'entityIds': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultEntityIds],
    'stats': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultStats],
    'diagnostics': NotRequired[CaptureSerpSnapshotOutputVariant1HarvestResultDiagnostics],
    'whatPeopleSaying': NotRequired[list[CaptureSerpSnapshotOutputVariant1HarvestResultWhatPeopleSayingItem]],
})
CaptureSerpSnapshotOutputVariant1HarvestResult.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1ExpectedVariant1 = TypedDict('CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1ExpectedVariant1', {
    'city': Required[str],
    'regionCode': Required[Union[str, None]],
    'canonicalLocation': Required[str],
})
CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1ExpectedVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1CandidatesItem = TypedDict('CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1CandidatesItem', {
    'city': Required[str],
    'regionCode': Required[str],
    'count': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'examples': Required[list[str]],
})
CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1CandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1 = TypedDict('CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1', {
    'status': Required[Literal['not_requested', 'matched', 'mismatch', 'unknown']],
    'expected': Required[Union[CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1ExpectedVariant1, None]],
    'candidates': Required[list[CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1CandidatesItem]],
})
CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CaptureSerpSnapshotOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    schema_version: Literal['serp-intelligence.capture.v1'] = Field(..., alias='schemaVersion', description='')
    status: str = Field(..., alias='status', description='')
    query: Union[str, None] = Field(..., alias='query', description='')
    location: Union[str, None] = Field(..., alias='location', description='')
    captured_at: Union[str, None] = Field(..., alias='capturedAt', description='')
    result_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='resultCount', description='')
    organic_result_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='organicResultCount', description='')
    local_pack_result_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='localPackResultCount', description='')
    page_snapshot_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='pageSnapshotCount', description='')
    page_snapshot_failed_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='pageSnapshotFailedCount', description='')
    snapshot_id: Union[str, None] = Field(..., alias='snapshotId', description='')
    resolved_inputs: dict[str, Any] = Field(..., alias='resolvedInputs', description='')
    artifacts: list[CaptureSerpSnapshotOutputVariant1ArtifactsItem] = Field(..., alias='artifacts', description='')
    billing: Union[CaptureSerpSnapshotOutputVariant1BillingVariant1, None] = Field(..., alias='billing', description='')
    diagnostics: Union[CaptureSerpSnapshotOutputVariant1DiagnosticsVariant1, None] = Field(..., alias='diagnostics', description='')
    harvest_result: CaptureSerpSnapshotOutputVariant1HarvestResult = Field(..., alias='harvestResult', description='')
    location_evidence: Union[CaptureSerpSnapshotOutputVariant1LocationEvidenceVariant1, None] = Field(..., alias='locationEvidence', description='')


CaptureSerpSnapshotOutputVariant2DeliveryArtifactsItem = TypedDict('CaptureSerpSnapshotOutputVariant2DeliveryArtifactsItem', {
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
CaptureSerpSnapshotOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant2DeliveryAvailableExportsItem = TypedDict('CaptureSerpSnapshotOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CaptureSerpSnapshotOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CaptureSerpSnapshotOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CaptureSerpSnapshotOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant2Delivery = TypedDict('CaptureSerpSnapshotOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CaptureSerpSnapshotOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CaptureSerpSnapshotOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CaptureSerpSnapshotOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CaptureSerpSnapshotOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant2RecoveryOperation = TypedDict('CaptureSerpSnapshotOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CaptureSerpSnapshotOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant2Recovery = TypedDict('CaptureSerpSnapshotOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CaptureSerpSnapshotOutputVariant2RecoveryOperation],
})
CaptureSerpSnapshotOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CaptureSerpSnapshotOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CaptureSerpSnapshotOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CaptureSerpSnapshotOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CaptureSerpSnapshotOutput).
CaptureSerpSnapshotOutput = Union[CaptureSerpSnapshotOutputVariant1, CaptureSerpSnapshotOutputVariant2]

_CaptureSerpSnapshotInputAdapter = TypeAdapter(CaptureSerpSnapshotInput)
_CaptureSerpSnapshotOutputAdapter = TypeAdapter(CaptureSerpSnapshotOutput)