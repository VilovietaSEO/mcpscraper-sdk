from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SiteExportImageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    job_id: Annotated[str, Field(min_length=1)] = Field(..., alias='jobId', description='Site export job ID returned by extract_site, analyze_site_similarity, or audit_site.')
    image_id: str = Field(..., alias='imageId', description='Downloaded image ID returned by a site_export_read manifest.')


class SiteExportImageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    image_id: str = Field(..., alias='imageId', description='')
    source_page: Union[Union[str, None], None] = Field(None, alias='sourcePage', description='')
    source_url: Union[Union[str, None], None] = Field(None, alias='sourceUrl', description='')
    mime_type: str = Field(..., alias='mimeType', description='')
    bytes: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='bytes', description='')
    sha256: Union[Union[str, None], None] = Field(None, alias='sha256', description='')


SiteExportImageOutputVariant2DeliveryArtifactsItem = TypedDict('SiteExportImageOutputVariant2DeliveryArtifactsItem', {
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
SiteExportImageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SiteExportImageOutputVariant2DeliveryAvailableExportsItem = TypedDict('SiteExportImageOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
SiteExportImageOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SiteExportImageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SiteExportImageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SiteExportImageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SiteExportImageOutputVariant2Delivery = TypedDict('SiteExportImageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SiteExportImageOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[SiteExportImageOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SiteExportImageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SiteExportImageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SiteExportImageOutputVariant2RecoveryOperation = TypedDict('SiteExportImageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SiteExportImageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SiteExportImageOutputVariant2Recovery = TypedDict('SiteExportImageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SiteExportImageOutputVariant2RecoveryOperation],
})
SiteExportImageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SiteExportImageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SiteExportImageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SiteExportImageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SiteExportImageOutput).
SiteExportImageOutput = Union[SiteExportImageOutputVariant1, SiteExportImageOutputVariant2]

_SiteExportImageInputAdapter = TypeAdapter(SiteExportImageInput)
_SiteExportImageOutputAdapter = TypeAdapter(SiteExportImageOutput)