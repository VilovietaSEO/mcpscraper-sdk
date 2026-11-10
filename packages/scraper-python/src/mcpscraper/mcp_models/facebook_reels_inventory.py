from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


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

    source_url: str | None = Field(None, alias="sourceUrl", description="")
    profile_url: str | None = Field(None, alias="profileUrl", description="")
    page_url: str | None = Field(None, alias="pageUrl", description="")
    profile_name: Any | None = Field(None, alias="profileName", description="")
    browser: dict[str, Any] | None = Field(None, alias="browser", description="")
    requested_max_urls: int | None = Field(None, alias="requestedMaxUrls", description="")
    effective_max_urls: int | None = Field(None, alias="effectiveMaxUrls", description="")
    anonymous_cap: float | None = Field(None, alias="anonymousCap", description="")
    anonymous_cap_applied: bool | None = Field(None, alias="anonymousCapApplied", description="")
    saved_profile_requested: bool | None = Field(None, alias="savedProfileRequested", description="")
    authentication_status: Literal['authenticated', 'logged_out', 'unknown'] | None = Field(None, alias="authenticationStatus", description="")
    collected_url_count: int | None = Field(None, alias="collectedUrlCount", description="")
    resumed_url_count: int | None = Field(None, alias="resumedUrlCount", description="")
    newly_collected_url_count: int | None = Field(None, alias="newlyCollectedUrlCount", description="")
    complete: bool | None = Field(None, alias="complete", description="")
    partial: bool | None = Field(None, alias="partial", description="")
    stopped_reason: Literal['max_urls', 'anonymous_cap', 'deadline', 'login_wall', 'stable_scrolls', 'max_scrolls', 'no_scrolls', 'navigation_error', 'browser_error'] | None = Field(None, alias="stoppedReason", description="")
    pagination: dict[str, Any] | None = Field(None, alias="pagination", description="")
    items: list[dict[str, Any]] | None = Field(None, alias="items", description="")
    limitations: list[str] | None = Field(None, alias="limitations", description="")
    recoverable_error: Any | None = Field(None, alias="recoverableError", description="")
    extracted_at: str | None = Field(None, alias="extractedAt", description="")
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
