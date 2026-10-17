export interface Input {
  /**
   * Optional name for the rank tracker project, client, or campaign.
   */
  projectName?: string;
  /**
   * Primary domain to track in organic results, AI Overview citations, and PAA sources.
   */
  targetDomain?: string;
  /**
   * Primary Google Business Profile/brand name to match in Maps results. Supply it when matching one business against Maps results.
   */
  targetBusinessName?: string;
  /**
   * Rank tracker surfaces to build: maps, organic, ai_overview, paa.
   *
   * @minItems 1
   * @maxItems 4
   */
  trackingModes?:
    | ["maps" | "organic" | "ai_overview" | "paa"]
    | ["maps" | "organic" | "ai_overview" | "paa", "maps" | "organic" | "ai_overview" | "paa"]
    | [
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa"
      ]
    | [
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa"
      ];
  /**
   * Seed keywords or service queries to track. Leave empty to derive from user input downstream.
   *
   * @maxItems 200
   */
  keywords?: string[];
  /**
   * Markets, cities, ZIPs, or service areas to track, e.g. "Denver, CO".
   *
   * @maxItems 100
   */
  locations?: string[];
  /**
   * Optional competitor domains or business names to persist as comparison targets.
   *
   * @maxItems 100
   */
  competitors?: string[];
  /**
   * Database family to target when generating migrations.
   */
  database?: "postgres" | "neon" | "supabase" | "sqlite" | "mysql";
  /**
   * Include dashboard/reporting requirements.
   */
  includeDashboard?: boolean;
  /**
   * Include saved change findings when manually comparing rank movement and SERP features.
   */
  includeAlerts?: boolean;
  /**
   * Extra product, client, stack, or hosting requirements.
   */
  notes?: string;
}

export type Output =
  | {
      projectName: string;
      targetDomain: string | null;
      targetBusinessName: string | null;
      trackingModes: ("maps" | "organic" | "ai_overview" | "paa")[];
      database: string;
      recommendedTools: {
        tool: string;
        purpose: string;
      }[];
      tables: {
        name: string;
        purpose: string;
        keyColumns: string[];
      }[];
      steps: {
        name: string;
        purpose: string;
        modes: ("maps" | "organic" | "ai_overview" | "paa")[];
        recommendedTools: string[];
      }[];
      metrics: string[];
      implementationPrompt: string;
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
