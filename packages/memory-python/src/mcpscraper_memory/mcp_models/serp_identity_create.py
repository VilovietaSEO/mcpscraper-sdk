from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SerpIdentityCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(..., alias="name", description="Stable caller-facing name, e.g. google-us-primary.")
    country: str | None = Field(None, alias="country", description="Two-letter country for the static network identity. Defaults to US.")


class SerpIdentityCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tool: str = Field(..., alias="tool", description="")
    session_id: str = Field(..., alias="session_id", description="Live Google takeover session opened on the new persistent identity.")
    watch_url: str = Field(..., alias="watch_url", description="Give this URL to the user so they can clear consent or CAPTCHA directly on google.com.")
    url: str = Field(..., alias="url", description="")
    identity: dict[str, Any] = Field(..., alias="identity", description="")
    next_steps: list[str] = Field(..., alias="next_steps", description="")
