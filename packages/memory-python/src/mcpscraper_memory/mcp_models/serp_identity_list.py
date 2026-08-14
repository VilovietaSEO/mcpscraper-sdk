from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SerpIdentityListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class SerpIdentityListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="")
    identities: list[dict[str, Any]] = Field(..., alias="identities", description="")
    count: int = Field(..., alias="count", description="")
