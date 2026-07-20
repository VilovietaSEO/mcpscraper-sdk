from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class InstagramProfileContentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    handle: str | None = Field(None, alias="handle", description="Instagram handle, with or without @. Provide handle or url.")
    url: str | None = Field(None, alias="url", description="Instagram profile URL. Provide handle or url.")
    profile: str | None = Field(None, alias="profile", description="Optional saved hosted browser profile name for authenticated Instagram access.")
    save_profile_changes: bool | None = Field(None, alias="saveProfileChanges", description="Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved login.")
    max_items: int | None = Field(None, alias="maxItems", description="Maximum grid URLs to collect. Default 50, maximum 2000.")
    max_scrolls: int | None = Field(None, alias="maxScrolls", description="Maximum pagination scroll attempts. Default 10, maximum 250.")
    scroll_delay_ms: int | None = Field(None, alias="scrollDelayMs", description="Delay after each scroll before collecting new links. Default 1200ms.")
    stable_scroll_limit: int | None = Field(None, alias="stableScrollLimit", description="Stop after this many consecutive scrolls with no new links.")


class InstagramProfileContentOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
