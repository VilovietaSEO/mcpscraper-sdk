from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CommonsValidateEntityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str | None = Field(None, alias="idempotencyKey", description="Optional write idempotency key. Validation does not write, so this is checked only when supplied.")
    title: str | None = Field(None, alias="title", description="Candidate public page title. Validation reports an error when it is absent or shorter than the publishable minimum.")
    description: str | None = Field(None, alias="description", description="Candidate schema.org description. Validation reports an error when it is absent or shorter than the publishable minimum.")
    slug: str | None = Field(None, alias="slug", description="Optional URL slug. Omit to derive one from title.")
    entity_id: str | None = Field(None, alias="entityId", description="Existing Transparent Public Wiki entity id when proposing an edit. New entities normally omit this and receive a TPW-Q id.")
    entity_type: str | None = Field(None, alias="entityType", description="Backend Wikidata-style type. Prefer precise entity classes such as SoftwareApplication, Organization, Person, Event, Place, Taxon, ScienceConcept, MathConcept, TechArticle, or PublicArticle; the public article structure should match the selected type.")
    disambiguation_name: str | None = Field(None, alias="disambiguationName", description="Clarifying name used when the concept could be confused with another entity.")
    featured_image: dict[str, Any] | None = Field(None, alias="featuredImage", description="Required for auto-published public entities. First call commons_host_image with attachment bytes, an image artifact, a direct image URL, or a webpage URL, then place its returned permanent URL here. Validation does not fetch external images and reports unregistered URLs as not publishable. Submit retains a compatibility fallback for public URLs. The image is also added to the media manifest if absent.")
    source: dict[str, Any] | None = Field(None, alias="source", description="Source provenance. Store original URL, source byline, and origin canonical here; canonical does not replace rights review.")
    tags: list[str] | None = Field(None, alias="tags", description="Standardized topic tags. Use existing/searchable concepts when possible.")
    keywords: list[str] | None = Field(None, alias="keywords", description="SEO and retrieval keywords.")
    related_entities: list[dict[str, Any]] | None = Field(None, alias="relatedEntities", description="Related concepts, including trails. Existing entities should use entityId.")
    claims: list[dict[str, Any]] | None = Field(None, alias="claims", description="Governed relationship assertions. Supplying claims replaces the accepted claim set for this entity; omitting claims preserves it. Only approved, active, non-disputed claims project into the RFC 9264 linkset.")
    body_markdown: str | None = Field(None, alias="bodyMarkdown", description="Structured encyclopedia body in neutral Markdown, not a raw scrape dump or blog essay. Use H2 for entity-profile sections and H3/H4/H5 for subtopics; every heading appears in the public page menu. Call commons_prepare_entity first for the live entity profile and commons_validate_entity before submit. Profile sections are adaptive: include History, Pricing, Reception, Timeline, Classification, or similar sections only when source evidence supports them; omit unsupported sections instead of adding empty/filler headings. Apply NPOV, verifiability, and no-original-research rules; self-published sources can support only uncontroversial source-owned facts.")
    content_sections: list[dict[str, Any]] | None = Field(None, alias="contentSections", description="Structured article sections. If bodyMarkdown is omitted, these are rendered into the article body. Headings should follow the selected entity profile, and body text may include H3/H4/H5 subheadings for every visible page-menu subitem.")
    article_sections: dict[str, Any] | None = Field(None, alias="articleSections", description="Wikipedia-style bottom article sections: See also, Notes, Citations, External links, Categories.")
    media: list[dict[str, Any]] | None = Field(None, alias="media", description="Image, video, and audio assets for the public entity. Videos are kept in the media manifest but are not vectorized as comments/community content.")
    json_ld: dict[str, Any] | None = Field(None, alias="jsonLd", description="Optional caller-supplied JSON-LD. Omit to let the server generate schema.org Article JSON-LD from the entity fields.")
    seo: dict[str, Any] | None = Field(None, alias="seo", description="schema.org/SEO controls. Use relCanonical for substantial source republishing.")
    actor_channel: Literal['mcp', 'frontend', 'api'] | None = Field(None, alias="actorChannel", description="How this contribution was made.")
    actor_label: str | None = Field(None, alias="actorLabel", description="Human, agent, team, or organization label recorded in the public contribution ledger.")
    change_summary: str | None = Field(None, alias="changeSummary", description="Short contribution note recorded in the ledger.")
    base_revision: int | None = Field(None, alias="baseRevision", description="Required when editing an existing entity if you want auto-publish. Without a matching revision, the proposal is held for review.")
    review_policy: Literal['auto_publish_if_safe', 'always_review'] | None = Field(None, alias="reviewPolicy", description="Default auto-publishes only safe non-conflicting writes. Use always_review when the contributor wants human review.")


class CommonsValidateEntityOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: dict[str, Any] | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
