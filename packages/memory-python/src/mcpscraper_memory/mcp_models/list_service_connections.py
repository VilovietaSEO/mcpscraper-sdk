from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListServiceConnectionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class ListServiceConnectionsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connections: list[dict[str, Any]] = Field(..., alias="connections", description="")
