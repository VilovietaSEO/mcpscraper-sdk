from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class LocationMarketsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    state: str | None = Field(None, alias="state", description="US state abbreviation or full name, e.g. TN or Tennessee.")
    city: str | None = Field(None, alias="city", description="Optional city-name filter, matched case-insensitively before the result limit.")
    zip: str | None = Field(None, alias="zip", description="Optional exact five-digit ZIP filter.")
    min_population: int | None = Field(None, alias="minPopulation", description="Minimum hosted Census place population.")
    population_year: int | None = Field(None, alias="populationYear", description="Population estimate year from the hosted Census snapshot.")
    max_results: int | None = Field(None, alias="maxResults", description="Maximum markets to return, sorted by population descending.")
    include_zip_groups: bool | None = Field(None, alias="includeZipGroups", description="Include ZIP and county groups from the active hosted ZIP dataset.")


class LocationMarketsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    state: str = Field(..., alias="state", description="")
    city: Any = Field(..., alias="city", description="")
    zip: Any = Field(..., alias="zip", description="")
    min_population: int = Field(..., alias="minPopulation", description="")
    population_year: int = Field(..., alias="populationYear", description="")
    max_results: int = Field(..., alias="maxResults", description="")
    count: int = Field(..., alias="count", description="")
    markets: list[dict[str, Any]] = Field(..., alias="markets", description="")
    sources: dict[str, Any] = Field(..., alias="sources", description="")
    warnings: list[str] = Field(..., alias="warnings", description="")
