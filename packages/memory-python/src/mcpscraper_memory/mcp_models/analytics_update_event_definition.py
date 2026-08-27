from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsUpdateEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    definition_id: str = Field(..., alias="definitionId", description="Event definition id returned by analytics_list_event_definitions.")
    name: str | None = Field(None, alias="name", description="Human-readable definition name unique within the Site.")
    event_name: str | None = Field(None, alias="eventName", description="Canonical event name emitted when this definition matches.")
    trigger_kind: Literal['page', 'click', 'form', 'semantic'] | None = Field(None, alias="triggerKind", description="Declarative browser trigger. Semantic uses a data-xray-event tag.")
    path: Any | None = Field(None, alias="path", description="Replacement page path; null clears it.")
    path_match: Literal['exact', 'prefix'] | None = Field(None, alias="pathMatch", description="Replacement page path match mode.")
    selector: Any | None = Field(None, alias="selector", description="Replacement browser-only selector; null clears it.")
    hostnames: list[str] | None = Field(None, alias="hostnames", description="Replacement approved bare-hostname scope.")
    metadata: Any | None = Field(None, alias="metadata", description="Replacement safe metadata; null clears it.")
    once_per_session: bool | None = Field(None, alias="oncePerSession", description="Replacement once-per-browser-session behavior.")
    enabled: bool | None = Field(None, alias="enabled", description="Replacement enabled state.")


class AnalyticsUpdateEventDefinitionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
