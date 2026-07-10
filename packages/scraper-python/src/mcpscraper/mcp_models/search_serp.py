from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SearchSerpInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="The search query. KEEP the place in the query text for localized results (e.g. \"best dentist Brooklyn NY\") and also set location — city-in-query is what localizes reliably.")
    location: str | None = Field(None, alias="location", description="City, region, or country for geo signals. Set alongside city-in-query wording; alone it does NOT reliably localize.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from location or user language.")
    hl: str | None = Field(None, alias="hl", description="Google interface/content language inferred from user request.")
    device: Literal["desktop", "mobile"] | None = Field(None, alias="device", description="SERP device context. Use mobile only for mobile rankings.")
    proxy_mode: Literal["location", "configured", "none"] | None = Field(None, alias="proxyMode", description="Leave unset (clean egress). Do NOT set \"location\" just because a city was named — that comes from city-in-query wording. \"location\" forces residential geo-IP for rank-tracking fidelity, is frequently CAPTCHA-blocked, and accepts failures.")
    proxy_zip: str | None = Field(None, alias="proxyZip", description="US ZIP for residential geo-IP targeting. Only meaningful with proxyMode \"location\".")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized diagnostics for debugging localization, CAPTCHA, or proxy behavior.")
    pages: int | None = Field(None, alias="pages", description="Number of result pages to fetch (1–2).")


class SearchSerpOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
