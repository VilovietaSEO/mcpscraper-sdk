from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class InstagramMediaDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: str = Field(..., alias='url', description='Instagram post, reel, or tv URL, e.g. https://www.instagram.com/reel/SHORTCODE/.')
    profile: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='profile', description='Optional saved hosted browser profile name for authenticated Instagram access.')
    save_profile_changes: Union[bool, None] = Field(None, alias='saveProfileChanges', description='Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved login.')
    media_types: Union[list[Literal['image', 'video', 'audio']], None] = Field(None, alias='mediaTypes', description='Which media types to download when downloadMedia is true.')
    download_media: Union[bool, None] = Field(None, alias='downloadMedia', description='Download extracted text/media files to the output directory. Media URLs are always returned even when false.')
    download_all_tracks: Union[bool, None] = Field(None, alias='downloadAllTracks', description='Download every captured MP4 track instead of only the best video/audio pair.')
    include_transcript: Union[bool, None] = Field(None, alias='includeTranscript', description='Transcribe the selected audio track. Adds transcription cost and time.')
    mux: Union[bool, None] = Field(None, alias='mux', description='Mux separately downloaded video/audio tracks into one MP4 if ffmpeg is available.')


InstagramMediaDownloadOutputVariant1Browser = TypedDict('InstagramMediaDownloadOutputVariant1Browser', {
    'mode': Required[Literal['hosted']],
    'requestedMode': Required[Literal['hosted']],
    'profileName': Required[Union[str, None]],
    'profileSource': Required[Literal['hosted']],
    'profileDirConfigured': Required[bool],
    'executablePathConfigured': Required[bool],
})
InstagramMediaDownloadOutputVariant1Browser.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant1SelectedVideoTrackVariant1 = TypedDict('InstagramMediaDownloadOutputVariant1SelectedVideoTrackVariant1', {
    'url': Required[str],
    'streamType': Required[Literal['video', 'audio', 'unknown']],
    'bitrate': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'durationSec': Required[Union[Union[float, int], None]],
    'vencodeTag': Required[Union[str, None]],
    'width': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'height': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
})
InstagramMediaDownloadOutputVariant1SelectedVideoTrackVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant1SelectedAudioTrackVariant1 = TypedDict('InstagramMediaDownloadOutputVariant1SelectedAudioTrackVariant1', {
    'url': Required[str],
    'streamType': Required[Literal['video', 'audio', 'unknown']],
    'bitrate': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'durationSec': Required[Union[Union[float, int], None]],
    'vencodeTag': Required[Union[str, None]],
    'width': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'height': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
})
InstagramMediaDownloadOutputVariant1SelectedAudioTrackVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant1DownloadsItem = TypedDict('InstagramMediaDownloadOutputVariant1DownloadsItem', {
    'kind': Required[Literal['text', 'image', 'video', 'audio', 'muxed_video']],
    'url': Required[Union[str, None]],
    'savedPath': Required[Union[str, None]],
    'sizeBytes': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'mimeType': Required[Union[str, None]],
    'error': Required[Union[str, None]],
})
InstagramMediaDownloadOutputVariant1DownloadsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant1TranscriptVariant1ChunksItem = TypedDict('InstagramMediaDownloadOutputVariant1TranscriptVariant1ChunksItem', {
    'startSec': Required[Union[float, int]],
    'endSec': Required[Union[float, int]],
    'text': Required[str],
})
InstagramMediaDownloadOutputVariant1TranscriptVariant1ChunksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant1TranscriptVariant1 = TypedDict('InstagramMediaDownloadOutputVariant1TranscriptVariant1', {
    'wordCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'chunkCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'durationMs': Required[Union[Union[float, int], None]],
    'transcriptText': Required[str],
    'chunks': Required[list[InstagramMediaDownloadOutputVariant1TranscriptVariant1ChunksItem]],
})
InstagramMediaDownloadOutputVariant1TranscriptVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class InstagramMediaDownloadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    source_url: str = Field(..., alias='sourceUrl', description='')
    page_url: str = Field(..., alias='pageUrl', description='')
    browser: InstagramMediaDownloadOutputVariant1Browser = Field(..., alias='browser', description='')
    type: Union[Literal['post', 'reel', 'tv'], None] = Field(..., alias='type', description='')
    shortcode: Union[str, None] = Field(..., alias='shortcode', description='')
    owner_name: Union[str, None] = Field(..., alias='ownerName', description='')
    caption: Union[str, None] = Field(..., alias='caption', description='')
    image_url: Union[str, None] = Field(..., alias='imageUrl', description='')
    track_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='trackCount', description='')
    selected_video_track: Union[InstagramMediaDownloadOutputVariant1SelectedVideoTrackVariant1, None] = Field(..., alias='selectedVideoTrack', description='')
    selected_audio_track: Union[InstagramMediaDownloadOutputVariant1SelectedAudioTrackVariant1, None] = Field(..., alias='selectedAudioTrack', description='')
    downloads: list[InstagramMediaDownloadOutputVariant1DownloadsItem] = Field(..., alias='downloads', description='')
    output_dir: Union[str, None] = Field(..., alias='outputDir', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')
    limitations: list[str] = Field(..., alias='limitations', description='')
    transcript: Union[InstagramMediaDownloadOutputVariant1TranscriptVariant1, None] = Field(..., alias='transcript', description='')


InstagramMediaDownloadOutputVariant2DeliveryArtifactsItem = TypedDict('InstagramMediaDownloadOutputVariant2DeliveryArtifactsItem', {
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
InstagramMediaDownloadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant2DeliveryAvailableExportsItem = TypedDict('InstagramMediaDownloadOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
InstagramMediaDownloadOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('InstagramMediaDownloadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
InstagramMediaDownloadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant2Delivery = TypedDict('InstagramMediaDownloadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[InstagramMediaDownloadOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[InstagramMediaDownloadOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[InstagramMediaDownloadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
InstagramMediaDownloadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant2RecoveryOperation = TypedDict('InstagramMediaDownloadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
InstagramMediaDownloadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramMediaDownloadOutputVariant2Recovery = TypedDict('InstagramMediaDownloadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[InstagramMediaDownloadOutputVariant2RecoveryOperation],
})
InstagramMediaDownloadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class InstagramMediaDownloadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: InstagramMediaDownloadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: InstagramMediaDownloadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(InstagramMediaDownloadOutput).
InstagramMediaDownloadOutput = Union[InstagramMediaDownloadOutputVariant1, InstagramMediaDownloadOutputVariant2]

_InstagramMediaDownloadInputAdapter = TypeAdapter(InstagramMediaDownloadInput)
_InstagramMediaDownloadOutputAdapter = TypeAdapter(InstagramMediaDownloadOutput)