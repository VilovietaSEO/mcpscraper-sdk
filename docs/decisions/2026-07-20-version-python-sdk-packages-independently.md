# Version Python SDK packages independently from monorepo tags

- **Status:** Accepted
- **Date:** 2026-07-20
- **Scope:** MCP Scraper SDK package release workflow
- **Related:** `packages/scraper-python/pyproject.toml`, `packages/memory-python/pyproject.toml`, `CHANGELOG.md`
- **Supersedes:** None
- **Superseded by:** None

## Context

The Node packages, CLI, Python packages, and monorepo Git tags already move at different versions. PyPI publishing makes each Python version immutable, so the release workflow must not imply that a new Python package requires a no-op Node package release.

## Decision

Version and publish the two Python packages from their own `pyproject.toml` versions. Document each Python release in the shared changelog and map it to the source commit or GitHub release that produced it.

## Drivers

- Keep each registry artifact's semantic version tied to its own public contents.
- Avoid republishing unaffected Node packages merely to synchronize a monorepo tag.

## Alternatives considered

### Force every package to share the Git tag version

This would make the version table simpler but would create unnecessary Node package releases for Python-only corrections.

## Consequences

- **Positive:** Python fixes and documentation corrections can ship promptly and immutably without changing unaffected packages.
- **Negative:** Release notes must state the exact Python, Node, CLI, and Git release versions instead of implying one shared version.

## Revisit when

- The repository adopts package-aware release automation that can enforce a different versioning model across all artifacts.
