export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Unsaved funnel definition to evaluate without persistence.
   */
  definition: {
    /**
     * Draft funnel name.
     */
    name: string;
    /**
     * Ordered draft funnel stages.
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
     * Ignored by the dry run; retained for create parity.
     */
    isDefault?: boolean;
    /**
     * Draft lifecycle state.
     */
    status?: "active" | "disabled";
  };
  /**
   * Bounded safe fixtures. personId, contact data, IP, click IDs, device identifiers, and provider bodies are schema-invalid.
   *
   * @maxItems 10000
   */
  records: {
    /**
     * Synthetic fixture event id.
     */
    id: string;
    /**
     * Synthetic or opaque fixture subject used only to group the preview journey.
     */
    subjectRef: string;
    /**
     * Canonical fixture record family.
     */
    kind: "event" | "external" | "conversion";
    /**
     * Canonical event or conversion name.
     */
    eventName: string;
    /**
     * Optional browser event-definition id.
     */
    eventDefinitionId?: string | null;
    /**
     * Optional canonical external-event kind.
     */
    externalEventKind?: string | null;
    /**
     * Fixture occurrence time.
     */
    occurredAt: string;
    /**
     * Optional normalized acquisition source.
     */
    source?: string | null;
    /**
     * Optional normalized campaign.
     */
    campaign?: string | null;
    /**
     * Optional normalized ad id; never a visitor click id.
     */
    adId?: string | null;
    /**
     * Optional verified value in minor units.
     */
    valueMinor?: number | null;
    /**
     * ISO 4217 currency when valueMinor is present.
     */
    currency?: string | null;
  }[];
  /**
   * Inclusive fixture window start.
   */
  start: string;
  /**
   * Exclusive fixture window end.
   */
  end: string;
}

export interface Output {
  ok: boolean;
  result: {
    [k: string]: unknown;
  };
}
