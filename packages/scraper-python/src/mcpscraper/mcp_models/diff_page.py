from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class DiffPageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public http/https URL to check for changes since the last diff_page call.")
    allow_local: bool | None = Field(None, alias="allowLocal", description="Allow localhost and private-network URLs. Local development only.")
    reset_baseline: bool | None = Field(None, alias="resetBaseline", description="Discard any previously stored snapshot for this URL and capture the current content as a fresh baseline instead of diffing against history. Use when you deliberately want to restart change tracking.")


class DiffPageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="")
    title: Any = Field(..., alias="title", description="")
    status: Literal["baseline", "unchanged", "changed"] = Field(..., alias="status", description="\"baseline\" = first-ever check for this URL, or resetBaseline was used — nothing to compare against. \"unchanged\" = content hash matched the stored snapshot. \"changed\" = a diff was computed.")
    is_reset: bool = Field(..., alias="isReset", description="True only when resetBaseline discarded a real prior snapshot — distinguishes an explicit reset from a URL's true first-ever check.")
    previous_checked_at: Any = Field(..., alias="previousCheckedAt", description="ISO timestamp of the snapshot this was compared against, or null if there was none.")
    current_checked_at: str = Field(..., alias="currentCheckedAt", description="ISO timestamp of this check, now stored as the new snapshot.")
    content_hash: str = Field(..., alias="contentHash", description="sha256 of the full (untruncated) page content just captured.")
    previous_content_hash: Any = Field(..., alias="previousContentHash", description="")
    summary: dict[str, Any] = Field(..., alias="summary", description="")
    hunks: list[dict[str, Any]] = Field(..., alias="hunks", description="Ordered added/removed line hunks, capped for response size — see hunksTruncated.")
    content_truncated: bool = Field(..., alias="contentTruncated", description="True if the scraped page exceeded the 250,000-character storable cap and was truncated before hashing/diffing/storing — changes past that point are invisible to this comparison.")
    hunks_truncated: bool = Field(..., alias="hunksTruncated", description="True if the hunks list above was capped for response size — see hunksTruncatedReason.")
    hunks_truncated_reason: Any = Field(..., alias="hunksTruncatedReason", description="")
    total_changed_line_count: int = Field(..., alias="totalChangedLineCount", description="Total changed lines found before any hunksTruncated capping was applied.")
