export interface Input {
  /**
   * Existing governed entity identifier for this relation or edit.
   */
  entityId?: string;
  /**
   * Use 0 to create a Research Person; for an edit, supply the current positive revision read from research-person-get.
   */
  baseRevision: number;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.
   */
  displayName: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content?: string;
  /**
   * One or more cited source references supporting this Research capture.
   *
   * @minItems 1
   * @maxItems 100
   */
  sourceEvidence: [
    {
      /**
       * Source URL, retained artifact reference, or other source identifier supporting the Research evidence or field provenance.
       */
      sourceRef: string;
      /**
       * Bounded factual claim supported by the accompanying Research source reference.
       */
      claim?: string;
    },
    ...{
      /**
       * Source URL, retained artifact reference, or other source identifier supporting the Research evidence or field provenance.
       */
      sourceRef: string;
      /**
       * Bounded factual claim supported by the accompanying Research source reference.
       */
      claim?: string;
    }[]
  ];
  /**
   * Research topics supported by the captured source evidence.
   *
   * @maxItems 100
   */
  topics?: string[];
  /**
   * Sourced roles associated with this Research subject.
   *
   * @maxItems 100
   */
  researchRoles?: string[];
  /**
   * Complete governed note properties required by the target vault contract.
   */
  props?: {
    [k: string]: unknown;
  };
  /**
   * Field authority, sensitivity, source, observation time, and confidence recorded with this governed write.
   */
  lineage: {
    /**
     * Source authority or ownership context supporting this content.
     */
    authority?: "memory_manual" | "memory_agent" | "connected_source" | "crm_import" | "xray_derived";
    /**
     * Governed field sensitivity: public, internal, personal, or restricted.
     */
    sensitivity: "public" | "internal" | "personal" | "restricted";
    /**
     * Source URL, retained artifact reference, or other source identifier supporting the Research evidence or field provenance.
     */
    sourceRef?: string | null;
    /**
     * ISO 8601 timestamp when this source or governed value was observed.
     */
    observedAt: string;
    /**
     * Bounded confidence value for the supplied assertion.
     */
    confidence?: number | null;
  };
}

export type Output =
  | (
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
          receipt?: {
            receiptId: string;
            replayed?: boolean;
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
