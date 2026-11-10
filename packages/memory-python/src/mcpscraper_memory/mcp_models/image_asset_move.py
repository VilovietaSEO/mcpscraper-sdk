from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ImageAssetMoveInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    asset_id: str = Field(..., alias="assetId", description="Opaque image asset identifier returned by an image asset tool.")
    project_id: Any | None = Field(None, alias="projectId", description="Opaque image project identifier returned by an image project tool.")
    folder_id: Any | None = Field(None, alias="folderId", description="Opaque image folder identifier; omit only when the project root is intended.")


class ImageAssetMoveOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    asset: dict[str, Any] | None = Field(None, alias="asset", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
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
