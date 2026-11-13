from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MemoryUploadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to upload into. Optional; defaults to the session active vault, then the first vault the caller is entitled to.')
    path: Annotated[str, Field(min_length=1)] = Field(..., alias='path', description='Vault-relative path to store the document at, e.g. docs/handbook. Writing an existing path replaces it.')
    content: Annotated[str, Field(min_length=1)] = Field(..., alias='content', description='Full text content of the file/document to store and index. Must be non-empty.')
    title: Union[str, None] = Field(None, alias='title', description='Optional human-readable title; defaults to the path when omitted.')
    source: Union[str, None] = Field(None, alias='source', description='Optional origin tag recorded with the note (e.g. a filename or URL); defaults to "upload".')


class MemoryUploadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the document was stored and indexed; false on auth/scope error.')
    path: Union[str, None] = Field(None, alias='path', description='Vault-relative path the document was stored at.')
    indexed: Union[Union[float, int], None] = Field(None, alias='indexed', description='Number of search chunks indexed for the content.')
    code: Union[str, None] = Field(None, alias='code', description='Machine-readable denial code when ok is false: quota_exceeded or free_cost_cap.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


MemoryUploadOutputVariant2DeliveryArtifactsItem = TypedDict('MemoryUploadOutputVariant2DeliveryArtifactsItem', {
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
MemoryUploadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryUploadOutputVariant2DeliveryAvailableExportsItem = TypedDict('MemoryUploadOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
MemoryUploadOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryUploadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemoryUploadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemoryUploadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryUploadOutputVariant2Delivery = TypedDict('MemoryUploadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemoryUploadOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[MemoryUploadOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemoryUploadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemoryUploadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryUploadOutputVariant2RecoveryOperation = TypedDict('MemoryUploadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemoryUploadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryUploadOutputVariant2Recovery = TypedDict('MemoryUploadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemoryUploadOutputVariant2RecoveryOperation],
})
MemoryUploadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryUploadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemoryUploadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemoryUploadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemoryUploadOutput).
MemoryUploadOutput = Union[MemoryUploadOutputVariant2, MemoryUploadOutputVariant1]

_MemoryUploadInputAdapter = TypeAdapter(MemoryUploadInput)
_MemoryUploadOutputAdapter = TypeAdapter(MemoryUploadOutput)