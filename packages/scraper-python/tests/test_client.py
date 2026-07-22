import json

import pytest
import responses

from mcpscraper import ScraperClient, ScraperApiError
from mcpscraper._mcp_generated_client import MCP_TOOL_BINDINGS, MCP_TOOL_COUNT


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
def test_call_tool_result_preserves_native_image_content():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/mcp",
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "content": [
                    {"type": "text", "text": "# Creative"},
                    {"type": "image", "data": "iVBORw0KGgo=", "mimeType": "image/png"},
                ],
                "structuredContent": {"ok": True, "creativeId": "creative_1"},
            },
        },
        status=200,
    )
    result = ScraperClient(api_key="sk_test").tools.call_tool_result(
        "meta_ad_creative_media", {"connectionId": "conn_1", "adId": "12345"}
    )
    assert result["content"][1]["type"] == "image"
    assert result["content"][1]["data"] == "iVBORw0KGgo="


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
def test_serp_capture_sends_retry_key_and_returns_receipt():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/serp-intelligence/capture",
        json={"billing": {"creditsUsed": 4}},
        headers={"Idempotency-Key": "accepted-serp-key"},
        status=200,
    )
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/serp-intelligence/capture",
        json={"billing": {"creditsUsed": 4}},
        headers={"Idempotency-Key": "generated-serp-key"},
        status=200,
    )
    client = ScraperClient(api_key="sk_test")

    client.serp_intelligence.capture(
        {"query": "roofers near me"}, idempotency_key="caller-serp-key"
    )
    receipt = client.serp_intelligence.capture_with_receipt(
        {"query": "roofers near me"}
    )

    assert responses.calls[0].request.headers["Idempotency-Key"] == "caller-serp-key"
    assert "Idempotency-Key" not in responses.calls[1].request.headers
    assert receipt == {
        "data": {"billing": {"creditsUsed": 4}},
        "idempotency_key": "generated-serp-key",
    }


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


@responses.activate
def test_snake_case_kwargs_are_sent_as_camel_case():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/extract-site",
        json={"pages": []},
        status=200,
    )
    client = ScraperClient(api_key="sk_test")
    client.extract_site("https://example.com", max_pages=100, deposit_to_vault=True, vault_name="research")

    sent_body = json.loads(responses.calls[0].request.body)
    assert sent_body["maxPages"] == 100
    assert sent_body["depositToVault"] is True
    assert sent_body["vaultName"] == "research"
    assert "max_pages" not in sent_body


def test_unified_bindings_contain_all_166_unique_tools():
    assert MCP_TOOL_COUNT == 166
    names = {binding["name"] for binding in MCP_TOOL_BINDINGS}
    assert len(names) == 166
    assert {
        "export_connected_service_data",
        "export_search_console_table_data",
        "renew_connected_data_download",
        "describe_service_connection_tool",
        "import_service_connection_to_memory",
    } <= names


@responses.activate
def test_unified_tool_dispatches_through_mcp():
    search_result = {
        "query": "roofers denver",
        "location": None,
        "organicResults": [],
        "localPack": [],
        "aiOverview": None,
        "entityIds": None,
    }
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/mcp",
        json={"jsonrpc": "2.0", "id": 1, "result": {"structuredContent": search_result}},
        status=200,
    )
    client = ScraperClient(api_key="sk_test")
    result = client.tools.search.search_serp(query="roofers denver")
    sent_body = json.loads(responses.calls[0].request.body)
    assert sent_body["params"]["name"] == "search_serp"
    assert sent_body["params"]["arguments"] == {"query": "roofers denver"}
    assert result.model_dump(by_alias=True) == search_result


@responses.activate
def test_bulk_connected_data_export_dispatches_as_one_mcp_call():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/mcp",
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "result": {"structuredContent": {"ok": True, "complete": True, "error": None}},
        },
        status=200,
    )
    client = ScraperClient(api_key="sk_test")
    result = client.tools.connections.export_connected_service_data(
        connection_id="meta_conn_123",
        dataset="meta_ads_insights",
        last_days=30,
        delivery="artifact",
    )
    sent_body = json.loads(responses.calls[0].request.body)
    assert sent_body["params"]["name"] == "export_connected_service_data"
    assert sent_body["params"]["arguments"] == {
        "connectionId": "meta_conn_123",
        "dataset": "meta_ads_insights",
        "lastDays": 30,
        "delivery": "artifact",
    }
    dumped = result.model_dump(by_alias=True) if hasattr(result, "model_dump") else result
    assert dumped["ok"] is True
    assert dumped["complete"] is True
    assert dumped["error"] is None


@responses.activate
def test_unified_tools_list_retries_transient_migration_failure():
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/mcp",
        json={"error_code": "migration_failed"},
        status=503,
    )
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/mcp",
        json={"jsonrpc": "2.0", "id": 2, "result": {"tools": [{"name": "search_serp"}]}},
        status=200,
    )
    client = ScraperClient(api_key="sk_test")
    client.tools._retry_delay_s = 0
    assert client.tools.list_tools()[0]["name"] == "search_serp"
    assert len(responses.calls) == 2
