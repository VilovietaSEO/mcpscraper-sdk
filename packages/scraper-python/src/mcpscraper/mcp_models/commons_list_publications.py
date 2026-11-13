from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsListPublicationsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum number of owned publications to return.')
    after: Union[Annotated[str, Field(max_length=50)], None] = Field(None, alias='after', description='nextCursor from the preceding page; omit for the first page.')


CommonsListPublicationsOutputVariant1DataPublicationsItem = TypedDict('CommonsListPublicationsOutputVariant1DataPublicationsItem', {
    'id': Required[str],
    'ownerUserId': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'subdomain': Required[str],
    'title': Required[str],
    'description': Required[str],
    'revision': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'latestEditionId': Required[Union[str, None]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
    'publicUrl': Required[str],
    'archiveUrl': Required[str],
})
CommonsListPublicationsOutputVariant1DataPublicationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListPublicationsOutputVariant1Data = TypedDict('CommonsListPublicationsOutputVariant1Data', {
    'publications': Required[Annotated[list[CommonsListPublicationsOutputVariant1DataPublicationsItem], Field(max_length=100)]],
    'nextCursor': Required[Union[str, None]],
})
CommonsListPublicationsOutputVariant1Data.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsListPublicationsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[CommonsListPublicationsOutputVariant1Data, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsListPublicationsOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsListPublicationsOutputVariant2DeliveryArtifactsItem', {
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
CommonsListPublicationsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListPublicationsOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsListPublicationsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsListPublicationsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListPublicationsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsListPublicationsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsListPublicationsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListPublicationsOutputVariant2Delivery = TypedDict('CommonsListPublicationsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsListPublicationsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsListPublicationsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsListPublicationsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsListPublicationsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListPublicationsOutputVariant2RecoveryOperation = TypedDict('CommonsListPublicationsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsListPublicationsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListPublicationsOutputVariant2Recovery = TypedDict('CommonsListPublicationsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsListPublicationsOutputVariant2RecoveryOperation],
})
CommonsListPublicationsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsListPublicationsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsListPublicationsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsListPublicationsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsListPublicationsOutput).
CommonsListPublicationsOutput = Union[CommonsListPublicationsOutputVariant2, CommonsListPublicationsOutputVariant1]

_CommonsListPublicationsInputAdapter = TypeAdapter(CommonsListPublicationsInput)
_CommonsListPublicationsOutputAdapter = TypeAdapter(CommonsListPublicationsOutput)