from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RankTrackerWorkflowInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    project_name: str | None = Field(None, alias="projectName", description="Optional name for the rank tracker project, client, or campaign.")
    target_domain: str | None = Field(None, alias="targetDomain", description="Primary domain to track in organic results, AI Overview citations, and PAA sources.")
    target_business_name: str | None = Field(None, alias="targetBusinessName", description="Primary Google Business Profile/brand name to match in Maps results. Required for Maps tracking.")
    tracking_modes: list[Literal["maps", "organic", "ai_overview", "paa"]] | None = Field(None, alias="trackingModes", description="Rank tracker surfaces to build: maps, organic, ai_overview, paa.")
    keywords: list[str] | None = Field(None, alias="keywords", description="Seed keywords or service queries to track. Leave empty to derive from user input downstream.")
    locations: list[str] | None = Field(None, alias="locations", description="Markets, cities, ZIPs, or service areas to track, e.g. \"Denver, CO\".")
    competitors: list[str] | None = Field(None, alias="competitors", description="Optional competitor domains or business names to persist as comparison targets.")
    database: Literal["postgres", "neon", "supabase", "sqlite", "mysql"] | None = Field(None, alias="database", description="Database family to target when generating migrations.")
    schedule_cadence: Literal["daily", "weekly", "monthly", "custom"] | None = Field(None, alias="scheduleCadence", description="Default recurring rank check cadence.")
    custom_cron: str | None = Field(None, alias="customCron", description="Cron expression to use when scheduleCadence is custom.")
    timezone: str | None = Field(None, alias="timezone", description="IANA timezone for scheduled rank checks.")
    include_cron: bool | None = Field(None, alias="includeCron", description="Include a cron/heartbeat worker plan.")
    include_dashboard: bool | None = Field(None, alias="includeDashboard", description="Include dashboard/reporting requirements.")
    include_alerts: bool | None = Field(None, alias="includeAlerts", description="Include alert rules for rank movement and SERP feature changes.")
    notes: str | None = Field(None, alias="notes", description="Extra product, client, stack, or hosting requirements.")


class RankTrackerWorkflowOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    project_name: str = Field(..., alias="projectName", description="")
    target_domain: Any = Field(..., alias="targetDomain", description="")
    target_business_name: Any = Field(..., alias="targetBusinessName", description="")
    tracking_modes: list[Literal["maps", "organic", "ai_overview", "paa"]] = Field(..., alias="trackingModes", description="")
    database: str = Field(..., alias="database", description="")
    recommended_tools: list[dict[str, Any]] = Field(..., alias="recommendedTools", description="")
    tables: list[dict[str, Any]] = Field(..., alias="tables", description="")
    cron: dict[str, Any] = Field(..., alias="cron", description="")
    metrics: list[str] = Field(..., alias="metrics", description="")
    implementation_prompt: str = Field(..., alias="implementationPrompt", description="")
