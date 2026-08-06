from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsPrepareEntityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    title: str = Field(..., alias="title", description="Candidate public page title. Used to derive slug, choose a profile, and search duplicate entities.")
    description: str | None = Field(None, alias="description", description="Optional candidate summary. Include when known so the prepare pass can route and validate the article shape.")
    slug: str | None = Field(None, alias="slug", description="Optional desired URL slug. Omit to derive one from title.")
    entity_type: str | None = Field(None, alias="entityType", description="Candidate backend Wikidata-style type. Use precise classes when possible: SoftwareApplication, Organization, Person, Event, Place, Taxon, ScienceConcept, MathConcept, TechArticle, Trail, or PublicArticle.")
    schema_org_type: str | None = Field(None, alias="schemaOrgType", description="Optional candidate schema.org @type. If omitted, the profile chooses one from entityType.")
    source: dict[str, Any] | None = Field(None, alias="source", description="Candidate source provenance used for duplicate checks and rel=canonical guidance.")
    tags: list[str] | None = Field(None, alias="tags", description="Candidate topic tags to resolve against existing Commons tag vocabulary.")
    keywords: list[str] | None = Field(None, alias="keywords", description="Candidate SEO/retrieval keywords to resolve against existing Commons vocabulary.")
    body_markdown: str | None = Field(None, alias="bodyMarkdown", description="Optional draft article body. Prepare will inspect headings and return profile alignment guidance without writing anything.")
    content_sections: list[dict[str, Any]] | None = Field(None, alias="contentSections", description="Optional structured draft sections. Use when composing a page from source evidence before submit.")
    max_candidates: int | None = Field(None, alias="maxCandidates", description="Maximum duplicate candidates to return.")


class CommonsPrepareEntityOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
