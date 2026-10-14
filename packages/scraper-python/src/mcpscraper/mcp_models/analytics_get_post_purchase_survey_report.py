from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetPostPurchaseSurveyReportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id.')
    survey_id: str = Field(..., alias='surveyId', description='Owner-bound survey id.')


AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportSurveyOptionsItem = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportSurveyOptionsItem', {
    'optionId': Required[Annotated[str, Field(min_length=1)]],
    'label': Required[Annotated[str, Field(min_length=1)]],
    'position': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportSurveyOptionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportSurvey = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportSurvey', {
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
    'options': Required[Annotated[list[AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportSurveyOptionsItem], Field(min_length=2)]],
})
AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportSurvey.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportInfluencesItem = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportInfluencesItem', {
    'evidenceId': Required[str],
    'responseId': Required[str],
    'conversionId': Required[str],
    'optionId': Required[Annotated[str, Field(min_length=1)]],
    'optionLabel': Required[Annotated[str, Field(min_length=1)]],
})
AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportInfluencesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportOptionCountsItem = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportOptionCountsItem', {
    'optionId': Required[Annotated[str, Field(min_length=1)]],
    'optionLabel': Required[Annotated[str, Field(min_length=1)]],
    'responseCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportOptionCountsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPostPurchaseSurveyReportOutputVariant1Report = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant1Report', {
    'survey': Required[AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportSurvey],
    'eligibleInvitationCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'responseCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'coverage': Required[Union[Annotated[Union[float, int], Field(ge=0, le=1)], None]],
    'influences': Required[list[AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportInfluencesItem]],
    'optionCounts': Required[list[AnalyticsGetPostPurchaseSurveyReportOutputVariant1ReportOptionCountsItem]],
})
AnalyticsGetPostPurchaseSurveyReportOutputVariant1Report.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetPostPurchaseSurveyReportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    report: AnalyticsGetPostPurchaseSurveyReportOutputVariant1Report = Field(..., alias='report', description='')


AnalyticsGetPostPurchaseSurveyReportOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetPostPurchaseSurveyReportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPostPurchaseSurveyReportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetPostPurchaseSurveyReportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPostPurchaseSurveyReportOutputVariant2Delivery = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetPostPurchaseSurveyReportOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetPostPurchaseSurveyReportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetPostPurchaseSurveyReportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPostPurchaseSurveyReportOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetPostPurchaseSurveyReportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPostPurchaseSurveyReportOutputVariant2Recovery = TypedDict('AnalyticsGetPostPurchaseSurveyReportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetPostPurchaseSurveyReportOutputVariant2RecoveryOperation],
})
AnalyticsGetPostPurchaseSurveyReportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetPostPurchaseSurveyReportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetPostPurchaseSurveyReportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetPostPurchaseSurveyReportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetPostPurchaseSurveyReportOutput).
AnalyticsGetPostPurchaseSurveyReportOutput = Union[AnalyticsGetPostPurchaseSurveyReportOutputVariant2, AnalyticsGetPostPurchaseSurveyReportOutputVariant1]

_AnalyticsGetPostPurchaseSurveyReportInputAdapter = TypeAdapter(AnalyticsGetPostPurchaseSurveyReportInput)
_AnalyticsGetPostPurchaseSurveyReportOutputAdapter = TypeAdapter(AnalyticsGetPostPurchaseSurveyReportOutput)