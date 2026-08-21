export interface Input {
  /**
   * Public https image URL to download and host. The wiki never serves a third-party URL directly, so pass the original source here rather than putting it on the entity.
   */
  sourceUrl?: string;
  /**
   * Base64 image bytes for an image you already hold. Use for images under about 3 MB; larger files should be published from a URL.
   */
  imageBase64?: string;
  /**
   * Alt text describing the image for readers who cannot see it.
   */
  alt?: string;
  /**
   * License or usage terms of the original image, preserved with the hosted copy.
   */
  license?: string;
  /**
   * Credit line for the original photographer, publication, or archive.
   */
  attribution?: string;
}

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
