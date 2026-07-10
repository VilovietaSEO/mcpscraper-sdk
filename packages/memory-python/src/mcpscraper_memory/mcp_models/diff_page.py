from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class DiffPageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public http/https URL to check for changes since the last diff_page call.")
    allow_local: bool | None = Field(None, alias="allowLocal", description="Allow localhost and private-network URLs. Local development only.")
    reset_baseline: bool | None = Field(None, alias="resetBaseline", description="Discard any previously stored snapshot for this URL and capture the current content as a fresh baseline instead of diffing against history. Use when you deliberately want to restart change tracking.")


class DiffPageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
