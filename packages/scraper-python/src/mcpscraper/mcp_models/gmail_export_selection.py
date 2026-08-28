from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailExportSelectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="The tenant-owned Gmail connectionId bound into this immutable selection.")
    selection_id: str = Field(..., alias="selectionId", description="Immutable owner-bound selectionId returned by gmail_prepare_selection with purpose export.")
    selection_sha256: str = Field(..., alias="selectionSha256", description="Unchanged selection digest returned by gmail_prepare_selection.")
    expected_count: int = Field(..., alias="expectedCount", description="Exact frozen message count; export fails if the receipt does not match.")


class GmailExportSelectionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    selection_id: str | None = Field(None, alias="selectionId", description="")
    count: int | None = Field(None, alias="count", description="")
    complete: bool | None = Field(None, alias="complete", description="")
    preview: list[dict[str, Any]] | None = Field(None, alias="preview", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: Any = Field(..., alias="error", description="")
