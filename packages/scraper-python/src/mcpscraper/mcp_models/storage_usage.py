from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class StorageUsageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class StorageUsageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when usage was computed; false on an auth/scope error.")
    total_bytes: float | None = Field(None, alias="totalBytes", description="Total stored bytes across all the caller vaults. Present when ok is true.")
    total_gb: float | None = Field(None, alias="totalGb", description="Total stored size in decimal GB (bytes / 1e9), rounded to 2 decimals. Present when ok is true.")
    quota_bytes: Any | None = Field(None, alias="quotaBytes", description="Storage quota in bytes for the caller plan. Null when the plan is unlimited. Present when ok is true.")
    quota_gb: Any | None = Field(None, alias="quotaGb", description="Storage quota in decimal GB, rounded to 2 decimals. Null when the plan is unlimited. Present when ok is true.")
    unlimited: bool | None = Field(None, alias="unlimited", description="True when the caller plan is unlimited (no storage ceiling). Render \"Unlimited\" instead of a quota figure.")
    per_vault: list[dict[str, Any]] | None = Field(None, alias="perVault", description="Per-vault storage breakdown for the caller vaults. Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
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
