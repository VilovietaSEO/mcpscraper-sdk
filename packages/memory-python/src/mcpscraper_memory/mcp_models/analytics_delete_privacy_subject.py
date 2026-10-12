from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsDeletePrivacySubjectInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    subject_ref: Annotated[str, Field(min_length=8, max_length=240)] = Field(..., alias='subjectRef', description='Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.')


class AnalyticsDeletePrivacySubjectOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    deleted: bool = Field(..., alias='deleted', description='')
    counts: dict[str, Annotated[int, Field(ge=0, le=9007199254740991)]] = Field(..., alias='counts', description='')


AnalyticsDeletePrivacySubjectOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsDeletePrivacySubjectOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsDeletePrivacySubjectOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsDeletePrivacySubjectOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsDeletePrivacySubjectOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsDeletePrivacySubjectOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsDeletePrivacySubjectOutputVariant2Delivery = TypedDict('AnalyticsDeletePrivacySubjectOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsDeletePrivacySubjectOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsDeletePrivacySubjectOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsDeletePrivacySubjectOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsDeletePrivacySubjectOutputVariant2RecoveryOperation = TypedDict('AnalyticsDeletePrivacySubjectOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsDeletePrivacySubjectOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsDeletePrivacySubjectOutputVariant2Recovery = TypedDict('AnalyticsDeletePrivacySubjectOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsDeletePrivacySubjectOutputVariant2RecoveryOperation],
})
AnalyticsDeletePrivacySubjectOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsDeletePrivacySubjectOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsDeletePrivacySubjectOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsDeletePrivacySubjectOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsDeletePrivacySubjectOutput).
AnalyticsDeletePrivacySubjectOutput = Union[AnalyticsDeletePrivacySubjectOutputVariant2, AnalyticsDeletePrivacySubjectOutputVariant1]

_AnalyticsDeletePrivacySubjectInputAdapter = TypeAdapter(AnalyticsDeletePrivacySubjectInput)
_AnalyticsDeletePrivacySubjectOutputAdapter = TypeAdapter(AnalyticsDeletePrivacySubjectOutput)