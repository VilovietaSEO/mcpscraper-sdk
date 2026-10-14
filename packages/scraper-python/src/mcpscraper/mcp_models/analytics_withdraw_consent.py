from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsWithdrawConsentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    subject_ref: Annotated[str, Field(min_length=8, max_length=240)] = Field(..., alias='subjectRef', description='Opaque consent subject reference returned by consent coverage or a safe journey. MCP cannot grant visitor consent.')
    occurred_at: Union[str, None] = Field(None, alias='occurredAt', description='Optional visitor-reported withdrawal time; defaults to server time.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.')


AnalyticsWithdrawConsentOutputVariant1Downstream = TypedDict('AnalyticsWithdrawConsentOutputVariant1Downstream', {
    'candidateAssociationsExpired': Required[bool],
    'activationEligible': Required[bool],
})
AnalyticsWithdrawConsentOutputVariant1Downstream.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsWithdrawConsentOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    receipt: dict[str, Any] = Field(..., alias='receipt', description='')
    downstream: AnalyticsWithdrawConsentOutputVariant1Downstream = Field(..., alias='downstream', description='')


AnalyticsWithdrawConsentOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsWithdrawConsentOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsWithdrawConsentOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsWithdrawConsentOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsWithdrawConsentOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsWithdrawConsentOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsWithdrawConsentOutputVariant2Delivery = TypedDict('AnalyticsWithdrawConsentOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsWithdrawConsentOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsWithdrawConsentOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsWithdrawConsentOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsWithdrawConsentOutputVariant2RecoveryOperation = TypedDict('AnalyticsWithdrawConsentOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsWithdrawConsentOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsWithdrawConsentOutputVariant2Recovery = TypedDict('AnalyticsWithdrawConsentOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsWithdrawConsentOutputVariant2RecoveryOperation],
})
AnalyticsWithdrawConsentOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsWithdrawConsentOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsWithdrawConsentOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsWithdrawConsentOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsWithdrawConsentOutput).
AnalyticsWithdrawConsentOutput = Union[AnalyticsWithdrawConsentOutputVariant2, AnalyticsWithdrawConsentOutputVariant1]

_AnalyticsWithdrawConsentInputAdapter = TypeAdapter(AnalyticsWithdrawConsentInput)
_AnalyticsWithdrawConsentOutputAdapter = TypeAdapter(AnalyticsWithdrawConsentOutput)