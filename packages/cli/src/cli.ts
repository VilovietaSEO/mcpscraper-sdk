#!/usr/bin/env node
import { Command } from 'commander'
import { fileURLToPath } from 'node:url'
import { mkdirSync, realpathSync, writeFileSync } from 'node:fs'
import { homedir } from 'node:os'
import { join } from 'node:path'
import { ScraperClient, ScraperApiError, type McpContentBlock, type McpToolCallResult } from 'mcpscraper-sdk'
import { CLI_VERSION } from './version.js'
import { MCP_TOOL_CATALOG, MCP_TOOL_COUNT } from './generated-tools.js'

function printResult(result: unknown, json: boolean, summarize: (result: unknown) => void): void {
  if (json) {
    console.log(JSON.stringify(result, null, 2))
  } else {
    summarize(result)
  }
}

function parseToolArgs(value: string): Record<string, unknown> {
  let parsed: unknown
  try {
    parsed = JSON.parse(value)
  } catch (error) {
    throw new Error(`--args must be valid JSON: ${error instanceof Error ? error.message : String(error)}`)
  }
  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
    throw new Error('--args must be a JSON object')
  }
  return parsed as Record<string, unknown>
}

function mediaExtension(mimeType: string | undefined): string {
  switch (mimeType?.toLowerCase()) {
    case 'image/png': return 'png'
    case 'image/jpeg': return 'jpg'
    case 'image/gif': return 'gif'
    case 'image/webp': return 'webp'
    case 'image/avif': return 'avif'
    case 'audio/mpeg': return 'mp3'
    case 'audio/mp4': return 'm4a'
    case 'audio/wav':
    case 'audio/x-wav': return 'wav'
    case 'audio/ogg': return 'ogg'
    case 'audio/flac': return 'flac'
    case 'audio/aac': return 'aac'
    case 'application/pdf': return 'pdf'
    default: return 'bin'
  }
}

function safeToolName(name: string): string {
  return name.replace(/[^a-zA-Z0-9_-]+/g, '-').replace(/^-+|-+$/g, '') || 'tool'
}

function decodeBase64(data: string): Buffer {
  const normalized = data.replace(/\s+/g, '')
  if (normalized.length === 0 || !/^[A-Za-z0-9+/]*={0,2}$/.test(normalized)) {
    throw new Error('Refusing to save malformed base64 content from an MCP tool result')
  }
  const unpadded = normalized.replace(/=+$/, '')
  const remainder = unpadded.length % 4
  const expectedPadding = remainder === 0 ? 0 : 4 - remainder
  const providedPadding = normalized.length - unpadded.length
  if (remainder === 1 || (providedPadding > 0 && providedPadding !== expectedPadding)) {
    throw new Error('Refusing to save malformed base64 content from an MCP tool result')
  }
  return Buffer.from(unpadded.padEnd(unpadded.length + expectedPadding, '='), 'base64')
}

function saveToolMedia(
  name: string,
  result: McpToolCallResult,
  mediaDir?: string,
): McpToolCallResult {
  const outputDirectory = mediaDir ?? process.env.MCP_SCRAPER_OUTPUT_DIR ?? join(homedir(), 'Downloads', 'mcp-scraper')
  let mediaNumber = 0
  const saveBinary = (data: string, mimeType: string | undefined, kind: string) => {
    const bytes = decodeBase64(data)
    if (bytes.byteLength > 10 * 1024 * 1024) {
      throw new Error(`Refusing to save inline MCP ${kind} larger than 10 MiB (${bytes.byteLength} bytes)`)
    }
    mkdirSync(outputDirectory, { recursive: true })
    mediaNumber += 1
    const filename = `${safeToolName(name)}-${Date.now()}-${mediaNumber}.${mediaExtension(mimeType)}`
    const savedPath = join(outputDirectory, filename)
    writeFileSync(savedPath, bytes, { mode: 0o600 })
    return { bytes: bytes.byteLength, savedPath }
  }
  const content = (result.content ?? []).map((block: McpContentBlock) => {
    if ((block.type === 'image' || block.type === 'audio') && typeof block.data === 'string') {
      return {
        ...block,
        data: undefined,
        ...saveBinary(block.data, block.mimeType, block.type),
      }
    }
    if (block.type === 'resource' && block.resource && typeof block.resource === 'object') {
      const resource = block.resource as Record<string, unknown>
      if (typeof resource.blob === 'string') {
        return {
          ...block,
          resource: {
            ...resource,
            blob: undefined,
            ...saveBinary(resource.blob, typeof resource.mimeType === 'string' ? resource.mimeType : undefined, 'resource'),
          },
        }
      }
    }
    return block
  })
  return { ...result, content }
}

