export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * The vault (channel) to list members of. You must own it.
   */
  vault: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope/ownership error.
   */
  ok: boolean;
  /**
   * The channel owner.
   */
  owner?: string;
  /**
   * True if the caller is the owner (and so can call remove-channel-member).
   */
  canManage?: boolean;
  /**
   * Present when ok is true. Always includes at least the owner.
   */
  members?: {
    /**
     * The member, including the owner.
     */
    identity: string;
    /**
     * Permissions this member has.
     */
    scope: {
      read: boolean;
      write: boolean;
      export: boolean;
      index: boolean;
      admin: boolean;
      swap: boolean;
    };
    /**
     * When they were added.
     */
    since: string;
    /**
     * True if this identity has flagged itself as an AI agent (set-agent-identity).
     */
    isAgent: boolean;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
