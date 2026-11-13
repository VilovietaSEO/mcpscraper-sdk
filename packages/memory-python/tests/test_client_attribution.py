import json

import pytest
import responses

from mcpscraper_memory import MemoryApiError, MemoryClient, McpToolError, McpToolsClient


@responses.activate
@pytest.mark.parametrize("kind", ["direct", "unified"])
def test_memory_attribution_and_response_receipt_keep_auth_and_result(kind):
    response = {"jsonrpc": "2.0", "id": 1, "result": {"structuredContent": {"ok": True, "results": [{"text": "fixture"}]}}}
    responses.add(responses.POST, "https://mcpscraper.dev/mcp", json=response,
                  headers={"x-mcp-request-id": "memory-request"})
    receipts = []
    factory = MemoryClient if kind == "direct" else McpToolsClient
    client = factory("test-key", client_attribution={"install_channel": "source", "ai_client": "claude-code", "ai_model": "claude/opus-4"}, on_response=receipts.append)
    result = client.memory.search(query="fixture") if kind == "direct" else client.call_tool("searchTool", {"query": "fixture"})
    assert result.ok if kind == "direct" else result["ok"]
    headers = responses.calls[0].request.headers
    assert headers["x-api-key"] == "test-key"
    assert headers["x-mcp-client-surface"] == "sdk"
    assert headers["x-mcp-install-channel"] == "source"
    assert headers["x-mcp-ai-client"] == "claude-code"
    assert headers["x-mcp-ai-model"] == "claude/opus-4"
    assert receipts == [{"request_id": "memory-request", "status": 200}]
    assert client.last_request_id == "memory-request"


@responses.activate
@pytest.mark.parametrize("kind", ["direct", "unified"])
def test_memory_unknown_labels_do_not_read_environment_or_guess_client(kind, monkeypatch):
    monkeypatch.setenv("MCP_SCRAPER_AI_CLIENT", "codex")
    responses.add(responses.POST, "https://mcpscraper.dev/mcp",
                  json={"jsonrpc": "2.0", "id": 1, "result": {"structuredContent": {"ok": True, "results": []}}})
    factory = MemoryClient if kind == "direct" else McpToolsClient
    client = factory("test-key", client_attribution={"install_channel": "pip", "ai_client": "unknown", "ai_model": "private model name"})
    client.memory.search(query="fixture") if kind == "direct" else client.call_tool("searchTool", {"query": "fixture"})
    headers = responses.calls[0].request.headers
    assert {k.lower(): v for k, v in headers.items() if k.lower().startswith("x-mcp-")} == {"x-mcp-client-surface": "sdk"}


@responses.activate
@pytest.mark.parametrize("kind", ["direct", "unified"])
@pytest.mark.parametrize("failure", ["http", "rpc", "tool"])
def test_memory_error_correlation_is_per_response_and_no_paid_retry(kind, failure):
    body = {"error_code": "response_lost", "message": "Unknown outcome"} if failure == "http" else {"jsonrpc": "2.0", "id": 1, **(
        {"error": {"code": -32603, "message": "RPC failed"}} if failure == "rpc"
        else {"result": {"isError": True, "structuredContent": {"message": "Tool failed"}}})}
    responses.add(responses.POST, "https://mcpscraper.dev/mcp", json=body, status=503 if failure == "http" else 200,
                  headers={"x-mcp-request-id": "failure-request"})
    factory, error_class = (MemoryClient, MemoryApiError) if kind == "direct" else (McpToolsClient, McpToolError)
    client = factory("test-key", on_response=lambda receipt: setattr(client, "last_request_id", "other-thread"))
    with pytest.raises(error_class) as caught:
        client.memory.search(query="fixture") if kind == "direct" else client.call_tool("searchTool", {"query": "fixture"})
    assert caught.value.request_id == "failure-request"
    assert len(responses.calls) == 1


