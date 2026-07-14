from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class DescribeServiceConnectionToolInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned connectionId from list_service_connections.")
    tool: str = Field(..., alias="tool", description="One exact name from that connection's readTools or actionTools. Admin-blocked and arbitrary names are rejected.")
    fresh: bool | None = Field(None, alias="fresh", description="Bypass the short-lived sanitized schema cache. Ownership, connection state, and tool policy are still rechecked; use only when a provider tool catalog just changed.")


class DescribeServiceConnectionToolOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tool: dict[str, Any] | None = Field(None, alias="tool", description="")
    retryable: bool | None = Field(None, alias="retryable", description="")
    error_code: str | None = Field(None, alias="errorCode", description="")
    error: Any = Field(..., alias="error", description="")
