import json

import pytest
import responses

from mcpscraper_memory import MemoryClient, MemoryApiError, McpToolsClient
from mcpscraper_memory._mcp_generated_client import MCP_TOOL_BINDINGS, MCP_TOOL_COUNT
from mcpscraper_memory.models.create_scheduled_action import (
    CreateScheduledActionInput,
    CreateScheduledActionOutput,
)
from mcpscraper_memory.mcp_models.update_scheduled_action import (
    UpdateScheduledActionInput as UnifiedUpdateScheduledActionInput,
)
from mcpscraper_memory.models.get_schedule_link import GetScheduleLinkOutput
from mcpscraper_memory.models.get_schedule_status import GetScheduleStatusOutput
from mcpscraper_memory.models.resume_scheduled_action import ResumeScheduledActionOutput
from mcpscraper_memory.models.set_schedule_entitlement import SetScheduleEntitlementInput

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
def test_files_file_asset_save_exposes_original_attachment_persistence():
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
                    "result": {"structuredContent": {"ok": True, "reusedObject": False}},
                }
            ),
        )

    responses.add_callback(responses.POST, f"{BASE_URL}/mcp", callback=handler, content_type="application/json")

    result = MemoryClient(api_key="mk_test").files.file_asset_save(
        artifactId="artifact_gmail_attachment_1",
        title="invoice.pdf",
        idempotencyKey="gmail-import-attachment-1",
    )

    assert captured["body"]["params"]["name"] == "file_asset_save"
    assert captured["body"]["params"]["arguments"] == {
        "artifactId": "artifact_gmail_attachment_1",
        "title": "invoice.pdf",
        "idempotencyKey": "gmail-import-attachment-1",
    }
    assert result.ok is True


@responses.activate
def test_mcp_tools_client_preserves_native_image_content():
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
                "structuredContent": {"ok": True},
            },
        },
        status=200,
    )
    result = McpToolsClient(api_key="sk_test").call_tool_result(
        "meta_ad_creative_media", {"connectionId": "conn_1", "adId": "12345"}
    )
    assert result["content"][1]["type"] == "image"
    assert result["content"][1]["data"] == "iVBORw0KGgo="


@responses.activate
def test_mcp_tools_client_parses_hosted_sse_response():
    structured = {
        "balanceCredits": 100,
        "matchedCost": None,
        "costs": [],
        "ledger": [],
        "concurrency": None,
        "connectedAccounts": None,
    }
    responses.add(
        responses.POST,
        "https://mcpscraper.dev/mcp",
        body=f'event: message\ndata: {json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"structuredContent": structured}})}\n\n',
        status=200,
        content_type="text/event-stream",
    )

    result = McpToolsClient(api_key="sk_test").billing.credits_info()
    assert result.balance_credits == 100


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


def test_unified_bindings_contain_every_contract_tool():
    assert MCP_TOOL_COUNT == len(MCP_TOOL_BINDINGS)
    names = {binding["name"] for binding in MCP_TOOL_BINDINGS}
    assert len(set(names)) == MCP_TOOL_COUNT
    assert {
        "export_connected_service_data",
        "export_search_console_table_data",
        "renew_connected_data_download",
        "describe_service_connection_tool",
        "import_service_connection_to_memory",
        "archive_read",
        "list_scheduled_runs",
        "create_artifact_template",
        "create_scheduled_run_view_link",
    } <= names


def test_direct_scheduling_models_match_the_credit_metered_contract():
    create_input = CreateScheduledActionInput(
        description="Sync Drive",
        vault="Knowledge",
        cadence="daily",
        executionMode="connection_sync",
    )
    assert create_input.execution_mode == "connection_sync"

    create_output = CreateScheduledActionOutput(
        ok=True,
        executionMode="agent",
        artifactSelection={"mode": "none"},
    )
    assert create_output.execution_mode == "agent"
    assert "code" in CreateScheduledActionOutput.model_fields
    assert "code" in GetScheduleLinkOutput.model_fields
    assert "code" in GetScheduleStatusOutput.model_fields
    assert "code" in ResumeScheduledActionOutput.model_fields
    assert {
        "billing_mode",
        "run_base_credits",
        "llm_cost_multiplier",
        "default_timezone",
    } <= set(GetScheduleStatusOutput.model_fields)

    entitlement = SetScheduleEntitlementInput(granteeIdentity="owner@example.com")
    assert entitlement.enabled is None

    pinned_update = UnifiedUpdateScheduledActionInput(
        id="schedule_1",
        artifactSelection={
            "mode": "saved_template",
            "templateId": "00000000-0000-4000-8000-000000000001",
            "templateVersionId": "00000000-0000-4000-8000-000000000002",
        },
    )
    assert pinned_update.artifact_selection["mode"] == "saved_template"


@responses.activate
def test_scheduled_results_and_templates_use_exact_unified_wire_names():
    captured = []

    def handler(request):
        body = json.loads(request.body)
        captured.append(body)
        if body["params"]["name"] == "list_scheduled_runs":
            result = {"ok": True, "items": [], "nextCursor": None}
        else:
            result = {"ok": True, "presets": [], "templates": []}
        return (
            200,
            {},
            json.dumps(
                {
                    "jsonrpc": "2.0",
                    "id": body["id"],
                    "result": {"structuredContent": result},
                }
            ),
        )

    responses.add_callback(
        responses.POST,
        "https://mcpscraper.dev/mcp",
        callback=handler,
        content_type="application/json",
    )

    client = McpToolsClient(api_key="sk_test")
    runs = client.schedule.list_scheduled_runs(view="inbox", limit=30)
    templates = client.schedule.list_artifact_templates(status="all")

    assert captured[0]["params"] == {
        "name": "list_scheduled_runs",
        "arguments": {"view": "inbox", "limit": 30},
    }
    assert captured[1]["params"] == {
        "name": "list_artifact_templates",
        "arguments": {"status": "all"},
    }
    assert runs.next_cursor is None
    assert templates.templates == []


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
