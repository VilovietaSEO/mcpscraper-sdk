from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class HarvestPaaStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by harvest_paa_start.")


class HarvestPaaStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="")
    status: Any = Field(..., alias="status", description="")
    replayed: bool = Field(..., alias="replayed", description="")
    progress: dict[str, Any] = Field(..., alias="progress", description="")
    result: Any = Field(..., alias="result", description="")
    billing: dict[str, Any] = Field(..., alias="billing", description="")
