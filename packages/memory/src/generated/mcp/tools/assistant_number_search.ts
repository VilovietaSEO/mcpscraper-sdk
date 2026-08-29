export interface Input {
  /**
   * Opaque caller-owned phone connection reference; never provide account credentials.
   */
  connectionRef: string;
  /**
   * Two-letter country code for the desired number inventory.
   */
  countryCode: string;
  /**
   * Number inventory family to search.
   */
  numberType: "local" | "mobile" | "tollFree";
  /**
   * Required capabilities; returned candidates must satisfy every selected capability.
   *
   * @minItems 1
   * @maxItems 3
   */
  capabilities:
    | ["sms" | "mms" | "voice"]
    | ["sms" | "mms" | "voice", "sms" | "mms" | "voice"]
    | ["sms" | "mms" | "voice", "sms" | "mms" | "voice", "sms" | "mms" | "voice"];
  /**
   * Optional national area code or prefix used to narrow the search.
   */
  areaCode?: string;
  /**
   * Maximum expiring candidates to return from this bounded provider search.
   */
  pageSize?: number;
  /**
   * Stable request identity for this bounded search.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: true;
      data: {
        /**
         * @maxItems 20
         */
        items:
          | []
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ]
          | [
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              },
              {
                candidateRef: string;
                kind: "available" | "owned";
                numberDisplay: string;
                countryCode: string;
                numberType: "local" | "mobile" | "tollFree";
                capabilities: {
                  sms: boolean;
                  mms: boolean;
                  voice: boolean;
                };
                requirements: {
                  bundle: "not_required" | "required" | "unknown";
                  address: "none" | "any" | "local" | "foreign" | "unknown";
                };
                price: {
                  status: "quoted" | "unknown";
                  recurring: {
                    currency: string;
                    amountMinor: number;
                    interval: "month";
                  } | null;
                  blocker: "provider_quote_unavailable" | null;
                };
                expiresAt: string;
              }
            ];
        expiresAt: string | null;
      };
      receipt?: {
        receiptRef: string;
        idempotencyKey: string;
        requestDigest: string;
        resultDigest: string | null;
        state:
          "accepted" | "denied" | "pending_provider" | "confirmed" | "failed" | "unknown" | "reconciled" | "cancelled";
        replayed: boolean;
        occurredAt: string;
        error: {
          code: string;
          message: string;
          retryClass: "never" | "safe_read" | "same_identity_after_reconciliation" | "new_review";
          traceRef?: string;
        } | null;
      };
      meta: {
        requestRef: string;
        projectionVersion?: string;
        fetchedAt?: string;
        /**
         * @maxItems 20
         */
        nextActions:
          | []
          | [string]
          | [string, string]
          | [string, string, string]
          | [string, string, string, string]
          | [string, string, string, string, string]
          | [string, string, string, string, string, string]
          | [string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string, string]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ];
      };
      resourceUri?: string;
      offload?: {
        resourceUri: string;
        nextCursor: string | null;
        reason: "result_exceeded_inline_budget";
      };
      truncated: boolean;
      untrustedContent: boolean;
    }
  | {
      ok: true;
      receipt?: {
        receiptRef: string;
        idempotencyKey: string;
        requestDigest: string;
        resultDigest: string | null;
        state:
          "accepted" | "denied" | "pending_provider" | "confirmed" | "failed" | "unknown" | "reconciled" | "cancelled";
        replayed: boolean;
        occurredAt: string;
        error: {
          code: string;
          message: string;
          retryClass: "never" | "safe_read" | "same_identity_after_reconciliation" | "new_review";
          traceRef?: string;
        } | null;
      };
      meta: {
        requestRef: string;
        projectionVersion?: string;
        fetchedAt?: string;
        /**
         * @maxItems 20
         */
        nextActions:
          | []
          | [string]
          | [string, string]
          | [string, string, string]
          | [string, string, string, string]
          | [string, string, string, string, string]
          | [string, string, string, string, string, string]
          | [string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string, string]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ];
      };
      resourceUri: string;
      offload: {
        resourceUri: string;
        nextCursor: string | null;
        reason: "result_exceeded_inline_budget";
      };
      truncated: true;
      untrustedContent: boolean;
    }
  | {
      ok: false;
      resourceUri?: string;
      truncated: false;
      untrustedContent: boolean;
      error: {
        code:
          | "not_authenticated"
          | "validation_failed"
          | "idempotency_key_invalid"
          | "request_too_large"
          | "not_found"
          | "registration_review_expired"
          | "schedule_confirmation_conflict"
          | "response_too_large"
          | "service_not_configured"
          | "invalid_caller"
          | "invalid_request"
          | "policy_denied"
          | "approval_required"
          | "assistant_service_failed"
          | "assistant_request_cancelled"
          | "assistant_request_failed"
          | "assistant_resource_failed"
          | "assistant_response_invalid"
          | "assistant_response_rejected"
          | "assistant_response_too_large"
          | "mcp_http_error"
          | "mcp_request_timeout"
          | "response_lost"
          | "service_unavailable"
          | "idempotency_conflict"
          | "idempotency_in_progress";
        message: string;
        retryClass:
          | "never"
          | "safe_read"
          | "receipt_lookup"
          | "reconcile_first"
          | "same_identity_after_reconciliation"
          | "new_review";
        requestRef?: string;
        /**
         * @maxItems 20
         */
        nextActions:
          | []
          | [string]
          | [string, string]
          | [string, string, string]
          | [string, string, string, string]
          | [string, string, string, string, string]
          | [string, string, string, string, string, string]
          | [string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string, string]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ];
      };
    };
