from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetEntitlementInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



AnalyticsGetEntitlementOutputVariant1EntitlementBilling = TypedDict('AnalyticsGetEntitlementOutputVariant1EntitlementBilling', {
    'standalonePriceUsdMonthly': Required[Annotated[Union[float, int], Field(ge=0)]],
    'includedWithThorbitSubscriptionAtOrAboveUsdMonthly': Required[Annotated[Union[float, int], Field(ge=0)]],
    'consumesMcpScraperCredits': Required[Literal[False]],
})
AnalyticsGetEntitlementOutputVariant1EntitlementBilling.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetEntitlementOutputVariant1EntitlementOwner = TypedDict('AnalyticsGetEntitlementOutputVariant1EntitlementOwner', {
    'name': Required[Literal['Thorbit']],
    'productUrl': Required[str],
    'host': Required[Literal['MCP Scraper']],
})
AnalyticsGetEntitlementOutputVariant1EntitlementOwner.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetEntitlementOutputVariant1Entitlement = TypedDict('AnalyticsGetEntitlementOutputVariant1Entitlement', {
    'product': Required[Literal['x_ray_pixel']],
    'productName': Required[str],
    'access': Required[bool],
    'status': Required[Literal['trial', 'trial_expired', 'eligible', 'ineligible', 'stale', 'bridge_unavailable']],
    'reason': Required[str],
    'planId': Required[Union[str, None]],
    'subscriptionStatus': Required[Union[str, None]],
    'monthlyRecurringRevenueCents': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'minimumMonthlyRecurringRevenueCents': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'verifiedAt': Required[Union[str, None]],
    'connectionSource': Required[Union[Literal['api_key', 'thorbit_session'], None]],
    'thorbitOrganizationHint': Required[Union[str, None]],
    'trialStartedAt': Required[str],
    'trialEndsAt': Required[str],
    'trialDaysRemaining': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'bridgeConfigured': Required[bool],
    'billing': Required[AnalyticsGetEntitlementOutputVariant1EntitlementBilling],
    'owner': Required[AnalyticsGetEntitlementOutputVariant1EntitlementOwner],
})
AnalyticsGetEntitlementOutputVariant1Entitlement.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetEntitlementOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    entitlement: AnalyticsGetEntitlementOutputVariant1Entitlement = Field(..., alias='entitlement', description='')


AnalyticsGetEntitlementOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetEntitlementOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetEntitlementOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetEntitlementOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetEntitlementOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetEntitlementOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetEntitlementOutputVariant2Delivery = TypedDict('AnalyticsGetEntitlementOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetEntitlementOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetEntitlementOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetEntitlementOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetEntitlementOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetEntitlementOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetEntitlementOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetEntitlementOutputVariant2Recovery = TypedDict('AnalyticsGetEntitlementOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetEntitlementOutputVariant2RecoveryOperation],
})
AnalyticsGetEntitlementOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetEntitlementOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetEntitlementOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetEntitlementOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetEntitlementOutput).
AnalyticsGetEntitlementOutput = Union[AnalyticsGetEntitlementOutputVariant2, AnalyticsGetEntitlementOutputVariant1]

_AnalyticsGetEntitlementInputAdapter = TypeAdapter(AnalyticsGetEntitlementInput)
_AnalyticsGetEntitlementOutputAdapter = TypeAdapter(AnalyticsGetEntitlementOutput)