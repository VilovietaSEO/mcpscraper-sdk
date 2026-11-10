from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CommonsClaimPublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    requested_subdomain: str = Field(..., alias="requestedSubdomain", description="Requested publication name under transparent-commons.cc. The server normalizes spaces to hyphens, rejects reserved names, and keeps names globally unique; accounts may own multiple names.")
    title: str | None = Field(None, alias="title", description="Reader-facing publication title. Omit to derive it from the chosen subdomain.")
    description: str | None = Field(None, alias="description", description="Short description used on the publication archive and discovery surfaces.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Unique key for this intended claim. Reuse it only when retrying the same claim.")


class CommonsClaimPublicationOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
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
