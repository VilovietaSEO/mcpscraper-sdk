from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class BrowserReplayDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions.')
    replay_id: str = Field(..., alias='replay_id', description='The replay id returned by browser_replay_start or browser_list_replays.')
    filename: Union[str, None] = Field(None, alias='filename', description='Optional local MP4 filename. Defaults to a timestamped replay filename.')


class BrowserReplayDownloadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: Literal['browser_replay_download'] = Field(..., alias='tool', description='')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    replay_id: Union[str, None] = Field(..., alias='replay_id', description='Replay id when the response is scoped to a replay.')
    file_path: Union[str, None] = Field(..., alias='file_path', description='')
    bytes: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='bytes', description='')
    mime_type: Union[str, None] = Field(..., alias='mime_type', description='')
    download_url: Union[str, None] = Field(..., alias='download_url', description='')


BrowserReplayDownloadOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserReplayDownloadOutputVariant2DeliveryArtifactsItem', {
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
BrowserReplayDownloadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayDownloadOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserReplayDownloadOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserReplayDownloadOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayDownloadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserReplayDownloadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserReplayDownloadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayDownloadOutputVariant2Delivery = TypedDict('BrowserReplayDownloadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserReplayDownloadOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserReplayDownloadOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserReplayDownloadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserReplayDownloadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayDownloadOutputVariant2RecoveryOperation = TypedDict('BrowserReplayDownloadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserReplayDownloadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayDownloadOutputVariant2Recovery = TypedDict('BrowserReplayDownloadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserReplayDownloadOutputVariant2RecoveryOperation],
})
BrowserReplayDownloadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserReplayDownloadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserReplayDownloadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserReplayDownloadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserReplayDownloadOutput).
BrowserReplayDownloadOutput = Union[BrowserReplayDownloadOutputVariant1, BrowserReplayDownloadOutputVariant2]

_BrowserReplayDownloadInputAdapter = TypeAdapter(BrowserReplayDownloadInput)
_BrowserReplayDownloadOutputAdapter = TypeAdapter(BrowserReplayDownloadOutput)