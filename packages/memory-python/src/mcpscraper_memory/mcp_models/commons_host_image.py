from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsHostImageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str | None = Field(None, alias="sourceUrl", description="Stable direct public HTTPS URL whose response is the image bytes to host. Do not pass an HTML webpage, chat attachment reference, caller-local path, temporary or signed URL, or private/authenticated URL.")
    image_base64: str | None = Field(None, alias="imageBase64", description="Base64 image bytes for an image you already hold, including forwarded chat attachment bytes. Prefer this over a temporary attachment URL when the serialized request remains under about 3 MB; larger files require a stable direct public HTTPS source URL.")
    alt: str | None = Field(None, alias="alt", description="Alt text describing the image for readers who cannot see it.")
    license: str | None = Field(None, alias="license", description="License or usage terms of the original image, preserved with the hosted copy.")
    attribution: str | None = Field(None, alias="attribution", description="Credit line for the original photographer, publication, or archive.")


class CommonsHostImageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
