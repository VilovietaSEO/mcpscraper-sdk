import { ScraperClient } from '../packages/scraper/dist/index.js'
import { MemoryClient } from '../packages/memory/dist/index.js'

interface CheckResult {
  name: string
  ok: boolean
  error?: string
}

const results: CheckResult[] = []

async function check(name: string, fn: () => Promise<void>): Promise<void> {
  try {
    await fn()
    results.push({ name, ok: true })
    console.log(`PASS  ${name}`)
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err)
    results.push({ name, ok: false, error: message })
    console.log(`FAIL  ${name}: ${message}`)
  }
}

async function main(): Promise<void> {
  const scraperKey = process.env.MCP_SCRAPER_API_KEY
  const memoryAdminKey = process.env.MCP_MEMORY_ADMIN_KEY
  if (!scraperKey) throw new Error('MCP_SCRAPER_API_KEY is required')
  if (!memoryAdminKey) throw new Error('MCP_MEMORY_ADMIN_KEY is required')

  const scraper = new ScraperClient({ apiKey: scraperKey })

  await check('scraper.getLedger', async () => {
    await scraper.getLedger()
  })

  await check('scraper.searchSerp', async () => {
    const result = await scraper.searchSerp({ query: 'mcpscraper-sdk smoke test' })
    if (!result) throw new Error('empty response')
  })

  await check('scraper.memoryTools.vaults.listVaults', async () => {
    const result = (await scraper.memoryTools.vaults.listVaults({} as never)) as { ok?: boolean }
    if (result.ok === false) throw new Error(`ok:false — ${JSON.stringify(result)}`)
  })

  const admin = new MemoryClient({ apiKey: memoryAdminKey })
  const identity = `smoke-test+${Date.now()}@mcpscraper-sdk.test`
  let throwawayKey: string | undefined
  let keyId: string | undefined
  let vaults: string[] = []

  await check('memory.vaults.provisionDefaults (throwaway identity)', async () => {
    const result = (await admin.vaults.provisionDefaults({ granteeIdentity: identity, issueKey: true, plan: 'free' } as never)) as {
      ok: boolean
      error?: string
      secret?: string
      keyId?: string
      vaults?: string[]
    }
    if (!result.ok) throw new Error(`provisioning failed: ${result.error}`)
    if (!result.secret) throw new Error('no secret returned')
    throwawayKey = result.secret
    keyId = result.keyId
    vaults = result.vaults ?? []
  })

  if (throwawayKey) {
    const memory = new MemoryClient({ apiKey: throwawayKey })

    await check('memory.memory.search (throwaway identity)', async () => {
      const result = (await memory.memory.search({ query: 'anything' } as never)) as { ok?: boolean; error?: string }
      if (result.ok === false) throw new Error(result.error ?? 'search failed')
    })

    await check('memory.vaults.listVaults (throwaway identity)', async () => {
      const result = (await memory.vaults.listVaults({} as never)) as { ok?: boolean; error?: string }
      if (result.ok === false) throw new Error(result.error ?? 'listVaults failed')
    })

    for (const vault of vaults) {
      await check(`cleanup: deleteVault(${vault})`, async () => {
        const result = (await memory.vaults.deleteVault({ vault } as never)) as { ok?: boolean; error?: string }
        if (result.ok === false) throw new Error(result.error ?? 'delete failed')
      })
    }

    if (keyId) {
      const finalKeyId = keyId
      await check('cleanup: access.revokeKey', async () => {
        const result = (await memory.access.revokeKey({ keyId: finalKeyId } as never)) as { ok?: boolean; error?: string }
        if (result.ok === false) throw new Error(result.error ?? 'revoke failed')
      })
    }
  }

  const failed = results.filter(r => !r.ok)
  console.log(`\n${results.length - failed.length}/${results.length} passed`)
  process.exitCode = failed.length ? 1 : 0
}

main().catch(err => {
  console.error(err)
  process.exitCode = 1
})
