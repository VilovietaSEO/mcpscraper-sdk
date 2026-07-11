export interface Input {
  /**
   * A scheduled action id returned by create-scheduled-action or list-scheduled-actions.
   */
  scheduleActionId: string;
  /**
   * Exact connection and tool grants for this schedule. Pass an empty array to remove every external-service grant.
   *
   * @maxItems 20
   */
  connections:
    | []
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ]
    | [
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        },
        {
          /**
           * A tenant-scoped connectionId from list_service_connections.
           */
          connectionId: string;
          /**
           * The matching providerConfigKey returned with that connection.
           */
          providerConfigKey: string;
          /**
           * Exact readTools and, only when live actions are enabled, actionTools this schedule may use.
           *
           * @minItems 1
           * @maxItems 100
           */
          allowedTools: [string, ...string[]];
        }
      ];
}

export type Output = unknown
