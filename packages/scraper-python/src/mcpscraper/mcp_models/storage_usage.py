from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class StorageUsageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class StorageUsageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when usage was computed; false on an auth/scope error.")
    total_bytes: float | None = Field(None, alias="totalBytes", description="Total stored bytes across all the caller vaults. Present when ok is true.")
    total_gb: float | None = Field(None, alias="totalGb", description="Total stored size in decimal GB (bytes / 1e9), rounded to 2 decimals. Present when ok is true.")
    quota_bytes: Any | None = Field(None, alias="quotaBytes", description="Storage quota in bytes for the caller plan. Null when the plan is unlimited. Present when ok is true.")
    quota_gb: Any | None = Field(None, alias="quotaGb", description="Storage quota in decimal GB, rounded to 2 decimals. Null when the plan is unlimited. Present when ok is true.")
    unlimited: bool | None = Field(None, alias="unlimited", description="True when the caller plan is unlimited (no storage ceiling). Render \"Unlimited\" instead of a quota figure.")
    per_vault: list[dict[str, Any]] | None = Field(None, alias="perVault", description="Per-vault storage breakdown for the caller vaults. Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
