from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class EditorialReadingRoomGuideInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    focus: Literal["workflow", "content_contract", "example"] | None = Field(None, alias="focus", description="Which part of the reusable editorial-reading-room guide to return. Start with workflow; fetch the content contract or compact example only when needed.")


class EditorialReadingRoomGuideOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    focus: Literal["workflow", "content_contract", "example"] = Field(..., alias="focus", description="")
    guide: str = Field(..., alias="guide", description="")
