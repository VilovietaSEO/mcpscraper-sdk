export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * The chat link. Present only the first time a link is minted for this identity.
   */
  url?: string;
  /**
   * True when a link already exists and was NOT re-shown. Use revoke-chat-link then call this again to get a fresh one.
   */
  alreadyExists?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
