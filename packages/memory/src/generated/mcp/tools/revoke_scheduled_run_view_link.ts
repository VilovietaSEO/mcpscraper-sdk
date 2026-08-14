export interface Input {
  /**
   * Opaque scheduled-run identifier returned by a scheduled-results tool.
   */
  runId: string;
  /**
   * Opaque revocable share identifier returned when the view link was created.
   */
  shareId: string;
}

export interface Output {
  ok: boolean;
  revoked?: true;
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
