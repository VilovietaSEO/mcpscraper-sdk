from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LeadListEnrichCancelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    job_id: Annotated[str, Field(min_length=1)] = Field(..., alias='jobId', description='The jobId returned by lead_list_enrich. Poll until status is complete, partial, empty, failed, or cancelled.')


LeadListEnrichCancelOutputVariant1Progress = TypedDict('LeadListEnrichCancelOutputVariant1Progress', {
    'totalRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'completedRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failedRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'cancelledRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'rowsWithContact': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'rowsWithPeople': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
LeadListEnrichCancelOutputVariant1Progress.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant1Billing = TypedDict('LeadListEnrichCancelOutputVariant1Billing', {
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
LeadListEnrichCancelOutputVariant1Billing.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant1SampleRowsItemPeopleItemSourcesItem = TypedDict('LeadListEnrichCancelOutputVariant1SampleRowsItemPeopleItemSourcesItem', {
    'sourceType': Required[Literal['serp_snippet', 'ai_overview']],
    'purpose': Required[Literal['role', 'linkedin']],
    'sourceUrl': Required[str],
    'sourceTitle': Required[str],
    'sourcePosition': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'context': Required[str],
    'citationUrls': NotRequired[Annotated[list[str], Field(max_length=5)]],
})
LeadListEnrichCancelOutputVariant1SampleRowsItemPeopleItemSourcesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant1SampleRowsItemPeopleItem = TypedDict('LeadListEnrichCancelOutputVariant1SampleRowsItemPeopleItem', {
    'name': Required[str],
    'role': Required[str],
    'relationship': Required[Literal['owner', 'founder', 'executive', 'manager', 'team_member']],
    'linkedinUrl': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reasons': Required[Annotated[list[str], Field(max_length=10)]],
    'sources': Required[Annotated[list[LeadListEnrichCancelOutputVariant1SampleRowsItemPeopleItemSourcesItem], Field(max_length=3)]],
})
LeadListEnrichCancelOutputVariant1SampleRowsItemPeopleItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant1SampleRowsItem = TypedDict('LeadListEnrichCancelOutputVariant1SampleRowsItem', {
    'people': NotRequired[Annotated[list[LeadListEnrichCancelOutputVariant1SampleRowsItemPeopleItem], Field(max_length=3)]],
})
LeadListEnrichCancelOutputVariant1SampleRowsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant1AmbiguousRowsItemCandidatesItem = TypedDict('LeadListEnrichCancelOutputVariant1AmbiguousRowsItemCandidatesItem', {
    'name': Required[str],
    'websiteUrl': NotRequired[Union[str, None]],
    'mapsUrl': NotRequired[Union[str, None]],
    'confidence': NotRequired[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'evidence': NotRequired[list[str]],
})
LeadListEnrichCancelOutputVariant1AmbiguousRowsItemCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant1AmbiguousRowsItem = TypedDict('LeadListEnrichCancelOutputVariant1AmbiguousRowsItem', {
    'ordinal': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'candidates': Required[Annotated[list[LeadListEnrichCancelOutputVariant1AmbiguousRowsItemCandidatesItem], Field(max_length=3)]],
})
LeadListEnrichCancelOutputVariant1AmbiguousRowsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant1ArtifactsItem = TypedDict('LeadListEnrichCancelOutputVariant1ArtifactsItem', {
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
LeadListEnrichCancelOutputVariant1ArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LeadListEnrichCancelOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    status: Literal['queued', 'running', 'complete', 'partial', 'empty', 'failed', 'cancelled'] = Field(..., alias='status', description='')
    progress: LeadListEnrichCancelOutputVariant1Progress = Field(..., alias='progress', description='')
    billing: LeadListEnrichCancelOutputVariant1Billing = Field(..., alias='billing', description='')
    sample_rows: Annotated[list[LeadListEnrichCancelOutputVariant1SampleRowsItem], Field(max_length=10)] = Field(..., alias='sampleRows', description='')
    ambiguous_rows: Union[Annotated[list[LeadListEnrichCancelOutputVariant1AmbiguousRowsItem], Field(max_length=10)], None] = Field(None, alias='ambiguousRows', description='')
    artifacts: Annotated[list[LeadListEnrichCancelOutputVariant1ArtifactsItem], Field(max_length=2)] = Field(..., alias='artifacts', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')
    created_at: Union[str, None] = Field(None, alias='createdAt', description='')
    updated_at: Union[str, None] = Field(None, alias='updatedAt', description='')
    completed_at: Union[Union[str, None], None] = Field(None, alias='completedAt', description='')
    error_code: Union[Union[str, None], None] = Field(None, alias='errorCode', description='')
    error: Union[Union[str, None], None] = Field(None, alias='error', description='')
    retryable: Union[Union[bool, None], None] = Field(None, alias='retryable', description='')


LeadListEnrichCancelOutputVariant2DeliveryArtifactsItem = TypedDict('LeadListEnrichCancelOutputVariant2DeliveryArtifactsItem', {
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
LeadListEnrichCancelOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant2DeliveryAvailableExportsItem = TypedDict('LeadListEnrichCancelOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LeadListEnrichCancelOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LeadListEnrichCancelOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LeadListEnrichCancelOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant2Delivery = TypedDict('LeadListEnrichCancelOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LeadListEnrichCancelOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LeadListEnrichCancelOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LeadListEnrichCancelOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LeadListEnrichCancelOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant2RecoveryOperation = TypedDict('LeadListEnrichCancelOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LeadListEnrichCancelOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichCancelOutputVariant2Recovery = TypedDict('LeadListEnrichCancelOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LeadListEnrichCancelOutputVariant2RecoveryOperation],
})
LeadListEnrichCancelOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LeadListEnrichCancelOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LeadListEnrichCancelOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LeadListEnrichCancelOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LeadListEnrichCancelOutput).
LeadListEnrichCancelOutput = Union[LeadListEnrichCancelOutputVariant1, LeadListEnrichCancelOutputVariant2]

_LeadListEnrichCancelInputAdapter = TypeAdapter(LeadListEnrichCancelInput)
_LeadListEnrichCancelOutputAdapter = TypeAdapter(LeadListEnrichCancelOutput)