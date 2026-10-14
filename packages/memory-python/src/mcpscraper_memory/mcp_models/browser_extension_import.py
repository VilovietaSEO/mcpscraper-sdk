from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserExtensionImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    store_url: str = Field(..., alias='store_url', description='Chrome Web Store URL of the extension to add, e.g. https://chromewebstore.google.com/detail/<slug>/<id>.')
    name: Annotated[str, Field(min_length=1, max_length=64)] = Field(..., alias='name', description='Short name to save this extension under, e.g. "ani-ai". Reuse it later in extension_names on browser_open.')


class BrowserExtensionImportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Literal['browser_extension_import'] = Field(..., alias='tool', description='')
    session_id: None = Field(..., alias='session_id', description='')
    name: str = Field(..., alias='name', description='The name this extension was saved under.')
    source_url: str = Field(..., alias='source_url', description='The store URL this extension was imported from.')
    size_bytes: Union[Union[float, int], None] = Field(..., alias='size_bytes', description='Size of the extension package in bytes.')


BrowserExtensionImportOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserExtensionImportOutputVariant2DeliveryArtifactsItem', {
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
BrowserExtensionImportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionImportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserExtensionImportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserExtensionImportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionImportOutputVariant2Delivery = TypedDict('BrowserExtensionImportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserExtensionImportOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserExtensionImportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserExtensionImportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionImportOutputVariant2RecoveryOperation = TypedDict('BrowserExtensionImportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserExtensionImportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionImportOutputVariant2Recovery = TypedDict('BrowserExtensionImportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserExtensionImportOutputVariant2RecoveryOperation],
})
BrowserExtensionImportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserExtensionImportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserExtensionImportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserExtensionImportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserExtensionImportOutput).
BrowserExtensionImportOutput = Union[BrowserExtensionImportOutputVariant1, BrowserExtensionImportOutputVariant2]

_BrowserExtensionImportInputAdapter = TypeAdapter(BrowserExtensionImportInput)
_BrowserExtensionImportOutputAdapter = TypeAdapter(BrowserExtensionImportOutput)