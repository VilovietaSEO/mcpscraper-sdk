from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SiteExportReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    job_id: Annotated[str, Field(min_length=1)] = Field(..., alias='jobId', description='Site export job ID returned by extract_site, analyze_site_similarity, or audit_site.')
    page_id: Union[str, None] = Field(None, alias='pageId', description='Page ID returned by a manifest read. Omit to list the export manifest.')
    format: Union[Literal['manifest', 'json', 'html', 'markdown'], None] = Field(None, alias='format', description='manifest lists page/image IDs; JSON, HTML, and Markdown read one page representation.')
    offset: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='offset', description='UTF-8 byte offset. Continue from nextOffset until it is null.')
    max_bytes: Union[Annotated[int, Field(ge=1, le=1000000)], None] = Field(None, alias='maxBytes', description='Maximum UTF-8 bytes returned in this window.')


class SiteExportReadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    page_id: Union[str, None] = Field(..., alias='pageId', description='')
    format: Literal['manifest', 'json', 'html', 'markdown'] = Field(..., alias='format', description='')
    sha256: str = Field(..., alias='sha256', description='')
    text: str = Field(..., alias='text', description='')
    offset: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='offset', description='')
    total_bytes: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='totalBytes', description='')
    next_offset: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='nextOffset', description='')


SiteExportReadOutputVariant2DeliveryArtifactsItem = TypedDict('SiteExportReadOutputVariant2DeliveryArtifactsItem', {
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
SiteExportReadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SiteExportReadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SiteExportReadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SiteExportReadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SiteExportReadOutputVariant2Delivery = TypedDict('SiteExportReadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SiteExportReadOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SiteExportReadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SiteExportReadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SiteExportReadOutputVariant2RecoveryOperation = TypedDict('SiteExportReadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SiteExportReadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SiteExportReadOutputVariant2Recovery = TypedDict('SiteExportReadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SiteExportReadOutputVariant2RecoveryOperation],
})
SiteExportReadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SiteExportReadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SiteExportReadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SiteExportReadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SiteExportReadOutput).
SiteExportReadOutput = Union[SiteExportReadOutputVariant1, SiteExportReadOutputVariant2]

_SiteExportReadInputAdapter = TypeAdapter(SiteExportReadInput)
_SiteExportReadOutputAdapter = TypeAdapter(SiteExportReadOutput)