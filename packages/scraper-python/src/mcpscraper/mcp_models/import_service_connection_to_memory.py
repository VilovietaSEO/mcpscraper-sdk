from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ImportServiceConnectionToMemoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='connectionId', description='A tenant-owned connectionId from list_service_connections.')
    provider_config_key: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='providerConfigKey', description='The exact providerConfigKey returned with that connection. It is matched together with connectionId against the authenticated caller.')
    tool: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='tool', description='One exact current readTools entry for that connection. Actions, admin tools, and unlisted names are rejected.')
    args: Union[dict[str, Any], None] = Field(None, alias='args', description='JSON arguments for one bounded provider read. The serialized object may be at most 64 KiB.')
    vault: Annotated[str, Field(min_length=1, max_length=100)] = Field(..., alias='vault', description='An existing ordinary Memory vault the caller can write and index. Secure and channel vaults are rejected because this tool creates searchable RAG content.')
    title: Union[Annotated[str, Field(min_length=1, max_length=200)], None] = Field(None, alias='title', description='Optional human-readable snapshot title. The server always chooses the stable storage path.')


class ImportServiceConnectionToMemoryOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    stored: Union[bool, None] = Field(None, alias='stored', description='')
    status: Union[Literal['search_ready', 'stored_not_indexed'], None] = Field(None, alias='status', description='')
    search_ready: Union[bool, None] = Field(None, alias='searchReady', description='')
    provider_config_key: Union[str, None] = Field(None, alias='providerConfigKey', description='')
    connection_id: Union[str, None] = Field(None, alias='connectionId', description='')
    tool: Union[str, None] = Field(None, alias='tool', description='')
    vault: Union[str, None] = Field(None, alias='vault', description='')
    path: Union[str, None] = Field(None, alias='path', description='')
    source_bytes: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='sourceBytes', description='')
    content_sha256: Union[str, None] = Field(None, alias='contentSha256', description='')
    indexed_chunks: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='indexedChunks', description='')
    imported_at: Union[str, None] = Field(None, alias='importedAt', description='')
    untrusted_content: Union[Literal[True], None] = Field(None, alias='untrustedContent', description='')
    warning: Union[str, None] = Field(None, alias='warning', description='')
    error_code: Union[str, None] = Field(None, alias='errorCode', description='')
    retryable: Union[bool, None] = Field(None, alias='retryable', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


ImportServiceConnectionToMemoryOutputVariant2DeliveryArtifactsItem = TypedDict('ImportServiceConnectionToMemoryOutputVariant2DeliveryArtifactsItem', {
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
ImportServiceConnectionToMemoryOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImportServiceConnectionToMemoryOutputVariant2DeliveryAvailableExportsItem = TypedDict('ImportServiceConnectionToMemoryOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ImportServiceConnectionToMemoryOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImportServiceConnectionToMemoryOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ImportServiceConnectionToMemoryOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ImportServiceConnectionToMemoryOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImportServiceConnectionToMemoryOutputVariant2Delivery = TypedDict('ImportServiceConnectionToMemoryOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ImportServiceConnectionToMemoryOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ImportServiceConnectionToMemoryOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ImportServiceConnectionToMemoryOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ImportServiceConnectionToMemoryOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImportServiceConnectionToMemoryOutputVariant2RecoveryOperation = TypedDict('ImportServiceConnectionToMemoryOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ImportServiceConnectionToMemoryOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImportServiceConnectionToMemoryOutputVariant2Recovery = TypedDict('ImportServiceConnectionToMemoryOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ImportServiceConnectionToMemoryOutputVariant2RecoveryOperation],
})
ImportServiceConnectionToMemoryOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImportServiceConnectionToMemoryOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ImportServiceConnectionToMemoryOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ImportServiceConnectionToMemoryOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ImportServiceConnectionToMemoryOutput).
ImportServiceConnectionToMemoryOutput = Union[ImportServiceConnectionToMemoryOutputVariant2, ImportServiceConnectionToMemoryOutputVariant1]

_ImportServiceConnectionToMemoryInputAdapter = TypeAdapter(ImportServiceConnectionToMemoryInput)
_ImportServiceConnectionToMemoryOutputAdapter = TypeAdapter(ImportServiceConnectionToMemoryOutput)