from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


BrowserReplayMarkInputTarget = TypedDict('BrowserReplayMarkInputTarget', {
    'name': NotRequired[str],
    'selector': NotRequired[str],
    'text': NotRequired[str],
    'match': NotRequired[Literal['contains', 'exact']],
    'index': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
BrowserReplayMarkInputTarget.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class BrowserReplayMarkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    session_id: str = Field(..., alias='session_id', description='The session id returned by browser_open or browser_list_sessions. A replay must already be recording.')
    target: BrowserReplayMarkInputTarget = Field(..., alias='target', description='The exact DOM element or text range to mark in the current viewport.')
    type: Union[Literal['box', 'circle', 'underline', 'arrow'], None] = Field(None, alias='type', description='Annotation style to generate.')
    label: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='label', description='Optional callout text to render near the target.')
    color: Union[str, None] = Field(None, alias='color', description='Annotation color as hex, e.g. #ff3b30.')
    thickness: Union[Annotated[Union[float, int], Field(ge=1, le=24)], None] = Field(None, alias='thickness', description='Stroke thickness in pixels. Defaults to 5.')
    padding: Union[Annotated[Union[float, int], Field(ge=0, le=80)], None] = Field(None, alias='padding', description='Pixels to expand the DOM bounds so the highlight does not touch the text edge.')
    start_offset_seconds: Union[Annotated[Union[float, int], Field(ge=-5, le=10)], None] = Field(None, alias='start_offset_seconds', description='Offset from the current replay time; negative appears just before the mark action.')
    duration_seconds: Union[Annotated[Union[float, int], Field(ge=0.5, le=30)], None] = Field(None, alias='duration_seconds', description='How long the annotation should remain visible.')


class BrowserReplayMarkOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='Whether the browser-agent action succeeded.')
    tool: Literal['browser_replay_mark'] = Field(..., alias='tool', description='')
    session_id: Union[str, None] = Field(..., alias='session_id', description='Browser session id when the response is scoped to a session.')
    replay_id: Union[str, None] = Field(..., alias='replay_id', description='Replay id when the response is scoped to a replay.')
    annotation: dict[str, Any] = Field(..., alias='annotation', description='')
    source_width: Union[Union[float, int], None] = Field(..., alias='source_width', description='')
    source_height: Union[Union[float, int], None] = Field(..., alias='source_height', description='')
    target: Union[dict[str, Any], None] = Field(..., alias='target', description='')
    hint: str = Field(..., alias='hint', description='')


BrowserReplayMarkOutputVariant2DeliveryArtifactsItem = TypedDict('BrowserReplayMarkOutputVariant2DeliveryArtifactsItem', {
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
BrowserReplayMarkOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayMarkOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BrowserReplayMarkOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BrowserReplayMarkOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayMarkOutputVariant2Delivery = TypedDict('BrowserReplayMarkOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BrowserReplayMarkOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BrowserReplayMarkOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BrowserReplayMarkOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayMarkOutputVariant2RecoveryOperation = TypedDict('BrowserReplayMarkOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BrowserReplayMarkOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BrowserReplayMarkOutputVariant2Recovery = TypedDict('BrowserReplayMarkOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BrowserReplayMarkOutputVariant2RecoveryOperation],
})
BrowserReplayMarkOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BrowserReplayMarkOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BrowserReplayMarkOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BrowserReplayMarkOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BrowserReplayMarkOutput).
BrowserReplayMarkOutput = Union[BrowserReplayMarkOutputVariant1, BrowserReplayMarkOutputVariant2]

_BrowserReplayMarkInputAdapter = TypeAdapter(BrowserReplayMarkInput)
_BrowserReplayMarkOutputAdapter = TypeAdapter(BrowserReplayMarkOutput)