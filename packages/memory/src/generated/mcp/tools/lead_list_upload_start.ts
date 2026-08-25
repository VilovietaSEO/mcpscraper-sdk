export interface Input {
  /**
   * Required stable key for this intended upload session. Reuse it only to retry the same upload-start call.
   */
  idempotencyKey: string;
  /**
   * Optional display-only filename. It does not determine or authorize the uploaded format.
   */
  filenameHint?: string;
}

export interface Output {
  uploadId: string;
  status?: "awaiting_upload" | "ready";
  uploadUrl: string;
  uploadPageUrl: string;
  acceptedFormats: ("csv" | "tsv" | "xlsx")[];
  acceptedContentTypes: string[];
  maxBytes: number;
  uploadUrlExpiresAt: string;
  sourceExpiresAt: string;
}
