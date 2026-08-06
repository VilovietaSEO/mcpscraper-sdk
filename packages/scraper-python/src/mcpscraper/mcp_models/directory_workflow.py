from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class DirectoryWorkflowInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Business category, niche, or keyword to search on Google Maps for every market. Do not include the city.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required unique opaque ID for this intended directory job (a UUID is ideal). Reuse the same value only when retrying the same call after a timeout; use a new value for every intentional rerun. This prevents a lost response from creating or charging for a duplicate job.")
    state: str | None = Field(None, alias="state", description="US state abbreviation or name used to select Census places, e.g. TN.")
    min_population: int | None = Field(None, alias="minPopulation", description="Minimum Census place population for market selection.")
    population_year: int | None = Field(None, alias="populationYear", description="Census population estimate year (2020-2025 Population Estimates Program).")
    max_cities: int | None = Field(None, alias="maxCities", description="Maximum markets to process after sorting by population descending.")
    max_results_per_city: int | None = Field(None, alias="maxResultsPerCity", description="Google Maps candidates to collect per city.")
    concurrency: int | None = Field(None, alias="concurrency", description="City Maps searches to run in parallel.")
    include_zip_groups: bool | None = Field(None, alias="includeZipGroups", description="Attach ZIP and county groups from the active versioned hosted location dataset. Production never reads a server-local CSV.")
    save_csv: bool | None = Field(None, alias="saveCsv", description="Create a directory-ready CSV. Hosted runs return an owner-scoped artifact; local runs may also return a filesystem path.")
    background: bool | None = Field(None, alias="background", description="Hosted MCP directory jobs always run durably in the background. Poll directory_workflow_status for progress, terminal billing, and the owner-scoped CSV artifact.")


class DirectoryWorkflowOutput(BaseModel):
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
