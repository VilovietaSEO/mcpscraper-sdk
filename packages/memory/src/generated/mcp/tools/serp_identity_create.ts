export interface Input {
  /**
   * Stable caller-facing name, e.g. google-us-primary.
   */
  name: string;
  /**
   * Two-letter country for the static network identity. Defaults to US.
   */
  country?: string;
}

export type Output =
  | {
      ok: boolean;
      tool: "serp_identity_create";
      /**
       * Live Google takeover session opened on the new persistent identity.
       */
      session_id: string;
      /**
       * Give this URL to the user so they can clear consent or CAPTCHA directly on google.com.
       */
      watch_url: string;
      url: "https://www.google.com/";
      identity: {
        name: string;
        country: string;
        proxy_type: "static_isp";
        profile_persistence: "cookies_and_storage";
        ip_persistence: "fixed_for_identity_lifetime";
        status: "ready" | "deleting" | "error";
        created_at: string;
        last_used_at: string | null;
      };
      next_steps: string[];
    }
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
