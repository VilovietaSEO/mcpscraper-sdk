from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmFormPreviewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    name: str = Field(..., alias="name", description="Label identifying the form connection and its submission history.")
    mapping: dict[str, Any] = Field(..., alias="mapping", description="Map CRM destination fields to existing input names or provider payload paths.")
    allowed_origins: list[str] = Field(..., alias="allowedOrigins", description="Exact HTTPS website origins permitted to submit from a browser, without paths or trailing slashes.")
    relationship_type: Literal['prospect', 'customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other'] | None = Field(None, alias="relationshipType", description="Relationship type for newly created contacts; existing contacts retain their managed fields.")
    sample: dict[str, Any] = Field(..., alias="sample", description="One synthetic submission using the actual field names or provider JSON structure.")


class CrmFormPreviewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
    result: dict[str, Any] | None = Field(None, alias="result", description="")
