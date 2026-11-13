import json
from requests import Response
from mcpscraper_memory.mcp_client import McpToolsClient


def test_modern_routing_matches_body_metadata():
    calls = []

    class Session:
        def post(self, url, *, headers, json, timeout):
            assert headers["mcp-protocol-version"] == "2026-07-28"
            assert json["params"]["_meta"]["io.modelcontextprotocol/clientCapabilities"] == {}
            assert json["params"]["_meta"]["io.modelcontextprotocol/clientInfo"] == {"name": "mcpscraper-python", "version": "1"}
            assert headers["mcp-method"] == json["method"]
            assert json["params"]["_meta"]["io.modelcontextprotocol/protocolVersion"] == "2026-07-28"
            assert headers.get("mcp-name") == json["params"].get("name")
            calls.append(json)
            response = Response()
            response.status_code = 200
            response.headers["content-type"] = "application/json"
            response._content = b'{"jsonrpc":"2.0","id":1,"result":{"tools":[]}}'
            return response

    client = McpToolsClient("test-key", session=Session())
    client.list_tools()
    client._request("tools/call", {"name": "maps_place_status", "arguments": {"runId": "existing"}})
    assert [c["method"] for c in calls] == ["tools/list", "tools/call"]
