export interface Input {
  /**
   * Webhook id, from list-webhooks.
   */
  id: string;
}

export interface Output {
  ok: boolean;
  revoked?: boolean;
  error?: string;
}
