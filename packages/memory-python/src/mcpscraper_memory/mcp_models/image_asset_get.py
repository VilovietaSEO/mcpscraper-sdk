from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="")
    asset_id: str = Field(..., alias="assetId", description="")
    include_preview: bool | None = Field(None, alias="includePreview", description="")


class ImageAssetGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: Literal[True, False] = Field(..., alias="ok", description="")
    asset: dict[str, Any] | None = Field(None, alias="asset", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
