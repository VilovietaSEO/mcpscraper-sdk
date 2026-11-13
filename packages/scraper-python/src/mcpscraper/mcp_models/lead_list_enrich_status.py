from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LeadListEnrichStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    job_id: Annotated[str, Field(min_length=1)] = Field(..., alias='jobId', description='The jobId returned by lead_list_enrich. Poll until status is complete, partial, empty, failed, or cancelled.')


LeadListEnrichStatusOutputVariant1Progress = TypedDict('LeadListEnrichStatusOutputVariant1Progress', {
    'totalRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'completedRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failedRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'cancelledRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'rowsWithContact': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'rowsWithPeople': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
LeadListEnrichStatusOutputVariant1Progress.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant1Billing = TypedDict('LeadListEnrichStatusOutputVariant1Billing', {
    'heldMc': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'finalMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'refundMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'mapsSearches': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'pageAttempts': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'serpSearches': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'mapsMc': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'pageMc': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'serpMc': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
LeadListEnrichStatusOutputVariant1Billing.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant1SampleRowsItemPeopleItemSourcesItem = TypedDict('LeadListEnrichStatusOutputVariant1SampleRowsItemPeopleItemSourcesItem', {
    'sourceType': Required[Literal['serp_snippet', 'ai_overview']],
    'purpose': Required[Literal['role', 'linkedin']],
    'sourceUrl': Required[str],
    'sourceTitle': Required[str],
    'sourcePosition': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'context': Required[str],
    'citationUrls': NotRequired[Annotated[list[str], Field(max_length=5)]],
})
LeadListEnrichStatusOutputVariant1SampleRowsItemPeopleItemSourcesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant1SampleRowsItemPeopleItem = TypedDict('LeadListEnrichStatusOutputVariant1SampleRowsItemPeopleItem', {
    'name': Required[str],
    'role': Required[str],
    'relationship': Required[Literal['owner', 'founder', 'executive', 'manager', 'team_member']],
    'linkedinUrl': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reasons': Required[Annotated[list[str], Field(max_length=10)]],
    'sources': Required[Annotated[list[LeadListEnrichStatusOutputVariant1SampleRowsItemPeopleItemSourcesItem], Field(max_length=3)]],
})
LeadListEnrichStatusOutputVariant1SampleRowsItemPeopleItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant1SampleRowsItem = TypedDict('LeadListEnrichStatusOutputVariant1SampleRowsItem', {
    'people': NotRequired[Annotated[list[LeadListEnrichStatusOutputVariant1SampleRowsItemPeopleItem], Field(max_length=3)]],
})
LeadListEnrichStatusOutputVariant1SampleRowsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant1AmbiguousRowsItemCandidatesItem = TypedDict('LeadListEnrichStatusOutputVariant1AmbiguousRowsItemCandidatesItem', {
    'name': Required[str],
    'websiteUrl': NotRequired[Union[str, None]],
    'mapsUrl': NotRequired[Union[str, None]],
    'confidence': NotRequired[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'evidence': NotRequired[list[str]],
})
LeadListEnrichStatusOutputVariant1AmbiguousRowsItemCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant1AmbiguousRowsItem = TypedDict('LeadListEnrichStatusOutputVariant1AmbiguousRowsItem', {
    'ordinal': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'candidates': Required[Annotated[list[LeadListEnrichStatusOutputVariant1AmbiguousRowsItemCandidatesItem], Field(max_length=3)]],
})
LeadListEnrichStatusOutputVariant1AmbiguousRowsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant1ArtifactsItem = TypedDict('LeadListEnrichStatusOutputVariant1ArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'rowCount': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
})
LeadListEnrichStatusOutputVariant1ArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LeadListEnrichStatusOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    status: Literal['queued', 'running', 'complete', 'partial', 'empty', 'failed', 'cancelled'] = Field(..., alias='status', description='')
    progress: LeadListEnrichStatusOutputVariant1Progress = Field(..., alias='progress', description='')
    billing: LeadListEnrichStatusOutputVariant1Billing = Field(..., alias='billing', description='')
    sample_rows: Annotated[list[LeadListEnrichStatusOutputVariant1SampleRowsItem], Field(max_length=10)] = Field(..., alias='sampleRows', description='')
    ambiguous_rows: Union[Annotated[list[LeadListEnrichStatusOutputVariant1AmbiguousRowsItem], Field(max_length=10)], None] = Field(None, alias='ambiguousRows', description='')
    artifacts: Annotated[list[LeadListEnrichStatusOutputVariant1ArtifactsItem], Field(max_length=2)] = Field(..., alias='artifacts', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')
    created_at: Union[str, None] = Field(None, alias='createdAt', description='')
    updated_at: Union[str, None] = Field(None, alias='updatedAt', description='')
    completed_at: Union[Union[str, None], None] = Field(None, alias='completedAt', description='')
    error_code: Union[Union[str, None], None] = Field(None, alias='errorCode', description='')
    error: Union[Union[str, None], None] = Field(None, alias='error', description='')
    retryable: Union[Union[bool, None], None] = Field(None, alias='retryable', description='')


LeadListEnrichStatusOutputVariant2DeliveryArtifactsItem = TypedDict('LeadListEnrichStatusOutputVariant2DeliveryArtifactsItem', {
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
LeadListEnrichStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant2DeliveryAvailableExportsItem = TypedDict('LeadListEnrichStatusOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LeadListEnrichStatusOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LeadListEnrichStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LeadListEnrichStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant2Delivery = TypedDict('LeadListEnrichStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LeadListEnrichStatusOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LeadListEnrichStatusOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LeadListEnrichStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LeadListEnrichStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant2RecoveryOperation = TypedDict('LeadListEnrichStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LeadListEnrichStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichStatusOutputVariant2Recovery = TypedDict('LeadListEnrichStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LeadListEnrichStatusOutputVariant2RecoveryOperation],
})
LeadListEnrichStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LeadListEnrichStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LeadListEnrichStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LeadListEnrichStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LeadListEnrichStatusOutput).
LeadListEnrichStatusOutput = Union[LeadListEnrichStatusOutputVariant1, LeadListEnrichStatusOutputVariant2]

_LeadListEnrichStatusInputAdapter = TypeAdapter(LeadListEnrichStatusInput)
_LeadListEnrichStatusOutputAdapter = TypeAdapter(LeadListEnrichStatusOutput)