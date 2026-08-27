export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Supported CRM provider.
   */
  provider: "hubspot" | "salesforce" | "highlevel" | "zoho" | "pipedrive" | "keap";
  /**
   * Existing service connection reference for tenant-specific discovery.
   */
  connectionId: string;
  /**
   * Discovered tenant fields used to build a no-write preview.
   *
   * @maxItems 5000
   */
  fields: {
    /**
     * Provider object name.
     */
    object: string;
    /**
     * Provider field internal name.
     */
    internalName: string;
    /**
     * Provider field label.
     */
    label: string;
    /**
     * Provider field type.
     */
    type: "string" | "number" | "datetime" | "url" | "boolean";
    /**
     * Whether discovery says the field is writable.
     */
    writable: boolean;
    /**
     * Whether the provider requires the field.
     */
    required?: boolean;
  }[];
  /**
   * Tenant-discovered operations; these may narrow but never widen the public provider profile.
   *
   * @maxItems 100
   */
  allowedOperations?: string[];
}

export interface Output {
  ok: boolean;
  plan: {
    /**
     * Durable CRM provisioning-plan identifier returned by the planning operation.
     */
    planId: string;
    /**
     * Supported phone, CRM, or advertising provider for this governed connection.
     */
    provider: "hubspot" | "salesforce" | "highlevel" | "zoho" | "pipedrive" | "keap";
    /**
     * Existing authorized service-connection reference; never supply credentials or tokens.
     */
    connectionId: string;
    /**
     * Authorized provider object that stores confirmed people.
     */
    personObject: string;
    /**
     * Existing writable provider fields already mapped to namespaced X-Ray fields.
     */
    existingMappings: {
      [k: string]: string;
    };
    /**
     * Missing namespaced fields proposed by the no-write provisioning plan.
     *
     * @maxItems 50
     */
    proposedFields: {
      /**
       * Provider object selected for this explicit CRM mapping.
       */
      object: string;
      /**
       * Provider field internal name discovered from the authorized tenant.
       */
      internalName: string;
      /**
       * Human-readable label displayed for this field, link, or section.
       */
      label: string;
      /**
       * Governed content or record type used for routing and validation.
       */
      type: "string" | "number" | "datetime" | "url" | "boolean";
      /**
       * Whether the authorized tenant reports this provider field as writable.
       */
      writable: boolean;
      /**
       * Whether the form field must be completed before submission.
       */
      required?: boolean;
    }[];
    /**
     * Safe provider activity or note fallback selected by the canonical provider contract.
     */
    fallback: "note" | "activity";
    /**
     * Provider permissions required before approving this exact plan.
     *
     * @maxItems 50
     */
    permissionRequirements: string[];
    /**
     * Tenant schema fingerprint bound to the tested provisioning receipt.
     */
    schemaFingerprint: string;
    /**
     * Server-computed immutable request fingerprint used to detect conflicting reuse.
     */
    requestFingerprint: string;
    /**
     * ISO 8601 creation time recorded by the server.
     */
    createdAt: string;
  };
  reused: boolean;
}
