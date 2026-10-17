from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsCreateSavedViewInputSettingsDateRange = TypedDict('AnalyticsCreateSavedViewInputSettingsDateRange', {
    'from': Required[str],
    'to': Required[str],
    'timezone': NotRequired[Annotated[str, Field(min_length=1, max_length=100)]],
})
AnalyticsCreateSavedViewInputSettingsDateRange.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateSavedViewInputSettingsFiltersItem = TypedDict('AnalyticsCreateSavedViewInputSettingsFiltersItem', {
    'field': Required[Literal['channel', 'source', 'medium', 'campaign', 'journey_tier', 'path', 'conversion_name', 'event_name', 'event_kind', 'landing_page', 'converted', 'stage']],
    'operator': Required[Literal['eq', 'neq', 'in', 'not_in', 'contains', 'gte', 'lte', 'is_null']],
    'value': Required[Union[Union[Annotated[str, Field(max_length=2000)], Union[float, int], bool], Annotated[list[Union[Annotated[str, Field(max_length=2000)], Union[float, int], bool]], Field(min_length=1, max_length=100)], None]],
})
AnalyticsCreateSavedViewInputSettingsFiltersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateSavedViewInputSettingsSortItem = TypedDict('AnalyticsCreateSavedViewInputSettingsSortItem', {
    'column': Required[Literal['sessions', 'visitors', 'known_people', 'leads', 'conversions', 'conversion_rate', 'event_value', 'expected_value', 'verified_revenue', 'channel', 'source', 'medium', 'campaign', 'spend', 'cost_per_lead', 'roas', 'path', 'title', 'engaged_sessions', 'page_views', 'conversion_name', 'unique_people', 'event_name', 'event_kind', 'event_count', 'started_at', 'session_id', 'visitor_id', 'person_id', 'journey_tier', 'landing_page', 'duration_seconds', 'converted', 'stage', 'stage_order', 'entered', 'advanced', 'median_time_seconds']],
    'direction': Required[Literal['asc', 'desc']],
})
AnalyticsCreateSavedViewInputSettingsSortItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateSavedViewInputSettingsComparison = TypedDict('AnalyticsCreateSavedViewInputSettingsComparison', {
    'mode': NotRequired[Literal['none', 'previous_period', 'previous_year', 'custom']],
    'from': NotRequired[str],
    'to': NotRequired[str],
})
AnalyticsCreateSavedViewInputSettingsComparison.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateSavedViewInputSettingsAttributionCustomWeights = TypedDict('AnalyticsCreateSavedViewInputSettingsAttributionCustomWeights', {
    'first': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'middle': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'last': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
})
AnalyticsCreateSavedViewInputSettingsAttributionCustomWeights.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateSavedViewInputSettingsAttribution = TypedDict('AnalyticsCreateSavedViewInputSettingsAttribution', {
    'model': NotRequired[Literal['first_touch', 'last_touch', 'last_non_direct', 'linear', 'time_decay', 'position_based', 'position_40_20_40', 'custom_weighted']],
    'clickWindowDays': NotRequired[Union[Literal[7], Literal[14], Literal[30], Literal[60], Literal[90], Literal[180], Literal[365], Literal['lifetime']]],
    'viewWindowDays': NotRequired[Union[Literal[7], Literal[14], Literal[30], Literal[60], Literal[90], Literal[180], Literal[365], Literal['lifetime']]],
    'customWeights': NotRequired[AnalyticsCreateSavedViewInputSettingsAttributionCustomWeights],
})
AnalyticsCreateSavedViewInputSettingsAttribution.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateSavedViewInputSettingsPagination = TypedDict('AnalyticsCreateSavedViewInputSettingsPagination', {
    'limit': NotRequired[Annotated[int, Field(ge=1, le=1000)]],
    'cursor': NotRequired[Annotated[str, Field(min_length=1, max_length=8192)]],
})
AnalyticsCreateSavedViewInputSettingsPagination.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateSavedViewInputSettings = TypedDict('AnalyticsCreateSavedViewInputSettings', {
    'schemaVersion': Required[Literal[1]],
    'reportType': Required[Literal['overview', 'acquisition', 'content', 'conversions', 'events', 'sessions', 'funnel']],
    'dateRange': Required[AnalyticsCreateSavedViewInputSettingsDateRange],
    'columns': Required[Annotated[list[Literal['sessions', 'visitors', 'known_people', 'leads', 'conversions', 'conversion_rate', 'event_value', 'expected_value', 'verified_revenue', 'channel', 'source', 'medium', 'campaign', 'spend', 'cost_per_lead', 'roas', 'path', 'title', 'engaged_sessions', 'page_views', 'conversion_name', 'unique_people', 'event_name', 'event_kind', 'event_count', 'started_at', 'session_id', 'visitor_id', 'person_id', 'journey_tier', 'landing_page', 'duration_seconds', 'converted', 'stage', 'stage_order', 'entered', 'advanced', 'median_time_seconds']], Field(min_length=1, max_length=40)]],
    'filters': NotRequired[Annotated[list[AnalyticsCreateSavedViewInputSettingsFiltersItem], Field(max_length=100)]],
    'sort': Required[Annotated[list[AnalyticsCreateSavedViewInputSettingsSortItem], Field(min_length=1, max_length=3)]],
    'comparison': NotRequired[AnalyticsCreateSavedViewInputSettingsComparison],
    'attribution': NotRequired[AnalyticsCreateSavedViewInputSettingsAttribution],
    'journeyTier': NotRequired[Literal['confirmed', 'best_guess', 'all']],
    'pagination': NotRequired[AnalyticsCreateSavedViewInputSettingsPagination],
})
AnalyticsCreateSavedViewInputSettings.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsCreateSavedViewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Saved report name.')
    settings: AnalyticsCreateSavedViewInputSettings = Field(..., alias='settings', description='Complete versioned report settings validated by the same canonical parser as REST and exports.')
    is_default: Union[bool, None] = Field(None, alias='isDefault', description='Make this the operator default for the report family.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.')


class AnalyticsCreateSavedViewOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    view: dict[str, Any] = Field(..., alias='view', description='')


AnalyticsCreateSavedViewOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateSavedViewOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateSavedViewOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateSavedViewOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsCreateSavedViewOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsCreateSavedViewOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateSavedViewOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateSavedViewOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateSavedViewOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateSavedViewOutputVariant2Delivery = TypedDict('AnalyticsCreateSavedViewOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateSavedViewOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsCreateSavedViewOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateSavedViewOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateSavedViewOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateSavedViewOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateSavedViewOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateSavedViewOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateSavedViewOutputVariant2Recovery = TypedDict('AnalyticsCreateSavedViewOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateSavedViewOutputVariant2RecoveryOperation],
})
AnalyticsCreateSavedViewOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateSavedViewOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateSavedViewOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateSavedViewOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateSavedViewOutput).
AnalyticsCreateSavedViewOutput = Union[AnalyticsCreateSavedViewOutputVariant2, AnalyticsCreateSavedViewOutputVariant1]

_AnalyticsCreateSavedViewInputAdapter = TypeAdapter(AnalyticsCreateSavedViewInput)
_AnalyticsCreateSavedViewOutputAdapter = TypeAdapter(AnalyticsCreateSavedViewOutput)