#!/usr/bin/env node
import { Command } from 'commander'
import { fileURLToPath } from 'node:url'
import { ScraperClient, ScraperApiError } from 'mcpscraper-sdk'
import { CLI_VERSION } from './version.js'

function printResult(result: unknown, json: boolean, summarize: (result: unknown) => void): void {
  if (json) {
    console.log(JSON.stringify(result, null, 2))
  } else {
    summarize(result)
  }
}

async function run(fn: () => Promise<void>): Promise<void> {
  try {
    await fn()
  } catch (err) {
    if (err instanceof ScraperApiError) {
      console.error(`Error${err.code ? ` [${err.code}]` : ''}: ${err.message}`)
    } else {
      console.error(err instanceof Error ? err.message : String(err))
    }
    process.exitCode = 1
  }
}

export function createProgram(fetchImpl: typeof globalThis.fetch = globalThis.fetch): Command {
  function resolveApiKey(cmd: Command): string {
    const opts = cmd.optsWithGlobals() as { apiKey?: string }
    const key = opts.apiKey ?? process.env.MCPSCRAPER_API_KEY
    if (!key) {
      console.error('Missing API key. Pass --api-key <key> or set MCPSCRAPER_API_KEY.')
      process.exit(1)
    }
    return key
  }

  function client(cmd: Command): ScraperClient {
    return new ScraperClient({ apiKey: resolveApiKey(cmd), fetch: fetchImpl })
  }

  const program = new Command()
  program
    .name('mcpscraper')
    .description('CLI for mcpscraper.dev and memory.mcpscraper.dev — a curated subset of the full API, see mcpscraper-sdk for full coverage')
    .version(CLI_VERSION)
    .option('--api-key <key>', 'mcpscraper.dev API key (or set MCPSCRAPER_API_KEY)')

  program
    .command('search <query>')
    .description('Run a Google SERP search')
    .option('--location <location>', 'geographic location to search from')
    .option('--json', 'print raw JSON')
    .action(async (query: string, opts: { location?: string; json?: boolean }, cmd: Command) => {
      await run(async () => {
        const result = await client(cmd).searchSerp({
          query,
          location: opts.location,
          depth: 4,
          maxQuestions: 30,
          gl: 'us',
          hl: 'en',
          device: 'desktop',
          proxyMode: 'none',
          pages: 1,
          debug: false,
        })
        printResult(result, Boolean(opts.json), (r) => {
          const organic = (r as { result?: { organicResults?: Array<{ position: number; title: string; url: string }> } }).result?.organicResults ?? []
          for (const item of organic) {
            console.log(`${item.position}. ${item.title}\n   ${item.url}`)
          }
        })
      })
    })

  program
    .command('scrape <url>')
    .description('Extract a single page (markdown, headings, optional screenshot/vault deposit)')
    .option('--screenshot', 'capture a full-page screenshot')
    .option('--deposit-to-vault', 'save the full page into your mcp-memory vault')
    .option('--vault <name>', 'vault name for --deposit-to-vault')
    .option('--json', 'print raw JSON')
    .action(async (url: string, opts: { screenshot?: boolean; depositToVault?: boolean; vault?: string; json?: boolean }, cmd: Command) => {
      await run(async () => {
        const result = await client(cmd).extractUrl({
          url,
          screenshot: Boolean(opts.screenshot),
          screenshotDevice: 'desktop',
          extractBranding: false,
          downloadMedia: false,
          allowLocal: false,
          depositToVault: Boolean(opts.depositToVault),
          vaultName: opts.vault,
        })
        printResult(result, Boolean(opts.json), (r) => {
          const page = r as { title?: string; bodyMarkdown?: string; memory?: { deposited?: boolean; vault?: string } }
          console.log(page.title ?? '(untitled)')
          console.log((page.bodyMarkdown ?? '').slice(0, 500))
          if (page.memory) console.log(`\nVault deposit: ${page.memory.deposited ? `saved to ${page.memory.vault}` : 'failed'}`)
        })
      })
    })

  program
    .command('crawl <url>')
    .description('Crawl and extract every page of a site')
    .option('--max-pages <n>', 'maximum pages to crawl', (v) => parseInt(v, 10))
    .option('--json', 'print raw JSON')
    .action(async (url: string, opts: { maxPages?: number; json?: boolean }, cmd: Command) => {
      await run(async () => {
        const result = await client(cmd).extractSite({
          url,
          maxPages: opts.maxPages ?? 100,
          background: false,
          rotateProxies: false,
          rotateProxyEvery: 30,
          browserFallback: false,
          kernelFallback: false,
        })
        printResult(result, Boolean(opts.json), (r) => {
          const pages = (r as { pages?: unknown[] }).pages ?? []
          console.log(`Crawled ${pages.length} page(s).`)
        })
      })
    })

  program
    .command('map <url>')
    .description('Discover all URLs on a site')
    .option('--json', 'print raw JSON')
    .action(async (url: string, opts: { json?: boolean }, cmd: Command) => {
      await run(async () => {
        const result = await client(cmd).mapSiteUrls({
          url,
          maxUrls: 500,
          concurrency: 12,
          browserFallback: false,
          kernelFallback: false,
        })
        printResult(result, Boolean(opts.json), (r) => {
          const urls = (r as { urls?: string[] }).urls ?? []
          for (const u of urls) console.log(u)
        })
      })
    })

  program
    .command('maps-search <query>')
    .description('Search Google Maps for local businesses')
    .requiredOption('--location <location>', 'e.g. "Denver, CO"')
    .option('--json', 'print raw JSON')
    .action(async (query: string, opts: { location: string; json?: boolean }, cmd: Command) => {
      await run(async () => {
        const result = await client(cmd).maps.search({
          query,
          location: opts.location,
          gl: 'us',
          hl: 'en',
          maxResults: 10,
          proxyMode: 'location',
          debug: false,
        })
        printResult(result, Boolean(opts.json), (r) => {
          const results = (r as { results?: Array<{ position: number; name: string; rating?: string; address?: string }> }).results ?? []
          for (const item of results) {
            console.log(`${item.position}. ${item.name}${item.rating ? ` (${item.rating}★)` : ''}\n   ${item.address ?? ''}`)
          }
        })
      })
    })

  const memory = program.command('memory').description('Memory tools, dispatched through your mcpscraper.dev API key (see mcpscraper-memory-sdk for the full 74-tool surface)')

  memory
    .command('search <query>')
    .description('Semantic search across your mcp-memory vaults')
    .option('--json', 'print raw JSON')
    .action(async (query: string, opts: { json?: boolean }, cmd: Command) => {
      await run(async () => {
        const result = await client(cmd).memoryTools.memory.search({ query } as never)
        printResult(result, Boolean(opts.json), (r) => {
          const results = (r as { results?: Array<{ text: string; source: string; score: number }> }).results ?? []
          for (const item of results) {
            console.log(`[${item.score.toFixed(2)}] ${item.source}\n  ${item.text.slice(0, 160)}`)
          }
        })
      })
    })

  memory
    .command('list-vaults')
    .description('List your mcp-memory vaults')
    .option('--json', 'print raw JSON')
    .action(async (opts: { json?: boolean }, cmd: Command) => {
      await run(async () => {
        const result = await client(cmd).memoryTools.vaults.listVaults({} as never)
        printResult(result, Boolean(opts.json), (r) => {
          const vaults = (r as { vaults?: Array<{ vault: string; role: string; notes: number }> }).vaults ?? []
          for (const v of vaults) console.log(`${v.vault} (${v.notes} notes, ${v.role})`)
        })
      })
    })

  return program
}

const isMain = process.argv[1] === fileURLToPath(import.meta.url)
if (isMain) {
  await createProgram().parseAsync(process.argv)
}
