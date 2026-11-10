from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class BugReportingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    action: Literal['prepare', 'submit', 'status'] | None = Field(None, alias="action", description="prepare saves a private one-day draft for review; submit sends that exact draft to support; status reads your report receipt.")
    report: dict[str, Any] | None = Field(None, alias="report", description="Required for prepare. Collect known evidence from the conversation before asking the user for missing details.")
    report_id: str | None = Field(None, alias="reportId", description="ID returned by prepare; required for submit or status.")
    review_token: str | None = Field(None, alias="reviewToken", description="Exact token returned by prepare; required for submit. A changed report requires a new prepare.")
    user_approved: bool | None = Field(None, alias="userApproved", description="Set true only when the user has asked to submit this bug or approved the reviewed draft. Repeated errors alone do not authorize submission.")


class BugReportingOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    account_email: str | None = Field(None, alias="accountEmail", description="")
    report_id: str | None = Field(None, alias="reportId", description="")
    status: Literal['draft', 'submitted'] | None = Field(None, alias="status", description="")
    received_at: str | None = Field(None, alias="receivedAt", description="")
    submitted_at: Any | None = Field(None, alias="submittedAt", description="")
    expires_at: str | None = Field(None, alias="expiresAt", description="")
    report: dict[str, Any] | None = Field(None, alias="report", description="")
    review_token: str | None = Field(None, alias="reviewToken", description="")
    redacted: bool | None = Field(None, alias="redacted", description="")
    message: str | None = Field(None, alias="message", description="")
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
