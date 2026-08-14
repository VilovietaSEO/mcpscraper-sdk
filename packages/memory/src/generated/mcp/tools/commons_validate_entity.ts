export interface Input {
  /**
   * Optional write idempotency key. Validation does not write, so this is checked only when supplied.
   */
  idempotencyKey?: string;
  /**
   * Candidate public page title. Validation reports an error when it is absent or shorter than the publishable minimum.
   */
  title?: string;
  /**
   * Candidate schema.org description. Validation reports an error when it is absent or shorter than the publishable minimum.
   */
  description?: string;
  /**
   * Optional URL slug. Omit to derive one from title.
   */
  slug?: string;
  /**
   * Existing Transparent Public Wiki entity id when proposing an edit. New entities normally omit this and receive a TPW-Q id.
   */
  entityId?: string;
  /**
   * Backend Wikidata-style type. Prefer precise entity classes such as SoftwareApplication, Organization, Person, Event, Place, Taxon, ScienceConcept, MathConcept, TechArticle, or PublicArticle; the public article structure should match the selected type.
   */
  entityType?: string;
  /**
   * Clarifying name used when the concept could be confused with another entity.
   */
  disambiguationName?: string;
  /**
   * Required for auto-published public entities. The image is also added to the media manifest if absent.
   */
  featuredImage?: {
    /**
     * Required public image URL for a publishable entity. Use extract_url includeFeaturedImage or preserved media when available.
     */
    url: string;
    /**
     * Accessible alternative text describing the image.
     */
    alt?: string;
    /**
     * Visible image caption preserving useful context and credit.
     */
    caption?: string;
    /**
     * Original public source URL supporting this image, claim, or article.
     */
    sourceUrl?: string;
    /**
     * Known media or content license identifier; omit rather than guessing.
     */
    license?: string;
    /**
     * Intrinsic image width in pixels when known.
     */
    width?: number;
    /**
     * Intrinsic image height in pixels when known.
     */
    height?: number;
  };
  /**
   * Source provenance. Store original URL, source byline, and origin canonical here; canonical does not replace rights review.
   */
  source?: {
    /**
     * Original source URL when content was captured or republished.
     */
    originalUrl?: string;
    /**
     * Final URL after redirects.
     */
    resolvedUrl?: string;
    /**
     * Originator canonical URL discovered from metadata or declared by the contributor.
     */
    sourceCanonicalUrl?: string;
    /**
     * rel=canonical target to use when the public page is a substantial republish.
     */
    relCanonicalHref?: string;
    /**
     * Source byline/original author label.
     */
    sourceByline?: string;
    /**
     * Original publisher name preserved for attribution.
     */
    publisher?: string;
    /**
     * Original author names preserved for attribution.
     *
     * @maxItems 20
     */
    authors?:
      | []
      | [string]
      | [string, string]
      | [string, string, string]
      | [string, string, string, string]
      | [string, string, string, string, string]
      | [string, string, string, string, string, string]
      | [string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string, string, string]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ];
    /**
     * Original publication time or date preserved from the source.
     */
    publishedAt?: string;
    /**
     * ISO 8601 time when the source evidence was captured.
     */
    capturedAt?: string;
    /**
     * Known media or content license identifier; omit rather than guessing.
     */
    license?: string;
    /**
     * Concise known rights context; omit unsupported assumptions.
     */
    rightsSummary?: string;
    /**
     * Stable digest used to identify the captured source content.
     */
    contentHash?: string;
  };
  /**
   * Standardized topic tags. Use existing/searchable concepts when possible.
   *
   * @maxItems 24
   */
  tags?: string[];
  /**
   * SEO and retrieval keywords.
   *
   * @maxItems 50
   */
  keywords?: string[];
  /**
   * Related concepts, including trails. Existing entities should use entityId.
   *
   * @maxItems 200
   */
  relatedEntities?: {
    /**
     * Existing governed entity identifier for this relation or edit.
     */
    entityId?: string;
    /**
     * Human-readable title for the proposed record or authored content.
     */
    title: string;
    /**
     * Governed relationship type connecting the two entities.
     */
    relationship?: string;
    /**
     * Optional stable public slug; omit only when the tool is documented to derive it.
     */
    slug?: string;
    /**
     * Public HTTPS URL for this nested source, link, or media item.
     */
    url?: string;
    /**
     * Human-readable summary that distinguishes this record from similarly named records.
     */
    description?: string;
  }[];
  /**
   * Governed relationship assertions. Supplying claims replaces the accepted claim set for this entity; omitting claims preserves it. Only approved, active, non-disputed claims project into the RFC 9264 linkset.
   *
   * @maxItems 300
   */
  claims?: {
    /**
     * Registered link relation such as related, describedby, license, or type; alternatively an absolute HTTPS relation URI from a published vocabulary.
     */
    predicate: string;
    /**
     * Human-readable label for display and review. It does not replace the machine predicate.
     */
    predicateLabel?: string;
    /**
     * Existing Transparent Commons entity target. Use exactly one of objectEntityId or objectUrl.
     */
    objectEntityId?: string;
    /**
     * External or third-party target. Use exactly one of objectUrl or objectEntityId.
     */
    objectUrl?: string;
    /**
     * Human-readable title for the proposed record or authored content.
     */
    title?: string;
    /**
     * Optional RFC link target media type.
     */
    mediaType?: string;
    /**
     * Optional repeatable RFC link target language hints.
     *
     * @maxItems 20
     */
    hreflang?:
      | []
      | [string]
      | [string, string]
      | [string, string, string]
      | [string, string, string, string]
      | [string, string, string, string, string]
      | [string, string, string, string, string, string]
      | [string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string, string, string]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ];
    /**
     * Structured qualifiers that narrow the governed relationship claim.
     */
    qualifiers?: {
      [k: string]: string | number | boolean | null;
    };
    /**
     * Evidence supporting the relationship assertion.
     *
     * @maxItems 50
     */
    references?: {
      /**
       * Human-readable title for the proposed record or authored content.
       */
      title: string;
      /**
       * Public HTTPS URL for this nested source, link, or media item.
       */
      url?: string;
      /**
       * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
       */
      source?: string;
      /**
       * Exact memory note path or resolvable note reference used as the graph target.
       */
      note?: string;
      /**
       * ISO 8601 time when this source or record was accessed.
       */
      accessedAt?: string;
    }[];
    /**
     * Relative ordering or prominence rank for this item.
     */
    rank?: "preferred" | "normal" | "deprecated";
    /**
     * Bounded confidence value for the supplied assertion.
     */
    confidence?: number;
    /**
     * Short evidence-based explanation for the confidence value.
     */
    confidenceReason?: string;
    /**
     * Governance state describing whether the claim is disputed.
     */
    disputeState?: "undisputed" | "attributed" | "disputed" | "contested" | "needs_review" | "deprecated";
    /**
     * ISO 8601 time when this governed assertion becomes active.
     */
    validFrom?: string;
    /**
     * ISO 8601 time when this governed assertion stops being active.
     */
    validTo?: string;
    /**
     * ISO 8601 date or time through which the supplied evidence is current.
     */
    asOf?: string;
    /**
     * Normalized source-family classification for this evidence.
     */
    sourceFamily?: "first_party" | "partner" | "independent" | "community" | "unknown";
  }[];
  /**
   * Structured encyclopedia body in neutral Markdown, not a raw scrape dump or blog essay. Use H2 for entity-profile sections and H3/H4/H5 for subtopics; every heading appears in the public page menu. Call commons_prepare_entity first for the live entity profile and commons_validate_entity before submit. Profile sections are adaptive: include History, Pricing, Reception, Timeline, Classification, or similar sections only when source evidence supports them; omit unsupported sections instead of adding empty/filler headings. Apply NPOV, verifiability, and no-original-research rules; self-published sources can support only uncontroversial source-owned facts.
   */
  bodyMarkdown?: string;
  /**
   * Structured article sections. If bodyMarkdown is omitted, these are rendered into the article body. Headings should follow the selected entity profile, and body text may include H3/H4/H5 subheadings for every visible page-menu subitem.
   *
   * @maxItems 80
   */
  contentSections?: {
    /**
     * Stable identifier for this nested record.
     */
    id?: string;
    /**
     * Visible section heading used in navigation and presentation.
     */
    heading: string;
    /**
     * Complete authored body content for this article or section.
     */
    body: string;
    /**
     * Ordered display or ranking position for this item.
     */
    position?: number;
    /**
     * Source citations supporting the surrounding claim or article.
     *
     * @maxItems 300
     */
    citations?: {
      /**
       * Human-readable title for the proposed record or authored content.
       */
      title: string;
      /**
       * Public HTTPS URL for this nested source, link, or media item.
       */
      url?: string;
      /**
       * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
       */
      source?: string;
      /**
       * Exact memory note path or resolvable note reference used as the graph target.
       */
      note?: string;
      /**
       * ISO 8601 time when this source or record was accessed.
       */
      accessedAt?: string;
    }[];
  }[];
  /**
   * Wikipedia-style bottom article sections: See also, Notes, Citations, External links, Categories.
   */
  articleSections?: {
    /**
     * See Also concept links. Resolve to entityId/slug when an entity exists; otherwise keep the concept with needsLink true so it enters the Commons needs-link backlog.
     *
     * @maxItems 100
     */
    relatedLinks?: {
      /**
       * See Also concept title. Use concept labels such as Model Context Protocol, Web scraping, or Hybrid RAG.
       */
      title: string;
      /**
       * Optional existing internal or external URL. Omit when the concept needs a new Commons page.
       */
      url?: string;
      /**
       * Existing Transparent Commons /wiki/ slug when available. Prefer this over a raw public URL for internal pages.
       */
      slug?: string;
      /**
       * Existing Transparent Public Wiki entity id when available. Prefer this for resolved internal concepts.
       */
      entityId?: string;
      /**
       * Short relationship label, such as protocol, retrieval pattern, source type, or related practice.
       */
      relationship?: string;
      /**
       * Short neutral snippet used by the public See Also row, hover cards, and Commons graph retrieval.
       */
      summary?: string;
      /**
       * Optional preview image for hover cards when available.
       */
      imageUrl?: string;
      /**
       * Set true when the concept belongs in See Also but no existing Commons entity/page exists yet. The backend exposes these records through commons_list_needs_links.
       */
      needsLink?: boolean;
    }[];
    /**
     * Optional operator or provenance notes attached to this nested record.
     *
     * @maxItems 100
     */
    notes?: {
      /**
       * Visual marker or badge applied by the selected renderer.
       */
      marker?: string;
      /**
       * Complete authored body content for this article or section.
       */
      body: string;
    }[];
    /**
     * Source citations supporting the surrounding claim or article.
     *
     * @maxItems 300
     */
    citations?: {
      /**
       * Human-readable title for the proposed record or authored content.
       */
      title: string;
      /**
       * Public HTTPS URL for this nested source, link, or media item.
       */
      url?: string;
      /**
       * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
       */
      source?: string;
      /**
       * Exact memory note path or resolvable note reference used as the graph target.
       */
      note?: string;
      /**
       * ISO 8601 time when this source or record was accessed.
       */
      accessedAt?: string;
    }[];
    /**
     * Curated public links associated with the article or entity.
     *
     * @maxItems 100
     */
    externalLinks?: {
      /**
       * Human-readable title for the proposed record or authored content.
       */
      title: string;
      /**
       * Public HTTPS URL for this nested source, link, or media item.
       */
      url: string;
      /**
       * Concise retrieval-ready summary of the nested record.
       */
      summary?: string;
    }[];
    /**
     * Canonical categories assigned to the authored content.
     *
     * @maxItems 50
     */
    categories?: string[];
  };
  /**
   * Image, video, and audio assets for the public entity. Videos are kept in the media manifest but are not vectorized as comments/community content.
   *
   * @maxItems 300
   */
  media?: {
    /**
     * Governed content or record type used for routing and validation.
     */
    type: "image" | "video" | "audio";
    /**
     * Public HTTPS URL for this nested source, link, or media item.
     */
    url: string;
    /**
     * Accessible alternative text describing the image.
     */
    alt?: string;
    /**
     * Visible image caption preserving useful context and credit.
     */
    caption?: string;
    /**
     * Public poster image URL for the referenced media.
     */
    posterUrl?: string;
    /**
     * Original public source URL supporting this image, claim, or article.
     */
    sourceUrl?: string;
    /**
     * Known media or content license identifier; omit rather than guessing.
     */
    license?: string;
    /**
     * Intrinsic image width in pixels when known.
     */
    width?: number;
    /**
     * Intrinsic image height in pixels when known.
     */
    height?: number;
    /**
     * Media duration in whole or fractional seconds.
     */
    durationSeconds?: number;
  }[];
  /**
   * Optional caller-supplied JSON-LD. Omit to let the server generate schema.org Article JSON-LD from the entity fields.
   */
  jsonLd?: {
    [k: string]: unknown;
  };
  /**
   * schema.org/SEO controls. Use relCanonical for substantial source republishing.
   */
  seo?: {
    /**
     * Canonical public URL for this article or entity.
     */
    canonicalUrl?: string;
    /**
     * Whether the renderer should emit the supplied canonical relationship.
     */
    relCanonical?: string;
    /**
     * Search and social title for the page; keep it faithful to visible content.
     */
    metaTitle?: string;
    /**
     * Search and social summary for the page; keep it faithful to visible content.
     */
    metaDescription?: string;
    /**
     * Open Graph image metadata for social previews.
     */
    ogImage?: string;
    /**
     * Accepted Schema.org subtype supported by the listing evidence.
     */
    schemaOrgType?: string;
    /**
     * When true, ask compliant crawlers not to index the rendered page.
     */
    noIndex?: boolean;
  };
  /**
   * How this contribution was made.
   */
  actorChannel?: "mcp" | "frontend" | "api";
  /**
   * Human, agent, team, or organization label recorded in the public contribution ledger.
   */
  actorLabel?: string;
  /**
   * Short contribution note recorded in the ledger.
   */
  changeSummary?: string;
  /**
   * Required when editing an existing entity if you want auto-publish. Without a matching revision, the proposal is held for review.
   */
  baseRevision?: number;
  /**
   * Default auto-publishes only safe non-conflicting writes. Use always_review when the contributor wants human review.
   */
  reviewPolicy?: "auto_publish_if_safe" | "always_review";
}

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
