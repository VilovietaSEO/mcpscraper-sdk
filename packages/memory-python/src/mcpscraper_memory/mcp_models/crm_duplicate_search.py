from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmDuplicateSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    domain: Literal['crm_person', 'crm_organization'] = Field(..., alias="domain", description="Exact governed entity domain selected from the operation contract; callers cannot choose a Research domain for CRM imports.")
    entity_id: str | None = Field(None, alias="entityId", description="Existing governed entity identifier for this relation or edit.")
    display_name: str | None = Field(None, alias="displayName", description="Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.")
    email: str | None = Field(None, alias="email", description="Confirmed contact email authorized for this CRM operation.")
    phone: str | None = Field(None, alias="phone", description="Confirmed contact phone authorized for this CRM operation.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows or records to return on this page; use the returned cursor for more.")


class CrmDuplicateSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    candidates: list[dict[str, Any]] | None = Field(None, alias="candidates", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
