export interface Input {
  /**
   * A tenant-owned connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * The exact providerConfigKey returned with that connection. It is matched together with connectionId against the authenticated caller.
   */
  providerConfigKey: string;
  /**
   * One exact current readTools entry for that connection. Actions, admin tools, and unlisted names are rejected.
   */
  tool: string;
  /**
   * JSON arguments for one bounded provider read. The serialized object may be at most 64 KiB.
   */
  args?: {
    [k: string]: unknown;
  };
  /**
   * An existing ordinary Memory vault the caller can write and index. Secure and channel vaults are rejected because this tool creates searchable RAG content.
   */
  vault: string;
  /**
   * Optional human-readable snapshot title. The server always chooses the stable storage path.
   */
  title?: string;
}

export type Output = unknown
