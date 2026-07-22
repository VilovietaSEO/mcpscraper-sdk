from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CaptureSerpSnapshotInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Search query to capture. KEEP the place in the query text for localized captures (e.g. \"botox clinic austin tx\") and also set location.")
    location: str | None = Field(None, alias="location", description="City, region, country, or service area for localized Google results.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from the requested market.")
    hl: str | None = Field(None, alias="hl", description="Google interface/content language inferred from the user request.")
    device: Literal["desktop", "mobile"] | None = Field(None, alias="device", description="SERP device context. Use mobile only for mobile rankings/evidence.")
    proxy_mode: Literal["location", "configured", "none"] | None = Field(None, alias="proxyMode", description="Leave unset (clean egress). Do NOT set \"location\" just because a city was named — that comes from city-in-query wording. \"location\" forces residential geo-IP, is frequently CAPTCHA-blocked, and accepts failures.")
    proxy_zip: str | None = Field(None, alias="proxyZip", description="US ZIP for residential geo-IP targeting. Only meaningful with proxyMode \"location\".")
    pages: int | None = Field(None, alias="pages", description="Google result pages to capture. Use 2 only for deeper ranking evidence.")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized browser/proxy/location diagnostics.")
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
    attempts: list[dict[str, Any]] = Field(..., alias="attempts", description="")
    billing: Any = Field(..., alias="billing", description="")
    diagnostics: Any = Field(..., alias="diagnostics", description="")
    provider_payload: dict[str, Any] = Field(..., alias="providerPayload", description="")
