from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class FacebookReelsInventoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public Facebook profile or Page URL whose Reel URLs should be collected. Do not pass an individual Reel, video, post, share, group, or event URL.")
    max_urls: int | None = Field(None, alias="maxUrls", description="Maximum Reel URLs requested. Logged-out collection is capped at 60 even when this is higher; a valid saved Facebook browser profile can continue toward the requested maximum.")
    profile: str | None = Field(None, alias="profile", description="Optional saved hosted browser profile name containing a Facebook login. Set one up with browser_profile_connect first. An expired or logged-out profile falls back to the anonymous 60-URL cap.")
    save_profile_changes: bool | None = Field(None, alias="saveProfileChanges", description="Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved Facebook login.")
    resume_urls: list[str] | None = Field(None, alias="resumeUrls", description="Previously returned Reel URLs to retain and deduplicate while continuing an interrupted collection.")
    max_scrolls: int | None = Field(None, alias="maxScrolls", description="Safety ceiling for pagination attempts. Default 250; collection normally stops earlier at maxUrls or a Facebook access boundary.")
    scroll_delay_ms: int | None = Field(None, alias="scrollDelayMs", description="Delay after each scroll before collecting the next DOM batch.")
    stable_scroll_limit: int | None = Field(None, alias="stableScrollLimit", description="Stop after this many consecutive pagination attempts add no Reel URLs.")


class FacebookReelsInventoryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str = Field(..., alias="sourceUrl", description="")
    profile_url: str = Field(..., alias="profileUrl", description="")
    page_url: str = Field(..., alias="pageUrl", description="")
    profile_name: Any = Field(..., alias="profileName", description="")
    browser: dict[str, Any] = Field(..., alias="browser", description="")
    requested_max_urls: int = Field(..., alias="requestedMaxUrls", description="")
    effective_max_urls: int = Field(..., alias="effectiveMaxUrls", description="")
    anonymous_cap: float = Field(..., alias="anonymousCap", description="")
    anonymous_cap_applied: bool = Field(..., alias="anonymousCapApplied", description="")
    saved_profile_requested: bool = Field(..., alias="savedProfileRequested", description="")
    authentication_status: Literal['authenticated', 'logged_out', 'unknown'] = Field(..., alias="authenticationStatus", description="")
    collected_url_count: int = Field(..., alias="collectedUrlCount", description="")
    resumed_url_count: int = Field(..., alias="resumedUrlCount", description="")
    newly_collected_url_count: int = Field(..., alias="newlyCollectedUrlCount", description="")
    complete: bool = Field(..., alias="complete", description="")
    partial: bool = Field(..., alias="partial", description="")
    stopped_reason: Literal['max_urls', 'anonymous_cap', 'deadline', 'login_wall', 'stable_scrolls', 'max_scrolls', 'no_scrolls', 'navigation_error', 'browser_error'] = Field(..., alias="stoppedReason", description="")
    pagination: dict[str, Any] = Field(..., alias="pagination", description="")
    items: list[dict[str, Any]] = Field(..., alias="items", description="")
    limitations: list[str] = Field(..., alias="limitations", description="")
    recoverable_error: Any = Field(..., alias="recoverableError", description="")
    extracted_at: str = Field(..., alias="extractedAt", description="")
