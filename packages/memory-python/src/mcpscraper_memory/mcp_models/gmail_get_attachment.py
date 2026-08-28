from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailGetAttachmentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    attachment_ref: str = Field(..., alias="attachmentRef", description="Opaque owner-bound attachmentRef returned by gmail_get_message; do not pass a provider attachment ID or URL.")


class GmailGetAttachmentOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    filename: str | None = Field(None, alias="filename", description="")
    declared_mime: str | None = Field(None, alias="declaredMime", description="")
    observed_mime: str | None = Field(None, alias="observedMime", description="")
    bytes: int | None = Field(None, alias="bytes", description="")
    sha256: str | None = Field(None, alias="sha256", description="")
    content_complete: bool | None = Field(None, alias="contentComplete", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    text: str | None = Field(None, alias="text", description="")
    text_complete: bool | None = Field(None, alias="textComplete", description="")
    next_offset: Any | None = Field(None, alias="nextOffset", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: Any = Field(..., alias="error", description="")
