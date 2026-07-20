export interface Input {
  /**
   * A tenant-owned connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * One exact name from that connection's readTools or actionTools. Admin-blocked and arbitrary names are rejected.
   */
  tool: string;
  /**
   * Bypass the short-lived sanitized schema cache. Ownership, connection state, and tool policy are still rechecked; use only when a provider tool catalog just changed.
   */
  fresh?: boolean;
}

export type Output = unknown
