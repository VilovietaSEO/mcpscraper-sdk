from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MapWaybackSnapshotsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Original public page/site URL, domain, or a web.archive.org replay URL to inventory.")
    scope: Literal["exact", "prefix", "host", "domain"] | None = Field(None, alias="scope", description="exact = one page; prefix = one path tree; host = one hostname; domain = the domain plus subdomains. Ignored when urls is provided.")
    urls: list[str] | None = Field(None, alias="urls", description="Optional selected page URLs to inventory together using exact matching. Every URL must belong to the same site as url.")
    from_: str | None = Field(None, alias="from", description="Inclusive beginning of the archive range: YYYY, YYYY-MM, YYYY-MM-DD, or a 14-digit Wayback timestamp.")
    to: str | None = Field(None, alias="to", description="Inclusive end of the archive range: YYYY, YYYY-MM, YYYY-MM-DD, or a 14-digit Wayback timestamp.")
    successful_html_only: bool | None = Field(None, alias="successfulHtmlOnly", description="Count only HTTP 200 text/html captures. Set false to include redirects, errors, and archived assets.")
    max_captures: int | None = Field(None, alias="maxCaptures", description="Maximum CDX capture rows to scan. If reached, countType is lower_bound instead of exact. Narrow the range or raise this cap for an exact large inventory.")
    include_captures: bool | None = Field(None, alias="includeCaptures", description="Return individual timestamp rows in addition to aggregate counts. Leave false for a compact count-only inventory.")
    max_capture_rows: int | None = Field(None, alias="maxCaptureRows", description="Maximum individual capture rows returned when includeCaptures is true. Aggregated counts still use every scanned capture.")
    delivery: Literal["auto", "inline", "artifact"] | None = Field(None, alias="delivery", description="auto returns bounded results and offloads large inventories; inline still offloads above the hard context limit; artifact always creates an owner-scoped report artifact.")


class MapWaybackSnapshotsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="")
    scope: Literal["exact", "prefix", "host", "domain"] = Field(..., alias="scope", description="")
    selected_urls: Any = Field(..., alias="selectedUrls", description="")
    from_: Any = Field(..., alias="from", description="")
    to: Any = Field(..., alias="to", description="")
    successful_html_only: bool = Field(..., alias="successfulHtmlOnly", description="")
    total_captures: int = Field(..., alias="totalCaptures", description="")
    count_type: Literal["exact", "lower_bound"] = Field(..., alias="countType", description="")
    complete: bool = Field(..., alias="complete", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    max_captures: int = Field(..., alias="maxCaptures", description="")
    query_pages: int = Field(..., alias="queryPages", description="")
    unique_urls: int = Field(..., alias="uniqueUrls", description="")
    unique_digests: int = Field(..., alias="uniqueDigests", description="")
    first_capture: Any = Field(..., alias="firstCapture", description="")
    last_capture: Any = Field(..., alias="lastCapture", description="")
    monthly_counts: list[dict[str, Any]] = Field(..., alias="monthlyCounts", description="")
    yearly_counts: list[dict[str, Any]] = Field(..., alias="yearlyCounts", description="")
    missing_months: list[str] = Field(..., alias="missingMonths", description="")
    per_url: list[dict[str, Any]] = Field(..., alias="perUrl", description="")
    per_url_truncated_count: int = Field(..., alias="perUrlTruncatedCount", description="")
    captures: list[Any] = Field(..., alias="captures", description="")
    capture_rows_truncated_count: int = Field(..., alias="captureRowsTruncatedCount", description="")
    duration_ms: float = Field(..., alias="durationMs", description="")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
