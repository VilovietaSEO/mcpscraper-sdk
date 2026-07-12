import json

import pytest
import responses

from mcpscraper_memory import MemoryClient, MemoryApiError, McpToolsClient
from mcpscraper_memory._mcp_generated_client import MCP_TOOL_BINDINGS, MCP_TOOL_COUNT

BASE_URL = "https://memory.mcpscraper.dev"


@responses.activate
def test_memory_search_sends_correct_wire_tool_name_and_parses_structured_content():
    captured = {}

    def handler(request):
        captured["body"] = json.loads(request.body)
        return (
            200,
            {},
            json.dumps(
                {
                    "jsonrpc": "2.0",
                    "id": captured["body"]["id"],
                    "result": {"structuredContent": {"ok": True, "results": [{"text": "hello", "source": "note:a", "score": 0.9}]}},
                }
            ),
        )

    responses.add_callback(responses.POST, f"{BASE_URL}/mcp", callback=handler, content_type="application/json")

    client = MemoryClient(api_key="mk_test")
    result = client.memory.search(query="hello world")

    assert captured["body"]["method"] == "tools/call"
    assert captured["body"]["params"]["name"] == "searchTool"
    assert captured["body"]["params"]["arguments"] == {"query": "hello world"}
    assert result.ok is True
    assert result.results[0]["text"] == "hello"


@responses.activate
def test_access_headers_include_accept_and_authorization():
    captured = {}

    def handler(request):
        captured["headers"] = dict(request.headers)
        captured["body"] = json.loads(request.body)
        vault = {"vault": "Ideas", "handle": "Ideas", "role": "owner", "notes": 3, "bytes": 1024, "kind": "notes"}
        return (200, {}, json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"structuredContent": {"ok": True, "vaults": [vault]}}}))

    responses.add_callback(responses.POST, f"{BASE_URL}/mcp", callback=handler, content_type="application/json")

    client = MemoryClient(api_key="mk_test")
    result = client.vaults.list_vaults()

    assert captured["headers"]["accept"] == "application/json, text/event-stream"
    assert captured["headers"]["authorization"] == "Bearer mk_test"
    assert captured["body"]["params"]["name"] == "listVaultsTool"
    assert result.ok is True


@responses.activate
def test_json_rpc_error_raises_memory_api_error():
    responses.add(
        responses.POST,
        f"{BASE_URL}/mcp",
        json={"jsonrpc": "2.0", "id": 1, "error": {"code": -32602, "message": "Invalid params"}},
        status=200,
    )

    client = MemoryClient(api_key="mk_test")
    with pytest.raises(MemoryApiError, match="Invalid params"):
        client.memory.search(query="x")


@responses.activate
def test_mcp_tool_level_is_error_raises_memory_api_error():
    responses.add(
        responses.POST,
        f"{BASE_URL}/mcp",
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "result": {"content": [{"type": "text", "text": json.dumps({"message": "vault not found"})}], "isError": True},
        },
        status=200,
    )

    client = MemoryClient(api_key="mk_test")
    with pytest.raises(MemoryApiError, match="vault not found"):
        client.vaults.list_vaults()


@responses.activate
def test_non_2xx_http_response_raises_memory_api_error():
    responses.add(responses.POST, f"{BASE_URL}/mcp", body="server error", status=500)

    client = MemoryClient(api_key="mk_test")
    with pytest.raises(MemoryApiError) as exc_info:
        client.memory.search(query="x")
    assert exc_info.value.http_status == 500


def test_unified_bindings_contain_all_157_unique_tools():
    assert MCP_TOOL_COUNT == 157
    names = {binding["name"] for binding in MCP_TOOL_BINDINGS}
    assert len(names) == 157
    assert {
        "export_connected_service_data",
        "renew_connected_data_download",
        "describe_service_connection_tool",
        "import_service_connection_to_memory",
    } <= names


@responses.activate
def test_memory_package_unified_client_calls_scraper_and_memory_tools():
    session_result = {
        "ok": True,
        "tool": "browser_list_sessions",
        "session_id": None,
        "sessions": [],
        "count": 0,
    }
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/mcp",
        json={"jsonrpc": "2.0", "id": 1, "result": {"structuredContent": session_result}},
        status=200,
    )
    client = McpToolsClient(api_key="sk_test")
    result = client.browser.list_sessions()
    sent_body = json.loads(responses.calls[0].request.body)
    assert sent_body["params"]["name"] == "browser_list_sessions"
    assert result.model_dump(by_alias=True) == session_result
