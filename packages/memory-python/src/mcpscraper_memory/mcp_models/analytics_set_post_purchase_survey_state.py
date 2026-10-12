from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsSetPostPurchaseSurveyStateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id.')
    survey_id: str = Field(..., alias='surveyId', description='Owner-bound survey id.')
    revision: Annotated[int, Field(le=9007199254740991, gt=0)] = Field(..., alias='revision', description='Exact survey revision being changed.')
    state: Literal['published', 'paused', 'archived'] = Field(..., alias='state', description='Publish or pause this revision. Archive is irreversible.')
    approved_copy_id: Union[Union[Annotated[str, Field(min_length=1, max_length=200)], None], None] = Field(None, alias='approvedCopyId', description='Approved privacy disclosure identifier required for production publication; it is not legal approval by itself.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


AnalyticsSetPostPurchaseSurveyStateOutputVariant1SurveyOptionsItem = TypedDict('AnalyticsSetPostPurchaseSurveyStateOutputVariant1SurveyOptionsItem', {
    'optionId': Required[Annotated[str, Field(min_length=1)]],
    'label': Required[Annotated[str, Field(min_length=1)]],
    'position': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsSetPostPurchaseSurveyStateOutputVariant1SurveyOptionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetPostPurchaseSurveyStateOutputVariant1Survey = TypedDict('AnalyticsSetPostPurchaseSurveyStateOutputVariant1Survey', {
    'surveyId': Required[str],
    'siteId': Required[str],
    'revision': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'state': Required[Literal['draft', 'published', 'paused', 'archived']],
    'name': Required[Annotated[str, Field(min_length=1)]],
    'question': Required[Annotated[str, Field(min_length=1)]],
    'selectionMode': Required[Literal['single', 'multiple']],
    'eligibleOutcomeFamilies': Required[Annotated[list[Annotated[str, Field(min_length=1)]], Field(min_length=1)]],
    'exchangeTtlSeconds': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'sessionTtlSeconds': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'approvedCopyId': Required[Union[Annotated[str, Field(min_length=1)], None]],
    'options': Required[Annotated[list[AnalyticsSetPostPurchaseSurveyStateOutputVariant1SurveyOptionsItem], Field(min_length=2)]],
})
AnalyticsSetPostPurchaseSurveyStateOutputVariant1Survey.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsSetPostPurchaseSurveyStateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    operation: Literal['state'] = Field(..., alias='operation', description='')
    survey: AnalyticsSetPostPurchaseSurveyStateOutputVariant1Survey = Field(..., alias='survey', description='')


AnalyticsSetPostPurchaseSurveyStateOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsSetPostPurchaseSurveyStateOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsSetPostPurchaseSurveyStateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetPostPurchaseSurveyStateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsSetPostPurchaseSurveyStateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsSetPostPurchaseSurveyStateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetPostPurchaseSurveyStateOutputVariant2Delivery = TypedDict('AnalyticsSetPostPurchaseSurveyStateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsSetPostPurchaseSurveyStateOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsSetPostPurchaseSurveyStateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsSetPostPurchaseSurveyStateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetPostPurchaseSurveyStateOutputVariant2RecoveryOperation = TypedDict('AnalyticsSetPostPurchaseSurveyStateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsSetPostPurchaseSurveyStateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetPostPurchaseSurveyStateOutputVariant2Recovery = TypedDict('AnalyticsSetPostPurchaseSurveyStateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsSetPostPurchaseSurveyStateOutputVariant2RecoveryOperation],
})
AnalyticsSetPostPurchaseSurveyStateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsSetPostPurchaseSurveyStateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsSetPostPurchaseSurveyStateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsSetPostPurchaseSurveyStateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsSetPostPurchaseSurveyStateOutput).
AnalyticsSetPostPurchaseSurveyStateOutput = Union[AnalyticsSetPostPurchaseSurveyStateOutputVariant2, AnalyticsSetPostPurchaseSurveyStateOutputVariant1]

_AnalyticsSetPostPurchaseSurveyStateInputAdapter = TypeAdapter(AnalyticsSetPostPurchaseSurveyStateInput)
_AnalyticsSetPostPurchaseSurveyStateOutputAdapter = TypeAdapter(AnalyticsSetPostPurchaseSurveyStateOutput)