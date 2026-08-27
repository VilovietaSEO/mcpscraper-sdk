export interface Input {
  /**
   * Public HTTPS direct image URL or webpage URL. A direct image is hosted as-is; an HTML page is inspected for Open Graph, Twitter, JSON-LD, and meaningful content images, then the first usable candidate is hosted. Temporary signed URLs are consumed immediately and query credentials are not retained as provenance.
   */
  sourceUrl?: string;
  /**
   * Base64 image bytes for an image already available to the caller, including a pasted attachment or AI-generated image. Use sourceType to preserve whether it was uploaded or generated. Keep the complete serialized request within the client transport limit.
   */
  imageBase64?: string;
  /**
   * Owner-scoped image artifact returned by an MCP Scraper media or screenshot workflow. The server reauthorizes ownership and reads the bytes directly; do not construct an artifact ID.
   */
  artifactId?: string;
  /**
   * Provenance for imageBase64 or artifactId. Use ai_generated only when an image model created the supplied bytes; otherwise use uploaded or omit it.
   */
  sourceType?: "uploaded" | "ai_generated";
  /**
   * Alt text describing the image for readers who cannot see it.
   */
  alt?: string;
  /**
   * License or usage terms of the original image, preserved with the hosted copy.
   */
  license?: string;
  /**
   * Credit line for the original photographer, publication, or archive.
   */
  attribution?: string;
}

export interface Output {
  ok: boolean;
  data?: {
    /**
     * Stable Commons image ID.
     */
    id: string;
    /**
     * Permanent Commons URL to use as featuredImage.url.
     */
    url: string;
    contentType: "image/jpeg" | "image/png" | "image/gif" | "image/webp";
    bytes: number;
    digest: string;
    /**
     * Sanitized direct asset URL that supplied the hosted bytes, when applicable.
     */
    sourceUrl: string | null;
    /**
     * Sanitized webpage URL from which the image was discovered, when applicable.
     */
    sourcePageUrl: string | null;
    sourceKind: "uploaded" | "ai_generated" | "artifact" | "direct_url" | "webpage" | "registered";
    selectionSource:
      | "provided_bytes"
      | "artifact"
      | "direct_url"
      | "og:image"
      | "twitter:image"
      | "json-ld"
      | "content-image"
      | "registered";
    /**
     * True when identical image bytes were already stored.
     */
    reused: boolean;
  };
  error?: string;
  message?: string;
}
