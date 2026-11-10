from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsCreateFormInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    pixel_id: str = Field(..., alias="pixelId", description="Analytics Pixel id belonging to the selected Site.")
    name: str = Field(..., alias="name", description="Human-readable name for the record being created or updated.")
    fields: list[dict[str, Any]] = Field(..., alias="fields", description="Ordered form-field definitions to render and validate for submissions.")
    brand: dict[str, Any] = Field(..., alias="brand", description="Validated visual-brand settings applied to the generated form.")
    submit_label: str | None = Field(None, alias="submitLabel", description="Optional text displayed on the form submission button.")
    success_message: str | None = Field(None, alias="successMessage", description="Optional confirmation shown after a successful form submission.")
    consent_text: str | None = Field(None, alias="consentText", description="Optional consent disclosure displayed with the form submission control.")
    publish: bool | None = Field(None, alias="publish", description="When true, publish the created form immediately; set false to keep it unpublished.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsCreateFormOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    form: dict[str, Any] | None = Field(None, alias="form", description="")
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
