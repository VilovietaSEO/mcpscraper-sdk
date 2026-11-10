from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsValidateActivationMappingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    journey_tier: str | None = Field(None, alias="journeyTier", description="External activation is confirmed-only. Best-guess and candidate-assisted journey evidence is schema-invalid.")
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias="platform", description="Destination provider.")
    external_dataset_id: str = Field(..., alias="externalDatasetId", description="Authorized dataset, Pixel, or conversion-action id.")
    event_mapping: dict[str, Any] = Field(..., alias="eventMapping", description="Confirmed X-Ray event to provider event mapping.")


class AnalyticsValidateActivationMappingOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    validation: dict[str, Any] | None = Field(None, alias="validation", description="")
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
