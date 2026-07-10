# mcpscraper-cli

Command-line interface for [mcpscraper.dev](https://mcpscraper.dev) and [memory.mcpscraper.dev](https://memory.mcpscraper.dev).

This is a **curated subset** of the full API — search, scrape, crawl, map, Maps search, and a couple of memory commands. It is not full API coverage. For every operation (40 scraper endpoints, 85 memory tools), use [`mcpscraper-sdk`](../scraper) and [`mcpscraper-memory-sdk`](../memory) directly.

## Install

```bash
npm install -g mcpscraper-cli
```

## Auth

```bash
export MCPSCRAPER_API_KEY=sk_live_your_key
```

or pass `--api-key <key>` on any command.

## Commands

### `mcpscraper search <query>`

```bash
$ mcpscraper search "best roofing companies denver"
1. TOP 10 BEST Roofing Companies in Denver, CO
   https://www.yelp.com/search?find_desc=Roofing+Companies&find_loc=Denver%2C+CO
2. Recomendations for roofing company in Denver - ASAP
   https://www.reddit.com/r/Denver/comments/1kh2gd3/...
```

Options: `--location <location>`, `--json`.

### `mcpscraper scrape <url>`

```bash
$ mcpscraper scrape https://example.com --deposit-to-vault --vault research
Example Domain
This domain is for use in illustrative examples...

Vault deposit: saved to research
```

Options: `--screenshot`, `--deposit-to-vault`, `--vault <name>`, `--json`.

### `mcpscraper crawl <url>`

Crawls and extracts every page of a site. Options: `--max-pages <n>` (default 100), `--json`.

### `mcpscraper map <url>`

Discovers all URLs on a site (no extraction). Options: `--json`.

### `mcpscraper maps-search <query> --location <location>`

```bash
$ mcpscraper maps-search "roofers" --location "Denver, CO"
1. Forest Roofs (4.9★)
   701 Birch Street
2. Mike & Sons Roofing (4.8★)
   ...
```

Options: `--json`.

### `mcpscraper memory search <query>`

Semantic search across your mcp-memory vaults, dispatched through your mcpscraper.dev API key (no separate memory key needed).

```bash
$ mcpscraper memory search "roofing warranty terms"
[0.83] note:competitor-research/roofing-warranties.md
  Standard roofing warranty terms cover materials for 25-30 years...
```

### `mcpscraper memory list-vaults`

```bash
$ mcpscraper memory list-vaults
Ideas (2 notes, owner)
Inspiration (2 notes, owner)
Knowledge (3 notes, owner)
```

## Every command supports `--json`

```bash
$ mcpscraper map https://example.com --json
{
  "urls": ["https://example.com/", "https://example.com/about"]
}
```

## See also

[Repo README](../../README.md) (multi-language examples with real sample output) · [`mcpscraper-sdk`](../scraper) · [`mcpscraper-memory-sdk`](../memory) · Python: [`mcpscraper-sdk`](../scraper-python) · [`mcpscraper-memory-sdk`](../memory-python)
