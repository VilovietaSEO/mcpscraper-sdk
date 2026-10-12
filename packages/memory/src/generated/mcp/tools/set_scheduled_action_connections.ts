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

export type Output =
  | {
      ok: boolean;
      connections?: unknown[];
      error: string | null;
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
