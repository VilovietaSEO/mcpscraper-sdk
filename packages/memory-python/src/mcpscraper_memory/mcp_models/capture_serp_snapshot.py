from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CaptureSerpSnapshotInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Search topic to capture. When location is supplied, the server sets Google UULE and adds the location to the executed query only if its city is not already present; do not add it manually.")
    location: str | None = Field(None, alias="location", description="City, region, country, or service area for localized Google results. It sets UULE and supplies the city text when missing from query; it does not select a proxy.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from the requested market.")
    hl: str | None = Field(None, alias="hl", description="Google interface/content language inferred from the user request.")
    device: Literal["desktop", "mobile"] | None = Field(None, alias="device", description="SERP device context. Use mobile only for mobile rankings/evidence.")
    proxy_mode: Literal["configured", "none"] | None = Field(None, alias="proxyMode", description="Leave unset for direct egress. Set configured only when the installed server has a configured proxy and the user explicitly needs it; location is handled separately with UULE and query text.")
    proxy_zip: str | None = Field(None, alias="proxyZip", description="Optional US ZIP override for configured proxy routing.")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized browser/proxy/location diagnostics.")
    pages: int | None = Field(None, alias="pages", description="Google result pages to capture. Use 2 only for deeper ranking evidence.")
    include_page_snapshots: bool | None = Field(None, alias="includePageSnapshots", description="Also capture ranking-page snapshots for selected SERP URLs. Each attempted snapshot adds 1 Credit.")
    page_snapshot_limit: int | None = Field(None, alias="pageSnapshotLimit", description="Maximum ranking-page snapshots when includePageSnapshots is true. This capacity is held up front and unused capacity is refunded.")


class CaptureSerpSnapshotOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    schema_version: str = Field(..., alias="schemaVersion", description="")
    status: str = Field(..., alias="status", description="")
    query: Any = Field(..., alias="query", description="")
    location: Any = Field(..., alias="location", description="")
    captured_at: Any = Field(..., alias="capturedAt", description="")
    result_count: Any = Field(..., alias="resultCount", description="")
    organic_result_count: int = Field(..., alias="organicResultCount", description="")
    local_pack_result_count: int = Field(..., alias="localPackResultCount", description="")
    page_snapshot_count: int = Field(..., alias="pageSnapshotCount", description="")
    page_snapshot_failed_count: int = Field(..., alias="pageSnapshotFailedCount", description="")
    snapshot_id: Any = Field(..., alias="snapshotId", description="")
    resolved_inputs: dict[str, Any] = Field(..., alias="resolvedInputs", description="")
    artifacts: list[dict[str, Any]] = Field(..., alias="artifacts", description="")
    billing: Any = Field(..., alias="billing", description="")
    diagnostics: Any = Field(..., alias="diagnostics", description="")
    provider_payload: dict[str, Any] = Field(..., alias="providerPayload", description="")
