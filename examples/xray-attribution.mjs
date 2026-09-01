import { randomUUID } from 'node:crypto'
import { McpToolsClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_SCRAPER_API_KEY
const siteId = process.env.XRAY_SITE_ID

if (!apiKey || !siteId) {
  throw new Error('Set MCP_SCRAPER_API_KEY and XRAY_SITE_ID before running this example.')
}

const client = new McpToolsClient({ apiKey })

// Start with the provider-neutral evidence contract. Customer-reported
// influence remains separate from observed touchpoints, and unavailable view
// evidence stays unavailable instead of being inferred.
const [methodology, viewEvidence] = await Promise.all([
  client.analytics.getAttributionMethodology({ siteId }),
  client.analytics.getViewEvidenceStatus({ siteId }),
])
console.log('attribution methodology', methodology.methodology)
console.log('view evidence', viewEvidence.status)

// Survey creation produces a draft only. Publication requires an approved copy
// identifier and a separate exact-revision state transition.
if (process.env.XRAY_CREATE_SURVEY_DRAFT === 'yes') {
  const draft = await client.analytics.createPostPurchaseSurvey({
    siteId,
    name: 'Subscription influence survey',
    question: 'What influenced your decision to subscribe?',
    selectionMode: 'multiple',
    eligibleOutcomeFamilies: ['subscription_revenue'],
    exchangeTtlSeconds: 900,
    sessionTtlSeconds: 1800,
    options: [
      { optionId: 'search', label: 'Search' },
      { optionId: 'recommendation', label: 'Recommendation' },
    ],
    idempotencyKey: randomUUID(),
  })
  console.log('survey draft', draft.survey)
}
