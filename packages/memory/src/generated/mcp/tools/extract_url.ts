export interface Input {
  /**
   * Public http/https URL to extract.
   */
  url: string;
  /**
   * Capture a full-page screenshot. Large captures may be offloaded to an owned artifact.
   */
  screenshot?: boolean;
  /**
   * Viewport: desktop = 1440×900, mobile = 390×844.
   */
  screenshotDevice?: "desktop" | "mobile";
  /**
   * Extract brand colors, fonts, logo, and favicon via a rendered session.
   */
  extractBranding?: boolean;
  /**
   * Return the best featured image from Open Graph, Twitter, JSON-LD, or page content. Wayback URLs get the timestamp-matched archived image.
   */
  includeFeaturedImage?: boolean;
  /**
   * Deprecated alias for preserveMedia; omit when using preserveMedia.
   */
  downloadMedia?: boolean;
  /**
   * Media types to download. Default all three.
   */
  mediaTypes?: ("image" | "video" | "audio")[];
  /**
   * Maximum media records to retain after filtering and variant collapse.
   */
  maxMediaAssets?: number;
  /**
   * Maximum images attached as AI-readable content blocks. All downloaded media stays available in the ZIP.
   */
  maxInlineImages?: number;
  /**
   * auto offloads large results; artifact always returns an artifact; memory stores in hosted Memory; inline is bounded.
   */
  delivery?: "auto" | "inline" | "artifact" | "memory";
  /**
   * Collect media from static plus rendered page content, collapse responsive variants, attach bounded previews, and create an owner-scoped ZIP readable with archive_read.
   */
  preserveMedia?: boolean;
  /**
   * Save the full page content into the user's MCP Memory vault, embedded for semantic recall — the full body is NOT returned to chat.
   */
  depositToVault?: boolean;
  /**
   * Optional vault to deposit into; defaults to the personal vault.
   */
  vaultName?: string;
  /**
   * Retry key: reuse after a timeout to avoid re-billing. New key per extraction.
   */
  idempotencyKey?: string;
}

