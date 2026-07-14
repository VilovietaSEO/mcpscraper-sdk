from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class InstagramMediaDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Instagram post, reel, or tv URL, e.g. https://www.instagram.com/reel/SHORTCODE/.")
    profile: str | None = Field(None, alias="profile", description="Optional saved hosted browser profile name for authenticated Instagram access.")
    save_profile_changes: bool | None = Field(None, alias="saveProfileChanges", description="Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved login.")
    media_types: list[Literal["image", "video", "audio"]] | None = Field(None, alias="mediaTypes", description="Which media types to download when downloadMedia is true.")
    download_media: bool | None = Field(None, alias="downloadMedia", description="Download extracted text/media files to the output directory. Media URLs are always returned even when false.")
    download_all_tracks: bool | None = Field(None, alias="downloadAllTracks", description="Download every captured MP4 track instead of only the best video/audio pair.")
    include_transcript: bool | None = Field(None, alias="includeTranscript", description="Transcribe the selected audio track. Adds transcription cost and time.")
    mux: bool | None = Field(None, alias="mux", description="Mux separately downloaded video/audio tracks into one MP4 if ffmpeg is available.")


class InstagramMediaDownloadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str = Field(..., alias="sourceUrl", description="")
    page_url: str = Field(..., alias="pageUrl", description="")
    browser: dict[str, Any] = Field(..., alias="browser", description="")
    type: Any = Field(..., alias="type", description="")
    shortcode: Any = Field(..., alias="shortcode", description="")
    owner_name: Any = Field(..., alias="ownerName", description="")
    caption: Any = Field(..., alias="caption", description="")
    image_url: Any = Field(..., alias="imageUrl", description="")
    track_count: int = Field(..., alias="trackCount", description="")
    selected_video_track: Any = Field(..., alias="selectedVideoTrack", description="")
    selected_audio_track: Any = Field(..., alias="selectedAudioTrack", description="")
    downloads: list[dict[str, Any]] = Field(..., alias="downloads", description="")
    output_dir: Any = Field(..., alias="outputDir", description="")
    warnings: list[str] = Field(..., alias="warnings", description="")
    limitations: list[str] = Field(..., alias="limitations", description="")
    transcript: Any = Field(..., alias="transcript", description="")
