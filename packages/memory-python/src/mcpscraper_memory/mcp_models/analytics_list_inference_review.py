from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsListInferenceReviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    namespace_id: str = Field(..., alias="namespaceId", description="Identity Namespace belonging to this Site.")
    limit: int | None = Field(None, alias="limit", description="Maximum safe rows.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque pagination cursor.")
    band: Literal['high', 'medium', 'low', 'ineligible'] | None = Field(None, alias="band", description="Candidate confidence band. Medium is review-only and low remains unlinked.")


class AnalyticsListInferenceReviewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    candidates: list[dict[str, Any]] | None = Field(None, alias="candidates", description="")
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