export interface Output {
  url: string;
  title: string | null;
  headings: {
    level: number;
    text: string;
  }[];
  schemaBlockCount: number;
  entityName: string | null;
  entityTypes: string[];
  /**
   * Logo declared by the selected Organization or LocalBusiness JSON-LD entity, separate from the rendered branding candidate ranking.
   */
  structuredDataLogo: string | null;
  napScore: number | null;
  missingSchemaFields: string[];
  /**
   * Bounded public contact occurrences extracted from the complete acquired document, including header and footer, while raw HTML remains omitted.
   */
  contactEvidence: {
    /**
     * @maxItems 20
     */
    emails:
      | []
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ]
      | [
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          },
          {
            value: string;
            sourceUrl: string;
            context: string;
            sourceType: "first_party_page" | "structured_data" | "provided" | "serp_snippet";
            sourceTitle?: string;
            sourcePosition?: number;
          }
        ];
    /**
     * @maxItems 20
     */
    socialProfiles:
      | []
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            network: string;
            sourceUrl: string;
            context: string;
          }
        ];
    /**
     * @maxItems 10
     */
    contactForms:
      | []
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ];
    /**
     * @maxItems 20
     */
    candidatePageUrls:
      | []
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ]
      | [
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          },
          {
            url: string;
            sourceUrl: string;
            context: string;
          }
        ];
  };
  screenshotSaved: string | null;
  /**
   * Owner-scoped private screenshot handoff created only when preserveMedia is true. Pass artifactId to image_asset_save to retain it in hosted Memory.
   */
  screenshotArtifact?: {
    artifactId: string;
    filename: string;
    contentType: string;
    bytes: number;
    sha256: string;
    expiresAt: string;
    downloadUrl: string | null;
    downloadUrlExpiresAt: string | null;
  };
  archive: {
    timestamp: string;
    originalUrl: string;
    replayUrl: string;
    rawReplayUrl: string;
  } | null;
  featuredImage: {
    url: string;
    archivedUrl: string | null;
    source: "og:image" | "twitter:image" | "json-ld" | "content-image";
  } | null;
  /**
   * Rendered brand and proof evidence. logo is the site identity, logoVariants are the same mark family, and proofImages are separately typed body trust signals. Inspect confidence and evidence rather than treating uncertain relationships as facts.
   */
  branding: {
    colorScheme: ("light" | "dark") | null;
    colors: {
      primary: string | null;
      accent: string | null;
      background: string | null;
      text: string | null;
      heading: string | null;
    };
    /**
     * Rendered provenance for each selected color so callers can distinguish explicit brand tokens and semantic elements from lower-confidence fallbacks.
     */
    colorEvidence: {
      primary: {
        value: string;
        source:
          | "css_variable"
          | "theme_color"
          | "visible_cta"
          | "navigation_background"
          | "header_svg"
          | "visible_background"
          | "body_background"
          | "body_text"
          | "heading_text";
        confidence: "high" | "medium" | "low";
        detail: string | null;
      } | null;
      accent: {
        value: string;
        source:
          | "css_variable"
          | "theme_color"
          | "visible_cta"
          | "navigation_background"
          | "header_svg"
          | "visible_background"
          | "body_background"
          | "body_text"
          | "heading_text";
        confidence: "high" | "medium" | "low";
        detail: string | null;
      } | null;
      background: {
        value: string;
        source: "body_background";
        confidence: "high" | "medium" | "low";
        detail: string | null;
      } | null;
      text: {
        value: string;
        source: "body_text";
        confidence: "high" | "medium" | "low";
        detail: string | null;
      } | null;
      heading: {
        value: string;
        source: "heading_text";
        confidence: "high" | "medium" | "low";
        detail: string | null;
      } | null;
    };
    fonts: {
      heading: string | null;
      body: string | null;
    };
    assets: {
      logo: string | null;
      favicon: string | null;
      logoConfidence: ("high" | "medium" | "low") | null;
      logoSelectionReason: string | null;
      /**
       * Responsive or original-size files from the same brand-logo family as logo; never partner, certification, award, press, or customer marks.
       */
      logoVariants: string[];
      logoCandidates: {
        url: string;
        score: number;
        confidence: "high" | "medium" | "low";
        region: "json_ld" | "header" | "nav" | "footer" | "body" | "favicon";
        evidence: string[];
        alt: string | null;
        width: number | null;
        height: number | null;
      }[];
      /**
       * Prominent body images supported by trust context, kept separate from the site logo. Classification is evidence-ranked rather than a claim that the depicted organization endorses the site.
       */
      proofImages: {
        url: string;
        proofType:
          | "certification"
          | "accreditation"
          | "award"
          | "membership"
          | "partner_or_customer"
          | "press_mention"
          | "trust_mark";
        score: number;
        confidence: "high" | "medium" | "low";
        evidence: string[];
        alt: string | null;
        context: string | null;
        width: number | null;
        height: number | null;
      }[];
    };
  } | null;
  /**
   * Backward-compatible flattened page-media inventory. Use media for completeness, warnings, and artifact delivery.
   */
  mediaAssets:
    | {
        url: string;
        type: "image" | "video" | "audio";
        mimeType: string | null;
        filename: string;
        savedPath: string | null;
        sizeBytes: number | null;
        discoveryMethods: string[];
        altTexts: string[];
        contexts: string[];
        width: number | null;
        height: number | null;
        variants: string[];
        finalUrl?: string | null;
        duplicateOf?: string | null;
        sha256?: string | null;
        downloadStatus?: "downloaded" | "failed" | "not_attempted";
        downloadError?: string | null;
        contentIndex: number | null;
      }[]
    | null;
  /**
   * Static-plus-rendered website media manifest with provenance, bounded image content-block indices, completion state, and owner-scoped ZIP delivery.
   */
  media: {
    pageUrl: string;
    staticFound: number;
    renderedFound: number;
    totalFound: number;
    filteredCount: number;
    retainedCount: number;
    completeness: "complete" | "partial";
    exhausted: boolean;
    stopReason: "page_exhausted" | "asset_limit" | "scroll_round_limit" | "render_unavailable";
    scrollRounds: number;
    warnings: string[];
    assets: {
      url: string;
      type: "image" | "video" | "audio";
      mimeType: string | null;
      filename: string;
      savedPath: string | null;
      sizeBytes: number | null;
      discoveryMethods: string[];
      altTexts: string[];
      contexts: string[];
      width: number | null;
      height: number | null;
      variants: string[];
      finalUrl?: string | null;
      duplicateOf?: string | null;
      sha256?: string | null;
      downloadStatus?: "downloaded" | "failed" | "not_attempted";
      downloadError?: string | null;
      contentIndex: number | null;
    }[];
    artifact: {
      artifactId: string;
      filename: string;
      contentType: string;
      bytes: number;
      sha256: string;
      expiresAt: string;
      downloadUrl: string | null;
      downloadUrlExpiresAt: string | null;
      localPath: string | null;
    } | null;
  } | null;
  memory?: {
    deposited: boolean;
    vault?: string;
    noteId?: string;
    path?: string;
    chunks?: number;
    fileUrl?: string;
    fileExpiresAt?: string;
    error?: string;
  };
  /**
   * Governed hosted Memory image saves, present only for delivery:"memory" with preserveMedia:true.
   */
  memoryImages?: {
    requested: number;
    saved: number;
    skipped: number;
    assets: {
      sourceUrl: string;
      sourceKind: "screenshot" | "page_image";
      saved: boolean;
      assetId?: string;
      error?: string;
    }[];
    error?: string;
  };
  delivery?: {
    requested: "auto" | "inline" | "artifact" | "memory";
    effective: "inline" | "artifact" | "memory" | "local_file";
    retained: boolean;
    nextAction: string | null;
  };
  /**
   * Server-generated local report path, present only on an installed stdio server that successfully wrote the file.
   */
  localPath?: string;
  artifact?: {
    artifactId: string;
    mimeType: string;
    sizeBytes: number;
    bytes: number;
    sha256: string;
    expiresAt: string;
    downloadUrl: string | null;
    downloadUrlExpiresAt: string | null;
    preview: string;
  };
}
