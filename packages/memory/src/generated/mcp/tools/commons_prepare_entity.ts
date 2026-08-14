export interface Input {
  /**
   * Candidate public page title. Used to derive slug, choose a profile, and search duplicate entities.
   */
  title: string;
  /**
   * Optional candidate summary. Include when known so the prepare pass can route and validate the article shape.
   */
  description?: string;
  /**
   * Optional desired URL slug. Omit to derive one from title.
   */
  slug?: string;
  /**
   * Candidate backend Wikidata-style type. Use precise classes when possible: SoftwareApplication, Organization, Person, Event, Place, Taxon, ScienceConcept, MathConcept, TechArticle, Trail, or PublicArticle.
   */
  entityType?: string;
  /**
   * Optional candidate schema.org @type. If omitted, the profile chooses one from entityType.
   */
  schemaOrgType?: string;
  /**
   * Candidate source provenance used for duplicate checks and rel=canonical guidance.
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
   * Candidate topic tags to resolve against existing Commons tag vocabulary.
   *
   * @maxItems 24
   */
  tags?: string[];
  /**
   * Candidate SEO/retrieval keywords to resolve against existing Commons vocabulary.
   *
   * @maxItems 50
   */
  keywords?: string[];
  /**
   * Optional draft article body. Prepare will inspect headings and return profile alignment guidance without writing anything.
   */
  bodyMarkdown?: string;
  /**
   * Optional structured draft sections. Use when composing a page from source evidence before submit.
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
   * Maximum duplicate candidates to return.
   */
  maxCandidates?: number;
}

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
