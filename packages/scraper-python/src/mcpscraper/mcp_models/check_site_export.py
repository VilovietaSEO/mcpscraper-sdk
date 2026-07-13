from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CheckSiteExportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by extract_site or audit_site when called with background (or downloadImages) set — poll this until status is \"complete\" (or \"failed\").")


class CheckSiteExportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
