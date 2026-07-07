export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Vault to record the fact in. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * The thing the fact is about (e.g. "db preference"). Canonicalized (lowercased/trimmed) to a stable key.
   */
  subject: string;
  /**
   * The current asserted value or conclusion for the subject (e.g. "Postgres").
   */
  value: string;
  /**
   * Where the fact came from: user / tool / chat / library:… . Optional; drives the source-priority precedence policy.
   */
  source?: string;
  /**
   * Salience/confidence in 0..1 on write. Optional; defaults to 0.5.
   */
  confidence?: number;
  /**
   * Why this assertion replaces the previous one — the audit reason recorded on the superseded fact. Optional; a default is used.
   */
  reason?: string;
}

export interface Output {
  /**
   * True when the fact was recorded (whether or not it superseded one); false on auth/scope/validation error.
   */
  ok: boolean;
  /**
   * The new (or refreshed) active fact. Present when ok is true.
   */
  fact?: {
    /**
     * Stable id of the fact.
     */
    id: string;
    /**
     * Canonical subject key the fact is about (lowercased/trimmed).
     */
    subject: string;
    /**
     * The asserted value/conclusion.
     */
    value: string;
    /**
     * Where the fact came from (chat / library:… / tool / user).
     */
    source: string;
    /**
     * Salience/confidence 0..1 recorded on write.
     */
    confidence: number;
    /**
     * "active" for the current truth, "superseded" once replaced.
     */
    status: "active" | "superseded";
    /**
     * Why this fact was superseded; null while active.
     */
    resolution: string | null;
    /**
     * Which policy decided supersession (recency/source-priority/intent-aware); null while active.
     */
    precedence: string | null;
    /**
     * ISO-8601 creation timestamp.
     */
    createdAt: string;
    /**
     * ISO-8601 last-update timestamp.
     */
    updatedAt: string;
  };
  superseded?: Fact;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
/**
 * The previously-active fact that this one replaced, with its resolution/precedence. Absent on an idempotent no-op or first assertion.
 */
export interface Fact {
  /**
   * Stable id of the fact.
   */
  id: string;
  /**
   * Canonical subject key the fact is about (lowercased/trimmed).
   */
  subject: string;
  /**
   * The asserted value/conclusion.
   */
  value: string;
  /**
   * Where the fact came from (chat / library:… / tool / user).
   */
  source: string;
  /**
   * Salience/confidence 0..1 recorded on write.
   */
  confidence: number;
  /**
   * "active" for the current truth, "superseded" once replaced.
   */
  status: "active" | "superseded";
  /**
   * Why this fact was superseded; null while active.
   */
  resolution: string | null;
  /**
   * Which policy decided supersession (recency/source-priority/intent-aware); null while active.
   */
  precedence: string | null;
  /**
   * ISO-8601 creation timestamp.
   */
  createdAt: string;
  /**
   * ISO-8601 last-update timestamp.
   */
  updatedAt: string;
}
