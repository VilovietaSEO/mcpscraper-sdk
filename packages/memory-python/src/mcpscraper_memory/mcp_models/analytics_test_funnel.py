from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsTestFunnelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    definition: dict[str, Any] = Field(..., alias="definition", description="Unsaved funnel definition to evaluate without persistence.")
    records: list[dict[str, Any]] = Field(..., alias="records", description="Bounded safe fixtures. personId, contact data, IP, click IDs, device identifiers, and provider bodies are schema-invalid.")
    start: str = Field(..., alias="start", description="Inclusive fixture window start.")
    end: str = Field(..., alias="end", description="Exclusive fixture window end.")


class AnalyticsTestFunnelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    result: dict[str, Any] = Field(..., alias="result", description="")
