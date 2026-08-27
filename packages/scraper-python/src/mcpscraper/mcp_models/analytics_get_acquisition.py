from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetAcquisitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    start: str | None = Field(None, alias="start", description="Inclusive ISO 8601 report start. Omit with end to use the last 30 days.")
    end: str | None = Field(None, alias="end", description="Exclusive ISO 8601 report end. Omit with start to use now.")
    pixel_ids: list[str] | None = Field(None, alias="pixelIds", description="Optional Pixel ids belonging to this Site. Omit for every active Pixel.")
    hostnames: list[str] | None = Field(None, alias="hostnames", description="Optional approved detected hostnames within the selected Pixels.")
    source: str | None = Field(None, alias="source", description="Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.")
    medium: str | None = Field(None, alias="medium", description="Exact normalized campaign medium used to filter or label analytics data.")
    campaign: str | None = Field(None, alias="campaign", description="Exact normalized campaign value used to filter or label analytics data.")
    event_name: str | None = Field(None, alias="eventName", description="Optional normalized analytics event-name filter.")
    attribution_model: Literal['first_touch', 'last_touch', 'last_non_direct', 'linear', 'time_decay', 'position_based', 'custom_weighted'] | None = Field(None, alias="attributionModel", description="Attribution model applied to the report; defaults to first touch.")
    click_window_days: Any | None = Field(None, alias="clickWindowDays", description="Independent click attribution window. Lifetime does not change retention.")
    view_window_days: Any | None = Field(None, alias="viewWindowDays", description="Independent view attribution window. Lifetime does not change retention.")
    journey_tier: Literal['confirmed', 'candidate_assisted'] | None = Field(None, alias="journeyTier", description="Confirmed is the default; candidate-assisted contributions remain separately labeled.")
    channel_family: Literal['llm', 'social', 'review', 'search', 'email', 'referral', 'direct', 'other'] | None = Field(None, alias="channelFamily", description="Optional normalized acquisition-channel family filter.")
    platform: str | None = Field(None, alias="platform", description="Normalized external platform selected for this operation.")
    referrer: str | None = Field(None, alias="referrer", description="Optional exact or normalized referrer filter for analytics rows.")
    path: str | None = Field(None, alias="path", description="Exact path value used by this tool; preserve its leading slash or vault-relative form as required.")
    device_class: Literal['desktop', 'tablet', 'mobile', 'unknown'] | None = Field(None, alias="deviceClass", description="Optional normalized device-class filter.")
    country_code: str | None = Field(None, alias="countryCode", description="Two-letter country code used to filter analytics rows.")
    region_code: str | None = Field(None, alias="regionCode", description="Optional regional subdivision code filter.")
    conversion_kind: str | None = Field(None, alias="conversionKind", description="Optional normalized conversion event kind filter.")


class AnalyticsGetAcquisitionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: dict[str, Any] = Field(..., alias="data", description="")
    filters: dict[str, Any] = Field(..., alias="filters", description="")
