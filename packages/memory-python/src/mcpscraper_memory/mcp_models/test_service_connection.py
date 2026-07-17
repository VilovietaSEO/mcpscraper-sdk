from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TestServiceConnectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned connectionId from list_service_connections.")
    provider_config_key: str | None = Field(None, alias="providerConfigKey", description="Optional provider hint from list_service_connections.")


class TestServiceConnectionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    operational_status: Literal["available", "unavailable"] | None = Field(None, alias="operationalStatus", description="")
    checked_at: str | None = Field(None, alias="checkedAt", description="")
    tool_count: int | None = Field(None, alias="toolCount", description="")
    code: str | None = Field(None, alias="code", description="")
    error: Any = Field(..., alias="error", description="")
