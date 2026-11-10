from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CreditsInfoInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    item: str | None = Field(None, alias="item", description="Optional tool, action, or feature to look up, e.g. \"maps reviews\", \"extract_url\", \"YouTube transcription\", or \"concurrency\"")
    include_ledger: bool | None = Field(None, alias="includeLedger", description="Whether to include recent credit ledger entries")


class CreditsInfoOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    balance_credits: Any | None = Field(None, alias="balanceCredits", description="")
    matched_cost: Any | None = Field(None, alias="matchedCost", description="")
    costs: list[dict[str, Any]] | None = Field(None, alias="costs", description="")
    ledger: list[dict[str, Any]] | None = Field(None, alias="ledger", description="")
    concurrency: Any | None = Field(None, alias="concurrency", description="")
    connected_accounts: Any | None = Field(None, alias="connectedAccounts", description="")
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
