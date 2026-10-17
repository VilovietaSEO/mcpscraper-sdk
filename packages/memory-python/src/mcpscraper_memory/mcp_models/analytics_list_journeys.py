from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsListJourneysInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    journey_tier: Union[Literal['confirmed', 'best_guess', 'all'], None] = Field(None, alias='journeyTier', description='Select confirmed journeys, separately labeled best-guess journeys, or both branches. Confirmed is the default; best-guess evidence can never drive CRM or advertising actions.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum rows returned in each selected journey branch.')
    cursor: Union[Annotated[str, Field(max_length=1000)], None] = Field(None, alias='cursor', description='Opaque keyset cursor returned in a selected branch pageInfo.nextCursor.')


AnalyticsListJourneysOutputVariant1ConfirmedVariant1ItemsItemRevenueVariant1 = TypedDict('AnalyticsListJourneysOutputVariant1ConfirmedVariant1ItemsItemRevenueVariant1', {
    'valueMinor': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'currency': Required[Union[Annotated[str, Field(min_length=3, max_length=3)], None]],
})
AnalyticsListJourneysOutputVariant1ConfirmedVariant1ItemsItemRevenueVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1ConfirmedVariant1ItemsItem = TypedDict('AnalyticsListJourneysOutputVariant1ConfirmedVariant1ItemsItem', {
    'journeyTier': Required[Literal['confirmed']],
    'personRef': Required[Annotated[str, Field(min_length=8, max_length=240)]],
    'firstSeenAt': Required[Union[str, None]],
    'lastSeenAt': Required[Union[str, None]],
    'sessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'events': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'revenue': Required[Union[AnalyticsListJourneysOutputVariant1ConfirmedVariant1ItemsItemRevenueVariant1, None]],
    'evidenceClass': Required[Literal['deterministic']],
})
AnalyticsListJourneysOutputVariant1ConfirmedVariant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1ConfirmedVariant1PageInfo = TypedDict('AnalyticsListJourneysOutputVariant1ConfirmedVariant1PageInfo', {
    'nextCursor': Required[Union[Annotated[str, Field(min_length=8, max_length=1000)], None]],
    'hasNextPage': Required[bool],
})
AnalyticsListJourneysOutputVariant1ConfirmedVariant1PageInfo.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1ConfirmedVariant1 = TypedDict('AnalyticsListJourneysOutputVariant1ConfirmedVariant1', {
    'journeyTier': Required[Literal['confirmed']],
    'items': Required[Annotated[list[AnalyticsListJourneysOutputVariant1ConfirmedVariant1ItemsItem], Field(max_length=100)]],
    'pageInfo': Required[AnalyticsListJourneysOutputVariant1ConfirmedVariant1PageInfo],
})
AnalyticsListJourneysOutputVariant1ConfirmedVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemConfirmedTotalsRevenueVariant1 = TypedDict('AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemConfirmedTotalsRevenueVariant1', {
    'valueMinor': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'currency': Required[Union[Annotated[str, Field(min_length=3, max_length=3)], None]],
})
AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemConfirmedTotalsRevenueVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemConfirmedTotals = TypedDict('AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemConfirmedTotals', {
    'sessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'events': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'revenue': Required[Union[AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemConfirmedTotalsRevenueVariant1, None]],
})
AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemConfirmedTotals.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemInferredIncrementalTotalsRevenueVariant1 = TypedDict('AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemInferredIncrementalTotalsRevenueVariant1', {
    'valueMinor': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'currency': Required[Union[Annotated[str, Field(min_length=3, max_length=3)], None]],
})
AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemInferredIncrementalTotalsRevenueVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemInferredIncrementalTotals = TypedDict('AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemInferredIncrementalTotals', {
    'sessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'events': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'revenue': Required[Union[AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemInferredIncrementalTotalsRevenueVariant1, None]],
})
AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemInferredIncrementalTotals.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItem = TypedDict('AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItem', {
    'journeyTier': Required[Literal['candidate_assisted']],
    'inferenceRef': Required[Annotated[str, Field(min_length=8, max_length=240)]],
    'confirmedTotals': Required[AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemConfirmedTotals],
    'inferredIncrementalTotals': Required[AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItemInferredIncrementalTotals],
    'candidateCount': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'confidenceBand': Required[Literal['high']],
    'modelVersion': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'featureClasses': Required[Annotated[list[Annotated[str, Field(min_length=1, max_length=160)]], Field(max_length=100)]],
    'coverage': Required[Literal['incremental_sessions_available', 'no_incremental_sessions']],
    'expiresAt': Required[str],
    'provenance': Required[Literal['consented_high_confidence_candidate_association']],
})
AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1BestGuessVariant1PageInfo = TypedDict('AnalyticsListJourneysOutputVariant1BestGuessVariant1PageInfo', {
    'nextCursor': Required[Union[Annotated[str, Field(min_length=8, max_length=1000)], None]],
    'hasNextPage': Required[bool],
})
AnalyticsListJourneysOutputVariant1BestGuessVariant1PageInfo.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant1BestGuessVariant1 = TypedDict('AnalyticsListJourneysOutputVariant1BestGuessVariant1', {
    'journeyTier': Required[Literal['candidate_assisted']],
    'totalsAreSeparated': Required[Literal[True]],
    'items': Required[Annotated[list[AnalyticsListJourneysOutputVariant1BestGuessVariant1ItemsItem], Field(max_length=100)]],
    'pageInfo': Required[AnalyticsListJourneysOutputVariant1BestGuessVariant1PageInfo],
})
AnalyticsListJourneysOutputVariant1BestGuessVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsListJourneysOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    journey_tier: Literal['confirmed', 'best_guess', 'all'] = Field(..., alias='journeyTier', description='')
    confirmed: Union[AnalyticsListJourneysOutputVariant1ConfirmedVariant1, None] = Field(..., alias='confirmed', description='')
    best_guess: Union[AnalyticsListJourneysOutputVariant1BestGuessVariant1, None] = Field(..., alias='bestGuess', description='')
    totals_are_separated: bool = Field(..., alias='totalsAreSeparated', description='')


AnalyticsListJourneysOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsListJourneysOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsListJourneysOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsListJourneysOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsListJourneysOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsListJourneysOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsListJourneysOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant2Delivery = TypedDict('AnalyticsListJourneysOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsListJourneysOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsListJourneysOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsListJourneysOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsListJourneysOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant2RecoveryOperation = TypedDict('AnalyticsListJourneysOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsListJourneysOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListJourneysOutputVariant2Recovery = TypedDict('AnalyticsListJourneysOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsListJourneysOutputVariant2RecoveryOperation],
})
AnalyticsListJourneysOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsListJourneysOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsListJourneysOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsListJourneysOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsListJourneysOutput).
AnalyticsListJourneysOutput = Union[AnalyticsListJourneysOutputVariant1, AnalyticsListJourneysOutputVariant2]

_AnalyticsListJourneysInputAdapter = TypeAdapter(AnalyticsListJourneysInput)
_AnalyticsListJourneysOutputAdapter = TypeAdapter(AnalyticsListJourneysOutput)