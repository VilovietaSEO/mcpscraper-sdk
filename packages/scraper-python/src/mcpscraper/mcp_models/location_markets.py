from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


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

    state: str | None = Field(None, alias="state", description="")
    city: Any | None = Field(None, alias="city", description="")
    zip: Any | None = Field(None, alias="zip", description="")
    min_population: int | None = Field(None, alias="minPopulation", description="")
    population_year: int | None = Field(None, alias="populationYear", description="")
    max_results: int | None = Field(None, alias="maxResults", description="")
    count: int | None = Field(None, alias="count", description="")
    markets: list[dict[str, Any]] | None = Field(None, alias="markets", description="")
    sources: dict[str, Any] | None = Field(None, alias="sources", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
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
