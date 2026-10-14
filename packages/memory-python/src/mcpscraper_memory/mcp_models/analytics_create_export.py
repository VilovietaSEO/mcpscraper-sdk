from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsCreateExportInput(BaseModel):
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
    report: Union[Literal['overview', 'acquisition', 'content', 'conversions'], None] = Field(None, alias='report', description='Analytics report family to render into the exported artifact.')
    format: Union[Literal['csv', 'json', 'markdown'], None] = Field(None, alias='format', description='Artifact serialization format to generate.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')


AnalyticsCreateExportOutputVariant1Artifact = TypedDict('AnalyticsCreateExportOutputVariant1Artifact', {
    'id': Required[str],
    'report': Required[Literal['overview', 'acquisition', 'content', 'conversions']],
    'format': Required[Literal['csv', 'json', 'markdown']],
    'mediaType': Required[str],
    'filename': Required[str],
    'content': Required[str],
})
AnalyticsCreateExportOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateExportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    artifact: AnalyticsCreateExportOutputVariant1Artifact = Field(..., alias='artifact', description='')


AnalyticsCreateExportOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateExportOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateExportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateExportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateExportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExportOutputVariant2Delivery = TypedDict('AnalyticsCreateExportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateExportOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateExportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateExportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExportOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateExportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateExportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExportOutputVariant2Recovery = TypedDict('AnalyticsCreateExportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateExportOutputVariant2RecoveryOperation],
})
AnalyticsCreateExportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateExportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateExportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateExportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateExportOutput).
AnalyticsCreateExportOutput = Union[AnalyticsCreateExportOutputVariant2, AnalyticsCreateExportOutputVariant1]

_AnalyticsCreateExportInputAdapter = TypeAdapter(AnalyticsCreateExportInput)
_AnalyticsCreateExportOutputAdapter = TypeAdapter(AnalyticsCreateExportOutput)