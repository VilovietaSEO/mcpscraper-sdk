from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserExtensionDeleteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    name: Annotated[str, Field(min_length=1)] = Field(..., alias='name', description='Name of the extension to remove, as returned by browser_extension_list.')


class BrowserExtensionDeleteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Literal['browser_extension_delete'] = Field(..., alias='tool', description='')
    session_id: None = Field(..., alias='session_id', description='')
    name: str = Field(..., alias='name', description='')
    deleted: bool = Field(..., alias='deleted', description='')


BrowserExtensionDeleteOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserExtensionDeleteOutputVariant2DeliveryArtifactsItem', {
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
BrowserExtensionDeleteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionDeleteOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserExtensionDeleteOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserExtensionDeleteOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionDeleteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserExtensionDeleteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserExtensionDeleteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionDeleteOutputVariant2Delivery = TypedDict('BrowserExtensionDeleteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserExtensionDeleteOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserExtensionDeleteOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserExtensionDeleteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserExtensionDeleteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionDeleteOutputVariant2RecoveryOperation = TypedDict('BrowserExtensionDeleteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserExtensionDeleteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserExtensionDeleteOutputVariant2Recovery = TypedDict('BrowserExtensionDeleteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserExtensionDeleteOutputVariant2RecoveryOperation],
})
BrowserExtensionDeleteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserExtensionDeleteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserExtensionDeleteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserExtensionDeleteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserExtensionDeleteOutput).
BrowserExtensionDeleteOutput = Union[BrowserExtensionDeleteOutputVariant1, BrowserExtensionDeleteOutputVariant2]

_BrowserExtensionDeleteInputAdapter = TypeAdapter(BrowserExtensionDeleteInput)
_BrowserExtensionDeleteOutputAdapter = TypeAdapter(BrowserExtensionDeleteOutput)