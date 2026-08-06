export interface Input {
  siteId: string;
  pixelId: string;
  name: string;
  /**
   * @minItems 1
   * @maxItems 30
   */
  fields: [
    {
      id: string;
      type: "text" | "email" | "tel" | "textarea" | "select" | "checkbox" | "radio" | "number";
      label: string;
      required: boolean;
      /**
       * @maxItems 30
       */
      options?: string[];
    },
    ...{
      id: string;
      type: "text" | "email" | "tel" | "textarea" | "select" | "checkbox" | "radio" | "number";
      label: string;
      required: boolean;
      /**
       * @maxItems 30
       */
      options?: string[];
    }[]
  ];
  brand: {
    primaryColor: string;
    backgroundColor: string;
    textColor: string;
    radius: number;
  };
  submitLabel?: string;
  successMessage?: string;
  consentText?: string;
  publish?: boolean;
}

export interface Output {
  ok: boolean;
}
