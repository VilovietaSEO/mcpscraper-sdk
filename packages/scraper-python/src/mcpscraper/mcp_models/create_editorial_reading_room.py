from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateEditorialReadingRoomInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site: dict[str, Any] = Field(..., alias="site", description="")
    deck: str = Field(..., alias="deck", description="Two or three sentences that explain the collection’s value and scope without generic marketing language.")
    articles: list[dict[str, Any]] = Field(..., alias="articles", description="One to forty fully authored articles, with no more than 2,000,000 Markdown bytes combined. Read all in-scope source material before composing them; preserve distinctions, uncertainty, and provenance instead of flattening the corpus.")
    filename: str | None = Field(None, alias="filename", description="Optional download filename. The server always normalizes it to a safe .html filename.")


class CreateEditorialReadingRoomOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    title: str = Field(..., alias="title", description="")
    filename: str = Field(..., alias="filename", description="")
    delivery: Literal['artifact', 'local_file'] = Field(..., alias="delivery", description="")
    article_count: int = Field(..., alias="articleCount", description="")
    word_count: int = Field(..., alias="wordCount", description="")
    bytes: int = Field(..., alias="bytes", description="")
    sha256: str = Field(..., alias="sha256", description="")
    generated_at: str = Field(..., alias="generatedAt", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
    local_path: str | None = Field(None, alias="localPath", description="")
    warnings: list[str] = Field(..., alias="warnings", description="")
