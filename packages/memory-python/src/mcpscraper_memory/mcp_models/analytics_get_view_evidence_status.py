from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetViewEvidenceStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id.')


AnalyticsGetViewEvidenceStatusOutputVariant1StatusProvidersItem = TypedDict('AnalyticsGetViewEvidenceStatusOutputVariant1StatusProvidersItem', {
    'status': Required[Literal['available', 'unavailable', 'unproven']],
    'evidenceDate': Required[str],
    'reasonCode': Required[Annotated[str, Field(min_length=1)]],
    'reason': Required[Annotated[str, Field(min_length=1)]],
    'requiredEvidence': Required[list[Annotated[str, Field(min_length=1)]]],
})
AnalyticsGetViewEvidenceStatusOutputVariant1StatusProvidersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetViewEvidenceStatusOutputVariant1Status = TypedDict('AnalyticsGetViewEvidenceStatusOutputVariant1Status', {
    'available': Required[bool],
    'providers': Required[list[AnalyticsGetViewEvidenceStatusOutputVariant1StatusProvidersItem]],
})
AnalyticsGetViewEvidenceStatusOutputVariant1Status.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetViewEvidenceStatusOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    status: AnalyticsGetViewEvidenceStatusOutputVariant1Status = Field(..., alias='status', description='')


AnalyticsGetViewEvidenceStatusOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetViewEvidenceStatusOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetViewEvidenceStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetViewEvidenceStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetViewEvidenceStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetViewEvidenceStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetViewEvidenceStatusOutputVariant2Delivery = TypedDict('AnalyticsGetViewEvidenceStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetViewEvidenceStatusOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetViewEvidenceStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetViewEvidenceStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetViewEvidenceStatusOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetViewEvidenceStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetViewEvidenceStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetViewEvidenceStatusOutputVariant2Recovery = TypedDict('AnalyticsGetViewEvidenceStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetViewEvidenceStatusOutputVariant2RecoveryOperation],
})
AnalyticsGetViewEvidenceStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetViewEvidenceStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetViewEvidenceStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetViewEvidenceStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetViewEvidenceStatusOutput).
AnalyticsGetViewEvidenceStatusOutput = Union[AnalyticsGetViewEvidenceStatusOutputVariant2, AnalyticsGetViewEvidenceStatusOutputVariant1]

_AnalyticsGetViewEvidenceStatusInputAdapter = TypeAdapter(AnalyticsGetViewEvidenceStatusInput)
_AnalyticsGetViewEvidenceStatusOutputAdapter = TypeAdapter(AnalyticsGetViewEvidenceStatusOutput)