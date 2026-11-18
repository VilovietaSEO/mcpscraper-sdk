export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  /**
   * Label identifying the form connection and its submission history.
   */
  name: string;
  /**
   * Map CRM destination fields to existing input names or provider payload paths.
   */
  mapping: {
    /**
     * Source field path containing the full contact name; use this or firstName.
     */
    name?: string;
    /**
     * Source field path containing the first name when no full-name field is mapped.
     */
    firstName?: string;
    /**
     * Source field path containing the optional last name.
     */
    lastName?: string;
    /**
     * Source field path containing an email address; map email or phone.
     */
    email?: string;
    /**
     * Source field path containing a phone number; map email or phone.
     */
    phone?: string;
    /**
     * Source field path containing a company label; this does not create an organization.
     */
    company?: string;
    /**
     * Source field path containing the inquiry text to retain in submission history.
     */
    message?: string;
    /**
     * Provider payload path containing its stable submission or event ID; otherwise send _submission_id or Idempotency-Key.
     */
    submissionId?: string;
    /**
     * Additional explicitly selected fields to retain in submission history; unmapped values are discarded.
     *
     * @maxItems 20
     */
    custom?:
      | []
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ]
      | [
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          },
          {
            /**
             * Readable label for this selected value in submission history.
             */
            label: string;
            /**
             * Source field path whose scalar value should be retained.
             */
            field: string;
          }
        ];
  };
  /**
   * Exact HTTPS website origins permitted to submit from a browser, without paths or trailing slashes.
   *
   * @minItems 1
   * @maxItems 10
   */
  allowedOrigins:
    | [string]
    | [string, string]
    | [string, string, string]
    | [string, string, string, string]
    | [string, string, string, string, string]
    | [string, string, string, string, string, string]
    | [string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string];
  /**
   * Relationship type for newly created contacts; existing contacts retain their managed fields.
   */
  relationshipType?:
    | "prospect"
    | "customer"
    | "friend"
    | "coworker"
    | "collaborator"
    | "vendor"
    | "partner"
    | "advisor"
    | "media"
    | "community"
    | "other";
  /**
   * Stable setup key; reuse unchanged arguments after an unknown result.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: boolean;
      message: string;
      code?: string;
      error?: string;
      result?: {
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
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
