from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class DirectoryWorkflowInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Business category, niche, or keyword to search on Google Maps for every market. Do not include the city.")
    state: str | None = Field(None, alias="state", description="US state abbreviation or name used to select Census places, e.g. TN.")
    min_population: int | None = Field(None, alias="minPopulation", description="Minimum Census place population for market selection.")
    population_year: int | None = Field(None, alias="populationYear", description="Census population estimate year (2020-2025 Population Estimates Program).")
    max_cities: int | None = Field(None, alias="maxCities", description="Maximum markets to process after sorting by population descending.")
    max_results_per_city: int | None = Field(None, alias="maxResultsPerCity", description="Google Maps candidates to collect per city.")
    concurrency: int | None = Field(None, alias="concurrency", description="City Maps searches to run in parallel.")
    include_zip_groups: bool | None = Field(None, alias="includeZipGroups", description="Attach ZIP groups from a configured US ZIPS CSV when available (MCP_SCRAPER_USZIPS_CSV_PATH or usZipsCsvPath).")
    us_zips_csv_path: str | None = Field(None, alias="usZipsCsvPath", description="Local/test-only path to a US ZIPS CSV (state_abbr, zipcode, county, city columns). Deployed APIs should use MCP_SCRAPER_USZIPS_CSV_PATH instead. For ZIP enrichment, set MCP_SCRAPER_USZIPS_CSV_PATH on the server, or pass this in local/test mode.")
    save_csv: bool | None = Field(None, alias="saveCsv", description="Save a directory-ready CSV of results to the MCP Scraper output directory and return its path.")
    proxy_mode: Literal["location", "configured", "none"] | None = Field(None, alias="proxyMode", description="Proxy behavior per city search. Leave unset for the default route (stealth browser on the managed ISP proxy, retried fresh on a Google block). location forces an explicit residential proxy — not recommended for Google.")
    proxy_zip: str | None = Field(None, alias="proxyZip", description="Optional ZIP override for proxy targeting; normally omitted.")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized browser/proxy diagnostics.")


class DirectoryWorkflowOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

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
    cities: list[dict[str, Any]] = Field(..., alias="cities", description="")
    duration_ms: int = Field(..., alias="durationMs", description="")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
