from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsListJourneysInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    journey_tier: Literal['confirmed', 'best_guess', 'all'] | None = Field(None, alias="journeyTier", description="Select confirmed journeys, separately labeled best-guess journeys, or both branches. Confirmed is the default; best-guess evidence can never drive CRM or advertising actions.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows returned in each selected journey branch.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque keyset cursor returned in a selected branch pageInfo.nextCursor.")


class AnalyticsListJourneysOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    journey_tier: Literal['confirmed', 'best_guess', 'all'] | None = Field(None, alias="journeyTier", description="")
    confirmed: Any | None = Field(None, alias="confirmed", description="")
    best_guess: Any | None = Field(None, alias="bestGuess", description="")
    totals_are_separated: bool | None = Field(None, alias="totalsAreSeparated", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
