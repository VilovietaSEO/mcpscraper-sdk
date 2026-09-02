from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageFolderCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    vault: str | None = Field(None, alias="vault", description="")
    project_id: str = Field(..., alias="projectId", description="")
    parent_id: str | None = Field(None, alias="parentId", description="")
    name: str = Field(..., alias="name", description="")


class ImageFolderCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    folder: dict[str, Any] | None = Field(None, alias="folder", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
