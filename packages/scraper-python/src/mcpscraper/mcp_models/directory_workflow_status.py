from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class DirectoryWorkflowStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by directory_workflow. Poll until status is complete, partial, empty, or failed.")


class DirectoryWorkflowStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: Any = Field(..., alias="jobId", description="")
    status: Literal['queued', 'running', 'complete', 'partial', 'empty', 'failed'] = Field(..., alias="status", description="")
    status_url: Any = Field(..., alias="statusUrl", description="")
    query: str = Field(..., alias="query", description="")
    state: str = Field(..., alias="state", description="")
    min_population: int = Field(..., alias="minPopulation", description="")
    population_year: int = Field(..., alias="populationYear", description="")
    max_results_per_city: int = Field(..., alias="maxResultsPerCity", description="")
    concurrency: int = Field(..., alias="concurrency", description="")
    census_source_url: str = Field(..., alias="censusSourceUrl", description="")
    us_zips_source_path: Any = Field(..., alias="usZipsSourcePath", description="")
    warnings: list[str] = Field(..., alias="warnings", description="")
    extracted_at: str = Field(..., alias="extractedAt", description="")
    selected_city_count: int = Field(..., alias="selectedCityCount", description="")
    total_result_count: int = Field(..., alias="totalResultCount", description="")
    csv_path: Any = Field(..., alias="csvPath", description="")
    csv_artifact: Any = Field(..., alias="csvArtifact", description="")
    progress: dict[str, Any] = Field(..., alias="progress", description="")
    billing: dict[str, Any] = Field(..., alias="billing", description="")
    error_code: Any = Field(..., alias="errorCode", description="")
    error: Any = Field(..., alias="error", description="")
    retryable: Any = Field(..., alias="retryable", description="")
    cities: list[dict[str, Any]] = Field(..., alias="cities", description="")
    duration_ms: int = Field(..., alias="durationMs", description="")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
