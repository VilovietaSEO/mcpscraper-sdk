from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserClickInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions.')
    x: Union[float, int] = Field(..., alias='x', description='X coordinate to click, in screenshot pixels. Use only coordinates from the latest browser_screenshot, browser_read, or browser_locate result; do not guess.')
    y: Union[float, int] = Field(..., alias='y', description='Y coordinate to click, in screenshot pixels. Use only coordinates from the latest browser_screenshot, browser_read, or browser_locate result; do not guess.')
    button: Union[Literal['left', 'right', 'middle'], None] = Field(None, alias='button', description='Mouse button.')
    num_clicks: Union[Annotated[int, Field(ge=1, le=3)], None] = Field(None, alias='num_clicks', description='Number of clicks, e.g. 2 for double-click.')


class BrowserClickOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: str = Field(..., alias='tool', description='Browser Agent MCP tool that produced this response.')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    result: dict[str, Any] = Field(..., alias='result', description='Provider action result. Check ok and follow with browser_screenshot/browser_read when page state matters.')
    next_recommended_tool: Union[str, None] = Field(..., alias='nextRecommendedTool', description='')


BrowserClickOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserClickOutputVariant2DeliveryArtifactsItem', {
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
BrowserClickOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserClickOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserClickOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserClickOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserClickOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserClickOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserClickOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserClickOutputVariant2Delivery = TypedDict('BrowserClickOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserClickOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserClickOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserClickOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserClickOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserClickOutputVariant2RecoveryOperation = TypedDict('BrowserClickOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserClickOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserClickOutputVariant2Recovery = TypedDict('BrowserClickOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserClickOutputVariant2RecoveryOperation],
})
BrowserClickOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserClickOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserClickOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserClickOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserClickOutput).
BrowserClickOutput = Union[BrowserClickOutputVariant1, BrowserClickOutputVariant2]

_BrowserClickInputAdapter = TypeAdapter(BrowserClickInput)
_BrowserClickOutputAdapter = TypeAdapter(BrowserClickOutput)