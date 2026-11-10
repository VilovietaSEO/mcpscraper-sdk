from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class DirectoryWorkflowStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by directory_workflow. Poll until status is complete, partial, empty, or failed.")


class DirectoryWorkflowStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: Any | None = Field(None, alias="jobId", description="")
    status: Literal['queued', 'running', 'complete', 'partial', 'empty', 'failed'] | None = Field(None, alias="status", description="")
    status_url: Any | None = Field(None, alias="statusUrl", description="")
    query: str | None = Field(None, alias="query", description="")
    state: str | None = Field(None, alias="state", description="")
    min_population: int | None = Field(None, alias="minPopulation", description="")
    population_year: int | None = Field(None, alias="populationYear", description="")
    max_results_per_city: int | None = Field(None, alias="maxResultsPerCity", description="")
    concurrency: int | None = Field(None, alias="concurrency", description="")
    census_source_url: str | None = Field(None, alias="censusSourceUrl", description="")
    us_zips_source_path: Any | None = Field(None, alias="usZipsSourcePath", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    extracted_at: str | None = Field(None, alias="extractedAt", description="")
    selected_city_count: int | None = Field(None, alias="selectedCityCount", description="")
    total_result_count: int | None = Field(None, alias="totalResultCount", description="")
    csv_path: Any | None = Field(None, alias="csvPath", description="")
    csv_artifact: Any | None = Field(None, alias="csvArtifact", description="")
    progress: dict[str, Any] | None = Field(None, alias="progress", description="")
    billing: dict[str, Any] | None = Field(None, alias="billing", description="")
    error_code: Any | None = Field(None, alias="errorCode", description="")
    error: Any | None = Field(None, alias="error", description="")
    retryable: Any | None = Field(None, alias="retryable", description="")
    cities: list[dict[str, Any]] | None = Field(None, alias="cities", description="")
    duration_ms: int | None = Field(None, alias="durationMs", description="")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
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
