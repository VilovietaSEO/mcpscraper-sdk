export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Human-readable funnel name.
   */
  name: string;
  /**
   * Ordered stage definitions.
   *
   * @minItems 2
   * @maxItems 20
   */
  stages:
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ]
    | [
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        },
        {
          /**
           * Stable stage key.
           */
          key: string;
          /**
           * Human-readable stage label.
           */
          label: string;
          /**
           * Allowlisted stage match rule; at least one matcher is required by REST.
           */
          rule: {
            /**
             * Canonical browser/server event names.
             *
             * @maxItems 100
             */
            eventNames?: string[];
            /**
             * Canonical conversion kinds.
             *
             * @maxItems 100
             */
            conversionKinds?: string[];
            /**
             * Canonical CRM/call event names.
             *
             * @maxItems 100
             */
            externalEventNames?: string[];
          };
        }
      ];
  /**
   * Make this version the Site default.
   */
  isDefault?: boolean;
  /**
   * Initial funnel status.
   */
  status?: "active" | "disabled";
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  definition: {
    [k: string]: unknown;
  };
}
