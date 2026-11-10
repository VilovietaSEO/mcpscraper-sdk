from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CaptureSerpSnapshotInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Search topic to capture, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.")
    location: str | None = Field(None, alias="location", description="Where Google should think the searcher is. Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.")
    gl: str | None = Field(None, alias="gl", description="Google country code inferred from the requested market.")
    hl: str | None = Field(None, alias="hl", description="Google interface/content language inferred from the user request.")
    device: Literal['desktop', 'mobile'] | None = Field(None, alias="device", description="SERP device context. Use mobile only for mobile rankings/evidence.")
    pages: int | None = Field(None, alias="pages", description="Google result pages to capture. Use 2 only for deeper ranking evidence.")
    include_page_snapshots: bool | None = Field(None, alias="includePageSnapshots", description="Also capture ranking-page snapshots for selected SERP URLs. Each attempted snapshot adds 1 Credit.")
    page_snapshot_limit: int | None = Field(None, alias="pageSnapshotLimit", description="Maximum ranking-page snapshots when includePageSnapshots is true. This capacity is held up front and unused capacity is refunded.")


class CaptureSerpSnapshotOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    schema_version: str | None = Field(None, alias="schemaVersion", description="")
    status: str | None = Field(None, alias="status", description="")
    query: Any | None = Field(None, alias="query", description="")
    location: Any | None = Field(None, alias="location", description="")
    captured_at: Any | None = Field(None, alias="capturedAt", description="")
    result_count: Any | None = Field(None, alias="resultCount", description="")
    organic_result_count: int | None = Field(None, alias="organicResultCount", description="")
    local_pack_result_count: int | None = Field(None, alias="localPackResultCount", description="")
    page_snapshot_count: int | None = Field(None, alias="pageSnapshotCount", description="")
    page_snapshot_failed_count: int | None = Field(None, alias="pageSnapshotFailedCount", description="")
    snapshot_id: Any | None = Field(None, alias="snapshotId", description="")
    resolved_inputs: dict[str, Any] | None = Field(None, alias="resolvedInputs", description="")
    artifacts: list[dict[str, Any]] | None = Field(None, alias="artifacts", description="")
    billing: Any | None = Field(None, alias="billing", description="")
    diagnostics: Any | None = Field(None, alias="diagnostics", description="")
    harvest_result: dict[str, Any] | None = Field(None, alias="harvestResult", description="")
    location_evidence: Any | None = Field(None, alias="locationEvidence", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
