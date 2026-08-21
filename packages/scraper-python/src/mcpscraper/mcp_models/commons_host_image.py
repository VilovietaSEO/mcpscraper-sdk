from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsHostImageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str | None = Field(None, alias="sourceUrl", description="Public https image URL to download and host. The wiki never serves a third-party URL directly, so pass the original source here rather than putting it on the entity.")
    image_base64: str | None = Field(None, alias="imageBase64", description="Base64 image bytes for an image you already hold. Use for images under about 3 MB; larger files should be published from a URL.")
    alt: str | None = Field(None, alias="alt", description="Alt text describing the image for readers who cannot see it.")
    license: str | None = Field(None, alias="license", description="License or usage terms of the original image, preserved with the hosted copy.")
    attribution: str | None = Field(None, alias="attribution", description="Credit line for the original photographer, publication, or archive.")


class CommonsHostImageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
