import json

import pytest
import responses

from mcpscraper import McpToolError, McpToolsClient, ScraperApiError, ScraperClient


ATTRIBUTION = {"install_channel": "npm", "ai_client": "codex", "ai_model": "gpt-6.1-sol"}


@responses.activate
@pytest.mark.parametrize("operation", ["rest", "raw", "mcp", "memory"])
def test_attribution_and_response_correlation_reach_every_scraper_transport(operation):
    path = {
        "rest": "/reddit/thread",
        "raw": "/workflows/runs/run-1/artifacts/artifact-1",
        "mcp": "/mcp",
        "memory": "/memory/mcp-call",
    }[operation]
    body = {"jsonrpc": "2.0", "id": 1, "result": {"structuredContent": {"ok": True}}} if operation == "mcp" else {"ok": True}
    responses.add(responses.GET if operation == "raw" else responses.POST,
                  "https://mcpscraper.dev" + path, json=body,
                  headers={"x-mcp-request-id": "request-1"})
    receipts = []
    client = ScraperClient("test-key", client_attribution=ATTRIBUTION, on_response=receipts.append)
    if operation == "rest":
        client.reddit.thread({"url": "https://reddit.com/r/test/comments/abc/test"}, idempotency_key="original-key")
    elif operation == "raw":
        client.workflows.get_run_artifact("run-1", "artifact-1")
    elif operation == "mcp":
        client.tools.call_tool("artifact_describe", {"artifactId": "artifact-1"})
    else:
        client.memory_tools.call_tool("searchTool", {"query": "test"})
    headers = responses.calls[0].request.headers
    assert headers["x-api-key"] == "test-key"
    assert headers["x-mcp-client-surface"] == "sdk"
    assert headers["x-mcp-install-channel"] == "npm"
    assert headers["x-mcp-ai-client"] == "codex"
    assert headers["x-mcp-ai-model"] == "gpt-6.1-sol"
    if operation == "rest":
        assert headers["Idempotency-Key"] == "original-key"
    assert receipts == [{"request_id": "request-1", "status": 200}]
    assert client.last_request_id == "request-1"


@responses.activate
@pytest.mark.parametrize("labels, expected", [
    (None, {}),
    ({"surface": "npx", "install_channel": "npx"}, {"x-mcp-install-channel": "npx"}),
    ({"surface": "unknown", "install_channel": "pip", "ai_client": "CLAUDE Code", "ai_model": "private prompt\nsecret"}, {}),
    ({"ai_client": "CLAUDE-CODE", "ai_model": "a" * 80}, {"x-mcp-ai-client": "claude-code", "x-mcp-ai-model": "a" * 80}),
    ({"ai_model": "a" * 81}, {}),
])
def test_only_declared_allowlisted_labels_are_sent(labels, expected, monkeypatch):
    monkeypatch.setenv("MCP_SCRAPER_AI_CLIENT", "chatgpt")
    monkeypatch.setenv("MCP_SCRAPER_INSTALL_CHANNEL", "npx")
    responses.add(responses.POST, "https://mcpscraper.dev/mcp",
                  json={"jsonrpc": "2.0", "id": 1, "result": {"tools": []}})
    McpToolsClient("test-key", client_attribution=labels).list_tools()
    headers = responses.calls[0].request.headers
    actual = {k.lower(): v for k, v in headers.items() if k.lower().startswith("x-mcp-")}
    assert actual == {"x-mcp-client-surface": "sdk", **expected}


