export interface Input {
  /**
   * Site export job ID returned by extract_site or audit_site.
   */
  jobId: string;
  /**
   * Page ID returned by a manifest read. Omit to list the export manifest.
   */
  pageId?: string;
  /**
   * manifest lists page/image IDs; JSON, HTML, and Markdown read one page representation.
   */
  format?: "manifest" | "json" | "html" | "markdown";
  /**
   * UTF-8 byte offset. Continue from nextOffset until it is null.
   */
  offset?: number;
  /**
   * Maximum UTF-8 bytes returned in this window.
   */
  maxBytes?: number;
}

export interface Output {
  jobId: string;
  pageId: string | null;
  format: "manifest" | "json" | "html" | "markdown";
  sha256: string;
  text: string;
  offset: number;
  totalBytes: number;
  nextOffset: number | null;
}
