export interface Input {
  /**
   * Opaque scheduled-run identifier returned by a scheduled-results tool.
   */
  runId: string;
  /**
   * Opaque artifact identifier returned by the creating or listing tool.
   */
  artifactId: string;
  /**
   * Requested view-link lifetime in days; the server enforces its maximum.
   */
  expiresInDays?: number;
}

export interface Output {
  ok: boolean;
  shareId?: string;
  /**
   * Opaque scheduled-run identifier returned by a scheduled-results tool.
   */
  runId?: string;
  artifactId?: string;
  url?: string;
  expiresAt?: string;
  createdAt?: string;
  error?: string;
  errorCode?:
    | "invalid_request"
    | "not_found"
    | "conflict"
    | "template_archived"
    | "renderer_unavailable"
    | "artifact_unavailable"
    | "view_link_unavailable"
    | "internal_error";
  requestId?: string;
}
