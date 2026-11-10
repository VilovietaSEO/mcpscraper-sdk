from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class FacebookPageIntelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str | None = Field(None, alias="pageId", description="Facebook advertiser/page ID. Use only a value returned by facebook_ad_search or copied from Ad Library.")
    library_id: str | None = Field(None, alias="libraryId", description="Facebook Ad Library archive ID. Use a value returned by facebook_ad_search, or a libraryId/adArchiveId visible in Ad Library.")
    query: str | None = Field(None, alias="query", description="Broad Ad Library keyword discovery when pageId/libraryId is not known. Results can mix unrelated advertisers; inspect matchConfidence, matchedAdvertisers, and warnings before analysis. One of pageId, libraryId, or query is required.")
    max_ads: int | None = Field(None, alias="maxAds", description="Maximum ads to inspect. Default 50, maximum 200.")
    country: str | None = Field(None, alias="country", description="Two-letter Ad Library country code. Default US.")


class FacebookPageIntelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    advertiser_name: Any | None = Field(None, alias="advertiserName", description="")
    input_mode: Literal['pageId', 'libraryId', 'query'] | None = Field(None, alias="inputMode", description="")
    match_confidence: Literal['high', 'medium', 'low'] | None = Field(None, alias="matchConfidence", description="")
    match_reason: str | None = Field(None, alias="matchReason", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    matched_advertisers: list[dict[str, Any]] | None = Field(None, alias="matchedAdvertisers", description="")
    total_ads: int | None = Field(None, alias="totalAds", description="")
    active_count: int | None = Field(None, alias="activeCount", description="")
    video_count: int | None = Field(None, alias="videoCount", description="")
    image_count: int | None = Field(None, alias="imageCount", description="")
    ads: list[dict[str, Any]] | None = Field(None, alias="ads", description="")
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
