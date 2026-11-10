from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmQualityListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    queue: Literal['classification', 'naming', 'duplicates', 'imports', 'merges', 'work'] | None = Field(None, alias="queue", description="Governance queue to list: classification, naming, duplicates, imports, merges, or work.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows or records to return on this page; use the returned cursor for more.")


class CrmQualityListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
