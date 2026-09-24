# Maintainer package publishing

The PyPI publishing credential is a macOS Keychain generic-password item with service `org.pypi.publishing` and account `__token__`. Check access without displaying the value:

```bash
security find-generic-password -s org.pypi.publishing -a __token__ -w >/dev/null 2>&1
```

For an authorized Python package release, pass that value only to the publishing process:

```bash
UV_PUBLISH_TOKEN="$(security find-generic-password -s org.pypi.publishing -a __token__ -w)" \
  uv publish dist/<wheel-file>.whl dist/<source-file>.tar.gz
```

Do not print, commit, or put the credential in a command argument. Verify the exact new version and both archive digests at PyPI after publication. The Memory and Scraper Python packages have independent versions; publish only packages changed by the release.

For npm, check `npm whoami` before publishing the inspected tarball. Registry upload success is provisional until the new version is visible and its downloaded archive matches the inspected build. Keep GitHub tag, npm, PyPI, and production deployment verification as separate receipts.