@responses.activate
def test_reddit_unknown_outcome_keeps_original_recovery_metadata_without_private_details():
    envelope = {
        "error_code": "response_lost", "error_type": "connection", "message": "Retry with the same key.",
        "retryable": True, "charge_status": "refund_pending",
        "operation": {"runId": "run-1", "idempotencyKey": "original-key", "state": "unknown", "providerToken": "private"},
        "details": {"retry_guidance": "Same request and key only.", "http_status": 503, "provider": "private"},
        "job_id": "job-1", "status": "unknown", "replayed": False,
        "provider": "private", "privateDebug": {"credential": "private"},
    }
    responses.add(responses.POST, "https://mcpscraper.dev/reddit/thread", json=envelope,
                  status=503, headers={"x-mcp-request-id": "failure-1"})
    client = ScraperClient("test-key")
    with pytest.raises(ScraperApiError) as caught:
        client.reddit.thread({"url": "https://reddit.com/r/test/comments/abc/test"}, idempotency_key="original-key")
    error = caught.value
    assert error.request_id == "failure-1"
    assert error.body["operation"] == {"runId": "run-1", "idempotencyKey": "original-key", "state": "unknown"}
    assert error.body["details"] == {"retry_guidance": "Same request and key only.", "http_status": 503}
    assert error.body["job_id"] == "job-1"
    assert "private" not in json.dumps(error.body)
    assert len(responses.calls) == 1


@responses.activate
def test_maps_failure_keeps_status_handle_but_hides_private_diagnostics():
    responses.add(responses.POST, "https://mcpscraper.dev/maps/place", status=500, json={
        "error_code": "maps_place_failed", "message": "Maps run failed", "runId": "run-1",
        "runStatus": "failed", "billingState": "pending_reconciliation", "statusPath": "/maps/place/runs/run-1",
        "detail": "private provider credential",
    })
    with pytest.raises(ScraperApiError) as caught:
        ScraperClient("test-key").maps.place({"businessName": "Fixture", "location": "Denver"})
    assert caught.value.body["statusPath"] == "/maps/place/runs/run-1"
    assert caught.value.body["billingState"] == "pending_reconciliation"
    assert "detail" not in caught.value.body
    assert str(caught.value) == "This operation is temporarily unavailable. Please retry later."


@responses.activate
@pytest.mark.parametrize("failure", ["http", "rpc", "tool"])
def test_mcp_error_has_per_response_request_id_even_if_latest_receipt_changes(failure):
    public = {"error_code": "response_lost", "message": "Same key recovery", "operation": {"runId": "run-1", "idempotencyKey": "original-key", "state": "unknown"}}
    body = public if failure == "http" else {"jsonrpc": "2.0", "id": 1, **(
        {"error": {"code": -32603, "message": "RPC failed", "data": public}} if failure == "rpc"
        else {"result": {"isError": True, "structuredContent": public}})}
    responses.add(responses.POST, "https://mcpscraper.dev/mcp", status=503 if failure == "http" else 200,
                  json=body, headers={"x-mcp-request-id": "failure-1"})
    client = McpToolsClient("test-key", on_response=lambda receipt: setattr(client, "last_request_id", "other-thread"))
    with pytest.raises(McpToolError) as caught:
        client.call_tool("reddit_thread", {"url": "https://reddit.com/r/test/comments/abc/test"})
    assert caught.value.request_id == "failure-1"
    assert len(responses.calls) == 1


@responses.activate
def test_artifact_result_keeps_download_resource_and_complete_structured_envelope():
    result = {"structuredContent": {"delivery": "artifact", "artifactId": "artifact-1", "expiresAt": "2026-10-13T00:00:00Z"},
              "content": [{"type": "resource_link", "uri": "https://mcpscraper.dev/artifacts/token", "name": "full-transcript.txt", "mimeType": "text/plain"}]}
    responses.add(responses.POST, "https://mcpscraper.dev/mcp", json={"jsonrpc": "2.0", "id": 1, "result": result})
    assert McpToolsClient("test-key").call_tool_result("youtube_transcribe", {"url": "https://youtube.com/watch?v=fixture"}) == result


@responses.activate
def test_directory_private_failure_keeps_polling_handle_only():
    responses.add(responses.POST, "https://mcpscraper.dev/directory/run", status=500, json={
        "error_code": "directory_billing_hold_failed", "error": "private provider credential", "jobId": "job-1", "retryable": True,
    })
    with pytest.raises(ScraperApiError) as caught:
        ScraperClient("test-key").directory.run({"query": "Fixture", "state": "Colorado"})
    assert caught.value.body["jobId"] == "job-1"
    assert "private" not in json.dumps(caught.value.body)