@responses.activate
def test_memory_direct_accepts_hosted_sse_without_losing_correlation():
    payload = {"jsonrpc": "2.0", "id": 1, "result": {"structuredContent": {"ok": True, "results": []}}}
    responses.add(responses.POST, "https://mcpscraper.dev/mcp", body=f'event: message\ndata: {json.dumps(payload)}\n\n',
                  content_type="text/event-stream", headers={"x-mcp-request-id": "sse-request"})
    client = MemoryClient("test-key")
    assert client.memory.search(query="fixture").ok
    assert client.last_request_id == "sse-request"


@responses.activate
def test_memory_unified_artifact_resources_are_preserved():
    result = {"structuredContent": {"delivery": "artifact", "artifactId": "artifact-1"},
              "content": [{"type": "resource_link", "uri": "https://mcpscraper.dev/artifacts/token", "name": "transcript.txt", "mimeType": "text/plain"}]}
    responses.add(responses.POST, "https://mcpscraper.dev/mcp", json={"jsonrpc": "2.0", "id": 1, "result": result})
    assert McpToolsClient("test-key").call_tool_result("artifact_download", {"artifactId": "artifact-1"}) == result


@responses.activate
@pytest.mark.parametrize("kind", ["direct", "unified"])
def test_install_channel_does_not_override_sdk_surface(kind):
    responses.add(responses.POST, "https://mcpscraper.dev/mcp", json={
        "jsonrpc": "2.0", "id": 1, "result": {"structuredContent": {"ok": True, "results": []}},
    })
    factory = MemoryClient if kind == "direct" else McpToolsClient
    client = factory("test-key", client_attribution={"surface": "npx", "install_channel": "npx"})
    client.memory.search(query="fixture") if kind == "direct" else client.call_tool("searchTool", {"query": "fixture"})
    headers = responses.calls[0].request.headers
    assert headers["x-mcp-client-surface"] == "sdk"
    assert headers["x-mcp-install-channel"] == "npx"


@responses.activate
@pytest.mark.parametrize("kind", ["direct", "unified"])
def test_memory_observer_failure_preserves_success_and_does_not_retry(kind):
    receipts = []

    def broken_observer(receipt):
        receipts.append(receipt)
        raise RuntimeError("observer unavailable")

    responses.add(responses.POST, "https://mcpscraper.dev/mcp", json={
        "jsonrpc": "2.0", "id": 1, "result": {"structuredContent": {"ok": True, "results": [{"text": "original success"}]}},
    }, headers={"x-mcp-request-id": "paid-memory-success"})
    factory = MemoryClient if kind == "direct" else McpToolsClient
    client = factory("test-key", on_response=broken_observer)
    result = client.memory.search(query="fixture") if kind == "direct" else client.call_tool("searchTool", {"query": "fixture"})
    assert result.results[0]["text"] == "original success" if kind == "direct" else result["results"][0]["text"] == "original success"
    assert receipts == [{"request_id": "paid-memory-success", "status": 200}]
    assert client.last_request_id == "paid-memory-success"
    assert len(responses.calls) == 1


@responses.activate
@pytest.mark.parametrize("kind", ["direct", "unified"])
def test_memory_observer_failure_preserves_original_error_and_correlation(kind):
    def broken_observer(receipt):
        raise RuntimeError("observer unavailable")

    responses.add(responses.POST, "https://mcpscraper.dev/mcp", json={
        "jsonrpc": "2.0", "id": 1, "result": {"isError": True, "structuredContent": {"message": "Original operation failure"}},
    }, headers={"x-mcp-request-id": "original-memory-failure"})
    factory, error_class = (MemoryClient, MemoryApiError) if kind == "direct" else (McpToolsClient, McpToolError)
    client = factory("test-key", on_response=broken_observer)
    with pytest.raises(error_class, match="Original operation failure") as caught:
        client.memory.search(query="fixture") if kind == "direct" else client.call_tool("searchTool", {"query": "fixture"})
    assert caught.value.request_id == "original-memory-failure"
    assert len(responses.calls) == 1
