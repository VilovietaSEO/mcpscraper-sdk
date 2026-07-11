export interface Input {
  /**
   * A Slack connectionId from list_service_connections, with actionsEnabled true.
   */
  connectionId: string;
  /**
   * Slack channel ID to send to, e.g. "C1234567890". Get this from the connection's own read tools, not guessed.
   */
  channel: string;
  /**
   * Message text to send.
   */
  text: string;
}

export type Output = unknown
