from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailBulkDeleteMessagesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirmed: bool | None = Field(None, alias="confirmed", description="Set true only after the person explicitly approves permanent deletion of this exact frozen message count; otherwise a capable client may request confirmation.")
    confirm_permanent_delete: bool = Field(..., alias="confirmPermanentDelete", description="Required literal boolean proving the caller selected irreversible deletion rather than reversible trash.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry key bound to this exact deletion receipt; a conflicting reuse fails before mutation.")
    connection_id: str = Field(..., alias="connectionId", description="The tenant-owned Gmail connectionId bound into this immutable selection.")
    selection_id: str = Field(..., alias="selectionId", description="Selection prepared with purpose mailbox_action.")
    selection_sha256: str = Field(..., alias="selectionSha256", description="Unchanged selection digest from gmail_prepare_selection.")
    expected_count: int = Field(..., alias="expectedCount", description="Exact reviewed selection count; the call fails if it no longer matches the receipt.")


class GmailBulkDeleteMessagesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    action_id: str = Field(..., alias="actionId", description="")
    selection_id: str = Field(..., alias="selectionId", description="")
    expected_count: int = Field(..., alias="expectedCount", description="")
    changed_count: int = Field(..., alias="changedCount", description="")
    failed_count: int = Field(..., alias="failedCount", description="")
    status: Literal['running', 'complete', 'partial', 'failed'] = Field(..., alias="status", description="")
    replay: bool | None = Field(None, alias="replay", description="")
    failed_chunks: list[dict[str, Any]] | None = Field(None, alias="failedChunks", description="")
    irreversible: bool = Field(..., alias="irreversible", description="")
    provider_guarantee: str = Field(..., alias="providerGuarantee", description="")
    error: Any = Field(..., alias="error", description="")
