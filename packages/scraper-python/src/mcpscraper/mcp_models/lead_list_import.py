from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class LeadListImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required stable key for this intended import. Reuse it only to retry the same import with identical source and options.")
    source: Any = Field(..., alias="source", description="Exactly one bounded source: rows, CSV/TSV text, or a completed private upload.")


class LeadListImportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status: Literal['ready', 'sheet_selection_required'] | None = Field(None, alias="status", description="")
    lead_list_id: Any | None = Field(None, alias="leadListId", description="")
    source_format: Literal['rows', 'csv', 'tsv', 'xlsx'] | None = Field(None, alias="sourceFormat", description="")
    sheets: list[dict[str, Any]] | None = Field(None, alias="sheets", description="")
    selected_sheet: Any | None = Field(None, alias="selectedSheet", description="")
    headers: list[str] | None = Field(None, alias="headers", description="")
    row_count: int | None = Field(None, alias="rowCount", description="")
    column_count: int | None = Field(None, alias="columnCount", description="")
    sample_rows: list[dict[str, Any]] | None = Field(None, alias="sampleRows", description="")
    suggested_column_map: dict[str, Any] | None = Field(None, alias="suggestedColumnMap", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    scan_state: Any | None = Field(None, alias="scanState", description="")
    expires_at: Any | None = Field(None, alias="expiresAt", description="")
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
