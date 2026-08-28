import { McpToolsClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_SCRAPER_API_KEY
const siteId = process.env.XRAY_SITE_ID

if (!apiKey || !siteId) {
  throw new Error('Set MCP_SCRAPER_API_KEY and XRAY_SITE_ID before running this example.')
}

const client = new McpToolsClient({ apiKey })

// Confirmed is the safe default and the only tier eligible to feed CRM or ad actions.
const confirmed = await client.analytics.listJourneys({ siteId, journeyTier: 'confirmed', limit: 25 })
if (!confirmed.ok || confirmed.journeyTier !== 'confirmed' || !confirmed.confirmed || confirmed.bestGuess !== null) {
  throw new Error('The confirmed journey response did not preserve its confirmed-only branch contract.')
}
console.log('confirmed journeys', confirmed.confirmed.items)

const visitorRef = confirmed.confirmed.items[0]?.personRef
if (visitorRef) {
  // The analytics journey uses a bounded, from-inclusive/to-exclusive window.
  // Omit both boundaries for the default 90-day window ending now.
  const detail = await client.analytics.getVisitorJourney({
    siteId,
    reference: visitorRef,
    from: '2026-08-01T00:00:00.000Z',
    to: '2026-09-01T00:00:00.000Z',
  })
  if (!detail.ok || detail.data.journeyTier !== 'confirmed' || detail.data.candidateAssisted !== null) {
    throw new Error('The visitor journey did not preserve its confirmed-only contract.')
  }
  console.log('visitor journey', {
    subject: detail.data.subject,
    range: detail.data.range,
    summary: detail.data.summary,
    commonPages: detail.data.commonPages,
    eventBreakdown: detail.data.eventBreakdown,
    acquisition: detail.data.acquisition,
    sessions: detail.data.sessions,
    chronology: detail.data.items,
    pageInfo: detail.data.pageInfo,
  })
}

// A cursor belongs to the selected branch. Replay it with the same selector.
if (confirmed.confirmed.pageInfo.hasNextPage && confirmed.confirmed.pageInfo.nextCursor) {
  const nextConfirmed = await client.analytics.listJourneys({
    siteId,
    journeyTier: 'confirmed',
    limit: 25,
    cursor: confirmed.confirmed.pageInfo.nextCursor,
  })
  console.log('next confirmed page', nextConfirmed.confirmed?.items ?? [])
}

// Best-guess journeys remain a separate candidate-assisted analysis branch.
// Never send these inferred increments to a CRM or advertising destination.
const bestGuess = await client.analytics.listJourneys({ siteId, journeyTier: 'best_guess', limit: 25 })
if (!bestGuess.ok || bestGuess.journeyTier !== 'best_guess' || bestGuess.confirmed !== null || !bestGuess.bestGuess) {
  throw new Error('The best-guess journey response did not preserve its separated branch contract.')
}
for (const journey of bestGuess.bestGuess.items) {
  if (journey.journeyTier !== 'candidate_assisted') throw new Error('Unlabeled candidate-assisted journey received.')
  console.log('candidate-assisted evidence', {
    confirmed: journey.confirmedTotals,
    inferredIncrement: journey.inferredIncrementalTotals,
    confidenceBand: journey.confidenceBand,
    expiresAt: journey.expiresAt,
  })
}
