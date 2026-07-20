from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImportServiceConnectionToMemoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned connectionId from list_service_connections.")
    provider_config_key: str = Field(..., alias="providerConfigKey", description="The exact providerConfigKey returned with that connection. It is matched together with connectionId against the authenticated caller.")
    tool: str = Field(..., alias="tool", description="One exact current readTools entry for that connection. Actions, admin tools, and unlisted names are rejected.")
    args: dict[str, Any] | None = Field(None, alias="args", description="JSON arguments for one bounded provider read. The serialized object may be at most 64 KiB.")
    vault: str = Field(..., alias="vault", description="An existing ordinary Memory vault the caller can write and index. Secure and channel vaults are rejected because this tool creates searchable RAG content.")
    title: str | None = Field(None, alias="title", description="Optional human-readable snapshot title. The server always chooses the stable storage path.")


class ImportServiceConnectionToMemoryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
