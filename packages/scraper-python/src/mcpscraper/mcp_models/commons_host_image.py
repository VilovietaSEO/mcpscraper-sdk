from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsHostImageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str | None = Field(None, alias="sourceUrl", description="Public HTTPS direct image URL or webpage URL. A direct image is hosted as-is; an HTML page is inspected for Open Graph, Twitter, JSON-LD, and meaningful content images, then the first usable candidate is hosted. Temporary signed URLs are consumed immediately and query credentials are not retained as provenance.")
    image_base64: str | None = Field(None, alias="imageBase64", description="Base64 image bytes for an image already available to the caller, including a pasted attachment or AI-generated image. Use sourceType to preserve whether it was uploaded or generated. Keep the complete serialized request within the client transport limit.")
    artifact_id: str | None = Field(None, alias="artifactId", description="Owner-scoped image artifact returned by an MCP Scraper media or screenshot workflow. The server reauthorizes ownership and reads the bytes directly; do not construct an artifact ID.")
    source_type: Literal['uploaded', 'ai_generated'] | None = Field(None, alias="sourceType", description="Provenance for imageBase64 or artifactId. Use ai_generated only when an image model created the supplied bytes; otherwise use uploaded or omit it.")
    alt: str | None = Field(None, alias="alt", description="Alt text describing the image for readers who cannot see it.")
    license: str | None = Field(None, alias="license", description="License or usage terms of the original image, preserved with the hosted copy.")
    attribution: str | None = Field(None, alias="attribution", description="Credit line for the original photographer, publication, or archive.")


class CommonsHostImageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: dict[str, Any] | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
