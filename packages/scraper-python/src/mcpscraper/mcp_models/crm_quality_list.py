from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmQualityListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    queue: Literal['classification', 'naming', 'duplicates', 'imports', 'merges', 'work'] | None = Field(None, alias="queue", description="Governance queue to list: classification, naming, identity, duplicates, or delivery.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows or records to return on this page; use the returned cursor for more.")


class CrmQualityListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    issues: list[dict[str, Any]] | None = Field(None, alias="issues", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
