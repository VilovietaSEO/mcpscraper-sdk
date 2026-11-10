export interface Input {
  /**
   * Chrome Web Store URL of the extension to add, e.g. https://chromewebstore.google.com/detail/<slug>/<id>.
   */
  store_url: string;
  /**
   * Short name to save this extension under, e.g. "ani-ai". Reuse it later in extension_names on browser_open.
   */
  name: string;
}

export type Output =
  | {
      ok: boolean;
      tool: "browser_extension_import";
      session_id: null;
      /**
       * The name this extension was saved under.
       */
      name: string;
      /**
       * The store URL this extension was imported from.
       */
      source_url: string;
      /**
       * Size of the extension package in bytes.
       */
      size_bytes: number | null;
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
