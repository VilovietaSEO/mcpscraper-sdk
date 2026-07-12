export interface Input {
  /**
   * Private artifactId returned by export_connected_service_data.
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
