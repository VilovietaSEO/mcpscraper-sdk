import { randomUUID } from 'node:crypto'
import { McpToolsClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_SCRAPER_API_KEY
if (!apiKey) throw new Error('MCP_SCRAPER_API_KEY is required.')
const client = new McpToolsClient({ apiKey })
const run = randomUUID()
const config = { name: 'Synthetic SDK form test', allowedOrigins: ['https://example.test'], relationshipType: 'prospect', mapping: { name: 'name', email: 'email', message: 'message' } }
const sample = { name: 'Synthetic SDK Contact', email: `sdk-form-${run}@example.test`, message: 'Synthetic example submission.', _submission_id: run }
const preview = await client.crm.formPreview({ ...config, sample })
if (!preview.ok) throw new Error('Preview failed.')
if (process.env.CRM_FORM_APPLY !== '1') {
  console.log('Mapping validated; no records created. Set CRM_FORM_APPLY=1 to create and verify a synthetic submission.')
} else {
  const created = await client.crm.formCreate({ ...config, idempotencyKey: `sdk-form-${run}` })
  if (!created.ok || typeof created.result?.submitUrl !== 'string') throw new Error('Connection creation failed.')
  const { formId, submitUrl } = { formId: created.result.form.formId, submitUrl: created.result.submitUrl }
  try {
    const post = () => fetch(submitUrl, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(sample) })
    const response = await post()
    if (!response.ok) throw new Error(`Submission failed: ${response.status}`)
    const receipt = await response.json()
    const retry = await (await post()).json()
    if (retry.receiptId !== receipt.receiptId || retry.replayed !== true) throw new Error('Replay verification failed.')
    const status = await client.crm.formStatus({ formId })
    const saved = status.result?.forms[0]?.lastSubmission
    if (!status.ok || saved?.receiptId !== receipt.receiptId) throw new Error('Delivery readback failed.')
    const person = await client.crm.personGet({ entityId: saved.personEntityId })
    if (!person.ok || person.record?.props.email !== sample.email) throw new Error('Contact readback failed.')
    console.log({ verified: true, receiptId: saved.receiptId, personEntityId: saved.personEntityId, activityId: saved.activityId })
  } finally {
    await client.crm.formRevoke({ formId })
  }
}
