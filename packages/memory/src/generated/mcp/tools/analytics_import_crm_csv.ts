export interface Input {
  siteId: string;
  sourceSystem: "hubspot" | "salesforce" | "gohighlevel" | "zoho" | "pipedrive" | "keap" | "other";
  filename: string;
  csv: string;
  mapping: {
    email?: string;
    firstName?: string;
    lastName?: string;
    name?: string;
    phone?: string;
    company?: string;
    externalId?: string;
  };
}

export interface Output {
  ok: boolean;
}
