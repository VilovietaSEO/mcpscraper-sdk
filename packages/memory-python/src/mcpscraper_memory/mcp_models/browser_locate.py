from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


BrowserLocateInputTargetsItem = TypedDict('BrowserLocateInputTargetsItem', {
    'name': NotRequired[str],
    'selector': NotRequired[str],
    'text': NotRequired[str],
    'match': NotRequired[Literal['contains', 'exact']],
    'index': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
BrowserLocateInputTargetsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class BrowserLocateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions.')
    targets: Annotated[list[BrowserLocateInputTargetsItem], Field(min_length=1, max_length=20)] = Field(..., alias='targets', description='DOM targets to locate in the current viewport. Use selectors for exact elements, or text for visible text ranges.')


class BrowserLocateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: Literal['browser_locate'] = Field(..., alias='tool', description='')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    url: Union[str, None] = Field(..., alias='url', description='')
    title: Union[str, None] = Field(..., alias='title', description='')
    viewport: Union[dict[str, Any], None] = Field(..., alias='viewport', description='')
    replay: Union[dict[str, Any], None] = Field(..., alias='replay', description='')
    targets: list[dict[str, Any]] = Field(..., alias='targets', description='')
    raw: Union[dict[str, Any], None] = Field(None, alias='raw', description='')


BrowserLocateOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserLocateOutputVariant2DeliveryArtifactsItem', {
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
BrowserLocateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserLocateOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserLocateOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserLocateOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserLocateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserLocateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserLocateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserLocateOutputVariant2Delivery = TypedDict('BrowserLocateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserLocateOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserLocateOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserLocateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserLocateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserLocateOutputVariant2RecoveryOperation = TypedDict('BrowserLocateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserLocateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserLocateOutputVariant2Recovery = TypedDict('BrowserLocateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserLocateOutputVariant2RecoveryOperation],
})
BrowserLocateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserLocateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserLocateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserLocateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserLocateOutput).
BrowserLocateOutput = Union[BrowserLocateOutputVariant1, BrowserLocateOutputVariant2]

_BrowserLocateInputAdapter = TypeAdapter(BrowserLocateInput)
_BrowserLocateOutputAdapter = TypeAdapter(BrowserLocateOutput)