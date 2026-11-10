from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class MemoryCaptureInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    folder: str | None = Field(None, alias="folder", description="Optional governed folder override inside the selected vault.")
    path: str = Field(..., alias="path", description="Exact path value used by this tool; preserve its leading slash or vault-relative form as required.")
    title: str = Field(..., alias="title", description="Human-readable title for the proposed record or authored content.")
    content: str = Field(..., alias="content", description="Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.")
    props: dict[str, Any] = Field(..., alias="props", description="Complete governed note properties required by the target vault contract.")
    base_revision: float | None = Field(None, alias="baseRevision", description="Last revision read by the caller; supply it to reject an update if the record changed meanwhile.")
    tag_decisions: list[dict[str, Any]] | None = Field(None, alias="tagDecisions", description="Required justification for any tag that does not already exist. Tags resolve against the account's existing vocabulary; new tags require a one-line description.")


class MemoryCaptureOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    valid: bool | None = Field(None, alias="valid", description="")
    errors: list[str] | None = Field(None, alias="errors", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    tag_resolutions: list[dict[str, Any]] | None = Field(None, alias="tagResolutions", description="")
    note: dict[str, Any] | None = Field(None, alias="note", description="")
    indexed: float | None = Field(None, alias="indexed", description="")
    verified: dict[str, Any] | None = Field(None, alias="verified", description="")
    conflict: bool | None = Field(None, alias="conflict", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
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
