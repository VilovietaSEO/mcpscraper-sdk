export interface Input {
  /**
   * Site export job ID returned by extract_site, analyze_site_similarity, or audit_site.
   */
  jobId: string;
  /**
   * Downloaded image ID returned by a site_export_read manifest.
   */
  imageId: string;
}

export interface Output {
  jobId: string;
  imageId: string;
  sourcePage?: string | null;
  sourceUrl?: string | null;
  mimeType: string;
  bytes: number;
  sha256?: string | null;
}
