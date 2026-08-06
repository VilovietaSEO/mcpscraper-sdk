from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateFormInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="")
    pixel_id: str = Field(..., alias="pixelId", description="")
    name: str = Field(..., alias="name", description="")
    fields: list[dict[str, Any]] = Field(..., alias="fields", description="")
    brand: dict[str, Any] = Field(..., alias="brand", description="")
    submit_label: str | None = Field(None, alias="submitLabel", description="")
    success_message: str | None = Field(None, alias="successMessage", description="")
    consent_text: str | None = Field(None, alias="consentText", description="")
    publish: bool | None = Field(None, alias="publish", description="")


class AnalyticsCreateFormOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
