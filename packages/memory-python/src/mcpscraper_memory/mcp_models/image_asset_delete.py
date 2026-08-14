from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetDeleteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    asset_id: str = Field(..., alias="assetId", description="Opaque image asset identifier returned by an image asset tool.")
    confirm_delete: bool = Field(..., alias="confirmDelete", description="Must be true after the caller has confirmed deletion.")


class ImageAssetDeleteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: Literal[True, False] = Field(..., alias="ok", description="")
    deleted: bool | None = Field(None, alias="deleted", description="")
    asset_id: str | None = Field(None, alias="assetId", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
