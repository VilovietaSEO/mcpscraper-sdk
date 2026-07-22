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

    handle: str = Field(..., alias="handle", description="")
    profile_url: str = Field(..., alias="profileUrl", description="")
    page_url: str = Field(..., alias="pageUrl", description="")
    browser: dict[str, Any] = Field(..., alias="browser", description="")
    profile_name: Any = Field(..., alias="profileName", description="")
    reported_post_count: Any = Field(..., alias="reportedPostCount", description="")
    reported_post_count_text: Any = Field(..., alias="reportedPostCountText", description="")
    follower_count_text: Any = Field(..., alias="followerCountText", description="")
    following_count_text: Any = Field(..., alias="followingCountText", description="")
    collected_content_count: int = Field(..., alias="collectedContentCount", description="")
    type_counts: dict[str, Any] = Field(..., alias="typeCounts", description="")
    pagination: dict[str, Any] = Field(..., alias="pagination", description="")
    limited: bool = Field(..., alias="limited", description="")
    limitations: list[str] = Field(..., alias="limitations", description="")
    items: list[dict[str, Any]] = Field(..., alias="items", description="")
