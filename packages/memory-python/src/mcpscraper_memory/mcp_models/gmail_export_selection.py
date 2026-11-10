from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GmailExportSelectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="The tenant-owned Gmail connectionId bound into this immutable selection.")
    selection_id: str = Field(..., alias="selectionId", description="Immutable owner-bound selectionId returned by gmail_prepare_selection with purpose export.")
    selection_sha256: str = Field(..., alias="selectionSha256", description="Unchanged selection digest returned by gmail_prepare_selection.")
    expected_count: int = Field(..., alias="expectedCount", description="Exact frozen message count; export fails if the receipt does not match.")


class GmailExportSelectionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    selection_id: str | None = Field(None, alias="selectionId", description="")
    count: int | None = Field(None, alias="count", description="")
    complete: bool | None = Field(None, alias="complete", description="")
    preview: Any | None = Field(None, alias="preview", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    untrusted_content: bool | None = Field(None, alias="untrustedContent", description="")
    error: Any | None = Field(None, alias="error", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
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
