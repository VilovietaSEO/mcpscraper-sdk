from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmQualityListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    queue: Literal['classification', 'naming', 'duplicates', 'imports', 'merges', 'work'] | None = Field(None, alias="queue", description="")
    limit: int | None = Field(None, alias="limit", description="")


class CrmQualityListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    issues: list[dict[str, Any]] | None = Field(None, alias="issues", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
