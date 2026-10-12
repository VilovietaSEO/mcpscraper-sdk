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

export type Output =
  | {
      ok: boolean;
      definition: {
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
