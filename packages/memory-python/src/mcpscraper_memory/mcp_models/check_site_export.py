from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CheckSiteExportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by extract_site or audit_site. Poll until status is complete, partial, or failed; partial jobs still return a downloadable bundle with successful pages and failure details.")


class CheckSiteExportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="")
    status: Literal['pending', 'running', 'complete', 'partial', 'failed'] = Field(..., alias="status", description="")
    start_url: str | None = Field(None, alias="startUrl", description="")
    total_urls: int | None = Field(None, alias="totalUrls", description="")
    done_urls: int | None = Field(None, alias="doneUrls", description="")
    discovered: int | None = Field(None, alias="discovered", description="")
    attempted: int | None = Field(None, alias="attempted", description="")
    successful: int | None = Field(None, alias="successful", description="")
    failed: int | None = Field(None, alias="failed", description="")
    remaining: int | None = Field(None, alias="remaining", description="")
    requested_max_pages: int | None = Field(None, alias="requestedMaxPages", description="Page cap requested by the caller.")
    effective_max_pages: int | None = Field(None, alias="effectiveMaxPages", description="Page cap funded by the available credit hold.")
    credit_limited: bool | None = Field(None, alias="creditLimited", description="True when available credits reduced the requested page cap.")
    credit_truncated: bool | None = Field(None, alias="creditTruncated", description="True when the crawl reached the reduced funded cap and may have omitted discoverable pages.")
    bundle_url: Any = Field(..., alias="bundleUrl", description="Downloadable ZIP URL for a terminal complete, partial, or diagnostic failed export; null while unavailable.")
    artifact_id: Any | None = Field(None, alias="artifactId", description="Owner-scoped artifact ID for archive_read. Prefer this over the temporary bundle URL.")
    bundle_bytes: Any = Field(..., alias="bundleBytes", description="ZIP size in bytes when a bundle is available; null otherwise.")
    bundle_expires_at: Any | None = Field(None, alias="bundleExpiresAt", description="Artifact retention expiry when the hosted bundle is private.")
    bundle_url_expires_at: Any | None = Field(None, alias="bundleUrlExpiresAt", description="Signed download URL expiry when applicable.")
    error: Any | None = Field(None, alias="error", description="Terminal error or partial-delivery explanation, when present.")
    error_code: str | None = Field(None, alias="error_code", description="")
    error_type: str | None = Field(None, alias="error_type", description="")
    retryable: bool | None = Field(None, alias="retryable", description="")
    retry_after_seconds: int | None = Field(None, alias="retry_after_seconds", description="")
    charge_status: Literal['not_charged', 'refund_pending', 'refunded', 'charged'] | None = Field(None, alias="charge_status", description="")
    next_actions: dict[str, Any] | None = Field(None, alias="nextActions", description="Machine-readable next tool calls for polling, direct page reads, image reads, and human download.")
    updated_at: str | None = Field(None, alias="updatedAt", description="")
    local_path: Any | None = Field(None, alias="localPath", description="Server-generated path when an installed stdio server mirrored the ZIP under MCP_SCRAPER_OUTPUT_DIR.")
    local_mirror_error: Any | None = Field(None, alias="localMirrorError", description="Why optional local mirroring failed; the owner-scoped artifact remains available.")
