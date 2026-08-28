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
   * Table name to permanently delete, from table-list.
   */
  tableName: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope error.
   */
  ok: boolean;
  /**
   * True if the table existed and was dropped; false if it did not exist.
   */
  dropped?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
