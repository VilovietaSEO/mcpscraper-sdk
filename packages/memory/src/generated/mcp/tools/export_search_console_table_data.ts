export interface Input {
  /**
   * Typed Search Console tableName returned by list_service_connections after a successful connection_sync run.
   */
  tableName: string;
  /**
   * Optional filters to AND together before download. Use table-describe or the documented typed columns.
   *
   * @maxItems 20
   */
  filters?:
    | []
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ]
    | [
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        },
        {
          /**
           * Typed Search Console table column to filter.
           */
          column:
            | "id"
            | "provider_record_id"
            | "connection_id"
            | "site_url"
            | "permission_level"
            | "date"
            | "query"
            | "page"
            | "country"
            | "device"
            | "clicks"
            | "impressions"
            | "ctr"
            | "position"
            | "captured_at"
            | "content_hash"
            | "created_at"
            | "updated_at";
          /**
           * Comparison operator. like performs a case-insensitive substring match; in requires an array value.
           */
          op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
          /**
           * Value to compare. For in, pass an array.
           */
          value?: {
            [k: string]: unknown;
          };
        }
      ];
  /**
   * Optional row ordering for the JSONL download.
   */
  sort?: {
    column:
      | "id"
      | "provider_record_id"
      | "connection_id"
      | "site_url"
      | "permission_level"
      | "date"
      | "query"
      | "page"
      | "country"
      | "device"
      | "clicks"
      | "impressions"
      | "ctr"
      | "position"
      | "captured_at"
      | "content_hash"
      | "created_at"
      | "updated_at";
    direction?: "asc" | "desc";
  };
  /**
   * Maximum matching persisted rows to place in this artifact. Use filters to bound large tables.
   */
  maxRows?: number;
}

export interface Output {
  ok: boolean;
  tableName?: string;
  rowsExported?: number;
  matchedRows?: number;
  complete?: boolean;
  artifact?: {
    artifactId: string;
    filename: string;
    contentType: "application/x-ndjson";
    bytes: number;
    sha256: string;
    expiresAt: string;
    downloadUrl: string | null;
    downloadUrlExpiresAt: string | null;
  };
  warnings?: string[];
  error: string | null;
}
