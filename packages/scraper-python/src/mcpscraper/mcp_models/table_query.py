from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class TableQueryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    table_name: str = Field(..., alias="tableName", description="Table name, from table-list.")
    filters: list[dict[str, Any]] | None = Field(None, alias="filters", description="Filters to AND together. Optional; omit to match every row.")
    sort: dict[str, Any] | None = Field(None, alias="sort", description="Column to sort by. Optional; defaults to id ascending (insertion order).")
    limit: int | None = Field(None, alias="limit", description="Max rows to return. Optional; default 100, max 2000.")
    offset: int | None = Field(None, alias="offset", description="Rows to skip, for pagination. Optional; default 0.")


class TableQueryOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True on success; false on auth/validation error.")
    table_name: str | None = Field(None, alias="tableName", description="The table name.")
    rows: list[dict[str, Any]] | None = Field(None, alias="rows", description="Matching rows, each an object of column name to value.")
    count: float | None = Field(None, alias="count", description="Total rows matching the filters, before limit/offset — use for pagination.")
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
