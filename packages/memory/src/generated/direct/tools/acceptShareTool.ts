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
   * The shareId from note-inbox to accept.
   */
  shareId: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * The accepted share.
   */
  shareId?: string;
  /**
   * Identity who shared the note.
   */
  owner?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
