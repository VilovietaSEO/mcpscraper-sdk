from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetLocalSourcebookContractInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    category: Literal['home', 'professional', 'restaurants', 'financial', 'realestate', 'auto', 'wellness'] | None = Field(None, alias="category", description="Optional category whose required canonical tag and contract details should be selected.")


class GetLocalSourcebookContractOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
