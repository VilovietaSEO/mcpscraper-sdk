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
    proxy_mode: Literal["location", "configured", "none"] | None = Field(None, alias="proxyMode", description="Proxy targeting per city search. Defaults to location (city/ZIP-group residential targeting); configured forces the service proxy; none is local debugging only.")
    proxy_zip: str | None = Field(None, alias="proxyZip", description="Optional ZIP override for proxy targeting; normally omitted.")
    debug: bool | None = Field(None, alias="debug", description="Include sanitized browser/proxy diagnostics.")


class DirectoryWorkflowOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
