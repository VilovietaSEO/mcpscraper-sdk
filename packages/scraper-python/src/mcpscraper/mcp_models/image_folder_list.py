from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageFolderListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="")
    project_id: str = Field(..., alias="projectId", description="")


class ImageFolderListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: Literal[True, False] = Field(..., alias="ok", description="")
    folders: list[dict[str, Any]] | None = Field(None, alias="folders", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
