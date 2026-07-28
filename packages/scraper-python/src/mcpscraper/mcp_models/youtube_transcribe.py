from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class YoutubeTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_id: str | None = Field(None, alias="videoId", description="YouTube video ID, e.g. dQw4w9WgXcQ. Use only an ID returned by youtube_harvest or visible in a YouTube URL; do not invent one.")
    url: str | None = Field(None, alias="url", description="Full YouTube URL. Use when the user pasted a URL instead of an ID. Provide videoId or url.")
    language: Literal["af", "am", "ar", "as", "az", "ba", "be", "bg", "bn", "bo", "br", "bs", "ca", "cs", "cy", "da", "de", "el", "en", "es", "et", "eu", "fa", "fi", "fo", "fr", "gl", "gu", "ha", "haw", "he", "hi", "hr", "ht", "hu", "hy", "id", "is", "it", "ja", "jw", "ka", "kk", "km", "kn", "ko", "la", "lb", "ln", "lo", "lt", "lv", "mg", "mi", "mk", "ml", "mn", "mr", "ms", "mt", "my", "ne", "nl", "nn", "no", "oc", "pa", "pl", "ps", "pt", "ro", "ru", "sa", "sd", "si", "sk", "sl", "sn", "so", "sq", "sr", "su", "sv", "sw", "ta", "te", "tg", "th", "tk", "tl", "tr", "tt", "uk", "ur", "uz", "vi", "yi", "yo", "zh"] | None = Field(None, alias="language", description="ISO language code of the video's spoken audio, e.g. \"es\", \"fr\". Defaults to \"en\" — set this when the user says the video is not in English, to avoid a failed transcription.")


class YoutubeTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_id: Any = Field(..., alias="videoId", description="")
    url: Any = Field(..., alias="url", description="")
    word_count: int = Field(..., alias="wordCount", description="")
    chunk_count: int = Field(..., alias="chunkCount", description="")
    duration_ms: Any = Field(..., alias="durationMs", description="")
    transcript_text: str = Field(..., alias="transcriptText", description="")
    chunks: list[dict[str, Any]] = Field(..., alias="chunks", description="")
    resolved_inputs: dict[str, Any] = Field(..., alias="resolvedInputs", description="")
