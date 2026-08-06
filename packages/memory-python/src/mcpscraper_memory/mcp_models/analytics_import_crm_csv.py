from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsImportCrmCsvInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="")
    source_system: Literal['hubspot', 'salesforce', 'gohighlevel', 'zoho', 'pipedrive', 'keap', 'other'] = Field(..., alias="sourceSystem", description="")
    filename: str = Field(..., alias="filename", description="")
    csv: str = Field(..., alias="csv", description="")
    mapping: dict[str, Any] = Field(..., alias="mapping", description="")


class AnalyticsImportCrmCsvOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
