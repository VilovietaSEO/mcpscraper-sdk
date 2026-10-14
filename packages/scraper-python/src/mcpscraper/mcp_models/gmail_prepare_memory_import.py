from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


GmailPrepareMemoryImportInputDestinationVariant1 = TypedDict('GmailPrepareMemoryImportInputDestinationVariant1', {
    'mode': Required[Literal['auto']],
})
GmailPrepareMemoryImportInputDestinationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


GmailPrepareMemoryImportInputDestinationVariant2 = TypedDict('GmailPrepareMemoryImportInputDestinationVariant2', {
    'mode': Required[Literal['vault']],
    'vault': Required[Annotated[str, Field(min_length=1, max_length=120)]],
})
GmailPrepareMemoryImportInputDestinationVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class GmailPrepareMemoryImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='connectionId', description='The tenant-owned Gmail connectionId bound into this immutable selection.')
    selection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='selectionId', description='Immutable selectionId returned by gmail_prepare_selection with purpose memory_import.')
    selection_sha256: str = Field(..., alias='selectionSha256', description='Unchanged selection digest to bind the reviewed Memory plan.')
    filing_policy: Union[Literal['source_archive', 'relationship_communications'], None] = Field(None, alias='filingPolicy', description='source_archive preserves evidence in Library by default; relationship_communications requires exact existing identity resolution and never creates People, Tasks, Deals, or Projects.')
    destination: Union[Union[GmailPrepareMemoryImportInputDestinationVariant1, GmailPrepareMemoryImportInputDestinationVariant2], None] = Field(None, alias='destination', description='Use auto for the policy-correct Library or Communications vault, or name one exact existing vault.')
    attachment_policy: Union[Literal['preserve_all', 'index_supported', 'metadata_only', 'exclude'], None] = Field(None, alias='attachmentPolicy', description='How original attachment bytes are handled; preserve_all is the default complete-evidence route.')


GmailPrepareMemoryImportOutputVariant1PlanDestinationVariant1 = TypedDict('GmailPrepareMemoryImportOutputVariant1PlanDestinationVariant1', {
    'mode': Required[Literal['auto']],
})
GmailPrepareMemoryImportOutputVariant1PlanDestinationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareMemoryImportOutputVariant1PlanDestinationVariant2 = TypedDict('GmailPrepareMemoryImportOutputVariant1PlanDestinationVariant2', {
    'mode': Required[Literal['vault']],
    'vault': Required[Annotated[str, Field(min_length=1, max_length=120)]],
})
GmailPrepareMemoryImportOutputVariant1PlanDestinationVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareMemoryImportOutputVariant1PlanRoutesItem = TypedDict('GmailPrepareMemoryImportOutputVariant1PlanRoutesItem', {
    'messageId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'vaultName': Required[str],
    'path': Required[str],
})
GmailPrepareMemoryImportOutputVariant1PlanRoutesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareMemoryImportOutputVariant1PlanRefusalsItem = TypedDict('GmailPrepareMemoryImportOutputVariant1PlanRefusalsItem', {
    'messageId': NotRequired[Annotated[str, Field(min_length=1, max_length=500)]],
    'code': Required[str],
    'reason': Required[str],
})
GmailPrepareMemoryImportOutputVariant1PlanRefusalsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareMemoryImportOutputVariant1Plan = TypedDict('GmailPrepareMemoryImportOutputVariant1Plan', {
    'importPlanId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'selectionId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'selectionSha256': Required[str],
    'messageCount': Required[Annotated[int, Field(ge=1, le=5000)]],
    'attachmentCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'attachmentBytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'filingPolicy': Required[Literal['source_archive', 'relationship_communications']],
    'destination': Required[Union[GmailPrepareMemoryImportOutputVariant1PlanDestinationVariant1, GmailPrepareMemoryImportOutputVariant1PlanDestinationVariant2]],
    'attachmentPolicy': Required[Literal['preserve_all', 'index_supported', 'metadata_only', 'exclude']],
    'routes': Required[Annotated[list[GmailPrepareMemoryImportOutputVariant1PlanRoutesItem], Field(max_length=25)]],
    'routesTruncated': Required[bool],
    'ambiguityCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'ambiguitySamples': Required[Annotated[list[dict[str, Any]], Field(max_length=25)]],
    'refusals': Required[Annotated[list[GmailPrepareMemoryImportOutputVariant1PlanRefusalsItem], Field(max_length=100)]],
    'createdAt': Required[str],
    'expiresAt': Required[str],
    'untrustedContent': Required[Literal[True]],
})
GmailPrepareMemoryImportOutputVariant1Plan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailPrepareMemoryImportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    plan: Union[GmailPrepareMemoryImportOutputVariant1Plan, None] = Field(None, alias='plan', description='')
    untrusted_content: Literal[True] = Field(..., alias='untrustedContent', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailPrepareMemoryImportOutputVariant2DeliveryArtifactsItem = TypedDict('GmailPrepareMemoryImportOutputVariant2DeliveryArtifactsItem', {
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
GmailPrepareMemoryImportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareMemoryImportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailPrepareMemoryImportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailPrepareMemoryImportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareMemoryImportOutputVariant2Delivery = TypedDict('GmailPrepareMemoryImportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailPrepareMemoryImportOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailPrepareMemoryImportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailPrepareMemoryImportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareMemoryImportOutputVariant2RecoveryOperation = TypedDict('GmailPrepareMemoryImportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailPrepareMemoryImportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailPrepareMemoryImportOutputVariant2Recovery = TypedDict('GmailPrepareMemoryImportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailPrepareMemoryImportOutputVariant2RecoveryOperation],
})
GmailPrepareMemoryImportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailPrepareMemoryImportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailPrepareMemoryImportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailPrepareMemoryImportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailPrepareMemoryImportOutput).
GmailPrepareMemoryImportOutput = Union[GmailPrepareMemoryImportOutputVariant2, GmailPrepareMemoryImportOutputVariant1]

_GmailPrepareMemoryImportInputAdapter = TypeAdapter(GmailPrepareMemoryImportInput)
_GmailPrepareMemoryImportOutputAdapter = TypeAdapter(GmailPrepareMemoryImportOutput)