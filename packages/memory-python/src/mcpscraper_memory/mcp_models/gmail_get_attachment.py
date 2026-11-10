from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GmailGetAttachmentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    attachment_ref: str = Field(..., alias="attachmentRef", description="Opaque owner-bound attachmentRef returned by gmail_get_message; do not pass a provider attachment ID or URL.")


class GmailGetAttachmentOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
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
    untrusted_content: bool | None = Field(None, alias="untrustedContent", description="")
    error: Any | None = Field(None, alias="error", description="")
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
