export interface Input {
  /**
   * Text filter applied to the selected result inventory.
   */
  query?: string;
  /**
   * Research topic used to filter sourced records.
   */
  topic?: string;
  /**
   * Optional sourced Research role to match on knowledge subjects; this is not a CRM relationship type.
   */
  role?: string;
  /**
   * Opaque continuation cursor returned by the previous page; omit for the first page.
   */
  cursor?: string;
  /**
   * Maximum rows or records to return on this page; use the returned cursor for more.
   */
  limit?: number;
}

export type Output =
  | (
      | {
          ok: boolean;
          message: string;
          items?: {
            entityId: string;
            domain: "research_person" | "research_organization" | "crm_person" | "crm_organization";
            entityKind: "person" | "organization";
            displayName: string;
            content: string;
            props: {
              [k: string]: unknown;
            };
            relationshipStatus: ("active" | "inactive" | "archived" | "merged") | null;
            relationshipTypes: (
              | "prospect"
              | "customer"
              | "former_customer"
              | "friend"
              | "coworker"
              | "collaborator"
              | "vendor"
              | "partner"
              | "advisor"
              | "media"
              | "community"
              | "other"
            )[];
            commercialLifecycle:
              ("lead" | "qualified" | "opportunity" | "customer" | "retained" | "churned" | "disqualified") | null;
            relationshipOwnerId: string | null;
            topics: string[];
            researchRoles: string[];
            revision: number;
            createdAt: string;
            updatedAt: string;
          }[];
          pageInfo?: {
            endCursor: string | null;
            hasNextPage: boolean;
          };
          code?: string;
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
        }
      | {
          idempotencyKey?: string;
          operation?: {
            runId: string | null;
            idempotencyKey: string;
            state: string;
          };
          error_code: string;
          error_type: string;
          message: string;
          retryable: boolean;
          retry_after_seconds?: number;
          charge_status?: string;
          details?: {
            [k: string]: unknown;
          };
        }
    )
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
