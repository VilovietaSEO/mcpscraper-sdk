from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetMoveInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    asset_id: str = Field(..., alias="assetId", description="Opaque image asset identifier returned by an image asset tool.")
    project_id: Any | None = Field(None, alias="projectId", description="Opaque image project identifier returned by an image project tool.")
    folder_id: Any | None = Field(None, alias="folderId", description="Opaque image folder identifier; omit only when the project root is intended.")


class ImageAssetMoveOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: Literal[True, False] = Field(..., alias="ok", description="")
    asset: dict[str, Any] | None = Field(None, alias="asset", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
