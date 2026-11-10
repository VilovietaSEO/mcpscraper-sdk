from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class RankTrackerWorkflowInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    project_name: str | None = Field(None, alias="projectName", description="Optional name for the rank tracker project, client, or campaign.")
    target_domain: str | None = Field(None, alias="targetDomain", description="Primary domain to track in organic results, AI Overview citations, and PAA sources.")
    target_business_name: str | None = Field(None, alias="targetBusinessName", description="Primary Google Business Profile/brand name to match in Maps results. Supply it when matching one business against Maps results.")
    tracking_modes: list[Literal['maps', 'organic', 'ai_overview', 'paa']] | None = Field(None, alias="trackingModes", description="Rank tracker surfaces to build: maps, organic, ai_overview, paa.")
    keywords: list[str] | None = Field(None, alias="keywords", description="Seed keywords or service queries to track. Leave empty to derive from user input downstream.")
    locations: list[str] | None = Field(None, alias="locations", description="Markets, cities, ZIPs, or service areas to track, e.g. \"Denver, CO\".")
    competitors: list[str] | None = Field(None, alias="competitors", description="Optional competitor domains or business names to persist as comparison targets.")
    database: Literal['postgres', 'neon', 'supabase', 'sqlite', 'mysql'] | None = Field(None, alias="database", description="Database family to target when generating migrations.")
    include_dashboard: bool | None = Field(None, alias="includeDashboard", description="Include dashboard/reporting requirements.")
    include_alerts: bool | None = Field(None, alias="includeAlerts", description="Include saved change findings when manually comparing rank movement and SERP features.")
    notes: str | None = Field(None, alias="notes", description="Extra product, client, stack, or hosting requirements.")


class RankTrackerWorkflowOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    project_name: str | None = Field(None, alias="projectName", description="")
    target_domain: Any | None = Field(None, alias="targetDomain", description="")
    target_business_name: Any | None = Field(None, alias="targetBusinessName", description="")
    tracking_modes: list[Literal['maps', 'organic', 'ai_overview', 'paa']] | None = Field(None, alias="trackingModes", description="")
    database: str | None = Field(None, alias="database", description="")
    recommended_tools: list[dict[str, Any]] | None = Field(None, alias="recommendedTools", description="")
    tables: list[dict[str, Any]] | None = Field(None, alias="tables", description="")
    steps: list[dict[str, Any]] | None = Field(None, alias="steps", description="")
    metrics: list[str] | None = Field(None, alias="metrics", description="")
    implementation_prompt: str | None = Field(None, alias="implementationPrompt", description="")
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
