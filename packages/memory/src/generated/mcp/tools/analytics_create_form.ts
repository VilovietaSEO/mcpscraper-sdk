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
}

export interface Output {
  ok: boolean;
}
