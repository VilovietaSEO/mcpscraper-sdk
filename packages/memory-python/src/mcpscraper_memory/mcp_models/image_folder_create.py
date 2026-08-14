from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageFolderCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    project_id: str = Field(..., alias="projectId", description="Opaque image project identifier returned by an image project tool.")
    parent_id: str | None = Field(None, alias="parentId", description="Parent image folder identifier; omit to create the folder at the project root.")
    name: str = Field(..., alias="name", description="Human-readable name for the record being created or updated.")


class ImageFolderCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: Literal[True, False] = Field(..., alias="ok", description="")
    folder: dict[str, Any] | None = Field(None, alias="folder", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
