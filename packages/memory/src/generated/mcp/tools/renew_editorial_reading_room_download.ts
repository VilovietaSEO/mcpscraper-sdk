export interface Input {
  /**
   * Private artifactId returned by create_editorial_reading_room.
   */
  artifactId: string;
}

export interface Output {
  ok: boolean;
  artifactId: string;
  downloadUrl: string;
  downloadUrlExpiresAt: string;
  expiresAt: string;
}
