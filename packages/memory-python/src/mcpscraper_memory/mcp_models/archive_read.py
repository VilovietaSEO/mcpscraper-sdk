from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ArchiveReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    artifact_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='artifactId', description='Preferred: private artifactId returned by check_site_export. The server reauthorizes ownership on every read.')
    url: Union[str, None] = Field(None, alias='url', description='Fallback: bounded public HTTPS ZIP URL. Use artifactId for MCP Scraper-owned exports.')
    path: Union[Annotated[str, Field(min_length=1, max_length=2000)], None] = Field(None, alias='path', description='Exact ZIP entry path to read. Omit to list the archive. Use a path returned by a previous archive_read listing.')
    offset: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='offset', description='Byte offset for a text-file read. Continue from nextOffset until it is null. Ignored when path is omitted.')
    max_bytes: Union[Annotated[int, Field(ge=1, le=200000)], None] = Field(None, alias='maxBytes', description='Maximum UTF-8 bytes to return from the selected text file. Default 50,000; maximum 200,000.')
    max_entries: Union[Annotated[int, Field(ge=1, le=1000)], None] = Field(None, alias='maxEntries', description='Maximum entry rows returned when listing. The server still validates the complete archive. Default 200; maximum 1,000.')
    deposit_to_library: Union[bool, None] = Field(None, alias='depositToLibrary', description='Store the complete selected text file in the tenant Library vault through library-ingest. Requires path. Preserves the ZIP URL and entry path as source provenance.')


ArchiveReadOutputVariant1EntriesItem = TypedDict('ArchiveReadOutputVariant1EntriesItem', {
    'path': Required[str],
    'directory': Required[bool],
    'compressedBytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'uncompressedBytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'contentType': Required[Union[str, None]],
    'readable': Required[bool],
    'modifiedAt': Required[Union[str, None]],
})
ArchiveReadOutputVariant1EntriesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveReadOutputVariant1Memory = TypedDict('ArchiveReadOutputVariant1Memory', {
    'deposited': Required[bool],
    'vault': NotRequired[str],
    'noteId': NotRequired[str],
    'path': NotRequired[str],
    'chunks': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'error': NotRequired[str],
})
ArchiveReadOutputVariant1Memory.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ArchiveReadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    mode: Literal['list', 'read'] = Field(..., alias='mode', description='')
    archive_url: str = Field(..., alias='archiveUrl', description='Public ZIP URL or private artifactId used for this read.')
    artifact_id: Union[str, None] = Field(None, alias='artifactId', description='')
    compressed_bytes: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='compressedBytes', description='')
    entry_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='entryCount', description='')
    total_uncompressed_bytes: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='totalUncompressedBytes', description='')
    entries: Union[list[ArchiveReadOutputVariant1EntriesItem], None] = Field(None, alias='entries', description='')
    entries_truncated: Union[bool, None] = Field(None, alias='entriesTruncated', description='')
    path: Union[str, None] = Field(None, alias='path', description='')
    content_type: Union[str, None] = Field(None, alias='contentType', description='')
    file_bytes: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='fileBytes', description='')
    offset: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='offset', description='')
    content: Union[str, None] = Field(None, alias='content', description='')
    next_offset: Union[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None], None] = Field(None, alias='nextOffset', description='')
    memory: Union[ArchiveReadOutputVariant1Memory, None] = Field(None, alias='memory', description='')


ArchiveReadOutputVariant2DeliveryArtifactsItem = TypedDict('ArchiveReadOutputVariant2DeliveryArtifactsItem', {
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
ArchiveReadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveReadOutputVariant2DeliveryAvailableExportsItem = TypedDict('ArchiveReadOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ArchiveReadOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveReadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ArchiveReadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ArchiveReadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveReadOutputVariant2Delivery = TypedDict('ArchiveReadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ArchiveReadOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ArchiveReadOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ArchiveReadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ArchiveReadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveReadOutputVariant2RecoveryOperation = TypedDict('ArchiveReadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ArchiveReadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArchiveReadOutputVariant2Recovery = TypedDict('ArchiveReadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ArchiveReadOutputVariant2RecoveryOperation],
})
ArchiveReadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ArchiveReadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ArchiveReadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ArchiveReadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ArchiveReadOutput).
ArchiveReadOutput = Union[ArchiveReadOutputVariant1, ArchiveReadOutputVariant2]

_ArchiveReadInputAdapter = TypeAdapter(ArchiveReadInput)
_ArchiveReadOutputAdapter = TypeAdapter(ArchiveReadOutput)