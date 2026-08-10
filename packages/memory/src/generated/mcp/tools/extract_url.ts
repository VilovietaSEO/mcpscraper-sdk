export interface Input {
  /**
   * Public http/https URL to extract.
   */
  url: string;
  /**
   * Capture a full-page screenshot and return it through the result contract. Large captures may be offloaded to an owned artifact.
   */
  screenshot?: boolean;
  /**
   * Viewport for screenshot. desktop = 1440×900, mobile = 390×844.
   */
  screenshotDevice?: "desktop" | "mobile";
  /**
   * Extract brand colors, fonts, logo, and favicon via a rendered browser session.
   */
  extractBranding?: boolean;
  /**
   * Return the best featured image from Open Graph, Twitter, JSON-LD, or page content. For Wayback replay URLs, also returns the timestamp-matched archived image URL when available.
   */
  includeFeaturedImage?: boolean;
  /**
   * Deprecated alias for preserveMedia. Omit when using preserveMedia; when omitted, media preservation defaults to false.
   */
  downloadMedia?: boolean;
  /**
   * Which media types to download. Default all three.
   */
  mediaTypes?: ("image" | "video" | "audio")[];
  /**
   * Maximum media records to retain and attempt to download after filtering and responsive-variant collapse.
   */
  maxMediaAssets?: number;
  /**
   * Maximum downloaded images to attach as AI-readable image content blocks. All successfully downloaded media remains available in the ZIP.
   */
  maxInlineImages?: number;
  /**
   * Where to deliver the result. auto keeps small results inline and offloads large ones; artifact always returns an owned artifact; memory stores the full page in hosted Memory; inline returns a bounded response.
   */
  delivery?: "auto" | "inline" | "artifact" | "memory";
  /**
   * Collect media from static source plus a rendered, lazy-loaded page; collapse responsive variants; return provenance and completeness; attach bounded image previews; and create an owner-scoped ZIP readable with archive_read.
   */
  preserveMedia?: boolean;
  /**
   * Save the full page content into the user's MCP Memory vault server-side, embedded for semantic recall — the full body is NOT returned to chat.
   */
  depositToVault?: boolean;
  /**
   * Optional vault to deposit into. Defaults to the user's personal vault.
   */
  vaultName?: string;
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
