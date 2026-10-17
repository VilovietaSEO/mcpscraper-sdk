from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


BrowserReplayAnnotateInputAnnotationsItem = TypedDict('BrowserReplayAnnotateInputAnnotationsItem', {
    'type': NotRequired[Literal['box', 'circle', 'underline', 'arrow', 'label']],
    'start_seconds': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'end_seconds': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
    'left': NotRequired[Union[float, int]],
    'top': NotRequired[Union[float, int]],
    'width': NotRequired[Annotated[Union[float, int], Field(gt=0)]],
    'height': NotRequired[Annotated[Union[float, int], Field(gt=0)]],
    'x': NotRequired[Union[float, int]],
    'y': NotRequired[Union[float, int]],
    'from_x': NotRequired[Union[float, int]],
    'from_y': NotRequired[Union[float, int]],
    'to_x': NotRequired[Union[float, int]],
    'to_y': NotRequired[Union[float, int]],
    'label': NotRequired[Annotated[str, Field(max_length=120)]],
    'color': NotRequired[str],
    'thickness': NotRequired[Annotated[Union[float, int], Field(ge=1, le=24)]],
})
BrowserReplayAnnotateInputAnnotationsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class BrowserReplayAnnotateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions.')
    replay_id: str = Field(..., alias='replay_id', description='The replay id returned by browser_replay_start or browser_list_replays.')
    annotations: Annotated[list[BrowserReplayAnnotateInputAnnotationsItem], Field(min_length=1, max_length=50)] = Field(..., alias='annotations', description='Timed overlay annotations. Prefer ones from browser_replay_mark; otherwise use exact DOM bounds from browser_locate.')
    filename: Union[str, None] = Field(None, alias='filename', description='Optional output MP4 filename. Defaults to a timestamped filename.')
    source_width: Union[Annotated[Union[float, int], Field(gt=0)], None] = Field(None, alias='source_width', description='Width of the screenshot coordinate space used for annotations. Defaults to the replay video width.')
    source_height: Union[Annotated[Union[float, int], Field(gt=0)], None] = Field(None, alias='source_height', description='Height of the annotation coordinate space; if smaller than the replay video height, the browser chrome offset is inferred.')
    source_left_offset: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(None, alias='source_left_offset', description='Explicit X offset from annotation to replay video coordinates. Usually omitted.')
    source_top_offset: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(None, alias='source_top_offset', description='Explicit Y offset from annotation to replay video coordinates. Usually omitted.')


class BrowserReplayAnnotateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: Literal['browser_replay_annotate'] = Field(..., alias='tool', description='')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    replay_id: Union[str, None] = Field(..., alias='replay_id', description='Replay id when the response is scoped to a replay.')
    source_file_path: Union[str, None] = Field(..., alias='source_file_path', description='')
    annotated_file_path: Union[str, None] = Field(..., alias='annotated_file_path', description='')
    bytes: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='bytes', description='')
    width: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='width', description='')
    height: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='height', description='')
    annotation_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='annotation_count', description='')
    mime_type: Union[str, None] = Field(..., alias='mime_type', description='')


BrowserReplayAnnotateOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserReplayAnnotateOutputVariant2DeliveryArtifactsItem', {
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
BrowserReplayAnnotateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayAnnotateOutputVariant2DeliveryAvailableExportsItem = TypedDict('BrowserReplayAnnotateOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BrowserReplayAnnotateOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayAnnotateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserReplayAnnotateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserReplayAnnotateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayAnnotateOutputVariant2Delivery = TypedDict('BrowserReplayAnnotateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserReplayAnnotateOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BrowserReplayAnnotateOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserReplayAnnotateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserReplayAnnotateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayAnnotateOutputVariant2RecoveryOperation = TypedDict('BrowserReplayAnnotateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserReplayAnnotateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayAnnotateOutputVariant2Recovery = TypedDict('BrowserReplayAnnotateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserReplayAnnotateOutputVariant2RecoveryOperation],
})
BrowserReplayAnnotateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserReplayAnnotateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserReplayAnnotateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserReplayAnnotateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserReplayAnnotateOutput).
BrowserReplayAnnotateOutput = Union[BrowserReplayAnnotateOutputVariant1, BrowserReplayAnnotateOutputVariant2]

_BrowserReplayAnnotateInputAdapter = TypeAdapter(BrowserReplayAnnotateInput)
_BrowserReplayAnnotateOutputAdapter = TypeAdapter(BrowserReplayAnnotateOutput)