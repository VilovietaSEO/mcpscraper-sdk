import { McpToolsClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_SCRAPER_API_KEY
const subdomain = process.env.COMMONS_PUBLICATION_SUBDOMAIN
if (!apiKey || !subdomain) throw new Error('Set MCP_SCRAPER_API_KEY and COMMONS_PUBLICATION_SUBDOMAIN for a publication you own.')
const tools = new McpToolsClient({ apiKey })
const page = await tools.commons.listPublications({ limit: 25 })
if (!page.ok) throw new Error(page.message ?? page.error)
console.log(JSON.stringify({ publications: page.data?.publications.map(p => p.subdomain), nextCursor: page.data?.nextCursor }))
const selected = await tools.commons.getPublication({ subdomain, includeArticles: true, includeEditions: true })
if (!selected.ok) throw new Error(selected.message ?? selected.error)
// This example reads only. To edit, use the returned edition revision as baseRevision
// in updateEditorialArticle and supply just the fields to change. To delete the entire
// publication, use its publication revision, not an edition revision. Always preserve
// the idempotencyKey for exact retries; a new change needs a new key.
console.log(JSON.stringify({ selected: subdomain, publicationRevision: selected.data?.publication?.revision, editions: selected.data?.editions?.map(e => ({ slug: e.editionSlug, revision: e.revision })) }))
