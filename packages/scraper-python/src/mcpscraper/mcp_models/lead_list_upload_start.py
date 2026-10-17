from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LeadListUploadStartInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required stable key for this intended upload session. Reuse it only to retry the same upload-start call.')
    filename_hint: Union[Annotated[str, Field(min_length=1, max_length=255)], None] = Field(None, alias='filenameHint', description='Optional display-only filename. It does not determine or authorize the uploaded format.')


class LeadListUploadStartOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    upload_id: str = Field(..., alias='uploadId', description='')
    status: Union[Literal['awaiting_upload', 'ready'], None] = Field(None, alias='status', description='')
    upload_url: str = Field(..., alias='uploadUrl', description='')
    upload_page_url: str = Field(..., alias='uploadPageUrl', description='')
    accepted_formats: list[Literal['csv', 'tsv', 'xlsx']] = Field(..., alias='acceptedFormats', description='')
    accepted_content_types: list[str] = Field(..., alias='acceptedContentTypes', description='')
    max_bytes: Annotated[int, Field(le=9007199254740991, gt=0)] = Field(..., alias='maxBytes', description='')
    upload_url_expires_at: str = Field(..., alias='uploadUrlExpiresAt', description='')
    source_expires_at: str = Field(..., alias='sourceExpiresAt', description='')


LeadListUploadStartOutputVariant2DeliveryArtifactsItem = TypedDict('LeadListUploadStartOutputVariant2DeliveryArtifactsItem', {
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
LeadListUploadStartOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListUploadStartOutputVariant2DeliveryAvailableExportsItem = TypedDict('LeadListUploadStartOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LeadListUploadStartOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListUploadStartOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LeadListUploadStartOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LeadListUploadStartOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListUploadStartOutputVariant2Delivery = TypedDict('LeadListUploadStartOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LeadListUploadStartOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LeadListUploadStartOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LeadListUploadStartOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LeadListUploadStartOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListUploadStartOutputVariant2RecoveryOperation = TypedDict('LeadListUploadStartOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LeadListUploadStartOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListUploadStartOutputVariant2Recovery = TypedDict('LeadListUploadStartOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LeadListUploadStartOutputVariant2RecoveryOperation],
})
LeadListUploadStartOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LeadListUploadStartOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LeadListUploadStartOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LeadListUploadStartOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LeadListUploadStartOutput).
LeadListUploadStartOutput = Union[LeadListUploadStartOutputVariant1, LeadListUploadStartOutputVariant2]

_LeadListUploadStartInputAdapter = TypeAdapter(LeadListUploadStartInput)
_LeadListUploadStartOutputAdapter = TypeAdapter(LeadListUploadStartOutput)