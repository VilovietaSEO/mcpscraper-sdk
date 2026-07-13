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
