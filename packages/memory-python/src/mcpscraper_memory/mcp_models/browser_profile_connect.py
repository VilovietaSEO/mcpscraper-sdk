from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class BrowserProfileConnectInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    email: str | None = Field(None, alias="email", description="Account email for the login. Derives a stable profile name and is recorded as a note. Does NOT import existing cookies — the user signs in fresh.")
    profile: str | None = Field(None, alias="profile", description="Profile to add this login to. Omit to derive from email. A single profile holds MANY logins — pass the same name with a different domain to stack accounts.")
    domain: str | None = Field(None, alias="domain", description="Site to log into, e.g. chatgpt.com, claude.ai, reddit.com. Defaults to chatgpt.com.")
    login_url: str | None = Field(None, alias="login_url", description="Login page for the domain. Defaults to https://<domain>/.")
    url: str | None = Field(None, alias="url", description="Deprecated alias for login_url.")
    note: str | None = Field(None, alias="note", description="Free-text note describing this login. Surfaced by browser_profile_list.")
    label: str | None = Field(None, alias="label", description="Optional human label for this sign-in setup session.")
    timeout_seconds: int | None = Field(None, alias="timeout_seconds", description="Sign-in session lifetime before auto-termination. Defaults to 600 and cannot exceed 600.")


class BrowserProfileConnectOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    tool: str | None = Field(None, alias="tool", description="")
    session_id: Any | None = Field(None, alias="session_id", description="The underlying live browser session id backing this sign-in.")
    auth_connection_id: str | None = Field(None, alias="auth_connection_id", description="")
    watch_url: str | None = Field(None, alias="watch_url", description="mcpscraper.dev sign-in link to give the user so they can complete this login.")
    live_view_url: Any | None = Field(None, alias="live_view_url", description="Deprecated; always null. Open watch_url to view the sign-in.")
    profile: str | None = Field(None, alias="profile", description="Profile this login was added to. Reuse it to stack more logins or to open a session.")
    domain: str | None = Field(None, alias="domain", description="")
    setup_url: str | None = Field(None, alias="setup_url", description="")
    account_email: Any | None = Field(None, alias="account_email", description="")
    note: Any | None = Field(None, alias="note", description="")
    status: str | None = Field(None, alias="status", description="")
    flow_status: Any | None = Field(None, alias="flow_status", description="Deprecated; always null.")
    flow_step: Any | None = Field(None, alias="flow_step", description="Deprecated; always null.")
    flow_expires_at: Any | None = Field(None, alias="flow_expires_at", description="Deprecated; always null.")
    post_login_url: Any | None = Field(None, alias="post_login_url", description="Deprecated; always null.")
    connected_logins: list[dict[str, Any]] | None = Field(None, alias="connected_logins", description="Every login currently saved in this profile, so you can see what else is connected.")
    next_steps: list[str] | None = Field(None, alias="next_steps", description="")
    raw: dict[str, Any] | None = Field(None, alias="raw", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
