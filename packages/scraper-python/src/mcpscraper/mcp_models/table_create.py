from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class TableCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    table_name: str = Field(..., alias="tableName", description="Table name: lowercase letters, numbers, underscores, starting with a letter (e.g. rank_tracker).")
    columns: list[dict[str, Any]] = Field(..., alias="columns", description="Columns to create, in addition to the automatic id/created_at/updated_at.")


class TableCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True on success; false on auth/scope/validation error.")
    table_name: str | None = Field(None, alias="tableName", description="The table name.")
    created: bool | None = Field(None, alias="created", description="True if the table was newly created; false if it already existed.")
    columns: list[dict[str, Any]] | None = Field(None, alias="columns", description="The columns requested (existing tables are not altered to match).")
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
