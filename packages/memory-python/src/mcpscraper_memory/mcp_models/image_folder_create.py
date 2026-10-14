from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ImageFolderCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    project_id: Annotated[str, Field(min_length=1)] = Field(..., alias='projectId', description='Opaque image project identifier returned by an image project tool.')
    parent_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='parentId', description='Parent image folder identifier; omit to create the folder at the project root.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')


ImageFolderCreateOutputVariant1Folder = TypedDict('ImageFolderCreateOutputVariant1Folder', {
    'id': Required[str],
    'projectId': Required[str],
    'parentId': Required[Union[str, None]],
    'name': Required[str],
    'depth': Required[Union[float, int]],
    'createdAt': Required[str],
})
ImageFolderCreateOutputVariant1Folder.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageFolderCreateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    folder: Union[ImageFolderCreateOutputVariant1Folder, None] = Field(None, alias='folder', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ImageFolderCreateOutputVariant2DeliveryArtifactsItem = TypedDict('ImageFolderCreateOutputVariant2DeliveryArtifactsItem', {
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
ImageFolderCreateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageFolderCreateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ImageFolderCreateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ImageFolderCreateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageFolderCreateOutputVariant2Delivery = TypedDict('ImageFolderCreateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ImageFolderCreateOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ImageFolderCreateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ImageFolderCreateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageFolderCreateOutputVariant2RecoveryOperation = TypedDict('ImageFolderCreateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ImageFolderCreateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageFolderCreateOutputVariant2Recovery = TypedDict('ImageFolderCreateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ImageFolderCreateOutputVariant2RecoveryOperation],
})
ImageFolderCreateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageFolderCreateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ImageFolderCreateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ImageFolderCreateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ImageFolderCreateOutput).
ImageFolderCreateOutput = Union[ImageFolderCreateOutputVariant2, ImageFolderCreateOutputVariant1]

_ImageFolderCreateInputAdapter = TypeAdapter(ImageFolderCreateInput)
_ImageFolderCreateOutputAdapter = TypeAdapter(ImageFolderCreateOutput)