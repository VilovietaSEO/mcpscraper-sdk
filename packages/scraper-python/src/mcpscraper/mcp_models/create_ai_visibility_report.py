from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CreateAiVisibilityReportInputBrand = TypedDict('CreateAiVisibilityReportInputBrand', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'domain': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'logoUrl': NotRequired[Annotated[str, Field(max_length=2000)]],
    'accentColor': NotRequired[str],
})
CreateAiVisibilityReportInputBrand.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputPreparedBy = TypedDict('CreateAiVisibilityReportInputPreparedBy', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'logoUrl': NotRequired[Annotated[str, Field(max_length=2000)]],
})
CreateAiVisibilityReportInputPreparedBy.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputPeriod = TypedDict('CreateAiVisibilityReportInputPeriod', {
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'from': NotRequired[Annotated[str, Field(min_length=1, max_length=40)]],
    'to': NotRequired[Annotated[str, Field(min_length=1, max_length=40)]],
})
CreateAiVisibilityReportInputPeriod.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputSummary = TypedDict('CreateAiVisibilityReportInputSummary', {
    'visibilityPct': Required[Annotated[Union[float, int], Field(ge=0, le=100)]],
    'answersNamed': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'answersTotal': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'visibilityChangePts': NotRequired[Annotated[Union[float, int], Field(ge=-100, le=100)]],
    'shareOfVoicePct': NotRequired[Annotated[Union[float, int], Field(ge=0, le=100)]],
    'shareRank': NotRequired[Annotated[int, Field(ge=1, le=1000)]],
    'brandsTracked': NotRequired[Annotated[int, Field(ge=1, le=1000)]],
    'failedRuns': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CreateAiVisibilityReportInputSummary.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputByAssistantItem = TypedDict('CreateAiVisibilityReportInputByAssistantItem', {
    'assistant': Required[Annotated[str, Field(min_length=1, max_length=60)]],
    'visibilityPct': Required[Annotated[Union[float, int], Field(ge=0, le=100)]],
    'answersTotal': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CreateAiVisibilityReportInputByAssistantItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputTrendItemCompetitorsItem = TypedDict('CreateAiVisibilityReportInputTrendItemCompetitorsItem', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'pct': Required[Annotated[Union[float, int], Field(ge=0, le=100)]],
})
CreateAiVisibilityReportInputTrendItemCompetitorsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputTrendItem = TypedDict('CreateAiVisibilityReportInputTrendItem', {
    'date': Required[Annotated[str, Field(min_length=1, max_length=40)]],
    'brandPct': Required[Annotated[Union[float, int], Field(ge=0, le=100)]],
    'answersTotal': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'competitors': NotRequired[Annotated[list[CreateAiVisibilityReportInputTrendItemCompetitorsItem], Field(max_length=8)]],
})
CreateAiVisibilityReportInputTrendItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputShareOfVoiceItem = TypedDict('CreateAiVisibilityReportInputShareOfVoiceItem', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'domain': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'sharePct': Required[Annotated[Union[float, int], Field(ge=0, le=100)]],
    'mentions': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'changePts': NotRequired[Annotated[Union[float, int], Field(ge=-100, le=100)]],
})
CreateAiVisibilityReportInputShareOfVoiceItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputPromptsItemResultsItem = TypedDict('CreateAiVisibilityReportInputPromptsItemResultsItem', {
    'assistant': Required[Annotated[str, Field(min_length=1, max_length=60)]],
    'runs': NotRequired[Annotated[int, Field(ge=1, le=10000)]],
    'namedRuns': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'citedRuns': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CreateAiVisibilityReportInputPromptsItemResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputPromptsItem = TypedDict('CreateAiVisibilityReportInputPromptsItem', {
    'prompt': Required[Annotated[str, Field(min_length=1, max_length=300)]],
    'topic': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'results': Required[Annotated[list[CreateAiVisibilityReportInputPromptsItemResultsItem], Field(max_length=12)]],
})
CreateAiVisibilityReportInputPromptsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputTopicsItemCompetitorsItem = TypedDict('CreateAiVisibilityReportInputTopicsItemCompetitorsItem', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'pct': Required[Annotated[Union[float, int], Field(ge=0, le=100)]],
})
CreateAiVisibilityReportInputTopicsItemCompetitorsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputTopicsItem = TypedDict('CreateAiVisibilityReportInputTopicsItem', {
    'topic': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'answersTotal': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'brandPct': Required[Annotated[Union[float, int], Field(ge=0, le=100)]],
    'competitors': NotRequired[Annotated[list[CreateAiVisibilityReportInputTopicsItemCompetitorsItem], Field(max_length=6)]],
})
CreateAiVisibilityReportInputTopicsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputSiteOutcome = TypedDict('CreateAiVisibilityReportInputSiteOutcome', {
    'cited': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'researched': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'absent': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CreateAiVisibilityReportInputSiteOutcome.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputSiteTypesItem = TypedDict('CreateAiVisibilityReportInputSiteTypesItem', {
    'type': Required[Annotated[str, Field(min_length=1, max_length=60)]],
    'sources': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'cited': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CreateAiVisibilityReportInputSiteTypesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputTopSourcesItem = TypedDict('CreateAiVisibilityReportInputTopSourcesItem', {
    'domain': Required[Annotated[str, Field(min_length=1, max_length=200)]],
    'siteType': NotRequired[Annotated[str, Field(min_length=1, max_length=60)]],
    'answers': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'cited': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CreateAiVisibilityReportInputTopSourcesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputSearchQueriesItem = TypedDict('CreateAiVisibilityReportInputSearchQueriesItem', {
    'query': Required[Annotated[str, Field(min_length=1, max_length=300)]],
    'count': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CreateAiVisibilityReportInputSearchQueriesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputWriteUpsItem = TypedDict('CreateAiVisibilityReportInputWriteUpsItem', {
    'heading': Required[Annotated[str, Field(min_length=1, max_length=140)]],
    'body': Required[Annotated[str, Field(min_length=1, max_length=6000)]],
})
CreateAiVisibilityReportInputWriteUpsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputRecommendationsItem = TypedDict('CreateAiVisibilityReportInputRecommendationsItem', {
    'title': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'detail': Required[Annotated[str, Field(min_length=1, max_length=1500)]],
})
CreateAiVisibilityReportInputRecommendationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateAiVisibilityReportInputMethod = TypedDict('CreateAiVisibilityReportInputMethod', {
    'assistants': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=60)]], Field(max_length=12)]],
    'runsPerPrompt': NotRequired[Annotated[int, Field(ge=1, le=1000)]],
    'notes': NotRequired[Annotated[str, Field(min_length=1, max_length=1500)]],
})
CreateAiVisibilityReportInputMethod.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CreateAiVisibilityReportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    title: Union[Annotated[str, Field(min_length=1, max_length=140)], None] = Field(None, alias='title', description='Report title shown at the top of the page.')
    brand: CreateAiVisibilityReportInputBrand = Field(..., alias='brand', description='The brand this report is about.')
    prepared_for: Union[Annotated[str, Field(min_length=1, max_length=120)], None] = Field(None, alias='preparedFor', description='Client or team the report is prepared for.')
    prepared_by: Union[CreateAiVisibilityReportInputPreparedBy, None] = Field(None, alias='preparedBy', description='Who presents the report (white-label).')
    period: CreateAiVisibilityReportInputPeriod = Field(..., alias='period', description='The period the measures cover.')
    summary: CreateAiVisibilityReportInputSummary = Field(..., alias='summary', description='Headline measures. The only required section.')
    by_assistant: Union[Annotated[list[CreateAiVisibilityReportInputByAssistantItem], Field(max_length=12)], None] = Field(None, alias='byAssistant', description='Visibility for each assistant.')
    trend: Union[Annotated[list[CreateAiVisibilityReportInputTrendItem], Field(max_length=120)], None] = Field(None, alias='trend', description='Visibility over time, oldest first; two points minimum.')
    share_of_voice: Union[Annotated[list[CreateAiVisibilityReportInputShareOfVoiceItem], Field(max_length=25)], None] = Field(None, alias='shareOfVoice', description='Share of voice for every tracked brand, including this one.')
    prompts: Union[Annotated[list[CreateAiVisibilityReportInputPromptsItem], Field(max_length=200)], None] = Field(None, alias='prompts', description='Each question, per assistant.')
    topics: Union[Annotated[list[CreateAiVisibilityReportInputTopicsItem], Field(max_length=50)], None] = Field(None, alias='topics', description='Visibility by topic against competitors.')
    site_outcome: Union[CreateAiVisibilityReportInputSiteOutcome, None] = Field(None, alias='siteOutcome', description="The brand's website across the answers.")
    site_types: Union[Annotated[list[CreateAiVisibilityReportInputSiteTypesItem], Field(max_length=20)], None] = Field(None, alias='siteTypes', description='The kinds of site the assistants relied on.')
    top_sources: Union[Annotated[list[CreateAiVisibilityReportInputTopSourcesItem], Field(max_length=100)], None] = Field(None, alias='topSources', description='Domains that appeared most often.')
    search_queries: Union[Annotated[list[CreateAiVisibilityReportInputSearchQueriesItem], Field(max_length=100)], None] = Field(None, alias='searchQueries', description="The assistants' own searches, when shown.")
    write_ups: Union[Annotated[list[CreateAiVisibilityReportInputWriteUpsItem], Field(max_length=12)], None] = Field(None, alias='writeUps', description='Written analysis. State only what the figures support.')
    recommendations: Union[Annotated[list[CreateAiVisibilityReportInputRecommendationsItem], Field(max_length=12)], None] = Field(None, alias='recommendations', description='Recommended next steps, most important first.')
    method: Union[CreateAiVisibilityReportInputMethod, None] = Field(None, alias='method', description='How the data was collected.')
    filename: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='filename', description='Optional file name; derived from brand and period when omitted.')
    pdf: Union[Literal['none', 'a4', 'letter'], None] = Field(None, alias='pdf', description='Also make a PDF file on A4 or US Letter paper. The PDF is charged; the page is free.')


CreateAiVisibilityReportOutputVariant1Artifact = TypedDict('CreateAiVisibilityReportOutputVariant1Artifact', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[Literal['text/html']],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
})
CreateAiVisibilityReportOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateAiVisibilityReportOutputVariant1PdfArtifact = TypedDict('CreateAiVisibilityReportOutputVariant1PdfArtifact', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[Literal['application/pdf']],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
})
CreateAiVisibilityReportOutputVariant1PdfArtifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateAiVisibilityReportOutputVariant1Pdf = TypedDict('CreateAiVisibilityReportOutputVariant1Pdf', {
    'ok': Required[bool],
    'paper': NotRequired[str],
    'artifact': NotRequired[CreateAiVisibilityReportOutputVariant1PdfArtifact],
    'chargedCredits': Required[Annotated[Union[float, int], Field(ge=0)]],
    'error': NotRequired[str],
})
CreateAiVisibilityReportOutputVariant1Pdf.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateAiVisibilityReportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    title: str = Field(..., alias='title', description='')
    filename: str = Field(..., alias='filename', description='')
    delivery: Literal['artifact', 'local_file'] = Field(..., alias='delivery', description='')
    sections: list[str] = Field(..., alias='sections', description='')
    bytes: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='bytes', description='')
    sha256: str = Field(..., alias='sha256', description='')
    generated_at: str = Field(..., alias='generatedAt', description='')
    artifact: Union[CreateAiVisibilityReportOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    local_path: Union[str, None] = Field(None, alias='localPath', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')
    pdf: Union[CreateAiVisibilityReportOutputVariant1Pdf, None] = Field(None, alias='pdf', description='')


CreateAiVisibilityReportOutputVariant2DeliveryArtifactsItem = TypedDict('CreateAiVisibilityReportOutputVariant2DeliveryArtifactsItem', {
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
CreateAiVisibilityReportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateAiVisibilityReportOutputVariant2DeliveryAvailableExportsItem = TypedDict('CreateAiVisibilityReportOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CreateAiVisibilityReportOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateAiVisibilityReportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CreateAiVisibilityReportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CreateAiVisibilityReportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateAiVisibilityReportOutputVariant2Delivery = TypedDict('CreateAiVisibilityReportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CreateAiVisibilityReportOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CreateAiVisibilityReportOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CreateAiVisibilityReportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CreateAiVisibilityReportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateAiVisibilityReportOutputVariant2RecoveryOperation = TypedDict('CreateAiVisibilityReportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CreateAiVisibilityReportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateAiVisibilityReportOutputVariant2Recovery = TypedDict('CreateAiVisibilityReportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CreateAiVisibilityReportOutputVariant2RecoveryOperation],
})
CreateAiVisibilityReportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateAiVisibilityReportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CreateAiVisibilityReportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CreateAiVisibilityReportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CreateAiVisibilityReportOutput).
CreateAiVisibilityReportOutput = Union[CreateAiVisibilityReportOutputVariant1, CreateAiVisibilityReportOutputVariant2]

_CreateAiVisibilityReportInputAdapter = TypeAdapter(CreateAiVisibilityReportInput)
_CreateAiVisibilityReportOutputAdapter = TypeAdapter(CreateAiVisibilityReportOutput)