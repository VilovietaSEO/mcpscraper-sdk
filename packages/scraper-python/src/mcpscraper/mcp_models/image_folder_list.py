from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ImageFolderListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    project_id: Annotated[str, Field(min_length=1)] = Field(..., alias='projectId', description='Opaque image project identifier returned by an image project tool.')


ImageFolderListOutputVariant1FoldersItem = TypedDict('ImageFolderListOutputVariant1FoldersItem', {
    'id': Required[str],
    'projectId': Required[str],
    'parentId': Required[Union[str, None]],
    'name': Required[str],
    'depth': Required[Union[float, int]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
ImageFolderListOutputVariant1FoldersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageFolderListOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    folders: Union[list[ImageFolderListOutputVariant1FoldersItem], None] = Field(None, alias='folders', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ImageFolderListOutputVariant2DeliveryArtifactsItem = TypedDict('ImageFolderListOutputVariant2DeliveryArtifactsItem', {
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
ImageFolderListOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageFolderListOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ImageFolderListOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ImageFolderListOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageFolderListOutputVariant2Delivery = TypedDict('ImageFolderListOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ImageFolderListOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ImageFolderListOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ImageFolderListOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageFolderListOutputVariant2RecoveryOperation = TypedDict('ImageFolderListOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ImageFolderListOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageFolderListOutputVariant2Recovery = TypedDict('ImageFolderListOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ImageFolderListOutputVariant2RecoveryOperation],
})
ImageFolderListOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageFolderListOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ImageFolderListOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ImageFolderListOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ImageFolderListOutput).
ImageFolderListOutput = Union[ImageFolderListOutputVariant2, ImageFolderListOutputVariant1]

_ImageFolderListInputAdapter = TypeAdapter(ImageFolderListInput)
_ImageFolderListOutputAdapter = TypeAdapter(ImageFolderListOutput)