from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CheckSiteExportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="The jobId returned by extract_site or audit_site when called with background (or downloadImages) set — poll this until status is \"complete\" (or \"failed\").")


class CheckSiteExportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="")
    status: Literal["pending", "running", "complete", "failed"] = Field(..., alias="status", description="")
    start_url: str | None = Field(None, alias="startUrl", description="")
    total_urls: int | None = Field(None, alias="totalUrls", description="")
    done_urls: int | None = Field(None, alias="doneUrls", description="")
    bundle_url: Any = Field(..., alias="bundleUrl", description="Downloadable zip URL once status is complete; null otherwise.")
    bundle_bytes: Any = Field(..., alias="bundleBytes", description="Zip size in bytes once status is complete; null otherwise.")
    error: Any | None = Field(None, alias="error", description="Present with a message when status is failed.")
