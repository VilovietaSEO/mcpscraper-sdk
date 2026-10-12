from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CreditsInfoInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    item: Union[str, None] = Field(None, alias='item', description='Optional tool, action, or feature to look up, e.g. "maps reviews", "extract_url", "YouTube transcription", or "concurrency"')
    include_ledger: Union[bool, None] = Field(None, alias='includeLedger', description='Whether to include recent credit ledger entries')


CreditsInfoOutputVariant1MatchedCostVariant1 = TypedDict('CreditsInfoOutputVariant1MatchedCostVariant1', {
    'label': Required[str],
    'credits': Required[Union[float, int]],
    'unit': Required[str],
    'notes': Required[Union[str, None]],
})
CreditsInfoOutputVariant1MatchedCostVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreditsInfoOutputVariant1CostsItem = TypedDict('CreditsInfoOutputVariant1CostsItem', {
    'key': Required[str],
    'label': Required[str],
    'credits': Required[Union[float, int]],
    'unit': Required[str],
    'notes': Required[Union[str, None]],
})
CreditsInfoOutputVariant1CostsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreditsInfoOutputVariant1LedgerItem = TypedDict('CreditsInfoOutputVariant1LedgerItem', {
    'createdAt': Required[str],
    'operation': Required[str],
    'credits': Required[Union[float, int]],
    'description': Required[Union[str, None]],
})
CreditsInfoOutputVariant1LedgerItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreditsInfoOutputVariant1ConcurrencyVariant1Upgrade = TypedDict('CreditsInfoOutputVariant1ConcurrencyVariant1Upgrade', {
    'product': Required[str],
    'ratePolicyVersion': Required[str],
    'priceLabel': Required[str],
    'unitAmountUsd': Required[Union[float, int]],
    'currency': Required[str],
    'interval': Required[str],
    'billingUnit': Required[Literal['pack']],
    'packQuantity': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'slotsPerPack': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'extraSlots': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'billingUrl': Required[str],
    'terminalCommand': Required[str],
    'terminalCommandWithApiKeyEnv': Required[str],
})
CreditsInfoOutputVariant1ConcurrencyVariant1Upgrade.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreditsInfoOutputVariant1ConcurrencyVariant1 = TypedDict('CreditsInfoOutputVariant1ConcurrencyVariant1', {
    'packQuantity': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'slotsPerPack': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'extraSlots': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'monthlyAmountUsd': Required[Annotated[Union[float, int], Field(ge=0)]],
    'currentExtraSlots': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'currentLimit': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'hasSubscription': Required[bool],
    'upgrade': Required[CreditsInfoOutputVariant1ConcurrencyVariant1Upgrade],
})
CreditsInfoOutputVariant1ConcurrencyVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreditsInfoOutputVariant1ConnectedAccountsVariant1 = TypedDict('CreditsInfoOutputVariant1ConnectedAccountsVariant1', {
    'monthlyUsdPerActiveConnection': Required[Union[float, int]],
    'functionCredits': Required[Union[float, int]],
    'proxyCredits': Required[Union[float, int]],
    'computeCreditsPerSecond': Required[Union[float, int]],
    'billingUrl': Required[str],
})
CreditsInfoOutputVariant1ConnectedAccountsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreditsInfoOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    balance_credits: Union[Union[float, int], None] = Field(..., alias='balanceCredits', description='')
    matched_cost: Union[CreditsInfoOutputVariant1MatchedCostVariant1, None] = Field(..., alias='matchedCost', description='')
    costs: list[CreditsInfoOutputVariant1CostsItem] = Field(..., alias='costs', description='')
    ledger: list[CreditsInfoOutputVariant1LedgerItem] = Field(..., alias='ledger', description='')
    concurrency: Union[CreditsInfoOutputVariant1ConcurrencyVariant1, None] = Field(..., alias='concurrency', description='')
    connected_accounts: Union[CreditsInfoOutputVariant1ConnectedAccountsVariant1, None] = Field(..., alias='connectedAccounts', description='')


CreditsInfoOutputVariant2DeliveryArtifactsItem = TypedDict('CreditsInfoOutputVariant2DeliveryArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Union[float, int]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'capabilities': Required[list[str]],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'downloadState': Required[Literal['available', 'local', 'unavailable']],
})
CreditsInfoOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreditsInfoOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CreditsInfoOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CreditsInfoOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreditsInfoOutputVariant2Delivery = TypedDict('CreditsInfoOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CreditsInfoOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CreditsInfoOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CreditsInfoOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreditsInfoOutputVariant2RecoveryOperation = TypedDict('CreditsInfoOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CreditsInfoOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreditsInfoOutputVariant2Recovery = TypedDict('CreditsInfoOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CreditsInfoOutputVariant2RecoveryOperation],
})
CreditsInfoOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreditsInfoOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CreditsInfoOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CreditsInfoOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CreditsInfoOutput).
CreditsInfoOutput = Union[CreditsInfoOutputVariant1, CreditsInfoOutputVariant2]

_CreditsInfoInputAdapter = TypeAdapter(CreditsInfoInput)
_CreditsInfoOutputAdapter = TypeAdapter(CreditsInfoOutput)