from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantNumberSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_ref: str = Field(..., alias="connectionRef", description="Opaque caller-owned phone connection reference; never provide account credentials.")
    country_code: str = Field(..., alias="countryCode", description="Two-letter country code for the desired number inventory.")
    number_type: Literal['local', 'mobile', 'tollFree'] = Field(..., alias="numberType", description="Number inventory family to search.")
    capabilities: list[Literal['sms', 'mms', 'voice']] = Field(..., alias="capabilities", description="Required capabilities; returned candidates must satisfy every selected capability.")
    area_code: str | None = Field(None, alias="areaCode", description="Optional national area code or prefix used to narrow the search.")
    page_size: int | None = Field(None, alias="pageSize", description="Maximum expiring candidates to return from this bounded provider search.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable request identity for this bounded search.")


class AssistantNumberSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
