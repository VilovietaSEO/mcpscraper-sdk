export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Analytics Pixel id belonging to the selected Site.
   */
  pixelId: string;
  /**
   * Human-readable name for the record being created or updated.
   */
  name: string;
  /**
   * Ordered form-field definitions to render and validate for submissions.
   *
   * @minItems 1
   * @maxItems 30
   */
  fields: [
    {
      /**
       * Stable identifier for this nested record.
       */
      id: string;
      /**
       * Governed content or record type used for routing and validation.
       */
      type: "text" | "email" | "tel" | "textarea" | "select" | "checkbox" | "radio" | "number";
      /**
       * Human-readable label displayed for this field, link, or section.
       */
      label: string;
      /**
       * Whether the form field must be completed before submission.
       */
      required: boolean;
      /**
       * Allowed selectable values for this form field.
       *
       * @maxItems 30
       */
      options?: string[];
    },
    ...{
      /**
       * Stable identifier for this nested record.
       */
      id: string;
      /**
       * Governed content or record type used for routing and validation.
       */
      type: "text" | "email" | "tel" | "textarea" | "select" | "checkbox" | "radio" | "number";
      /**
       * Human-readable label displayed for this field, link, or section.
       */
      label: string;
      /**
       * Whether the form field must be completed before submission.
       */
      required: boolean;
      /**
       * Allowed selectable values for this form field.
       *
       * @maxItems 30
       */
      options?: string[];
    }[]
  ];
  /**
   * Validated visual-brand settings applied to the generated form.
   */
  brand: {
    /**
     * Six-digit hexadecimal primary action color for the rendered form.
     */
    primaryColor: string;
    /**
     * Six-digit hexadecimal background color for the rendered form.
     */
    backgroundColor: string;
    /**
     * Six-digit hexadecimal text color for the rendered form.
     */
    textColor: string;
    /**
     * Corner radius in pixels for rendered form controls.
     */
    radius: number;
  };
  /**
   * Optional text displayed on the form submission button.
   */
  submitLabel?: string;
  /**
   * Optional confirmation shown after a successful form submission.
   */
  successMessage?: string;
  /**
   * Optional consent disclosure displayed with the form submission control.
   */
  consentText?: string;
  /**
   * When true, publish the created form immediately; set false to keep it unpublished.
   */
  publish?: boolean;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: boolean;
      form: {
        [k: string]: unknown;
      };
    }
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
