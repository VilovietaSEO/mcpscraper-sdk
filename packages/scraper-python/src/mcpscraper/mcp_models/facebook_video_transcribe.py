from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class FacebookVideoTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Organic Facebook reel/video/watch/post/share URL from facebook.com, m.facebook.com, or fb.watch.")
    quality: Literal["best", "hd", "sd"] | None = Field(None, alias="quality", description="Preferred progressive MP4 quality. Use best by default; hd prefers the highest HD progressive URL; sd forces the SD URL.")


class FacebookVideoTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
