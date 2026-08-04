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
   * Maximum duplicate candidates to return.
   */
  maxCandidates?: number;
}

export type Output = unknown
