from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class RenewConnectedDataDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str = Field(..., alias="artifactId", description="Private artifactId returned by export_connected_service_data or export_search_console_table_data.")


class RenewConnectedDataDownloadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    artifact_id: str | None = Field(None, alias="artifactId", description="")
    download_url: str | None = Field(None, alias="downloadUrl", description="")
    download_url_expires_at: str | None = Field(None, alias="downloadUrlExpiresAt", description="")
    expires_at: str | None = Field(None, alias="expiresAt", description="")
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
