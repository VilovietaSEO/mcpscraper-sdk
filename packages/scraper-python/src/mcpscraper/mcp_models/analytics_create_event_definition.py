from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    name: str = Field(..., alias="name", description="Human-readable definition name unique within the Site.")
    event_name: str = Field(..., alias="eventName", description="Canonical event name emitted when this definition matches.")
    trigger_kind: Literal['page', 'click', 'form', 'semantic'] = Field(..., alias="triggerKind", description="Declarative browser trigger. Semantic uses a data-xray-event tag.")
    path: str | None = Field(None, alias="path", description="URL path required for page triggers.")
    path_match: Literal['exact', 'prefix'] | None = Field(None, alias="pathMatch", description="Whether the page path must equal or begin with path.")
    selector: str | None = Field(None, alias="selector", description="CSS selector evaluated only by the first-party Pixel for click or form triggers.")
    hostnames: list[str] | None = Field(None, alias="hostnames", description="Optional approved bare hostnames. Empty applies across the Site Pixel hosts.")
    metadata: dict[str, Any] | None = Field(None, alias="metadata", description="Safe fixed event metadata; never form field values or arbitrary code.")
    once_per_session: bool | None = Field(None, alias="oncePerSession", description="Emit at most once per browser session when true.")
    enabled: bool | None = Field(None, alias="enabled", description="Whether the Pixel may emit this definition.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsCreateEventDefinitionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    definition: dict[str, Any] = Field(..., alias="definition", description="")
