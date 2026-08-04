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
    alt?: string;
    caption?: string;
    sourceUrl?: string;
    license?: string;
    width?: number;
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
    publisher?: string;
    /**
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
    publishedAt?: string;
    capturedAt?: string;
    license?: string;
    rightsSummary?: string;
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
    entityId?: string;
    title: string;
    relationship?: string;
    slug?: string;
    url?: string;
    description?: string;
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
    id?: string;
    heading: string;
    body: string;
    position?: number;
    /**
     * @maxItems 300
     */
    citations?: {
      title: string;
      url?: string;
      source?: string;
      note?: string;
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
     * @maxItems 100
     */
    notes?: {
      marker?: string;
      body: string;
    }[];
    /**
     * @maxItems 300
     */
    citations?: {
      title: string;
      url?: string;
      source?: string;
      note?: string;
      accessedAt?: string;
    }[];
    /**
     * @maxItems 100
     */
    externalLinks?: {
      title: string;
      url: string;
      summary?: string;
    }[];
    /**
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
    type: "image" | "video" | "audio";
    url: string;
    alt?: string;
    caption?: string;
    posterUrl?: string;
    sourceUrl?: string;
    license?: string;
    width?: number;
    height?: number;
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
    canonicalUrl?: string;
    relCanonical?: string;
    metaTitle?: string;
    metaDescription?: string;
    ogImage?: string;
    schemaOrgType?: string;
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

export type Output = unknown
