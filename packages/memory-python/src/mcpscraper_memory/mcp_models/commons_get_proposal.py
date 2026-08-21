from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsGetProposalInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    proposal_id: str = Field(..., alias="proposalId", description="Proposal id returned by commons_submit_entity, in the form commons-proposal-<uuid>.")


class CommonsGetProposalOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
