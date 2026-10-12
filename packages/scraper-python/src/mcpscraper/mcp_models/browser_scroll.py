from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserScrollInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions.')
    delta_y: Union[Union[float, int], None] = Field(None, alias='delta_y', description='Vertical scroll in wheel units. Positive scrolls down, negative up.')
    delta_x: Union[Union[float, int], None] = Field(None, alias='delta_x', description='Horizontal scroll in wheel units.')
    x: Union[Union[float, int], None] = Field(None, alias='x', description='X position to scroll at. Defaults to screen center.')
    y: Union[Union[float, int], None] = Field(None, alias='y', description='Y position to scroll at. Defaults to screen center.')


class BrowserScrollOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: str = Field(..., alias='tool', description='Browser Agent MCP tool that produced this response.')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    result: dict[str, Any] = Field(..., alias='result', description='Provider action result. Check ok and follow with browser_screenshot/browser_read when page state matters.')
    next_recommended_tool: Union[str, None] = Field(..., alias='nextRecommendedTool', description='')


BrowserScrollOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserScrollOutputVariant2DeliveryArtifactsItem', {
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
BrowserScrollOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserScrollOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserScrollOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserScrollOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserScrollOutputVariant2Delivery = TypedDict('BrowserScrollOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserScrollOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserScrollOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserScrollOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserScrollOutputVariant2RecoveryOperation = TypedDict('BrowserScrollOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserScrollOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserScrollOutputVariant2Recovery = TypedDict('BrowserScrollOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserScrollOutputVariant2RecoveryOperation],
})
BrowserScrollOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserScrollOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserScrollOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserScrollOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserScrollOutput).
BrowserScrollOutput = Union[BrowserScrollOutputVariant1, BrowserScrollOutputVariant2]

_BrowserScrollInputAdapter = TypeAdapter(BrowserScrollInput)
_BrowserScrollOutputAdapter = TypeAdapter(BrowserScrollOutput)