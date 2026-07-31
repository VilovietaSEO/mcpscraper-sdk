export interface Input {
  runId: string;
  artifactId: string;
  expiresInDays?: number;
}

export type Output = {
  [k: string]: unknown;
} & {
  ok: boolean;
  shareId?: string;
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
};
