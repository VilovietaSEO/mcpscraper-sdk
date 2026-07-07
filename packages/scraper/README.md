# mcpscraper-sdk

Official TypeScript/JavaScript client for the [mcpscraper.dev](https://mcpscraper.dev) REST API — SERP search, People-Also-Ask harvesting, single-page and whole-site extraction, YouTube, Facebook/Google Ads Transparency, Instagram, Reddit, video breakdown, Google Maps, and directory/rank-tracking workflows.

This is a thin HTTP client generated against [`../../contracts/scraper.openapi.yaml`](../../contracts/scraper.openapi.yaml), the public contract for the hosted API. It contains no scraping, proxy, or billing logic — only typed request/response plumbing.

## Install

```bash
npm install mcpscraper-sdk
```

## Usage

```ts
import { ScraperClient, ScraperApiError } from 'mcpscraper-sdk'

const client = new ScraperClient({ apiKey: process.env.MCPSCRAPER_API_KEY! })

const serp = await client.searchSerp({ query: 'roof repair Denver' })

try {
  const places = await client.maps.search({ query: 'roofers', location: 'Denver, CO' })
  console.log(places)
} catch (err) {
  if (err instanceof ScraperApiError && err.isInsufficientBalance()) {
    console.error(`Need ${err.body.required_credits} credits, have ${err.body.balance_credits}. Top up: ${err.body.topup_url}`)
  } else {
    throw err
  }
}
```

## Errors

Every non-2xx response throws a `ScraperApiError` with `status`, `code`, and the raw response `body`. Two cases have typed narrowing helpers:

- `err.isInsufficientBalance()` — narrows `err.body` to `{ balance_credits, required_credits, topup_url, ... }`.
- `err.isConcurrencyLimitExceeded()` — narrows `err.body` to `{ active, limit, retryable, ... }`.

## API surface

Core operations are flat on the client: `searchSerp`, `harvestPaa`, `extractUrl`, `mapSiteUrls`, `extractSite`, `auditSite`, `getExtractSiteStatus`, `listJobs`, `getJob`, `getHistory`, `getLedger`.

Everything else is namespaced by product area, matching the OpenAPI spec's tags: `client.youtube`, `client.screenshot`, `client.facebook`, `client.googleAds`, `client.instagram`, `client.reddit`, `client.video`, `client.maps`, `client.directory`, `client.serpIntelligence`, `client.workflows`.

## Regenerating types

`src/schema.ts` is generated from the OpenAPI spec and checked in. After editing `../../contracts/scraper.openapi.yaml`, regenerate with:

```bash
npm run generate
```
