from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExtractSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public website URL or domain to crawl for page CONTENT (map + scrape). For a technical SEO audit use audit_site instead — this returns content only, not analysis.")
    max_pages: int | None = Field(None, alias="maxPages", description="Maximum pages to extract. Bulk crawls (over 25 pages) switch to folder mode: each page saved as its own Markdown file, with a summary plus folder path returned instead of inlining content.")
    rotate_proxies: bool | None = Field(None, alias="rotateProxies", description="Use extra measures to get past sites that block normal crawling (403/429). Slower and pricier — use only when a site blocks normal crawling.")
    rotate_proxy_every: int | None = Field(None, alias="rotateProxyEvery", description="When rotateProxies is on, pages fetched per proxy before rotating. Default 30.")
    formats: list[Literal["markdown", "links", "json", "images", "branding"]] | None = Field(None, alias="formats", description="Per-page output formats: markdown, links, json, images are captured cheaply from HTML; branding (site-level logo/colors/fonts) requires a browser and adds time. Defaults to markdown+links.")
    background: bool | None = Field(None, alias="background", description="Run the crawl as a background job instead of blocking this call, returning a jobId immediately — poll it with check_site_export to get a downloadable zip (all page content, plus real image files if downloadImages is set) once ready. Use for large sites where a synchronous call would be slow.")
    download_images: bool | None = Field(None, alias="downloadImages", description="Download every discovered image as a real file into the export bundle (not just image URLs/stats). OFF by default — must be explicitly set true. Implies background regardless of the background flag, since downloading a whole site's images is too slow to run synchronously. Capped at 20 images/page and 500 images/site.")


class ExtractSiteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="")
    page_count: int | None = Field(None, alias="pageCount", description="Absent when background is true — the crawl has not finished yet.")
    pages: list[dict[str, Any]] | None = Field(None, alias="pages", description="Absent when background is true — the crawl has not finished yet.")
    duration_ms: float | None = Field(None, alias="durationMs", description="Absent when background is true — the crawl has not finished yet.")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    job_id: str | None = Field(None, alias="jobId", description="Present when background (or downloadImages) was set — poll with check_site_export.")
    status: Literal["pending"] | None = Field(None, alias="status", description="Present when background (or downloadImages) was set.")
    status_url: str | None = Field(None, alias="statusUrl", description="Present when background (or downloadImages) was set — informational; use check_site_export with jobId, not this URL directly.")
