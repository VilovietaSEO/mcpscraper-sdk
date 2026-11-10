from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsTestFunnelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    definition: dict[str, Any] = Field(..., alias="definition", description="Unsaved funnel definition to evaluate without persistence.")
    records: list[dict[str, Any]] = Field(..., alias="records", description="Bounded safe fixtures. personId, contact data, IP, click IDs, device identifiers, and provider bodies are schema-invalid.")
    start: str = Field(..., alias="start", description="Inclusive fixture window start.")
    end: str = Field(..., alias="end", description="Exclusive fixture window end.")


class AnalyticsTestFunnelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    result: dict[str, Any] | None = Field(None, alias="result", description="")
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
