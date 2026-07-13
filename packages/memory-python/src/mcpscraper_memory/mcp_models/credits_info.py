from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreditsInfoInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    item: str | None = Field(None, alias="item", description="Optional tool, action, or feature to look up, e.g. \"maps reviews\", \"extract_url\", \"YouTube transcription\", or \"concurrency\"")
    include_ledger: bool | None = Field(None, alias="includeLedger", description="Whether to include recent credit ledger entries")


class CreditsInfoOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
