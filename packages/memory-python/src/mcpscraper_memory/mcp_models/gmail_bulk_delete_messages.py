from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


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

    ok: bool | None = Field(None, alias="ok", description="")
    action_id: str | None = Field(None, alias="actionId", description="")
    selection_id: str | None = Field(None, alias="selectionId", description="")
    expected_count: int | None = Field(None, alias="expectedCount", description="")
    changed_count: int | None = Field(None, alias="changedCount", description="")
    failed_count: int | None = Field(None, alias="failedCount", description="")
    status: Literal['running', 'complete', 'partial', 'failed'] | None = Field(None, alias="status", description="")
    replay: bool | None = Field(None, alias="replay", description="")
    failed_chunks: list[dict[str, Any]] | None = Field(None, alias="failedChunks", description="")
    irreversible: bool | None = Field(None, alias="irreversible", description="")
    provider_guarantee: str | None = Field(None, alias="providerGuarantee", description="")
    error: Any | None = Field(None, alias="error", description="")
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
