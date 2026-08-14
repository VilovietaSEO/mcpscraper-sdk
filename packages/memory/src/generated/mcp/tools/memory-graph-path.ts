export interface Input {
  /**
   * Exact starting memory note path or resolvable note reference.
   */
  from: string;
  /**
   * Exact destination memory note path or resolvable note reference.
   */
  to: string;
  /**
   * Vault containing the starting memory note; omit only when the note reference already resolves unambiguously.
   */
  fromVault?: string;
  /**
   * Vault containing the destination memory note; omit only when the note reference already resolves unambiguously.
   */
  toVault?: string;
  /**
   * Maximum number of graph edges to traverse before reporting no path.
   */
  maxDepth?: number;
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
