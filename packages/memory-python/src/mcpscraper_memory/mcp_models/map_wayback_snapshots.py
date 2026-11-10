from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class MapWaybackSnapshotsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Original public page/site URL, domain, or a web.archive.org replay URL to inventory.")
    scope: Literal['exact', 'prefix', 'host', 'domain'] | None = Field(None, alias="scope", description="exact = one page; prefix = one path tree; host = one hostname; domain = the domain plus subdomains. Ignored when urls is provided.")
    urls: list[str] | None = Field(None, alias="urls", description="Optional selected page URLs to inventory together using exact matching. Every URL must belong to the same site as url.")
    from_: str | None = Field(None, alias="from", description="Inclusive beginning of the archive range: YYYY, YYYY-MM, YYYY-MM-DD, or a 14-digit Wayback timestamp.")
    to: str | None = Field(None, alias="to", description="Inclusive end of the archive range: YYYY, YYYY-MM, YYYY-MM-DD, or a 14-digit Wayback timestamp.")
    successful_html_only: bool | None = Field(None, alias="successfulHtmlOnly", description="Count only HTTP 200 text/html captures. Set false to include redirects, errors, and archived assets.")
    max_captures: int | None = Field(None, alias="maxCaptures", description="Maximum CDX capture rows to scan. If reached, countType is lower_bound instead of exact. Narrow the range or raise this cap for an exact large inventory.")
    include_captures: bool | None = Field(None, alias="includeCaptures", description="Return individual timestamp rows in addition to aggregate counts. Leave false for a compact count-only inventory.")
    max_capture_rows: int | None = Field(None, alias="maxCaptureRows", description="Maximum individual capture rows returned when includeCaptures is true. Aggregated counts still use every scanned capture.")
    delivery: Literal['auto', 'inline', 'artifact'] | None = Field(None, alias="delivery", description="auto returns bounded results and offloads large inventories; inline still offloads above the hard context limit; artifact always creates an owner-scoped report artifact.")


class MapWaybackSnapshotsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str | None = Field(None, alias="url", description="")
    scope: Any = Field(..., alias="scope", description="")
    selected_urls: Any | None = Field(None, alias="selectedUrls", description="")
    from_: Any | None = Field(None, alias="from", description="")
    to: Any | None = Field(None, alias="to", description="")
    successful_html_only: bool | None = Field(None, alias="successfulHtmlOnly", description="")
    total_captures: int | None = Field(None, alias="totalCaptures", description="")
    count_type: Literal['exact', 'lower_bound'] | None = Field(None, alias="countType", description="")
    complete: bool | None = Field(None, alias="complete", description="")
    truncated: bool | None = Field(None, alias="truncated", description="")
    max_captures: int | None = Field(None, alias="maxCaptures", description="")
    query_pages: int | None = Field(None, alias="queryPages", description="")
    unique_urls: int | None = Field(None, alias="uniqueUrls", description="")
    unique_digests: int | None = Field(None, alias="uniqueDigests", description="")
    first_capture: Any | None = Field(None, alias="firstCapture", description="")
    last_capture: Any | None = Field(None, alias="lastCapture", description="")
    monthly_counts: list[dict[str, Any]] | None = Field(None, alias="monthlyCounts", description="")
    yearly_counts: list[dict[str, Any]] | None = Field(None, alias="yearlyCounts", description="")
    missing_months: list[str] | None = Field(None, alias="missingMonths", description="")
    per_url: list[dict[str, Any]] | None = Field(None, alias="perUrl", description="")
    per_url_truncated_count: int | None = Field(None, alias="perUrlTruncatedCount", description="")
    captures: list[dict[str, Any]] | None = Field(None, alias="captures", description="")
    capture_rows_truncated_count: int | None = Field(None, alias="captureRowsTruncatedCount", description="")
    duration_ms: float | None = Field(None, alias="durationMs", description="")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    delivery: Any = Field(..., alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