@responses.activate
def test_durable_unknown_outcome_preserves_bounded_polling_and_hold_recovery():
    recovery = {"jobId": "job-1", "statusTool": "harvest_paa_status", "executionState": "unknown", "holdState": "unconfirmed"}
    responses.add(responses.POST, "https://mcpscraper.dev/harvest/sync", status=503, json={
        "error_code": "response_lost", "message": "Poll the saved job", "retryable": False,
        "recovery": {**recovery, "private": "drop"}, "job_id": "job-1", "status_tool": "harvest_paa_status",
        "executionState": "unknown", "hold_state": "unconfirmed", "idempotencyFingerprint": "a" * 16,
    })
    with pytest.raises(ScraperApiError) as caught:
        ScraperClient("test-key").harvest_paa("fixture")
    error = caught.value
    assert error.body["recovery"] == recovery
    assert error.body["status_tool"] == "harvest_paa_status"
    assert error.body["hold_state"] == "unconfirmed"
    assert error.body["idempotencyFingerprint"] == "a" * 16
    assert not error.body["retryable"]
    assert len(responses.calls) == 1


@responses.activate
def test_untrusted_recovery_values_are_not_exposed_as_handles():
    responses.add(responses.POST, "https://mcpscraper.dev/harvest/sync", status=503, json={
        "error_code": "response_lost", "message": "Outcome unknown", "job_id": "a" * 201,
        "status_tool": "private prompt", "idempotencyFingerprint": "credential",
        "operation": {"runId": "a" * 201, "idempotencyKey": "key", "state": "unknown"},
        "recovery": {"jobId": "bad job", "statusTool": "poll", "executionState": "unknown", "holdState": "held"},
    })
    with pytest.raises(ScraperApiError) as caught:
        ScraperClient("test-key").harvest_paa("fixture")
    assert not ({"job_id", "status_tool", "idempotencyFingerprint", "operation", "recovery"} & caught.value.body.keys())


@responses.activate
@pytest.mark.parametrize("kind", ["rest", "standalone-mcp", "nested-mcp"])
def test_observer_failure_does_not_replace_success_or_retry_operation(kind):
    receipts = []

    def broken_observer(receipt):
        receipts.append(receipt)
        raise RuntimeError("observer unavailable")

    result = {"ok": True, "result": "original success"}
    url = "https://mcpscraper.dev/reddit/thread" if kind == "rest" else "https://mcpscraper.dev/mcp"
    body = result if kind == "rest" else {"jsonrpc": "2.0", "id": 1, "result": {"structuredContent": result}}
    responses.add(responses.POST, url, json=body, headers={"x-mcp-request-id": "paid-success"})
    client = McpToolsClient("test-key", on_response=broken_observer) if kind == "standalone-mcp" else ScraperClient("test-key", on_response=broken_observer)
    actual = client.reddit.thread({"url": "https://reddit.com/r/test/comments/abc/test"}) if kind == "rest" else (client if kind == "standalone-mcp" else client.tools).call_tool("reddit_thread", {})
    assert actual == result
    assert receipts == [{"request_id": "paid-success", "status": 200}]
    assert client.last_request_id == "paid-success"
    assert len(responses.calls) == 1


@responses.activate
def test_standalone_mcp_observer_failure_preserves_original_error_and_correlation():
    def broken_observer(receipt):
        raise RuntimeError("observer unavailable")

    response = {"error_code": "response_lost", "message": "Original unknown outcome"}
    responses.add(responses.POST, "https://mcpscraper.dev/mcp", json=response, status=503,
                  headers={"x-mcp-request-id": "original-failure"})
    with pytest.raises(McpToolError, match="Original unknown outcome") as caught:
        McpToolsClient("test-key", on_response=broken_observer).call_tool("reddit_thread", {})
    assert caught.value.request_id == "original-failure"
    assert caught.value.http_status == 503
    assert len(responses.calls) == 1
