from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetSessionTimelineInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    reference: Annotated[str, Field(min_length=8, max_length=240)] = Field(..., alias='reference', description='Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.')
    from_: Union[str, None] = Field(None, alias='from', description='Inclusive ISO time. Defaults to 90 days before to; max window 366 days.')
    to: Union[str, None] = Field(None, alias='to', description='Exclusive ISO time. Defaults to now; max window 366 days.')


AnalyticsGetSessionTimelineOutputVariant1DataSubject = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataSubject', {
    'kind': Required[Literal['person', 'visitor', 'session']],
    'reference': Required[Annotated[str, Field(min_length=8)]],
    'personRef': Required[Union[Annotated[str, Field(min_length=8)], None]],
})
AnalyticsGetSessionTimelineOutputVariant1DataSubject.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataRange = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataRange', {
    'from': Required[str],
    'to': Required[str],
    'fromInclusive': Required[Literal[True]],
    'toExclusive': Required[Literal[True]],
})
AnalyticsGetSessionTimelineOutputVariant1DataRange.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataSummaryRevenueVariant1 = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataSummaryRevenueVariant1', {
    'valueMinor': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'currency': Required[Union[str, None]],
})
AnalyticsGetSessionTimelineOutputVariant1DataSummaryRevenueVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataSummary = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataSummary', {
    'sessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'pageviews': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'events': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'revenue': Required[Union[AnalyticsGetSessionTimelineOutputVariant1DataSummaryRevenueVariant1, None]],
    'totalEngagementMs': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
    'averageEngagementMs': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
})
AnalyticsGetSessionTimelineOutputVariant1DataSummary.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataCommonPagesItem = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataCommonPagesItem', {
    'path': Required[str],
    'visits': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'uniqueSessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'engagedMs': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsGetSessionTimelineOutputVariant1DataCommonPagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataAcquisitionItem = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataAcquisitionItem', {
    'source': Required[Union[str, None]],
    'medium': Required[Union[str, None]],
    'campaign': Required[Union[str, None]],
    'referrer': Required[Union[str, None]],
    'sessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'events': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsGetSessionTimelineOutputVariant1DataAcquisitionItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataEventBreakdownItem = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataEventBreakdownItem', {
    'name': Required[Annotated[str, Field(min_length=1)]],
    'count': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'uniqueSessions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsGetSessionTimelineOutputVariant1DataEventBreakdownItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataSessionsItemRevenueVariant1 = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataSessionsItemRevenueVariant1', {
    'valueMinor': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'currency': Required[Union[str, None]],
})
AnalyticsGetSessionTimelineOutputVariant1DataSessionsItemRevenueVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataSessionsItemAcquisitionVariant1 = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataSessionsItemAcquisitionVariant1', {
    'source': Required[Union[str, None]],
    'medium': Required[Union[str, None]],
    'campaign': Required[Union[str, None]],
    'referrer': Required[Union[str, None]],
})
AnalyticsGetSessionTimelineOutputVariant1DataSessionsItemAcquisitionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataSessionsItem = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataSessionsItem', {
    'sessionRef': Required[Annotated[str, Field(min_length=8)]],
    'startedAt': Required[str],
    'endedAt': Required[Union[str, None]],
    'durationMs': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
    'pageviews': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'events': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'conversions': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'revenue': Required[Union[AnalyticsGetSessionTimelineOutputVariant1DataSessionsItemRevenueVariant1, None]],
    'landingPath': Required[Union[str, None]],
    'exitPath': Required[Union[str, None]],
    'acquisition': Required[Union[AnalyticsGetSessionTimelineOutputVariant1DataSessionsItemAcquisitionVariant1, None]],
})
AnalyticsGetSessionTimelineOutputVariant1DataSessionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataItemsItemAcquisitionVariant1 = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataItemsItemAcquisitionVariant1', {
    'source': Required[Union[str, None]],
    'medium': Required[Union[str, None]],
    'campaign': Required[Union[str, None]],
})
AnalyticsGetSessionTimelineOutputVariant1DataItemsItemAcquisitionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataItemsItemValueVariant1 = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataItemsItemValueVariant1', {
    'valueMinor': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'currency': Required[Union[str, None]],
})
AnalyticsGetSessionTimelineOutputVariant1DataItemsItemValueVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataItemsItem = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataItemsItem', {
    'occurredAt': Required[str],
    'type': Required[Annotated[str, Field(min_length=1)]],
    'name': Required[Annotated[str, Field(min_length=1)]],
    'path': Required[Union[str, None]],
    'referrer': Required[Union[str, None]],
    'acquisition': Required[Union[AnalyticsGetSessionTimelineOutputVariant1DataItemsItemAcquisitionVariant1, None]],
    'value': Required[Union[AnalyticsGetSessionTimelineOutputVariant1DataItemsItemValueVariant1, None]],
    'evidenceClass': Required[Literal['deterministic', 'candidate']],
    'provenance': Required[Annotated[str, Field(min_length=1)]],
})
AnalyticsGetSessionTimelineOutputVariant1DataItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1DataPageInfo = TypedDict('AnalyticsGetSessionTimelineOutputVariant1DataPageInfo', {
    'nextCursor': Required[Union[Annotated[str, Field(min_length=1)], None]],
    'hasNextPage': Required[bool],
})
AnalyticsGetSessionTimelineOutputVariant1DataPageInfo.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant1Data = TypedDict('AnalyticsGetSessionTimelineOutputVariant1Data', {
    'subject': Required[AnalyticsGetSessionTimelineOutputVariant1DataSubject],
    'range': Required[AnalyticsGetSessionTimelineOutputVariant1DataRange],
    'journeyTier': Required[Literal['confirmed']],
    'candidateAssisted': Required[None],
    'summary': Required[AnalyticsGetSessionTimelineOutputVariant1DataSummary],
    'commonPages': Required[list[AnalyticsGetSessionTimelineOutputVariant1DataCommonPagesItem]],
    'acquisition': Required[list[AnalyticsGetSessionTimelineOutputVariant1DataAcquisitionItem]],
    'eventBreakdown': Required[list[AnalyticsGetSessionTimelineOutputVariant1DataEventBreakdownItem]],
    'sessions': Required[list[AnalyticsGetSessionTimelineOutputVariant1DataSessionsItem]],
    'items': Required[list[AnalyticsGetSessionTimelineOutputVariant1DataItemsItem]],
    'pageInfo': Required[AnalyticsGetSessionTimelineOutputVariant1DataPageInfo],
})
AnalyticsGetSessionTimelineOutputVariant1Data.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetSessionTimelineOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    data: AnalyticsGetSessionTimelineOutputVariant1Data = Field(..., alias='data', description='')


AnalyticsGetSessionTimelineOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetSessionTimelineOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetSessionTimelineOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsGetSessionTimelineOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsGetSessionTimelineOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetSessionTimelineOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetSessionTimelineOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant2Delivery = TypedDict('AnalyticsGetSessionTimelineOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetSessionTimelineOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsGetSessionTimelineOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetSessionTimelineOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetSessionTimelineOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetSessionTimelineOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetSessionTimelineOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetSessionTimelineOutputVariant2Recovery = TypedDict('AnalyticsGetSessionTimelineOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetSessionTimelineOutputVariant2RecoveryOperation],
})
AnalyticsGetSessionTimelineOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetSessionTimelineOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetSessionTimelineOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetSessionTimelineOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetSessionTimelineOutput).
AnalyticsGetSessionTimelineOutput = Union[AnalyticsGetSessionTimelineOutputVariant2, AnalyticsGetSessionTimelineOutputVariant1]

_AnalyticsGetSessionTimelineInputAdapter = TypeAdapter(AnalyticsGetSessionTimelineInput)
_AnalyticsGetSessionTimelineOutputAdapter = TypeAdapter(AnalyticsGetSessionTimelineOutput)