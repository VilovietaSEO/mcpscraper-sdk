export interface Input {
  /**
   * Artifact id returned inline by a tool whose result was too large to inline. Use only a returned artifactId; do not construct one yourself.
   */
  artifactId: string;
  /**
   * Byte offset to start reading from. Pass the previous call's nextOffset to continue.
   */
  offset?: number;
  /**
   * Maximum bytes of artifact text to return in this window.
   */
  maxBytes?: number;
}

export type Output = unknown
