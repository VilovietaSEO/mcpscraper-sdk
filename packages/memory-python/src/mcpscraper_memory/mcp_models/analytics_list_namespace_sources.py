from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsListNamespaceSourcesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    namespace_id: str = Field(..., alias="namespaceId", description="Identity Namespace belonging to this Site.")
    limit: int | None = Field(None, alias="limit", description="Maximum safe rows.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque pagination cursor.")


class AnalyticsListNamespaceSourcesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    sources: list[dict[str, Any]] = Field(..., alias="sources", description="")
