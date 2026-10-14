from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserExtensionListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



BrowserExtensionListOutputVariant1ExtensionsItem = TypedDict('BrowserExtensionListOutputVariant1ExtensionsItem', {
    'name': Required[str],
    'source': Required[str],
    'source_url': Required[Union[str, None]],
    'size_bytes': Required[Union[Union[float, int], None]],
    'created_at': Required[str],
})
BrowserExtensionListOutputVariant1ExtensionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserExtensionListOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Literal['browser_extension_list'] = Field(..., alias='tool', description='')
    session_id: None = Field(..., alias='session_id', description='')
    extensions: list[BrowserExtensionListOutputVariant1ExtensionsItem] = Field(..., alias='extensions', description='Every extension available to load via extension_names on browser_open.')
    count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='count', description='')


BrowserExtensionListOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserExtensionListOutputVariant2DeliveryArtifactsItem', {
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
BrowserExtensionListOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionListOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserExtensionListOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserExtensionListOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionListOutputVariant2Delivery = TypedDict('BrowserExtensionListOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserExtensionListOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserExtensionListOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserExtensionListOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionListOutputVariant2RecoveryOperation = TypedDict('BrowserExtensionListOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserExtensionListOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionListOutputVariant2Recovery = TypedDict('BrowserExtensionListOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserExtensionListOutputVariant2RecoveryOperation],
})
BrowserExtensionListOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserExtensionListOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserExtensionListOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserExtensionListOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserExtensionListOutput).
BrowserExtensionListOutput = Union[BrowserExtensionListOutputVariant1, BrowserExtensionListOutputVariant2]

_BrowserExtensionListInputAdapter = TypeAdapter(BrowserExtensionListInput)
_BrowserExtensionListOutputAdapter = TypeAdapter(BrowserExtensionListOutput)