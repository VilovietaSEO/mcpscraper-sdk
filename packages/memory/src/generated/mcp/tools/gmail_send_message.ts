export interface Input {
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

export type Output = unknown
