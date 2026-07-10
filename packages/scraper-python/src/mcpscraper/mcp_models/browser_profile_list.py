from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserProfileListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    profile: str | None = Field(None, alias="profile", description="Profile whose saved logins to list. Omit to derive from email.")
    email: str | None = Field(None, alias="email", description="Account email used to derive the profile name when profile is not given.")
    domain: str | None = Field(None, alias="domain", description="Restrict to one site login, e.g. chatgpt.com. Use this to poll a single login until its status reads AUTHENTICATED.")
    connection_id: str | None = Field(None, alias="connection_id", description="A specific login connection id returned by browser_profile_connect, to poll just that one.")


class BrowserProfileListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
