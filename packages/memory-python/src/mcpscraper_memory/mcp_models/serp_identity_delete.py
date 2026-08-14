from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SerpIdentityDeleteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(..., alias="name", description="Identity name returned by serp_identity_list.")
    confirm: bool = Field(..., alias="confirm", description="Must be true because deletion permanently removes the saved browser state and its fixed proxy.")


class SerpIdentityDeleteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="")
    name: str = Field(..., alias="name", description="")
    deleted: bool = Field(..., alias="deleted", description="")
