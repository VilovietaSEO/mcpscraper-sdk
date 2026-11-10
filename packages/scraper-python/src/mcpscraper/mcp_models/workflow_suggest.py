from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class WorkflowSuggestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    goal: str = Field(..., alias="goal", description="The user goal or job to route, e.g. \"market analysis for roofers in Tennessee\", \"ICP research for med spas\", \"CRO audit for this URL\", or \"brand design briefing\".")
    query: str | None = Field(None, alias="query", description="Business category, niche, or Maps query when known.")
    keyword: str | None = Field(None, alias="keyword", description="Search keyword, audience problem, or content topic when known.")
    domain: str | None = Field(None, alias="domain", description="Target domain or brand domain when known.")
    url: str | None = Field(None, alias="url", description="Target URL when the workflow should inspect a specific page.")
    location: str | None = Field(None, alias="location", description="City/region/country for localized research, e.g. Denver, CO.")
    state: str | None = Field(None, alias="state", description="US state abbreviation or name for state-wide market research.")
    max_suggestions: int | None = Field(None, alias="maxSuggestions", description="Number of matching workflow recipes to return.")


class WorkflowSuggestOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    goal: str | None = Field(None, alias="goal", description="")
    suggestions: list[dict[str, Any]] | None = Field(None, alias="suggestions", description="")
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
