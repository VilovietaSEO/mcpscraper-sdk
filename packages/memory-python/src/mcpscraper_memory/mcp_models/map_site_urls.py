from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class MapSiteUrlsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public website URL or domain to inventory internal URLs. Bare domains default to https://. Use extract_site directly when page content is needed; it discovers URLs during the crawl.")
    max_urls: int | None = Field(None, alias="maxUrls", description="Maximum URLs to discover. Use 100 for normal maps, up to 10000 for a full inventory. Large maps (over 500 URLs) write the complete inventory to a local file and return only a summary plus the file path instead of the full list inline.")
    delivery: Literal['auto', 'inline', 'artifact'] | None = Field(None, alias="delivery", description="auto returns a bounded inline map and offloads large inventories; inline requests bounded inline delivery but still offloads above the hard context limit; artifact always creates an owner-scoped report artifact.")


class MapSiteUrlsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    start_url: str | None = Field(None, alias="startUrl", description="")
    total_found: int | None = Field(None, alias="totalFound", description="")
    truncated: bool | None = Field(None, alias="truncated", description="")
    ok_count: int | None = Field(None, alias="okCount", description="")
    redirect_count: int | None = Field(None, alias="redirectCount", description="")
    broken_count: int | None = Field(None, alias="brokenCount", description="")
    urls: list[dict[str, Any]] | None = Field(None, alias="urls", description="")
    duration_ms: float | None = Field(None, alias="durationMs", description="")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    delivery: Any = Field(..., alias="delivery", description="")
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
