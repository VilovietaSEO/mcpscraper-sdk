export interface Input {
  /**
   * Set true only when the person explicitly authorized sending this exact email. If omitted, a 2026-capable client may ask for confirmation.
   */
  confirmed?: boolean;
  /**
   * Required stable key for this intended email. Reuse it only when retrying the same send after a lost response.
   */
  idempotencyKey: string;
  /**
   * A Gmail connectionId from list_service_connections, with actionsEnabled true.
   */
  connectionId: string;
  /**
   * Recipient email address.
   */
  to: string;
  /**
   * Email subject line.
   */
  subject: string;
  /**
   * Plain-text email body.
   */
  body: string;
}

export interface Output {
  ok: boolean;
  result?: unknown;
  error: string | null;
}
