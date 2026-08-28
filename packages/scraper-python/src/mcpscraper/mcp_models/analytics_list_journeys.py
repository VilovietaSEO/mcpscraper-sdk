from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsListJourneysInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    journey_tier: Literal['confirmed', 'best_guess', 'all'] | None = Field(None, alias="journeyTier", description="Select confirmed journeys, separately labeled best-guess journeys, or both branches. Confirmed is the default; best-guess evidence can never drive CRM or advertising actions.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows returned in each selected journey branch.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque keyset cursor returned in a selected branch pageInfo.nextCursor.")


class AnalyticsListJourneysOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    journey_tier: Literal['confirmed', 'best_guess', 'all'] = Field(..., alias="journeyTier", description="")
    confirmed: Any = Field(..., alias="confirmed", description="")
    best_guess: Any = Field(..., alias="bestGuess", description="")
    totals_are_separated: bool = Field(..., alias="totalsAreSeparated", description="")
