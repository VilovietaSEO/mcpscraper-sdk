from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MapSiteUrlsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public website URL or domain to crawl for internal URLs. Use before extract_site when the user asks to audit/map/crawl a site.")
    max_urls: int | None = Field(None, alias="maxUrls", description="Maximum URLs to discover. Use 100 for normal maps, up to 10000 for a full inventory. Large maps (over 500 URLs) write the complete inventory to a local file and return only a summary plus the file path instead of the full list inline.")


class MapSiteUrlsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    start_url: str = Field(..., alias="startUrl", description="")
    total_found: int = Field(..., alias="totalFound", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    ok_count: int = Field(..., alias="okCount", description="")
    redirect_count: int = Field(..., alias="redirectCount", description="")
    broken_count: int = Field(..., alias="brokenCount", description="")
    urls: list[dict[str, Any]] = Field(..., alias="urls", description="")
    duration_ms: float = Field(..., alias="durationMs", description="")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
