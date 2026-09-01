import { randomUUID } from 'node:crypto'
import { McpToolsClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_SCRAPER_API_KEY
const siteId = process.env.XRAY_SITE_ID

if (!apiKey || !siteId) {
  throw new Error('Set MCP_SCRAPER_API_KEY and XRAY_SITE_ID before running this example.')
}

const client = new McpToolsClient({ apiKey })

// Start with the evidence contract. Reported influence is a separate ledger and
// provider-unavailable view evidence must remain unavailable.
const [methodology, viewEvidence] = await Promise.all([
  client.analytics.getAttributionMethodology({ siteId }),
  client.analytics.getViewEvidenceStatus({ siteId }),
])
console.log('attribution methodology', methodology.methodology)
console.log('view evidence', viewEvidence.status)

// Revenue setup accepts only an existing connected-account reference, never a
// provider credential. Preparing is a durable mutation and therefore uses a
// retry key. Apply remains explicitly gated because it selects revenue authority.
const serviceConnectionRef = process.env.XRAY_SERVICE_CONNECTION_REF
if (serviceConnectionRef) {
  const prepared = await client.analytics.prepareRevenueSource({
    siteId,
    serviceConnectionRef,
    role: 'primary',
    idempotencyKey: randomUUID(),
  })
  console.log('review revenue setup', prepared.setup)

  if (process.env.XRAY_APPLY_REVENUE_SETUP === 'yes') {
    const applied = await client.analytics.applyRevenueSource({
      siteId,
      setupId: prepared.setup.setupId,
      revision: prepared.setup.revision,
      confirmed: true,
      idempotencyKey: randomUUID(),
    })
    console.log('applied revenue setup', applied.setup)

    const verified = await client.analytics.verifyRevenueSource({
      siteId,
      setupId: applied.setup.setupId,
      revision: applied.setup.revision,
      idempotencyKey: randomUUID(),
    })
    console.log('revenue evidence', verified.setup.verification)
  }
}

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
