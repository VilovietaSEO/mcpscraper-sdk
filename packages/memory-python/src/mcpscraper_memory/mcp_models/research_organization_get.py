from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResearchOrganizationGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    entity_id: str = Field(..., alias="entityId", description="Existing governed entity identifier for this relation or edit.")


class ResearchOrganizationGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
