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
   * Primary Google Business Profile/brand name to match in Maps results, and the brand name looked for in assistant answers. Supply it when matching one business against Maps results or tracking ai_answers.
   */
  targetBusinessName?: string;
  /**
   * Rank tracker surfaces to build: maps, organic, ai_overview, paa, and ai_answers (whether ChatGPT, Gemini or Claude name the brand when asked a question). ai_answers is not in the default set.
   *
   * @minItems 1
   * @maxItems 5
   */
  trackingModes?:
    | ["maps" | "organic" | "ai_overview" | "paa" | "ai_answers"]
    | [
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers"
      ]
    | [
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers"
      ]
    | [
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers"
      ]
    | [
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers",
        "maps" | "organic" | "ai_overview" | "paa" | "ai_answers"
      ];
  /**
   * For ai_answers: the full-sentence questions to ask the assistants, e.g. "What is the best CRM for roofing companies?". Leave empty to derive questions from keywords downstream.
   *
   * @maxItems 200
   */
  prompts?: string[];
  /**
   * For ai_answers: which assistants to ask. chatgpt and gemini need no sign-in; claude needs a saved signed-in profile.
   *
   * @minItems 1
   * @maxItems 3
   */
  assistants?:
    | ["chatgpt" | "gemini" | "claude"]
    | ["chatgpt" | "gemini" | "claude", "chatgpt" | "gemini" | "claude"]
    | ["chatgpt" | "gemini" | "claude", "chatgpt" | "gemini" | "claude", "chatgpt" | "gemini" | "claude"];
  /**
   * For ai_answers: how many times each question is asked on each assistant in one requested batch. Answers vary between runs, so the mention rate is the share of runs that name the brand.
   */
  runsPerPrompt?: number;
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
   * Optional competitor domains or business names to persist as comparison targets. For ai_answers, competitor names are looked for in each answer beside the target brand.
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
      trackingModes: ("maps" | "organic" | "ai_overview" | "paa" | "ai_answers")[];
      assistants: ("chatgpt" | "gemini" | "claude")[];
      runsPerPrompt: number;
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
        modes: ("maps" | "organic" | "ai_overview" | "paa" | "ai_answers")[];
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
