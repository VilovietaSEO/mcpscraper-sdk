from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserProfileConnectInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    email: str | None = Field(None, alias="email", description="Account email for the login. Derives a stable profile name and is recorded as a note. Does NOT import existing cookies — the user signs in fresh.")
    profile: str | None = Field(None, alias="profile", description="Profile to add this login to. Omit to derive from email. A single profile holds MANY logins — pass the same name with a different domain to stack accounts.")
    domain: str | None = Field(None, alias="domain", description="Site to log into, e.g. chatgpt.com, claude.ai, reddit.com. Defaults to chatgpt.com.")
    login_url: str | None = Field(None, alias="login_url", description="Login page for the domain. Defaults to https://<domain>/.")
    url: str | None = Field(None, alias="url", description="Deprecated alias for login_url.")
    note: str | None = Field(None, alias="note", description="Free-text note describing this login. Surfaced by browser_profile_list.")
    label: str | None = Field(None, alias="label", description="Optional human label for this sign-in setup session.")
    timeout_seconds: int | None = Field(None, alias="timeout_seconds", description="Sign-in session lifetime before auto-termination. Defaults to 600.")


class BrowserProfileConnectOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
