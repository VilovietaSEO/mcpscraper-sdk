from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateExportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    start: str | None = Field(None, alias="start", description="Inclusive ISO 8601 report start. Omit with end to use the last 30 days.")
    end: str | None = Field(None, alias="end", description="Exclusive ISO 8601 report end. Omit with start to use now.")
    pixel_ids: list[str] | None = Field(None, alias="pixelIds", description="Optional Pixel ids belonging to this Site. Omit for every active Pixel.")
    hostnames: list[str] | None = Field(None, alias="hostnames", description="Optional approved detected hostnames within the selected Pixels.")
    source: str | None = Field(None, alias="source", description="")
    medium: str | None = Field(None, alias="medium", description="")
    campaign: str | None = Field(None, alias="campaign", description="")
    event_name: str | None = Field(None, alias="eventName", description="")
    attribution_model: Literal['first_touch', 'last_touch'] | None = Field(None, alias="attributionModel", description="")
    channel_family: Literal['llm', 'social', 'review', 'search', 'email', 'referral', 'direct', 'other'] | None = Field(None, alias="channelFamily", description="")
    platform: str | None = Field(None, alias="platform", description="")
    referrer: str | None = Field(None, alias="referrer", description="")
    path: str | None = Field(None, alias="path", description="")
    device_class: Literal['desktop', 'tablet', 'mobile', 'unknown'] | None = Field(None, alias="deviceClass", description="")
    country_code: str | None = Field(None, alias="countryCode", description="")
    region_code: str | None = Field(None, alias="regionCode", description="")
    conversion_kind: str | None = Field(None, alias="conversionKind", description="")
    report: Literal['overview', 'acquisition', 'content', 'conversions'] | None = Field(None, alias="report", description="")
    format: Literal['csv', 'json', 'markdown'] | None = Field(None, alias="format", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")


class AnalyticsCreateExportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    artifact: dict[str, Any] = Field(..., alias="artifact", description="")
