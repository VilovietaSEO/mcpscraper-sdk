export interface Input {
  /**
   * Exact memory note path or resolvable note reference used as the graph target.
   */
  note: string;
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
}

export interface Output {
  ok: boolean;
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
