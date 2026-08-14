export interface Input {
  /**
   * Exact memory note path or resolvable note reference used as the graph target.
   */
  note: string;
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * Maximum graph traversal depth from the root note.
   */
  depth?: number;
  /**
   * Maximum graph nodes to return before marking the result truncated.
   */
  maxNodes?: number;
}

export interface Output {
  ok: boolean;
  root?: string;
  depth?: number;
  truncated?: boolean;
  nodes?: {
    id: string;
    vault: string;
    path: string;
    title: string;
    resolved: boolean;
  }[];
  edges?: {
    source: string;
    target: string;
    type: string;
    evidence: string;
    sourceField: string;
    resolved: boolean;
  }[];
  error?: string;
}
