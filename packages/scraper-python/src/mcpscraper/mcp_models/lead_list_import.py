from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class LeadListImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required stable key for this intended import. Reuse it only to retry the same import with identical source and options.")
    source: Any = Field(..., alias="source", description="Exactly one bounded source: rows, CSV/TSV text, or a completed private upload.")


class LeadListImportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status: Literal['ready', 'sheet_selection_required'] = Field(..., alias="status", description="")
    lead_list_id: Any = Field(..., alias="leadListId", description="")
    source_format: Literal['rows', 'csv', 'tsv', 'xlsx'] = Field(..., alias="sourceFormat", description="")
    sheets: list[dict[str, Any]] = Field(..., alias="sheets", description="")
    selected_sheet: Any = Field(..., alias="selectedSheet", description="")
    headers: list[str] = Field(..., alias="headers", description="")
    row_count: int = Field(..., alias="rowCount", description="")
    column_count: int = Field(..., alias="columnCount", description="")
    sample_rows: list[dict[str, Any]] = Field(..., alias="sampleRows", description="")
    suggested_column_map: dict[str, Any] = Field(..., alias="suggestedColumnMap", description="")
    warnings: list[str] = Field(..., alias="warnings", description="")
    scan_state: Any | None = Field(None, alias="scanState", description="")
    expires_at: Any = Field(..., alias="expiresAt", description="")
