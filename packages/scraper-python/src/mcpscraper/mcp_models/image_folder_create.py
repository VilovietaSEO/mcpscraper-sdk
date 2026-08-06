from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageFolderCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="")
    project_id: str = Field(..., alias="projectId", description="")
    parent_id: str | None = Field(None, alias="parentId", description="")
    name: str = Field(..., alias="name", description="")


class ImageFolderCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: Literal[True, False] = Field(..., alias="ok", description="")
    folder: dict[str, Any] | None = Field(None, alias="folder", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
