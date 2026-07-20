export interface Input {
  /**
   * Caller API key. Optional when the MCP session is authenticated.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Exact logical vault handle to search. Omit to search every entitled vault.
   */
  vault?: string;
  /**
   * A focused semantic reformulation of the request.
   */
  query: string;
  /**
   * Original human wording. Used as a distinct query variant when useful and logged for quality review.
   */
  userMessage?: string;
  /**
   * Caller-provided focused query variants. The planner deduplicates these with query, original wording, and tag/entity terms.
   *
   * @minItems 2
   * @maxItems 4
   */
  queries?: [string, string] | [string, string, string] | [string, string, string, string];
  /**
   * Named entities or exact terms used to form a focused query variant.
   *
   * @maxItems 20
   */
  entities?:
    | []
    | [string]
    | [string, string]
    | [string, string, string]
    | [string, string, string, string]
    | [string, string, string, string, string]
    | [string, string, string, string, string, string]
    | [string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string, string, string]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ];
  /**
   * Exact canonical tags used for tag-channel retrieval and filtering.
   *
   * @maxItems 20
   */
  tags?:
    | []
    | [string]
    | [string, string]
    | [string, string, string]
    | [string, string, string, string]
    | [string, string, string, string, string]
    | [string, string, string, string, string, string]
    | [string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string, string, string]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ];
  /**
   * Whether a note must match any or all supplied tags. Default any.
   */
  tagMode?: "any" | "all";
  /**
   * Exact persisted note-kind filter.
   */
  kind?: "note" | "library" | "capture" | "decision" | "message";
  /**
   * Exact props.type filter.
   */
  type?: string;
  /**
   * Inclusive lower bound for note updatedAt.
   */
  dateFrom?: string;
  /**
   * Inclusive upper bound for note updatedAt.
   */
  dateTo?: string;
  /**
   * Exact equality filters for primitive note props.
   */
  metadata?: {
    [k: string]: string | number | boolean;
  };
  /**
   * Number of variants. Default 3.
   */
  queryVariantCount?: number;
  /**
   * Total fused candidates before final reranking. Default 50.
   */
  candidatePool?: number;
  /**
   * Strong preliminary notes whose graph neighborhoods are considered. Default 8.
   */
  graphSeedCount?: number;
  /**
   * Graph expansion depth. Bounded to exactly one hop.
   */
  graphDepth?: 1;
  /**
   * Maximum outgoing-link plus backlink neighbors per seed. Default 5.
   */
  graphNeighborsPerSeed?: number;
  /**
   * Final results retained after Jina reranking. Default 30.
   */
  rerankTopN?: number;
  /**
   * Deprecated compatibility alias for rerankTopN. Prefer rerankTopN; default remains 30.
   */
  topK?: number;
  /**
   * Also search individually accepted shares. Default true. Exact note metadata filters exclude shares without accessible metadata.
   */
  includeShared?: boolean;
}

export interface Output {
  ok: boolean;
  vault?: string;
  vaultsSearched?: string[];
  planner?: {
    queryVariants: string[];
    candidatePool: number;
    graphSeedCount: number;
    graphDepth: number;
    graphNeighborsPerSeed: number;
    rerankTopN: number;
    seeds: string[];
    graphCandidatesAdded: number;
  };
  rerank?: {
    applied: boolean;
    provider: string;
    fallbackReason?: string;
  };
  results?: {
    text: string;
    source: string;
    score: number;
    originalScore: number;
    rerankScore?: number;
    vault?: string;
    sharedBy?: string;
    shareId?: string;
    matchChannels: ("semantic" | "tag" | "metadata" | "graph")[];
    matchedQueries: string[];
    graphFrom: string[];
  }[];
  error?: string;
}
