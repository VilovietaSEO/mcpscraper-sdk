from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsTestEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    definition_id: str = Field(..., alias="definitionId", description="Event definition id returned by analytics_list_event_definitions.")
    hostname: str = Field(..., alias="hostname", description="Bare hostname observed by the browser.")
    path: str = Field(..., alias="path", description="URL path observed by the browser.")
    trigger_kind: Literal['page', 'click', 'form', 'semantic'] = Field(..., alias="triggerKind", description="Trigger interaction being previewed.")
    tag_event_name: str | None = Field(None, alias="tagEventName", description="Validated data-xray-event name observed by the browser.")
    selector_matched: bool | None = Field(None, alias="selectorMatched", description="The browser-reported match result. The server never receives HTML or evaluates a selector.")


class AnalyticsTestEventDefinitionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
