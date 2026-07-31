export interface Input {
  runId: string;
  shareId: string;
}

export type Output = {
  [k: string]: unknown;
} & {
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
};
