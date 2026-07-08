import json

import pytest
import responses

from mcpscraper import ScraperClient, ScraperApiError


@responses.activate
def test_search_serp_sends_serp_only_true():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/harvest/sync",
        json={"job_id": "job_1", "status": "done", "result": {"organic": []}},
        status=200,
    )
    client = ScraperClient(api_key="sk_test")
    result = client.search_serp(query="roof repair denver")

    sent_body = json.loads(responses.calls[0].request.body)
    assert sent_body["serpOnly"] is True
    assert sent_body["query"] == "roof repair denver"
    assert responses.calls[0].request.headers["x-api-key"] == "sk_test"
    assert result["job_id"] == "job_1"


@responses.activate
def test_harvest_paa_omits_serp_only():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/harvest/sync",
        json={"job_id": "job_2", "status": "done"},
        status=200,
    )
    client = ScraperClient(api_key="sk_test")
    client.harvest_paa(query="roof repair cost")

    sent_body = json.loads(responses.calls[0].request.body)
    assert "serpOnly" not in sent_body


@responses.activate
def test_non_2xx_response_raises_scraper_api_error():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/extract-url",
        json={"error": "bad_request", "error_code": "invalid_query", "message": "query is required"},
        status=400,
    )
    client = ScraperClient(api_key="sk_test")

    with pytest.raises(ScraperApiError) as exc_info:
        client.extract_url(url="not-a-url")

    err = exc_info.value
    assert err.status == 400
    assert err.code == "invalid_query"
    assert str(err) == "query is required"


@responses.activate
def test_insufficient_balance_is_distinguishable():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/harvest/sync",
        json={
            "error": "insufficient_balance",
            "error_code": "insufficient_balance",
            "message": "Not enough credits",
            "balance_credits": 0.5,
            "required_credits": 1,
            "topup_url": "https://mcpscraper.dev/billing",
        },
        status=402,
    )
    client = ScraperClient(api_key="sk_test")

    with pytest.raises(ScraperApiError) as exc_info:
        client.harvest_paa(query="x")

    err = exc_info.value
    assert err.is_insufficient_balance()
    assert not err.is_concurrency_limit_exceeded()
    assert err.body["required_credits"] == 1


@responses.activate
def test_concurrency_limit_exceeded_is_distinguishable():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/map-urls",
        json={
            "error": "concurrency_limit_exceeded",
            "error_code": "concurrency_limit_exceeded",
            "error_type": "concurrency_limit",
            "message": "Too many concurrent operations",
            "retryable": True,
            "active": 1,
            "limit": 1,
        },
        status=429,
    )
    client = ScraperClient(api_key="sk_test")

    with pytest.raises(ScraperApiError) as exc_info:
        client.map_site_urls(url="https://example.com")

    err = exc_info.value
    assert err.is_concurrency_limit_exceeded()
    assert not err.is_insufficient_balance()


@responses.activate
def test_namespaced_methods_hit_the_right_path():
    responses.add(responses.POST, "https://mcpscraper.dev/maps/search", json={}, status=200)
    responses.add(responses.GET, "https://mcpscraper.dev/workflows/runs/run_123", json={}, status=200)

    client = ScraperClient(api_key="sk_test")
    client.maps.search({"query": "roofers", "location": "Austin, TX"})
    client.workflows.get_run("run_123")

    assert responses.calls[0].request.url == "https://mcpscraper.dev/maps/search"
    assert responses.calls[1].request.url == "https://mcpscraper.dev/workflows/runs/run_123"


@responses.activate
def test_extract_url_with_deposit_to_vault_returns_memory_field():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/extract-url",
        json={
            "title": "Example",
            "bodyMarkdown": "# Example",
            "memory": {"deposited": True, "vault": "research", "noteId": "note_1", "chunks": 3},
        },
        status=200,
    )
    client = ScraperClient(api_key="sk_test")
    result = client.extract_url(url="https://example.com", depositToVault=True, vaultName="research")

    sent_body = json.loads(responses.calls[0].request.body)
    assert sent_body["depositToVault"] is True
    assert sent_body["vaultName"] == "research"
    assert result["memory"]["deposited"] is True
    assert result["memory"]["noteId"] == "note_1"


@responses.activate
def test_memory_tools_dispatches_through_memory_mcp_call():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/memory/mcp-call",
        json={"ok": True, "results": [{"text": "a fact", "source": "note:roofing.md", "score": 0.9}]},
        status=200,
    )
    client = ScraperClient(api_key="sk_test")
    result = client.memory_tools.call_tool("searchTool", {"query": "roofing warranty terms"})

    sent_body = json.loads(responses.calls[0].request.body)
    assert sent_body["toolName"] == "searchTool"
    assert sent_body["args"] == {"query": "roofing warranty terms"}
    assert result["ok"] is True


@responses.activate
def test_memory_tools_raises_on_tool_level_ok_false():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/memory/mcp-call",
        json={"ok": False, "error": "vault not found"},
        status=200,
    )
    client = ScraperClient(api_key="sk_test")

    with pytest.raises(ScraperApiError) as exc_info:
        client.memory_tools.call_tool("listVaultsTool")

    assert str(exc_info.value) == "vault not found"
