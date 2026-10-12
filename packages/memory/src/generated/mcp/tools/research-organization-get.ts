export interface Input {
  /**
   * Existing governed entity identifier for this relation or edit.
   */
  entityId: string;
}

export type Output =
  | {
      ok: boolean;
      message: string;
      record?: {
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
      };
      aliases?: string[];
      associations?: {
        [k: string]: unknown;
      }[];
      counterpartEntityId?: string | null;
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
    };
