from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExportSearchConsoleTableDataInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    table_name: str = Field(..., alias="tableName", description="Typed Search Console tableName returned by list_service_connections after a successful connection_sync run.")
    filters: list[dict[str, Any]] | None = Field(None, alias="filters", description="Optional filters to AND together before download. Use table-describe or the documented typed columns.")
    sort: dict[str, Any] | None = Field(None, alias="sort", description="Optional row ordering for the JSONL download.")
    max_rows: int | None = Field(None, alias="maxRows", description="Maximum matching persisted rows to place in this artifact. Use filters to bound large tables.")


class ExportSearchConsoleTableDataOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    table_name: str | None = Field(None, alias="tableName", description="")
    rows_exported: int | None = Field(None, alias="rowsExported", description="")
    matched_rows: int | None = Field(None, alias="matchedRows", description="")
    complete: bool | None = Field(None, alias="complete", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    error: Any = Field(..., alias="error", description="")
