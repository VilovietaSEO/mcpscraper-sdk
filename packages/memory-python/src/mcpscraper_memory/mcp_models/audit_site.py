from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AuditSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public website URL or domain for a full technical SEO audit (issues, link graph, indexability, headings, images). For plain content use extract_site instead.")
    max_pages: int | None = Field(None, alias="maxPages", description="Maximum pages to crawl and audit. Always writes a folder of analysis files plus per-page content, returning a summary plus the folder path.")
    rotate_proxies: bool | None = Field(None, alias="rotateProxies", description="Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks. Slower/pricier — use only when a site blocks normal crawling.")
    rotate_proxy_every: int | None = Field(None, alias="rotateProxyEvery", description="When rotateProxies is on, pages fetched per proxy before rotating. Default 30.")
    background: bool | None = Field(None, alias="background", description="Run the audit as a background job instead of blocking this call, returning a jobId immediately — poll it with check_site_export to get a downloadable zip (full audit report, all page content, plus real image files if downloadImages is set) once ready. Use for large sites where a synchronous call would be slow.")
    download_images: bool | None = Field(None, alias="downloadImages", description="Download every discovered image as a real file into the export bundle (not just image URLs/stats). OFF by default — must be explicitly set true. Implies background regardless of the background flag, since downloading a whole site's images is too slow to run synchronously. Capped at 20 images/page and 500 images/site.")


class AuditSiteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
