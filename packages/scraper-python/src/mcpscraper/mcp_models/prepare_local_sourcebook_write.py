from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class PrepareLocalSourcebookWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    category: Literal["home", "professional", "restaurants", "financial", "realestate", "auto", "wellness"] = Field(..., alias="category", description="")
    state: str = Field(..., alias="state", description="")
    business_name: str = Field(..., alias="businessName", description="")
    website_url: str = Field(..., alias="websiteUrl", description="")
    slug: str | None = Field(None, alias="slug", description="")
    tags: list[str] | None = Field(None, alias="tags", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    tag_candidates: list[dict[str, Any]] | None = Field(None, alias="tagCandidates", description="")


class PrepareLocalSourcebookWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
