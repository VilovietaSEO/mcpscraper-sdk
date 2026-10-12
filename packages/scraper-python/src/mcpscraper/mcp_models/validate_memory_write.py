from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


ValidateMemoryWriteInputProps = TypedDict('ValidateMemoryWriteInputProps', {
    'status': NotRequired[str],
    'summary': NotRequired[str],
    'tags': NotRequired[list[str]],
    'pinned': NotRequired[bool],
    'source_type': NotRequired[str],
    'source_ref': NotRequired[str],
    'related': NotRequired[list[str]],
    'related_vault_notes': NotRequired[list[str]],
    'embed': NotRequired[bool],
    'embed_priority': NotRequired[Literal['low', 'normal', 'high']],
    'embedding_summary': NotRequired[str],
    'type': NotRequired[str],
    'domain': NotRequired[str],
    'folder': NotRequired[str],
    'script_links': NotRequired[list[str]],
    'reference_links': NotRequired[list[str]],
    'template_links': NotRequired[list[str]],
    'parentMessageId': NotRequired[str],
})
ValidateMemoryWriteInputProps.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class ValidateMemoryWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: str = Field(..., alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    title: str = Field(..., alias='title', description='Human-readable title for the proposed record or authored content.')
    content: str = Field(..., alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    props: ValidateMemoryWriteInputProps = Field(..., alias='props', description='Complete governed note properties required by the target vault contract.')


class ValidateMemoryWriteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    valid: Union[bool, None] = Field(None, alias='valid', description='')
    errors: Union[list[str], None] = Field(None, alias='errors', description='')
    warnings: Union[list[str], None] = Field(None, alias='warnings', description='')
    normalized_tags: Union[list[str], None] = Field(None, alias='normalizedTags', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ValidateMemoryWriteOutputVariant2DeliveryArtifactsItem = TypedDict('ValidateMemoryWriteOutputVariant2DeliveryArtifactsItem', {
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
ValidateMemoryWriteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ValidateMemoryWriteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ValidateMemoryWriteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ValidateMemoryWriteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ValidateMemoryWriteOutputVariant2Delivery = TypedDict('ValidateMemoryWriteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ValidateMemoryWriteOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ValidateMemoryWriteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ValidateMemoryWriteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ValidateMemoryWriteOutputVariant2RecoveryOperation = TypedDict('ValidateMemoryWriteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ValidateMemoryWriteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ValidateMemoryWriteOutputVariant2Recovery = TypedDict('ValidateMemoryWriteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ValidateMemoryWriteOutputVariant2RecoveryOperation],
})
ValidateMemoryWriteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ValidateMemoryWriteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ValidateMemoryWriteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ValidateMemoryWriteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ValidateMemoryWriteOutput).
ValidateMemoryWriteOutput = Union[ValidateMemoryWriteOutputVariant2, ValidateMemoryWriteOutputVariant1]

_ValidateMemoryWriteInputAdapter = TypeAdapter(ValidateMemoryWriteInput)
_ValidateMemoryWriteOutputAdapter = TypeAdapter(ValidateMemoryWriteOutput)