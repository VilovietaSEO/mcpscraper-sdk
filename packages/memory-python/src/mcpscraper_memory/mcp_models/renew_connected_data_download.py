from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RenewConnectedDataDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str = Field(..., alias="artifactId", description="Private artifactId returned by export_connected_service_data.")


class RenewConnectedDataDownloadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    artifact_id: str = Field(..., alias="artifactId", description="")
    download_url: str = Field(..., alias="downloadUrl", description="")
    download_url_expires_at: str = Field(..., alias="downloadUrlExpiresAt", description="")
    expires_at: str = Field(..., alias="expiresAt", description="")
