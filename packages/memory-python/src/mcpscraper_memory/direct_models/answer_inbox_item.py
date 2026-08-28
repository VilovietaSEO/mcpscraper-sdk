from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnswerInboxItemInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    question_id: str = Field(..., alias="questionId", description="The [Q-YYYY-MM-DD-NN] id shown on the inbox item.")
    answer: str = Field(..., alias="answer", description="Your decision in your own words. Stored verbatim as the policy reasoning.")
    action: Literal['answer', 'archive', 'delete', 'promote'] | None = Field(None, alias="action", description="answer keeps the note and records your decision; archive moves the evidence to a 30-day expiry; delete drops the item with no evidence retained; promote copies the subject note into the Skills vault as an active skill.")
    scope: Literal['instance', 'vault', 'account'] | None = Field(None, alias="scope", description="instance applies to this item only. vault or account records a policy that governs future scheduled runs.")
    rule_key: str | None = Field(None, alias="ruleKey", description="Machine-readable rule name when scope is vault or account, e.g. dwell.Tasks.to_do.")
    rule_value: Any | None = Field(None, alias="ruleValue", description="Value for ruleKey.")
    vault: str | None = Field(None, alias="vault", description="Logical vault name when scope is vault.")


class AnswerInboxItemOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    question_id: str | None = Field(None, alias="questionId", description="")
    action: str | None = Field(None, alias="action", description="")
    remaining_open: float | None = Field(None, alias="remainingOpen", description="")
    policy_path: str | None = Field(None, alias="policyPath", description="")
    applies_from: str | None = Field(None, alias="appliesFrom", description="")
    error: str | None = Field(None, alias="error", description="")
