import json
import pytest
from requests import Response
from mcpscraper.mcp_client import _parse_json_rpc_response


def response(body: str, encoding: str = "ISO-8859-1") -> Response:
    result = Response()
    result.status_code = 200
    result.headers["content-type"] = "text/event-stream"
    result.encoding = encoding
    result._content = body.encode("utf-8")
    return result


@pytest.mark.parametrize("text", ["★★★★★ café", "before\u2028after", "before\u0085after"])
def test_sse_decodes_utf8_without_splitting_unicode_text(text):
    payload = {"jsonrpc": "2.0", "id": 1, "result": {"text": text}}
    body = "event: message\ndata: " + json.dumps(payload, ensure_ascii=False) + "\n\n"
    assert _parse_json_rpc_response(response(body)) == payload


def test_sse_joins_data_lines_and_ignores_comments_and_done():
    body = ': keepalive\r\nevent: message\r\ndata: {"jsonrpc":"2.0",\r\ndata: "id":1,"result":{"ok":true}}\r\n\r\ndata: [DONE]\r\n\r\n'
    assert _parse_json_rpc_response(response(body))["result"] == {"ok": True}


def test_sse_keeps_response_when_a_notification_follows():
    body = 'data: {"id":1,"result":{"ok":true}}\n\ndata: {"method":"notifications/progress","params":{}}\n\n'
    assert _parse_json_rpc_response(response(body))["result"] == {"ok": True}


def test_sse_accepts_event_id_before_data():
    body = 'id: event-1\nretry: 1000\ndata: {"id":1,"result":{"ok":true}}\n\n'
    assert _parse_json_rpc_response(response(body))["result"] == {"ok": True}
