export interface Input {
  /**
   * Canonical tag name to create or curate.
   */
  tag: string;
  /**
   * Human-readable summary that distinguishes this record from similarly named records.
   */
  description?: string;
  /**
   * Alternative spellings that should resolve to this canonical value.
   */
  aliases?: string[];
  /**
   * Lifecycle status used to filter or update the selected records.
   */
  status?: "active" | "deprecated";
}

export type Output =
  | {
      ok: boolean;
      tag?: {
        tag: string;
        description: string | null;
        aliases: string[];
        status: "active" | "deprecated";
      };
      error?: string;
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
