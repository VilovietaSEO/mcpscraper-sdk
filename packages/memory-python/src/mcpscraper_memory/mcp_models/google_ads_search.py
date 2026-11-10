from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GoogleAdsSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="A domain (e.g. getviktor.com) or advertiser/brand name to look up in Google Ads Transparency Center.")
    region: str | None = Field(None, alias="region", description="Two-letter region code for where the ads are shown. Default US. Examples: US, CA, GB, AU.")
    max_results: int | None = Field(None, alias="maxResults", description="Maximum advertisers to return. Default 10, maximum 20.")


class GoogleAdsSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str | None = Field(None, alias="query", description="")
    region: str | None = Field(None, alias="region", description="")
    advertiser_count: int | None = Field(None, alias="advertiserCount", description="")
    advertisers: list[dict[str, Any]] | None = Field(None, alias="advertisers", description="")
    website_count: int | None = Field(None, alias="websiteCount", description="")
    websites: list[dict[str, Any]] | None = Field(None, alias="websites", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
