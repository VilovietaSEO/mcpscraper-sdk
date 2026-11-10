from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class MemoryQuestionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault to capture into. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    answers: list[dict[str, Any]] | None = Field(None, alias="answers", description="Up to 5 question/answer pairs to ingest. Omit (or empty) to instead RECEIVE the day questions.")


class MemoryQuestionsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when questions were returned or answers were ingested; false on auth/scope error.")
    questions: list[str] | None = Field(None, alias="questions", description="The day capture questions. Present only when called with no answers.")
    ingested: float | None = Field(None, alias="ingested", description="Number of answers stored as captures. Present only when answers were supplied.")
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
