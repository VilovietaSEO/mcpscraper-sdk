from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmOrganizationGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    entity_id: str = Field(..., alias="entityId", description="Existing governed entity identifier for this relation or edit.")


class CrmOrganizationGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
