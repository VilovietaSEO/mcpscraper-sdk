from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CreateEditorialReadingRoomInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site: dict[str, Any] = Field(..., alias="site", description="Complete editorial site payload containing the collection identity and authored articles.")
    deck: str = Field(..., alias="deck", description="Two or three sentences that explain the collection’s value and scope without generic marketing language.")
    articles: list[dict[str, Any]] = Field(..., alias="articles", description="One to one hundred fully authored articles, with no more than 2,000,000 Markdown bytes combined. Articles may include structured card/hero images, article-specific Open Graph images, and Markdown body images. Read all in-scope source material before composing them; preserve distinctions, uncertainty, image provenance, and rights context instead of flattening the corpus.")
    filename: str | None = Field(None, alias="filename", description="Optional download filename. The server always normalizes it to a safe .html filename.")


class CreateEditorialReadingRoomOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    title: str | None = Field(None, alias="title", description="")
    filename: str | None = Field(None, alias="filename", description="")
    delivery: Any = Field(..., alias="delivery", description="")
    article_count: int | None = Field(None, alias="articleCount", description="")
    word_count: int | None = Field(None, alias="wordCount", description="")
    bytes: int | None = Field(None, alias="bytes", description="")
    sha256: str | None = Field(None, alias="sha256", description="")
    generated_at: str | None = Field(None, alias="generatedAt", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    local_path: str | None = Field(None, alias="localPath", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
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
