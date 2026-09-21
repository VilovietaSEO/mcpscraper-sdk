from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExtractUrlStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by extract_url. Polling never starts or bills another extraction.")


class ExtractUrlStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="")
    status: Literal['pending', 'running', 'done', 'failed', 'cancelled'] = Field(..., alias="status", description="")
    status_tool: str = Field(..., alias="statusTool", description="")
    replayed: bool = Field(..., alias="replayed", description="")
    result: Any = Field(..., alias="result", description="")
    error: Any = Field(..., alias="error", description="")
    billing: dict[str, Any] = Field(..., alias="billing", description="")
