from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserOpenInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    label: str | None = Field(None, alias="label", description="Optional human label for this session, shown in the watch console.")
    url: str | None = Field(None, alias="url", description="Optional URL to navigate to immediately after opening.")
    profile: str | None = Field(None, alias="profile", description="Optional saved hosted profile name to load a logged-in session for a site.")
    save_profile_changes: bool | None = Field(None, alias="save_profile_changes", description="Persist cookies/storage back to the named profile on close. Avoid parallel sessions writing to the same profile.")
    timeout_seconds: int | None = Field(None, alias="timeout_seconds", description="Session lifetime before auto-termination. Defaults to 600.")
    extension_names: list[str] | None = Field(None, alias="extension_names", description="Names of extensions previously added with browser_extension_import (see browser_extension_list for what's available) to load into this session. Loading extensions restarts the browser, adding a few seconds to startup.")


class BrowserOpenOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tool: str = Field(..., alias="tool", description="")
    session_id: str = Field(..., alias="session_id", description="Session id returned by browser_open. Use only this exact value in later browser_* calls; do not construct one yourself.")
    watch_url: str = Field(..., alias="watch_url", description="Human watch/takeover URL for this browser session on mcpscraper.dev.")
    live_view_url: Any = Field(..., alias="live_view_url", description="Deprecated; always null. Open watch_url to view the live session.")
    url: Any = Field(..., alias="url", description="Initial URL requested by the caller, when provided.")
    hint: str = Field(..., alias="hint", description="")
    raw: dict[str, Any] | None = Field(None, alias="raw", description="")
