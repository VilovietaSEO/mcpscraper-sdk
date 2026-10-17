from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserReplayStopInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions.')
    replay_id: str = Field(..., alias='replay_id', description='The replay id returned by browser_replay_start or browser_list_replays.')


class BrowserReplayStopOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: Literal['browser_replay_stop'] = Field(..., alias='tool', description='')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    replay_id: Union[str, None] = Field(..., alias='replay_id', description='Replay id when the response is scoped to a replay.')
    view_url: Union[str, None] = Field(..., alias='view_url', description='')
    download_url: Union[str, None] = Field(..., alias='download_url', description='')
    raw: Union[dict[str, Any], None] = Field(None, alias='raw', description='')


BrowserReplayStopOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserReplayStopOutputVariant2DeliveryArtifactsItem', {
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
BrowserReplayStopOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayStopOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserReplayStopOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserReplayStopOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayStopOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserReplayStopOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserReplayStopOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayStopOutputVariant2Delivery = TypedDict('BrowserReplayStopOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserReplayStopOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserReplayStopOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserReplayStopOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserReplayStopOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayStopOutputVariant2RecoveryOperation = TypedDict('BrowserReplayStopOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserReplayStopOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayStopOutputVariant2Recovery = TypedDict('BrowserReplayStopOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserReplayStopOutputVariant2RecoveryOperation],
})
BrowserReplayStopOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserReplayStopOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserReplayStopOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserReplayStopOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserReplayStopOutput).
BrowserReplayStopOutput = Union[BrowserReplayStopOutputVariant1, BrowserReplayStopOutputVariant2]

_BrowserReplayStopInputAdapter = TypeAdapter(BrowserReplayStopInput)
_BrowserReplayStopOutputAdapter = TypeAdapter(BrowserReplayStopOutput)