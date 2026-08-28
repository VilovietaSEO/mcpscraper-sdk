from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateConversionRuleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    name: str = Field(..., alias="name", description="Human-readable name for the record being created or updated.")
    conversion_kind: str = Field(..., alias="conversionKind", description="Optional normalized conversion event kind filter.")
    condition: dict[str, Any] = Field(..., alias="condition", description="Declarative event conditions that must match before X-Ray creates a conversion.")
    default_value_minor: int | None = Field(None, alias="defaultValueMinor", description="Optional default conversion value in the currency minor unit.")
    default_currency: str | None = Field(None, alias="defaultCurrency", description="Three-letter default currency code used when a matched event has no value currency.")
    enabled: bool | None = Field(None, alias="enabled", description="Whether the new rule should begin evaluating events immediately.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsCreateConversionRuleOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    rule: dict[str, Any] = Field(..., alias="rule", description="")
