export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Exact durable plan returned by analytics_plan_crm_provisioning; altered plans are rejected.
   */
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
  /**
   * Exact proposed namespaced provider fields approved for creation.
   *
   * @maxItems 50
   */
  approvedFieldInternalNames: string[];
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  receipt: {
    /**
     * Durable redacted receipt identifier returned by the provider operation.
     */
    receiptId: string;
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
     * Lifecycle status used to filter or update the selected records.
     */
    status: "approved" | "tested" | "failed";
    /**
     * Exact namespaced provider fields created by the approved provisioning operation.
     *
     * @maxItems 50
     */
    createdFields: {
      /**
       * Provider object selected for this explicit CRM mapping.
       */
      object: string;
      /**
       * Provider field internal name discovered from the authorized tenant.
       */
      internalName: string;
      /**
       * Opaque provider field reference returned after field creation.
       */
      providerFieldId?: string;
    }[];
    /**
     * Existing writable provider fields already mapped to namespaced X-Ray fields.
     */
    existingMappings: {
      [k: string]: string;
    };
    /**
     * Bounded cleanup support and instructions for a provisioning test or field creation.
     */
    cleanup: {
      /**
       * Whether the provider supports the described governed operation.
       */
      supported: boolean;
      /**
       * Safe operator-facing recovery or cleanup instructions without credentials or provider bodies.
       */
      instructions: string;
    };
    /**
     * Server-computed fingerprint binding a provisioning receipt to its approved plan.
     */
    planFingerprint: string;
    /**
     * ISO 8601 timestamp when the source event actually occurred.
     */
    occurredAt: string;
    /**
     * Safe bounded error code; provider messages and record bodies are omitted.
     */
    errorCode?: string;
  };
}
