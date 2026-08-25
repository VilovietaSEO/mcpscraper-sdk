# Generated clients must match a canonical server contract

Date: 2026-08-24

## Decision

Every generated Node, Python, CLI, and cURL release must be derived from one checked-in MCP tool contract exported by the intended MCP Scraper server release. The SDK contract records the source server version and a canonical SHA-256 over the shared public tool names, descriptions, input schemas, and output schemas. Release verification compares that digest and the exact tool count against the final server manifest before any client package is published.

## Context

The 0.29.0 Node SDK release was current by package version and publication time but its checked-in MCP contract still came from MCP Scraper 0.62.0. It therefore exposed 254 tools while the 0.65.1 server exposed 259, omitting all four lead-list tools and `analyze_site_similarity`. Version checks and package-recency checks could not detect the missing forms.

## Consequences

- `update:mcp-contract` writes `sourceContractSha256` into `contracts/mcp.tools.json`.
- `verify:mcp-source-contract` fails on a source-version, tool-count, digest, or public schema mismatch.
- The same contract continues to generate both Node packages, both Python packages, the CLI catalog, and cURL documentation.
- A server release can no longer be considered complete merely because independently versioned client packages were recently published.
