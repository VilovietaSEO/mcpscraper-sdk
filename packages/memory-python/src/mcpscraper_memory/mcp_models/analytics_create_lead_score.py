from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateLeadScoreInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    namespace_id: str = Field(..., alias="namespaceId", description="Identity Namespace belonging to this Site.")
    name: str = Field(..., alias="name", description="Lead-score name.")
    kind: Literal['fit', 'engagement', 'combined'] = Field(..., alias="kind", description="Score purpose; a score is not a probability or currency value.")
    target_object: Literal['person', 'visitor'] = Field(..., alias="targetObject", description="Object the score evaluates.")
    minimum: int | None = Field(None, alias="minimum", description="Overall lower bound.")
    maximum: int | None = Field(None, alias="maximum", description="Overall upper bound.")
    groups: list[dict[str, Any]] = Field(..., alias="groups", description="Declarative score groups.")
    permitted_properties: list[str] | None = Field(None, alias="permittedProperties", description="Explicit property allowlist used by property predicates.")
    enabled: bool | None = Field(None, alias="enabled", description="Whether this version may evaluate.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsCreateLeadScoreOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    score: dict[str, Any] = Field(..., alias="score", description="")
