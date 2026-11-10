from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class InstagramMediaDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Instagram post, reel, or tv URL, e.g. https://www.instagram.com/reel/SHORTCODE/.")
    profile: str | None = Field(None, alias="profile", description="Optional saved hosted browser profile name for authenticated Instagram access.")
    save_profile_changes: bool | None = Field(None, alias="saveProfileChanges", description="Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved login.")
    media_types: list[Literal['image', 'video', 'audio']] | None = Field(None, alias="mediaTypes", description="Which media types to download when downloadMedia is true.")
    download_media: bool | None = Field(None, alias="downloadMedia", description="Download extracted text/media files to the output directory. Media URLs are always returned even when false.")
    download_all_tracks: bool | None = Field(None, alias="downloadAllTracks", description="Download every captured MP4 track instead of only the best video/audio pair.")
    include_transcript: bool | None = Field(None, alias="includeTranscript", description="Transcribe the selected audio track. Adds transcription cost and time.")
    mux: bool | None = Field(None, alias="mux", description="Mux separately downloaded video/audio tracks into one MP4 if ffmpeg is available.")


class InstagramMediaDownloadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str | None = Field(None, alias="sourceUrl", description="")
    page_url: str | None = Field(None, alias="pageUrl", description="")
    browser: dict[str, Any] | None = Field(None, alias="browser", description="")
    type: Any | None = Field(None, alias="type", description="")
    shortcode: Any | None = Field(None, alias="shortcode", description="")
    owner_name: Any | None = Field(None, alias="ownerName", description="")
    caption: Any | None = Field(None, alias="caption", description="")
    image_url: Any | None = Field(None, alias="imageUrl", description="")
    track_count: int | None = Field(None, alias="trackCount", description="")
    selected_video_track: Any | None = Field(None, alias="selectedVideoTrack", description="")
    selected_audio_track: Any | None = Field(None, alias="selectedAudioTrack", description="")
    downloads: list[dict[str, Any]] | None = Field(None, alias="downloads", description="")
    output_dir: Any | None = Field(None, alias="outputDir", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    limitations: list[str] | None = Field(None, alias="limitations", description="")
    transcript: Any | None = Field(None, alias="transcript", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
