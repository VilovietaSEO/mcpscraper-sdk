from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetFunnelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    start: Union[str, None] = Field(None, alias='start', description='Inclusive ISO 8601 report start. Omit with end to use the last 30 days.')
    end: Union[str, None] = Field(None, alias='end', description='Exclusive ISO 8601 report end. Omit with start to use now.')
    pixel_ids: Union[Annotated[list[str], Field(max_length=20)], None] = Field(None, alias='pixelIds', description='Optional Pixel ids belonging to this Site. Omit for every active Pixel.')
    hostnames: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=253)]], Field(max_length=20)], None] = Field(None, alias='hostnames', description='Optional approved detected hostnames within the selected Pixels.')
    source: Union[Annotated[str, Field(min_length=1, max_length=180)], None] = Field(None, alias='source', description='Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.')
    medium: Union[Annotated[str, Field(min_length=1, max_length=180)], None] = Field(None, alias='medium', description='Exact normalized campaign medium used to filter or label analytics data.')
    campaign: Union[Annotated[str, Field(min_length=1, max_length=240)], None] = Field(None, alias='campaign', description='Exact normalized campaign value used to filter or label analytics data.')
    event_name: Union[str, None] = Field(None, alias='eventName', description='Optional normalized analytics event-name filter.')
    attribution_model: Union[Literal['first_touch', 'last_touch', 'last_non_direct', 'linear', 'time_decay', 'position_based', 'custom_weighted'], None] = Field(None, alias='attributionModel', description='Attribution model applied to the report; defaults to first touch.')
    click_window_days: Union[Union[Literal[7], Literal[14], Literal[30], Literal[60], Literal[90], Literal[180], Literal[365], Literal['lifetime']], None] = Field(None, alias='clickWindowDays', description='Independent click attribution window. Lifetime does not change retention.')
    view_window_days: Union[Union[Literal[7], Literal[14], Literal[30], Literal[60], Literal[90], Literal[180], Literal[365], Literal['lifetime']], None] = Field(None, alias='viewWindowDays', description='Independent view attribution window. Lifetime does not change retention.')
    journey_tier: Union[Literal['confirmed', 'candidate_assisted'], None] = Field(None, alias='journeyTier', description='Confirmed is the default; candidate-assisted contributions remain separately labeled.')
    channel_family: Union[Literal['llm', 'social', 'review', 'search', 'email', 'referral', 'direct', 'other'], None] = Field(None, alias='channelFamily', description='Optional normalized acquisition-channel family filter.')
    platform: Union[Annotated[str, Field(min_length=1, max_length=180)], None] = Field(None, alias='platform', description='Normalized external platform selected for this operation.')
    referrer: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='referrer', description='Optional exact or normalized referrer filter for analytics rows.')
    path: Union[Annotated[str, Field(max_length=2000)], None] = Field(None, alias='path', description='Exact path value used by this tool; preserve its leading slash or vault-relative form as required.')
    device_class: Union[Literal['desktop', 'tablet', 'mobile', 'unknown'], None] = Field(None, alias='deviceClass', description='Optional normalized device-class filter.')
    country_code: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='countryCode', description='Two-letter country code used to filter analytics rows.')
    region_code: Union[Annotated[str, Field(min_length=1, max_length=8)], None] = Field(None, alias='regionCode', description='Optional regional subdivision code filter.')
    conversion_kind: Union[str, None] = Field(None, alias='conversionKind', description='Optional normalized conversion event kind filter.')
    funnel_id: str = Field(..., alias='funnelId', description='Funnel definition id returned by analytics_list_funnels.')
    limit: Union[Annotated[int, Field(ge=1, le=250)], None] = Field(None, alias='limit', description='Maximum drill-down rows.')
    cursor: Union[Annotated[str, Field(max_length=1000)], None] = Field(None, alias='cursor', description='Opaque pagination cursor.')


class AnalyticsGetFunnelOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: dict[str, Any] = Field(..., alias='data', description='')
    filters: dict[str, Any] = Field(..., alias='filters', description='')


AnalyticsGetFunnelOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetFunnelOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetFunnelOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetFunnelOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetFunnelOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetFunnelOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetFunnelOutputVariant2Delivery = TypedDict('AnalyticsGetFunnelOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetFunnelOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetFunnelOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetFunnelOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetFunnelOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetFunnelOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetFunnelOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetFunnelOutputVariant2Recovery = TypedDict('AnalyticsGetFunnelOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetFunnelOutputVariant2RecoveryOperation],
})
AnalyticsGetFunnelOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetFunnelOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetFunnelOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetFunnelOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetFunnelOutput).
AnalyticsGetFunnelOutput = Union[AnalyticsGetFunnelOutputVariant2, AnalyticsGetFunnelOutputVariant1]

_AnalyticsGetFunnelInputAdapter = TypeAdapter(AnalyticsGetFunnelInput)
_AnalyticsGetFunnelOutputAdapter = TypeAdapter(AnalyticsGetFunnelOutput)