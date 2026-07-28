from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExtractSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public website URL/domain or web.archive.org replay URL. Without wayback, this crawls live content or one archived site snapshot. With wayback, it creates a multi-month archive timeline.")
    max_pages: int | None = Field(None, alias="maxPages", description="Maximum pages per Wayback month, or maximum total pages for a normal crawl. Multi-month jobs remain capped at 10,000 total captures and 500 pages per month.")
    wayback: dict[str, Any] | None = Field(None, alias="wayback", description="Optional temporal archive plan. Provide explicit YYYY-MM months or a from/to range plus intervalMonths. Omit urls for whole-site monthly snapshots, provide one URL for a single-page timeline, or several URLs for selected-page timelines. All results share one durable export.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required unique opaque ID for this intended export (a UUID is ideal). Reuse the same value only when retrying the same call after a timeout; use a new value for every intentional rerun. This prevents a lost response from creating or charging for a duplicate job.")
    rotate_proxies: bool | None = Field(None, alias="rotateProxies", description="Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks (403/429). Slower and pricier — use only when a site blocks normal crawling.")
    rotate_proxy_every: int | None = Field(None, alias="rotateProxyEvery", description="When rotateProxies is on, pages fetched per proxy before rotating. Default 30.")
    formats: list[Literal["markdown", "links", "json", "images", "branding"]] | None = Field(None, alias="formats", description="Per-page output formats: markdown, links, json, images are captured cheaply from HTML; branding (site-level logo/colors/fonts) requires a browser and adds time. Defaults to markdown+links.")
    background: bool | None = Field(None, alias="background", description="MCP multi-page crawls always run as durable background jobs. Poll check_site_export for progress, outcome counters, and the hosted ZIP.")
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
    requested_max_pages: int | None = Field(None, alias="requestedMaxPages", description="")
    effective_max_pages: int | None = Field(None, alias="effectiveMaxPages", description="")
    credit_limited: bool | None = Field(None, alias="creditLimited", description="")
    credit_truncated: bool | None = Field(None, alias="creditTruncated", description="")
