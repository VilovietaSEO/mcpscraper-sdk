from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetVaultContractInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="One governed vault: Ideas, Examples and Inspirations, Knowledge, Library, People, Organizations, Deals, Communication, Calendar, Tasks, Projects, Issues, Improvement Log, Experiments, Sprint, or Skills. Former names Inspiration and Communications still resolve.")


class GetVaultContractOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    vault: str | None = Field(None, alias="vault", description="")
    contract: dict[str, Any] | None = Field(None, alias="contract", description="")
    error: str | None = Field(None, alias="error", description="")
