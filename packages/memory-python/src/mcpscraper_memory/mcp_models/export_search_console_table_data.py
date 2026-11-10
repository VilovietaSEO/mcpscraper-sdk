from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ExportSearchConsoleTableDataInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    table_name: str = Field(..., alias="tableName", description="Existing tenant-owned Search Console tableName returned by list_service_connections; confirm its columns with table-describe.")
    filters: list[dict[str, Any]] | None = Field(None, alias="filters", description="Optional filters to AND together before download. Use table-describe or the documented typed columns.")
    sort: dict[str, Any] | None = Field(None, alias="sort", description="Optional row ordering for the JSONL download.")
    max_rows: int | None = Field(None, alias="maxRows", description="Maximum matching persisted rows to place in this artifact. Use filters to bound large tables.")


class ExportSearchConsoleTableDataOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    table_name: str | None = Field(None, alias="tableName", description="")
    rows_exported: int | None = Field(None, alias="rowsExported", description="")
    matched_rows: int | None = Field(None, alias="matchedRows", description="")
    complete: bool | None = Field(None, alias="complete", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
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
