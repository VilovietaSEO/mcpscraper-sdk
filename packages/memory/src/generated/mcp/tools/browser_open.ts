export interface Input {
  /**
   * Optional human label for this session, shown in the watch console.
   */
  label?: string;
  /**
   * Optional URL to navigate to immediately after opening.
   */
  url?: string;
  /**
   * Optional saved hosted profile name to load a logged-in session for a site.
   */
  profile?: string;
  /**
   * Optional persistent SERP identity. Loads its saved browser state and fixed network identity; do not combine with profile.
   */
  serp_identity?: string;
  /**
   * Persist cookies/storage back to the named profile on close. Avoid parallel sessions writing to the same profile.
   */
  save_profile_changes?: boolean;
  /**
   * Session lifetime before auto-termination. Defaults to 600 and cannot exceed 600.
   */
  timeout_seconds?: number;
  /**
   * Names of extensions previously added with browser_extension_import (see browser_extension_list for what's available) to load into this session. Loading extensions restarts the browser, adding a few seconds to startup.
   */
  extension_names?: string[];
}

export type Output =
  | {
      ok: boolean;
      tool: "browser_open";
      /**
       * Session id returned by browser_open. Use only this exact value in later browser_* calls; do not construct one yourself.
       */
      session_id: string;
      /**
       * Human watch/takeover URL for this browser session on mcpscraper.dev.
       */
      watch_url: string;
      /**
       * Deprecated; always null. Open watch_url to view the live session.
       */
      live_view_url: string | null;
      /**
       * Initial URL requested by the caller, when provided.
       */
      url: string | null;
      hint: string;
      raw?: {
        [k: string]: unknown;
      };
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
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
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
