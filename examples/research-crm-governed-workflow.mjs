import { randomUUID } from 'node:crypto'
import { MemoryClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_MEMORY_API_KEY
if (!apiKey) throw new Error('Set MCP_MEMORY_API_KEY to a synthetic test identity')

const client = new MemoryClient({ apiKey })
const observedAt = new Date().toISOString()

// Research records hold sourced knowledge. They do not become CRM contacts.
const research = await client.research.personCapture({
  baseRevision: 0,
  idempotencyKey: `example-research-${randomUUID()}`,
  displayName: 'Synthetic Historical Person',
  content: 'Synthetic example used to demonstrate the Research domain.',
  sourceEvidence: [{ sourceRef: 'https://example.com/', claim: 'Synthetic example source.' }],
  lineage: { authority: 'memory_agent', sensitivity: 'public', observedAt },
})

// CRM records express an actual relationship. A friend or coworker needs no deal.
const crm = await client.crm.personUpsert({
  baseRevision: 0,
  idempotencyKey: `example-crm-${randomUUID()}`,
  displayName: 'Synthetic Coworker',
  relationshipTypes: ['coworker', 'friend'],
  commercialLifecycle: null,
  lineage: { authority: 'memory_agent', sensitivity: 'personal', observedAt },
})

console.log({ researchDomain: research.record?.domain, crmDomain: crm.record?.domain })

if (!research.record || !crm.record) throw new Error('The synthetic records were not returned')

// Counterpart creation is preview/apply and link-only: it copies no fields.
if (process.env.APPLY_SYNTHETIC_COUNTERPART !== '1') {
  console.log('Set APPLY_SYNTHETIC_COUNTERPART=1 to preview and apply the synthetic link.')
  console.log('External CRM providers remain unavailable; this SDK exposes no provider setup or write wrapper.')
  process.exit(0)
}

const preview = await client.crm.counterpartPreview({
  researchEntityId: research.record.entityId,
  crmEntityId: crm.record.entityId,
  idempotencyKey: `example-link-preview-${randomUUID()}`,
  mode: 'link_only',
})
if (!preview.plan) throw new Error('The counterpart preview did not return a plan')

const applied = await client.crm.counterpartApply({
  planId: preview.plan.planId,
  planHandle: preview.plan.planHandle,
  digest: preview.plan.digest,
  idempotencyKey: `example-link-apply-${randomUUID()}`,
})

console.log({ mode: preview.plan.mode, copiedFields: preview.plan.copiedFields, link: applied.link })
console.log('External CRM providers remain unavailable; this SDK exposes no provider setup or write wrapper.')
