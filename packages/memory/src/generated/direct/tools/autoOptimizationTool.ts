export interface Input {
  apiKey?: string;
  sessionId?: string;
  /**
   * Omit to read the current setting. off stops automatic runs entirely; deterministic suggests using rules only and never charges; full adds AI judging and does charge.
   */
  mode?: "off" | "deterministic" | "full";
}

export interface Output {
  ok: boolean;
  mode?: string;
  changed?: boolean;
  costsCredits?: boolean;
  options?: {
    [k: string]: string;
  };
  error?: string;
}
