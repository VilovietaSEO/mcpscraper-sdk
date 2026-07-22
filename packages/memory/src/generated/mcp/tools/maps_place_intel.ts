export interface Input {
  /**
   * Business name only, e.g. "Elite Roofing" (not "Elite Roofing Denver CO" — put the city in location).
   */
  businessName: string;
  /**
   * City/region/country where the business should be searched, e.g. "Denver, CO".
   */
  location: string;
  /**
   * Google country code inferred from location.
   */
  gl?: string;
  /**
   * Language inferred from user request.
   */
  hl?: string;
  /**
   * Fetch individual review cards — for reviews, customer pain, complaints, or praise themes.
   */
  includeReviews?: boolean;
  /**
   * Max review cards when includeReviews is true. Default 50, maximum 500.
   */
  maxReviews?: number;
  /**
   * Fetch the business's configured services list and areas-served list, when the profile has them. Adds one extra page visit; not present for every business.
   */
  includeServices?: boolean;
}

export interface Output {
  name: string;
  rating: string | null;
  reviewCount: string | null;
  category: string | null;
  address: string | null;
  phone: string | null;
  website: string | null;
  hoursSummary: string | null;
  bookingUrl: string | null;
  kgmid: string | null;
  cidDecimal: string | null;
  cidUrl: string | null;
  lat: number | null;
  lng: number | null;
  reviewsStatus: string;
  reviewsCollected: number;
  reviewTopics: {
    label: string;
    count: string;
  }[];
  services: string[];
  areasServed: string[];
  servicesStatus: string;
}
