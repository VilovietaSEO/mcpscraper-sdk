from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AuditSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public website URL or domain for a full technical SEO audit (issues, link graph, indexability, headings, images). For plain content use extract_site instead.")
    max_pages: int | None = Field(None, alias="maxPages", description="Maximum pages to crawl and audit. Always writes a folder of analysis files plus per-page content, returning a summary plus the folder path.")
    rotate_proxies: bool | None = Field(None, alias="rotateProxies", description="Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks. Slower/pricier — use only when a site blocks normal crawling.")
    rotate_proxy_every: int | None = Field(None, alias="rotateProxyEvery", description="When rotateProxies is on, pages fetched per proxy before rotating. Default 30.")


class AuditSiteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="")
    page_count: int = Field(..., alias="pageCount", description="")
    duration_ms: float = Field(..., alias="durationMs", description="")
    bulk_folder: Any = Field(..., alias="bulkFolder", description="")
    issues: dict[str, Any] = Field(..., alias="issues", description="")
    images: dict[str, Any] = Field(..., alias="images", description="")
    links: dict[str, Any] = Field(..., alias="links", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
