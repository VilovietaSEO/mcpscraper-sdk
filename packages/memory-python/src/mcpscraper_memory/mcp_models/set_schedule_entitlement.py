from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SetScheduleEntitlementInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    grantee_identity: Annotated[str, Field(min_length=1)] = Field(..., alias='granteeIdentity', description='Identity whose scheduling entitlement is being set (e.g. an email).')
    enabled: Union[bool, None] = Field(None, alias='enabled', description='Historical entitlement value for migration/recovery only. Omit to preserve the stored value.')
    quota_per_period: Union[Union[float, int], None] = Field(None, alias='quotaPerPeriod', description='Historical monthly quota for migration/recovery only. Omit to preserve the stored value.')
    mcp_scraper_api_key: Union[str, None] = Field(None, alias='mcpScraperApiKey', description="The identity's mcp-scraper API key, stored encrypted, used to reach mcp-scraper tools during scheduled-action execution.")


class SetScheduleEntitlementOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the entitlement was set; false on auth/scope error.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


SetScheduleEntitlementOutputVariant2DeliveryArtifactsItem = TypedDict('SetScheduleEntitlementOutputVariant2DeliveryArtifactsItem', {
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
SetScheduleEntitlementOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduleEntitlementOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SetScheduleEntitlementOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SetScheduleEntitlementOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduleEntitlementOutputVariant2Delivery = TypedDict('SetScheduleEntitlementOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SetScheduleEntitlementOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SetScheduleEntitlementOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SetScheduleEntitlementOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduleEntitlementOutputVariant2RecoveryOperation = TypedDict('SetScheduleEntitlementOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SetScheduleEntitlementOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduleEntitlementOutputVariant2Recovery = TypedDict('SetScheduleEntitlementOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SetScheduleEntitlementOutputVariant2RecoveryOperation],
})
SetScheduleEntitlementOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SetScheduleEntitlementOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SetScheduleEntitlementOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SetScheduleEntitlementOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SetScheduleEntitlementOutput).
SetScheduleEntitlementOutput = Union[SetScheduleEntitlementOutputVariant2, SetScheduleEntitlementOutputVariant1]

_SetScheduleEntitlementInputAdapter = TypeAdapter(SetScheduleEntitlementInput)
_SetScheduleEntitlementOutputAdapter = TypeAdapter(SetScheduleEntitlementOutput)