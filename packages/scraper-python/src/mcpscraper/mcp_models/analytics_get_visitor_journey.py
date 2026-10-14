from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetVisitorJourneyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    reference: Annotated[str, Field(min_length=8, max_length=240)] = Field(..., alias='reference', description='Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.')
    from_: Union[str, None] = Field(None, alias='from', description='Inclusive ISO time. Defaults to 90 days before to; max window 366 days.')
    to: Union[str, None] = Field(None, alias='to', description='Exclusive ISO time. Defaults to now; max window 366 days.')


AnalyticsGetVisitorJourneyOutputVariant1DataSubject = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataSubject', {
    'kind': Required[Literal['person', 'visitor', 'session']],
    'reference': Required[Annotated[str, Field(min_length=8)]],
    'personRef': Required[Union[Annotated[str, Field(min_length=8)], None]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataSubject.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataRange = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataRange', {
    'from': Required[str],
    'to': Required[str],
    'fromInclusive': Required[Literal[True]],
    'toExclusive': Required[Literal[True]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataRange.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataSummaryRevenueVariant1 = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataSummaryRevenueVariant1', {
    'valueMinor': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'currency': Required[Union[str, None]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataSummaryRevenueVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataSummary = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataSummary', {
    'sessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'pageviews': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'events': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'revenue': Required[Union[AnalyticsGetVisitorJourneyOutputVariant1DataSummaryRevenueVariant1, None]],
    'totalEngagementMs': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
    'averageEngagementMs': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataSummary.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataCommonPagesItem = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataCommonPagesItem', {
    'path': Required[str],
    'visits': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'uniqueSessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'engagedMs': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataCommonPagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataAcquisitionItem = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataAcquisitionItem', {
    'source': Required[Union[str, None]],
    'medium': Required[Union[str, None]],
    'campaign': Required[Union[str, None]],
    'referrer': Required[Union[str, None]],
    'sessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'events': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataAcquisitionItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataEventBreakdownItem = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataEventBreakdownItem', {
    'name': Required[Annotated[str, Field(min_length=1)]],
    'count': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'uniqueSessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataEventBreakdownItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItemRevenueVariant1 = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItemRevenueVariant1', {
    'valueMinor': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'currency': Required[Union[str, None]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItemRevenueVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItemAcquisitionVariant1 = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItemAcquisitionVariant1', {
    'source': Required[Union[str, None]],
    'medium': Required[Union[str, None]],
    'campaign': Required[Union[str, None]],
    'referrer': Required[Union[str, None]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItemAcquisitionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItem = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItem', {
    'sessionRef': Required[Annotated[str, Field(min_length=8)]],
    'startedAt': Required[str],
    'endedAt': Required[Union[str, None]],
    'durationMs': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
    'pageviews': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'events': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'revenue': Required[Union[AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItemRevenueVariant1, None]],
    'landingPath': Required[Union[str, None]],
    'exitPath': Required[Union[str, None]],
    'acquisition': Required[Union[AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItemAcquisitionVariant1, None]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataItemsItemAcquisitionVariant1 = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataItemsItemAcquisitionVariant1', {
    'source': Required[Union[str, None]],
    'medium': Required[Union[str, None]],
    'campaign': Required[Union[str, None]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataItemsItemAcquisitionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataItemsItemValueVariant1 = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataItemsItemValueVariant1', {
    'valueMinor': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'currency': Required[Union[str, None]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataItemsItemValueVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataItemsItem = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataItemsItem', {
    'occurredAt': Required[str],
    'type': Required[Annotated[str, Field(min_length=1)]],
    'name': Required[Annotated[str, Field(min_length=1)]],
    'path': Required[Union[str, None]],
    'referrer': Required[Union[str, None]],
    'acquisition': Required[Union[AnalyticsGetVisitorJourneyOutputVariant1DataItemsItemAcquisitionVariant1, None]],
    'value': Required[Union[AnalyticsGetVisitorJourneyOutputVariant1DataItemsItemValueVariant1, None]],
    'evidenceClass': Required[Literal['deterministic', 'candidate']],
    'provenance': Required[Annotated[str, Field(min_length=1)]],
})
AnalyticsGetVisitorJourneyOutputVariant1DataItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1DataPageInfo = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1DataPageInfo', {
    'nextCursor': Required[Union[Annotated[str, Field(min_length=1)], None]],
    'hasNextPage': Required[bool],
})
AnalyticsGetVisitorJourneyOutputVariant1DataPageInfo.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant1Data = TypedDict('AnalyticsGetVisitorJourneyOutputVariant1Data', {
    'subject': Required[AnalyticsGetVisitorJourneyOutputVariant1DataSubject],
    'range': Required[AnalyticsGetVisitorJourneyOutputVariant1DataRange],
    'journeyTier': Required[Literal['confirmed']],
    'candidateAssisted': Required[None],
    'summary': Required[AnalyticsGetVisitorJourneyOutputVariant1DataSummary],
    'commonPages': Required[list[AnalyticsGetVisitorJourneyOutputVariant1DataCommonPagesItem]],
    'acquisition': Required[list[AnalyticsGetVisitorJourneyOutputVariant1DataAcquisitionItem]],
    'eventBreakdown': Required[list[AnalyticsGetVisitorJourneyOutputVariant1DataEventBreakdownItem]],
    'sessions': Required[list[AnalyticsGetVisitorJourneyOutputVariant1DataSessionsItem]],
    'items': Required[list[AnalyticsGetVisitorJourneyOutputVariant1DataItemsItem]],
    'pageInfo': Required[AnalyticsGetVisitorJourneyOutputVariant1DataPageInfo],
})
AnalyticsGetVisitorJourneyOutputVariant1Data.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetVisitorJourneyOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    data: AnalyticsGetVisitorJourneyOutputVariant1Data = Field(..., alias='data', description='')


AnalyticsGetVisitorJourneyOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetVisitorJourneyOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetVisitorJourneyOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetVisitorJourneyOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetVisitorJourneyOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant2Delivery = TypedDict('AnalyticsGetVisitorJourneyOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetVisitorJourneyOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetVisitorJourneyOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetVisitorJourneyOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetVisitorJourneyOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetVisitorJourneyOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetVisitorJourneyOutputVariant2Recovery = TypedDict('AnalyticsGetVisitorJourneyOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetVisitorJourneyOutputVariant2RecoveryOperation],
})
AnalyticsGetVisitorJourneyOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetVisitorJourneyOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetVisitorJourneyOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetVisitorJourneyOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetVisitorJourneyOutput).
AnalyticsGetVisitorJourneyOutput = Union[AnalyticsGetVisitorJourneyOutputVariant2, AnalyticsGetVisitorJourneyOutputVariant1]

_AnalyticsGetVisitorJourneyInputAdapter = TypeAdapter(AnalyticsGetVisitorJourneyInput)
_AnalyticsGetVisitorJourneyOutputAdapter = TypeAdapter(AnalyticsGetVisitorJourneyOutput)