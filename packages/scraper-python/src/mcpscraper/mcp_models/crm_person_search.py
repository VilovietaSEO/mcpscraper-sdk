from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmPersonSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str | None = Field(None, alias="query", description="Text filter applied to the selected result inventory.")
    relationship_type: Literal['prospect', 'customer', 'former_customer', 'friend', 'coworker', 'collaborator', 'vendor', 'partner', 'advisor', 'media', 'community', 'other'] | None = Field(None, alias="relationshipType", description="One managed relationship type used to filter CRM records.")
    relationship_status: Literal['active', 'inactive', 'archived', 'merged'] | None = Field(None, alias="relationshipStatus", description="Operational relationship status independent of optional commercial lifecycle.")
    commercial_lifecycle: Literal['lead', 'qualified', 'opportunity', 'customer', 'retained', 'churned', 'disqualified'] | None = Field(None, alias="commercialLifecycle", description="Optional commercial lifecycle; friends, coworkers, and other non-commercial relationships may leave it null.")
    relationship_owner_id: str | None = Field(None, alias="relationshipOwnerId", description="Optional owner identifier responsible for the CRM relationship.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque continuation cursor returned by the previous page; omit for the first page.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows or records to return on this page; use the returned cursor for more.")


class CrmPersonSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    items: list[dict[str, Any]] | None = Field(None, alias="items", description="")
    page_info: dict[str, Any] | None = Field(None, alias="pageInfo", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
