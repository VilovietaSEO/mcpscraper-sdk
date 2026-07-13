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
