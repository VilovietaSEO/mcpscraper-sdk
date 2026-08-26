export interface Input {
  /**
   * Stable direct public HTTPS URL whose response is the image bytes to host. Do not pass an HTML webpage, chat attachment reference, caller-local path, temporary or signed URL, or private/authenticated URL.
   */
  sourceUrl?: string;
  /**
   * Base64 image bytes for an image you already hold, including forwarded chat attachment bytes. Prefer this over a temporary attachment URL when the serialized request remains under about 3 MB; larger files require a stable direct public HTTPS source URL.
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
