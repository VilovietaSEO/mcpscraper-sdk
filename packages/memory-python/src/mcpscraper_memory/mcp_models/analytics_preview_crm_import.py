from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsPreviewCrmImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    source_system: Literal['hubspot', 'salesforce', 'gohighlevel', 'zoho', 'pipedrive', 'keap', 'other'] = Field(..., alias="sourceSystem", description="CRM system represented by the uploaded CSV.")
    filename: str = Field(..., alias="filename", description="Original CSV filename retained for the import receipt; this is not a local path.")
    csv: str = Field(..., alias="csv", description="Complete bounded CSV text to validate and stage; do not pass a local filesystem path.")
    mapping: dict[str, Any] = Field(..., alias="mapping", description="CSV-column mapping used to identify and protect supported CRM fields.")


class AnalyticsPreviewCrmImportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    preview: Any = Field(..., alias="preview", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
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
