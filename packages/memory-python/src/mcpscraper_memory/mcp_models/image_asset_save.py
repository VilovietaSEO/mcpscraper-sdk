from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ImageAssetSaveInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    project_id: str | None = Field(None, alias="projectId", description="Opaque image project identifier returned by an image project tool.")
    folder_id: str | None = Field(None, alias="folderId", description="Opaque image folder identifier; omit only when the project root is intended.")
    source_url: str | None = Field(None, alias="sourceUrl", description="Public HTTPS image URL. Private-network and redirect targets are rejected.")
    artifact_id: str | None = Field(None, alias="artifactId", description="Owned MCP Scraper artifact ID. Available through the aggregate MCP handoff.")
    image_base64: str | None = Field(None, alias="imageBase64", description="Bounded base64 image for clients without an upload transport; maximum decoded size is 20 MiB.")
    title: str = Field(..., alias="title", description="Human-readable title for the proposed record or authored content.")
    description: str | None = Field(None, alias="description", description="Human-readable summary that distinguishes this record from similarly named records.")
    alt_text: str | None = Field(None, alias="altText", description="Concise accessible description of the image content and purpose.")
    tags: list[str] | None = Field(None, alias="tags", description="Canonical tag filter or tag set; use the appropriate vocabulary-listing tool before writing new tags.")
    source_ref: dict[str, Any] | None = Field(None, alias="sourceRef", description="Original source URL or opaque artifact reference preserved as image provenance.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable key for this logical save. Retrying the same request returns the same asset without another write.")


class ImageAssetSaveOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    asset: dict[str, Any] | None = Field(None, alias="asset", description="")
    reused_object: bool | None = Field(None, alias="reusedObject", description="")
    next_action: str | None = Field(None, alias="nextAction", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
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
