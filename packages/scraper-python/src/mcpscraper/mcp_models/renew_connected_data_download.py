from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RenewConnectedDataDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str = Field(..., alias="artifactId", description="Private artifactId returned by export_connected_service_data or export_search_console_table_data.")


class RenewConnectedDataDownloadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
