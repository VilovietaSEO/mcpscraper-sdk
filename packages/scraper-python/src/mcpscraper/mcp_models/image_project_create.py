from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ImageProjectCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Writable logical Memory vault. Defaults to the active vault.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    description: Union[Annotated[str, Field(max_length=2000)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')


ImageProjectCreateOutputVariant1Project = TypedDict('ImageProjectCreateOutputVariant1Project', {
    'id': Required[str],
    'name': Required[str],
    'description': Required[Union[str, None]],
    'createdAt': Required[str],
})
ImageProjectCreateOutputVariant1Project.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageProjectCreateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    project: Union[ImageProjectCreateOutputVariant1Project, None] = Field(None, alias='project', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ImageProjectCreateOutputVariant2DeliveryArtifactsItem = TypedDict('ImageProjectCreateOutputVariant2DeliveryArtifactsItem', {
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
ImageProjectCreateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageProjectCreateOutputVariant2DeliveryAvailableExportsItem = TypedDict('ImageProjectCreateOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ImageProjectCreateOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageProjectCreateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ImageProjectCreateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ImageProjectCreateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageProjectCreateOutputVariant2Delivery = TypedDict('ImageProjectCreateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ImageProjectCreateOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ImageProjectCreateOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ImageProjectCreateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ImageProjectCreateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageProjectCreateOutputVariant2RecoveryOperation = TypedDict('ImageProjectCreateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ImageProjectCreateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageProjectCreateOutputVariant2Recovery = TypedDict('ImageProjectCreateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ImageProjectCreateOutputVariant2RecoveryOperation],
})
ImageProjectCreateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageProjectCreateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ImageProjectCreateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ImageProjectCreateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ImageProjectCreateOutput).
ImageProjectCreateOutput = Union[ImageProjectCreateOutputVariant2, ImageProjectCreateOutputVariant1]

_ImageProjectCreateInputAdapter = TypeAdapter(ImageProjectCreateInput)
_ImageProjectCreateOutputAdapter = TypeAdapter(ImageProjectCreateOutput)