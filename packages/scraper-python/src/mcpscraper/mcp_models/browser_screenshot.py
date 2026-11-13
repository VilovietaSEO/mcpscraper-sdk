from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserScreenshotInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions.')


BrowserScreenshotOutputVariant1ScreenshotVariant1 = TypedDict('BrowserScreenshotOutputVariant1ScreenshotVariant1', {
    'mime_type': Required[str],
    'inline': Required[bool],
})
BrowserScreenshotOutputVariant1ScreenshotVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserScreenshotOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: Literal['browser_screenshot'] = Field(..., alias='tool', description='')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    url: Union[str, None] = Field(..., alias='url', description='')
    title: Union[str, None] = Field(..., alias='title', description='')
    text: str = Field(..., alias='text', description='')
    elements: list[dict[str, Any]] = Field(..., alias='elements', description='')
    screenshot: Union[BrowserScreenshotOutputVariant1ScreenshotVariant1, None] = Field(..., alias='screenshot', description='')


BrowserScreenshotOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserScreenshotOutputVariant2DeliveryArtifactsItem', {
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
BrowserScreenshotOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserScreenshotOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserScreenshotOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserScreenshotOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserScreenshotOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserScreenshotOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserScreenshotOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserScreenshotOutputVariant2Delivery = TypedDict('BrowserScreenshotOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserScreenshotOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserScreenshotOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserScreenshotOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserScreenshotOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserScreenshotOutputVariant2RecoveryOperation = TypedDict('BrowserScreenshotOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserScreenshotOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserScreenshotOutputVariant2Recovery = TypedDict('BrowserScreenshotOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserScreenshotOutputVariant2RecoveryOperation],
})
BrowserScreenshotOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserScreenshotOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserScreenshotOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserScreenshotOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserScreenshotOutput).
BrowserScreenshotOutput = Union[BrowserScreenshotOutputVariant1, BrowserScreenshotOutputVariant2]

_BrowserScreenshotInputAdapter = TypeAdapter(BrowserScreenshotInput)
_BrowserScreenshotOutputAdapter = TypeAdapter(BrowserScreenshotOutput)