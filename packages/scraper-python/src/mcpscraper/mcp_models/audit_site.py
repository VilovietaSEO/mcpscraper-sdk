from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AuditSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public website URL or domain for a full technical SEO audit (issues, link graph, indexability, headings, images). Bare domains default to https://. For plain content use extract_site instead.")
    max_pages: int | None = Field(None, alias="maxPages", description="Maximum pages to crawl and audit. MCP audits always run as durable background exports and return a jobId; poll check_site_export for the hosted audit ZIP.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required unique opaque ID for this intended audit (a UUID is ideal). Reuse the same value only when retrying the same call after a timeout; use a new value for every intentional rerun. This prevents a lost response from creating or charging for a duplicate job.")
    rotate_proxies: bool | None = Field(None, alias="rotateProxies", description="Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks. Slower/pricier — use only when a site blocks normal crawling.")
    rotate_proxy_every: int | None = Field(None, alias="rotateProxyEvery", description="When rotateProxies is on, pages fetched per proxy before rotating. Default 30.")
    background: bool | None = Field(None, alias="background", description="MCP technical audits always run as durable background jobs. Poll check_site_export for progress, outcome counters, and the hosted audit ZIP.")
    delivery: Literal['auto', 'artifact'] | None = Field(None, alias="delivery", description="Technical audits are durable exports. auto and artifact both return a job handle followed by an owner-scoped ZIP; artifact explicitly requests that durable destination.")
    preserve_media: bool | None = Field(None, alias="preserveMedia", description="Include supported images in the export bundle. This is the preferred replacement for downloadImages.")
    download_images: bool | None = Field(None, alias="downloadImages", description="Deprecated alias for preserveMedia. Omit when using preserveMedia; when omitted, image preservation defaults to false.")


class AuditSiteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="")
    page_count: int | None = Field(None, alias="pageCount", description="Absent when background is true — the audit has not finished yet.")
    duration_ms: float | None = Field(None, alias="durationMs", description="Absent when background is true — the audit has not finished yet.")
    bulk_folder: Any | None = Field(None, alias="bulkFolder", description="Absent when background is true — the audit has not finished yet.")
    issues: dict[str, Any] | None = Field(None, alias="issues", description="Absent when background is true — the audit has not finished yet.")
    images: dict[str, Any] | None = Field(None, alias="images", description="Absent when background is true — the audit has not finished yet.")
    links: dict[str, Any] | None = Field(None, alias="links", description="Absent when background is true — the audit has not finished yet.")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    job_id: str | None = Field(None, alias="jobId", description="Present when background (or downloadImages) was set — poll with check_site_export.")
    status: Literal['pending'] | None = Field(None, alias="status", description="Present when background (or downloadImages) was set.")
    status_url: str | None = Field(None, alias="statusUrl", description="Present when background (or downloadImages) was set — informational; use check_site_export with jobId, not this URL directly.")
    requested_max_pages: int | None = Field(None, alias="requestedMaxPages", description="")
    effective_max_pages: int | None = Field(None, alias="effectiveMaxPages", description="")
    credit_limited: bool | None = Field(None, alias="creditLimited", description="")
    credit_truncated: bool | None = Field(None, alias="creditTruncated", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
