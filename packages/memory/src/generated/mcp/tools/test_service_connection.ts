export interface Input {
  /**
   * A tenant-owned connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * Optional provider hint from list_service_connections.
   */
  providerConfigKey?: string;
}

export type Output = unknown
