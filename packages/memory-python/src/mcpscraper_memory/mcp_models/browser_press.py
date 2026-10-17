from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserPressInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions.')
    keys: Annotated[list[str], Field(min_length=1)] = Field(..., alias='keys', description='Keys or combinations to press, e.g. ["Return"], ["Ctrl+a"], ["Ctrl+Shift+Tab"].')


class BrowserPressOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: str = Field(..., alias='tool', description='Browser Agent MCP tool that produced this response.')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    result: dict[str, Any] = Field(..., alias='result', description='Provider action result. Check ok and follow with browser_screenshot/browser_read when page state matters.')
    next_recommended_tool: Union[str, None] = Field(..., alias='nextRecommendedTool', description='')


BrowserPressOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserPressOutputVariant2DeliveryArtifactsItem', {
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
BrowserPressOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserPressOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserPressOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserPressOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserPressOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserPressOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserPressOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserPressOutputVariant2Delivery = TypedDict('BrowserPressOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserPressOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserPressOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserPressOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserPressOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserPressOutputVariant2RecoveryOperation = TypedDict('BrowserPressOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserPressOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserPressOutputVariant2Recovery = TypedDict('BrowserPressOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserPressOutputVariant2RecoveryOperation],
})
BrowserPressOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserPressOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserPressOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserPressOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserPressOutput).
BrowserPressOutput = Union[BrowserPressOutputVariant1, BrowserPressOutputVariant2]

_BrowserPressInputAdapter = TypeAdapter(BrowserPressInput)
_BrowserPressOutputAdapter = TypeAdapter(BrowserPressOutput)