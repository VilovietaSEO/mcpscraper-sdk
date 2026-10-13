from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class HarvestPaaStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    job_id: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='jobId', description='The jobId returned by harvest_paa_start.')


HarvestPaaStatusOutputVariant1StatusVariant1 = TypedDict('HarvestPaaStatusOutputVariant1StatusVariant1', {
    'state': Required[Literal['pending']],
    'terminal': Required[Literal[False]],
    'pollAfterSeconds': Required[Annotated[int, Field(ge=20, le=9007199254740991)]],
    'retryGuidance': Required[str],
})
HarvestPaaStatusOutputVariant1StatusVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1StatusVariant2 = TypedDict('HarvestPaaStatusOutputVariant1StatusVariant2', {
    'state': Required[Literal['running']],
    'terminal': Required[Literal[False]],
    'pollAfterSeconds': Required[Annotated[int, Field(ge=20, le=9007199254740991)]],
    'retryGuidance': Required[str],
})
HarvestPaaStatusOutputVariant1StatusVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1StatusVariant3 = TypedDict('HarvestPaaStatusOutputVariant1StatusVariant3', {
    'state': Required[Literal['done']],
    'terminal': Required[Literal[True]],
    'pollAfterSeconds': Required[None],
    'retryGuidance': Required[str],
})
HarvestPaaStatusOutputVariant1StatusVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1StatusVariant4 = TypedDict('HarvestPaaStatusOutputVariant1StatusVariant4', {
    'state': Required[Literal['failed']],
    'terminal': Required[Literal[True]],
    'pollAfterSeconds': Required[None],
    'retryGuidance': Required[str],
})
HarvestPaaStatusOutputVariant1StatusVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1StatusVariant5 = TypedDict('HarvestPaaStatusOutputVariant1StatusVariant5', {
    'state': Required[Literal['cancelled']],
    'terminal': Required[Literal[True]],
    'pollAfterSeconds': Required[None],
    'retryGuidance': Required[str],
})
HarvestPaaStatusOutputVariant1StatusVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1Execution = TypedDict('HarvestPaaStatusOutputVariant1Execution', {
    'state': Required[Literal['unknown']],
    'physicalOutcome': Required[Literal['unknown']],
    'holdState': Required[Literal['held', 'unconfirmed']],
    'retryGuidance': Required[str],
})
HarvestPaaStatusOutputVariant1Execution.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ProgressPaginationVariant1 = TypedDict('HarvestPaaStatusOutputVariant1ProgressPaginationVariant1', {
    'requestedPages': Required[Union[Literal[1], Literal[2]]],
    'capturedPages': Required[Union[Literal[1], Literal[2]]],
    'page2Status': Required[Literal['not_requested', 'not_attempted', 'captured', 'unavailable', 'failed']],
    'page1OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'page2OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failureCode': NotRequired[Literal['missing_next', 'invalid_next', 'empty_page', 'captcha', 'timeout', 'navigation_error', 'unsupported_driver']],
})
HarvestPaaStatusOutputVariant1ProgressPaginationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ProgressLifecycleVariant1RetryBreakdown = TypedDict('HarvestPaaStatusOutputVariant1ProgressLifecycleVariant1RetryBreakdown', {
    'controlRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'browserRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'providerFallbacks': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'runtimeRecoveries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'idempotentReplays': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
HarvestPaaStatusOutputVariant1ProgressLifecycleVariant1RetryBreakdown.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ProgressLifecycleVariant1 = TypedDict('HarvestPaaStatusOutputVariant1ProgressLifecycleVariant1', {
    'requestedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'questionsFound': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'targetStatus': Required[Literal['met', 'not_met']],
    'discoveryStatus': Required[Literal['in_progress', 'target_reached', 'frontier_exhausted', 'no_paa_observed', 'interrupted', 'recovery_exhausted']],
    'materialStatus': Required[Literal['complete', 'partial']],
    'completionReason': Required[str],
    'automaticRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'retryBreakdown': Required[HarvestPaaStatusOutputVariant1ProgressLifecycleVariant1RetryBreakdown],
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
HarvestPaaStatusOutputVariant1ProgressLifecycleVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ProgressInteractionSummary = TypedDict('HarvestPaaStatusOutputVariant1ProgressInteractionSummary', {
    'observations': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'dispatched': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'confirmed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'unconfirmed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'dispatchFailures': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'confirmedWithoutDispatchAck': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'expandedSignals': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'answerSignals': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sourceSignals': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'questionGrowthBatches': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'checkpoint700ms': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'checkpoint1000ms': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'checkpoint1400ms': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
HarvestPaaStatusOutputVariant1ProgressInteractionSummary.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ProgressRecentInteractionsItem = TypedDict('HarvestPaaStatusOutputVariant1ProgressRecentInteractionsItem', {
    'id': Required[str],
    'questionId': Required[str],
    'question': Required[str],
    'batchNumber': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'controlAttempt': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'observedAt': Required[Union[str, None]],
    'dispatched': Required[bool],
    'outcome': Required[Literal['confirmed', 'unconfirmed', 'dispatch_failed']],
    'confirmationSignals': Required[list[Literal['expanded', 'answer', 'source', 'question_growth']]],
    'confirmationCheckpointMs': Required[Union[Union[Literal[700], Literal[1000], Literal[1400]], None]],
    'confirmedAtMs': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'dispatchDurationMs': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalDurationMs': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'beforeQuestionCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'afterQuestionCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'newQuestionCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'expandedBefore': Required[bool],
    'expandedAfter': Required[bool],
    'answerObserved': Required[bool],
    'sourceCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'errorCode': Required[Union[Literal['click_failed', 'click_ack_timeout', 'control_missing', 'confirmation_timeout'], None]],
})
HarvestPaaStatusOutputVariant1ProgressRecentInteractionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1Progress = TypedDict('HarvestPaaStatusOutputVariant1Progress', {
    'pagination': Required[Union[HarvestPaaStatusOutputVariant1ProgressPaginationVariant1, None]],
    'requestedQuestions': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'capturedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'answeredQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sourcedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'missingAnswers': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'missingSources': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'incompleteAnswers': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'lifecycle': Required[Union[HarvestPaaStatusOutputVariant1ProgressLifecycleVariant1, None]],
    'interactionSummary': Required[HarvestPaaStatusOutputVariant1ProgressInteractionSummary],
    'recentInteractions': Required[Annotated[list[HarvestPaaStatusOutputVariant1ProgressRecentInteractionsItem], Field(max_length=20)]],
})
HarvestPaaStatusOutputVariant1Progress.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1PaginationVariant1 = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1PaginationVariant1', {
    'requestedPages': Required[Union[Literal[1], Literal[2]]],
    'capturedPages': Required[Union[Literal[1], Literal[2]]],
    'page2Status': Required[Literal['not_requested', 'not_attempted', 'captured', 'unavailable', 'failed']],
    'page1OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'page2OrganicCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failureCode': NotRequired[Literal['missing_next', 'invalid_next', 'empty_page', 'captcha', 'timeout', 'navigation_error', 'unsupported_driver']],
})
HarvestPaaStatusOutputVariant1ResultVariant1PaginationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1PaaLifecycleVariant1RetryBreakdown = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1PaaLifecycleVariant1RetryBreakdown', {
    'controlRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'browserRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'providerFallbacks': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'runtimeRecoveries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'idempotentReplays': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
HarvestPaaStatusOutputVariant1ResultVariant1PaaLifecycleVariant1RetryBreakdown.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1PaaLifecycleVariant1 = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1PaaLifecycleVariant1', {
    'requestedQuestions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'questionsFound': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'targetStatus': Required[Literal['met', 'not_met']],
    'discoveryStatus': Required[Literal['in_progress', 'target_reached', 'frontier_exhausted', 'no_paa_observed', 'interrupted', 'recovery_exhausted']],
    'materialStatus': Required[Literal['complete', 'partial']],
    'completionReason': Required[str],
    'automaticRetries': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'retryBreakdown': Required[HarvestPaaStatusOutputVariant1ResultVariant1PaaLifecycleVariant1RetryBreakdown],
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
HarvestPaaStatusOutputVariant1ResultVariant1PaaLifecycleVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1PhaseTimingsVariant1 = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1PhaseTimingsVariant1', {
    'providerConnectMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'navigationMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'serpParseMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaExpansionMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'linkResolutionMs': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalServerMs': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
HarvestPaaStatusOutputVariant1ResultVariant1PhaseTimingsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1QuestionsItemSourcesItem = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1QuestionsItemSourcesItem', {
    'url': Required[str],
    'rawUrl': Required[str],
    'resolvedUrl': Required[Union[str, None]],
    'linkType': Required[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': Required[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
    'title': Required[Union[str, None]],
    'site': Required[Union[str, None]],
    'description': NotRequired[Union[str, None]],
})
HarvestPaaStatusOutputVariant1ResultVariant1QuestionsItemSourcesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1QuestionsItem = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1QuestionsItem', {
    'questionId': Required[str],
    'googleLinkId': Required[Union[str, None]],
    'googleEvidenceId': Required[Union[str, None]],
    'question': Required[str],
    'answer': Required[Union[str, None]],
    'answerExpansionIncomplete': NotRequired[bool],
    'sources': Required[list[HarvestPaaStatusOutputVariant1ResultVariant1QuestionsItemSourcesItem]],
    'sourceTitle': Required[Union[str, None]],
    'sourceSite': Required[Union[str, None]],
    'sourceUrl': Required[Union[str, None]],
})
HarvestPaaStatusOutputVariant1ResultVariant1QuestionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1OrganicResultsItem = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1OrganicResultsItem', {
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
HarvestPaaStatusOutputVariant1ResultVariant1OrganicResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1AiOverviewVariant1CitationsItem = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1AiOverviewVariant1CitationsItem', {
    'text': Required[str],
    'href': Required[str],
    'rawUrl': Required[str],
    'resolvedUrl': Required[Union[str, None]],
    'linkType': Required[Literal['plain', 'google_url_redirect', 'google_goto_redirect']],
    'resolutionStatus': Required[Literal['not_needed', 'resolved', 'unresolved', 'rejected']],
})
HarvestPaaStatusOutputVariant1ResultVariant1AiOverviewVariant1CitationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1AiOverviewVariant1 = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1AiOverviewVariant1', {
    'detected': Required[bool],
    'text': Required[Union[str, None]],
    'citations': Required[list[HarvestPaaStatusOutputVariant1ResultVariant1AiOverviewVariant1CitationsItem]],
    'expanded': Required[bool],
    'fullyExpanded': Required[bool],
    'sections': Required[list[str]],
    'shareUrl': NotRequired[Union[str, None]],
})
HarvestPaaStatusOutputVariant1ResultVariant1AiOverviewVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1EntityIdsVariant1EntitiesItem = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1EntityIdsVariant1EntitiesItem', {
    'name': Required[str],
    'kgId': Required[Union[str, None]],
    'cid': Required[Union[str, None]],
    'gcid': Required[Union[str, None]],
})
HarvestPaaStatusOutputVariant1ResultVariant1EntityIdsVariant1EntitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1EntityIdsVariant1 = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1EntityIdsVariant1', {
    'entities': Required[list[HarvestPaaStatusOutputVariant1ResultVariant1EntityIdsVariant1EntitiesItem]],
    'kgIds': Required[list[str]],
    'cids': Required[list[str]],
    'gcids': Required[list[str]],
})
HarvestPaaStatusOutputVariant1ResultVariant1EntityIdsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1ResultVariant1 = TypedDict('HarvestPaaStatusOutputVariant1ResultVariant1', {
    'pagination': Required[Union[HarvestPaaStatusOutputVariant1ResultVariant1PaginationVariant1, None]],
    'completionStatus': Required[Union[str, None]],
    'resultQuality': Required[Union[str, None]],
    'retryRecommended': Required[Union[bool, None]],
    'paaLifecycle': Required[Union[HarvestPaaStatusOutputVariant1ResultVariant1PaaLifecycleVariant1, None]],
    'phaseTimings': Required[Union[HarvestPaaStatusOutputVariant1ResultVariant1PhaseTimingsVariant1, None]],
    'questionCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'paaIncompleteAnswers': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'questions': Required[list[HarvestPaaStatusOutputVariant1ResultVariant1QuestionsItem]],
    'organicResults': Required[list[HarvestPaaStatusOutputVariant1ResultVariant1OrganicResultsItem]],
    'aiOverview': Required[Union[HarvestPaaStatusOutputVariant1ResultVariant1AiOverviewVariant1, None]],
    'entityIds': Required[Union[HarvestPaaStatusOutputVariant1ResultVariant1EntityIdsVariant1, None]],
})
HarvestPaaStatusOutputVariant1ResultVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant1Billing = TypedDict('HarvestPaaStatusOutputVariant1Billing', {
    'state': Required[Literal['held', 'settled', 'refund_pending', 'refunded', 'unknown']],
    'holdMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'billedMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'refundMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
})
HarvestPaaStatusOutputVariant1Billing.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class HarvestPaaStatusOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    operation_id: str = Field(..., alias='operationId', description='')
    task_id: str = Field(..., alias='taskId', description='')
    status: Union[HarvestPaaStatusOutputVariant1StatusVariant1, HarvestPaaStatusOutputVariant1StatusVariant2, HarvestPaaStatusOutputVariant1StatusVariant3, HarvestPaaStatusOutputVariant1StatusVariant4, HarvestPaaStatusOutputVariant1StatusVariant5] = Field(..., alias='status', description='')
    execution: Union[HarvestPaaStatusOutputVariant1Execution, None] = Field(None, alias='execution', description='')
    replayed: bool = Field(..., alias='replayed', description='')
    progress: HarvestPaaStatusOutputVariant1Progress = Field(..., alias='progress', description='')
    result: Union[HarvestPaaStatusOutputVariant1ResultVariant1, None] = Field(..., alias='result', description='')
    billing: HarvestPaaStatusOutputVariant1Billing = Field(..., alias='billing', description='')


HarvestPaaStatusOutputVariant2DeliveryArtifactsItem = TypedDict('HarvestPaaStatusOutputVariant2DeliveryArtifactsItem', {
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
HarvestPaaStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('HarvestPaaStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
HarvestPaaStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant2Delivery = TypedDict('HarvestPaaStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[HarvestPaaStatusOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[HarvestPaaStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
HarvestPaaStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant2RecoveryOperation = TypedDict('HarvestPaaStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
HarvestPaaStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


HarvestPaaStatusOutputVariant2Recovery = TypedDict('HarvestPaaStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[HarvestPaaStatusOutputVariant2RecoveryOperation],
})
HarvestPaaStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class HarvestPaaStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: HarvestPaaStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: HarvestPaaStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(HarvestPaaStatusOutput).
HarvestPaaStatusOutput = Union[HarvestPaaStatusOutputVariant1, HarvestPaaStatusOutputVariant2]

_HarvestPaaStatusInputAdapter = TypeAdapter(HarvestPaaStatusInput)
_HarvestPaaStatusOutputAdapter = TypeAdapter(HarvestPaaStatusOutput)