function printableToolResult(result: McpToolCallResult): unknown {
  const hasNonTextContent = result.content?.some(block => block.type !== 'text') ?? false
  if (hasNonTextContent) return result
  if (result.structuredContent !== undefined) return result.structuredContent
  const text = result.content?.find(block => block.type === 'text')?.text
  if (typeof text !== 'string') return result
  try {
    return JSON.parse(text)
  } catch {
    return text
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
    .description(`CLI for all ${MCP_TOOL_COUNT} mcpscraper.dev MCP tools plus ergonomic shortcuts`)
    .version(CLI_VERSION)
    .option('--api-key <key>', 'mcpscraper.dev API key (or set MCPSCRAPER_API_KEY)')

  program
    .command('search <query>')
    .description('Run a Google SERP search')
    .option('--location <location>', 'geographic location to search from')
    .option('--json', 'print the complete JSON result (inline binary data is saved and replaced with file metadata)')
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
          downloadImages: false,
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

  const memory = program.command('memory').description(`Ergonomic memory shortcuts; use tools list/call for the complete ${MCP_TOOL_COUNT}-tool surface`)

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

  const tools = program
    .command('tools')
    .description(`Discover, inspect, and call every unified MCP tool (${MCP_TOOL_COUNT} total)`)

  tools
    .command('list')
    .description(`List the complete local ${MCP_TOOL_COUNT}-tool catalog`)
    .option('--category <name>', 'filter by SDK category')
    .option('--json', 'print the complete catalog as JSON')
    .action((opts: { category?: string; json?: boolean }) => {
      const catalog = opts.category
        ? MCP_TOOL_CATALOG.filter(tool => tool.category === opts.category)
        : MCP_TOOL_CATALOG
      if (opts.json) {
        console.log(JSON.stringify(catalog, null, 2))
        return
      }
      for (const tool of catalog) console.log(`${tool.name}\t${tool.category}\t${tool.title}`)
      console.log(`\n${catalog.length}/${MCP_TOOL_COUNT} tools`)
    })

  tools
    .command('describe <name>')
    .description('Show a tool description, input schema, and safety annotations')
    .action((name: string) => {
      const tool = MCP_TOOL_CATALOG.find(entry => entry.name === name)
      if (!tool) throw new Error(`Unknown tool "${name}". Run "mcpscraper tools list" for all ${MCP_TOOL_COUNT} names.`)
      console.log(JSON.stringify(tool, null, 2))
    })

  tools
    .command('call <name>')
    .description(`Call any of the ${MCP_TOOL_COUNT} MCP tools by exact wire name`)
    .option('--args <json>', 'tool arguments as a JSON object', '{}')
    .option('--yes', 'confirm a tool marked destructive')
    .option('--media-dir <path>', 'directory for inline MCP images (defaults to ~/Downloads/mcp-scraper)')
    .option('--json', 'print raw JSON')
    .action(async (name: string, opts: { args: string; yes?: boolean; mediaDir?: string; json?: boolean }, cmd: Command) => {
      await run(async () => {
        const tool = MCP_TOOL_CATALOG.find(entry => entry.name === name)
        if (!tool) throw new Error(`Unknown tool "${name}". Run "mcpscraper tools list" for all ${MCP_TOOL_COUNT} names.`)
        const annotations = tool.annotations as { destructiveHint?: boolean }
        if (annotations.destructiveHint && !opts.yes) {
          throw new Error(`Tool "${name}" is marked destructive. Re-run with --yes to confirm.`)
        }
        const rawResult = await client(cmd).tools.callToolResult(name, parseToolArgs(opts.args))
        const result = printableToolResult(saveToolMedia(name, rawResult, opts.mediaDir))
        if (opts.json || typeof result !== 'string') console.log(JSON.stringify(result, null, 2))
        else console.log(result)
      })
    })

  return program
}

export function isMainModule(metaUrl: string, argvPath = process.argv[1]): boolean {
  if (!argvPath) return false
  try {
    return realpathSync(argvPath) === realpathSync(fileURLToPath(metaUrl))
  } catch {
    return false
  }
}

const isMain = isMainModule(import.meta.url)
if (isMain) {
  await createProgram().parseAsync(process.argv)
}
