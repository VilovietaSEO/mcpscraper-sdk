export interface Input {
  /**
   * Owner-scoped ingestId returned by gmail_import_to_memory; this status call never continues work.
   */
  ingestId: string;
}

export type Output =
  | {
      ok: boolean;
      ingest?: {
        ingestId: string;
        importPlanId: string;
        status: "pending" | "running" | "complete" | "partial" | "failed";
        messages: {
          planned: number;
          stored: number;
          indexed: number;
          failed: number;
        };
        attachments: {
          planned: number;
          stored: number;
          indexed: number;
          storedUnindexed: number;
          failed: number;
        };
        manifestStored: boolean;
        complete: boolean;
        /**
         * @maxItems 25
         */
        samples: {
          sourceKey: string;
          state: "pending" | "stored_unindexed" | "indexed" | "failed";
          path?: string;
          error?: string;
        }[];
        nextAction: "call_gmail_import_to_memory" | "call_gmail_import_status" | "complete" | "inspect_failures";
      };
      error: string | null;
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
