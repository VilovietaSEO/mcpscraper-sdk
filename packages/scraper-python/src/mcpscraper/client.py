from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

import requests

from .errors import ScraperApiError
from .mcp_client import McpToolsClient

JsonDict = dict[str, Any]


def _camel_key(key: str) -> str:
    if "_" not in key:
        return key
    head, *rest = key.split("_")
    return head + "".join(word[:1].upper() + word[1:] for word in rest if word)


def _camelize(value: Any) -> Any:
    if isinstance(value, dict):
        return {_camel_key(k) if isinstance(k, str) else k: _camelize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_camelize(v) for v in value]
    return value


class _Requester:
    def __init__(self, api_key: str, base_url: str, session: requests.Session, timeout: float) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._session = session
        self._timeout = timeout

    def call(
        self,
        method: str,
        path: str,
        body: Optional[JsonDict] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Any:
        data, _response = self.call_with_receipt(method, path, body, headers)
        return data

    def call_with_receipt(
        self,
        method: str,
        path: str,
        body: Optional[JsonDict] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> tuple[Any, requests.Response]:
        request_headers = {"x-api-key": self._api_key}
        if headers:
            request_headers.update(headers)
        payload = _camelize(body) if body is not None else None
        try:
            response = self._session.request(
                method,
                f"{self._base_url}{path}",
                json=payload,
                headers=request_headers,
                timeout=self._timeout,
            )
        except requests.Timeout as error:
            raise ScraperApiError(408, {
                "error": "mcp_request_timeout",
                "error_code": "mcp_request_timeout",
                "error_type": "timeout",
                "message": f"The client stopped waiting after {self._timeout:g}s. This does not prove server-side work stopped; reuse the same Idempotency-Key or poll its job before starting another paid run.",
                "retryable": True,
            }) from error
        try:
            data = response.json()
        except ValueError:
            data = None
        if not response.ok:
            raise ScraperApiError(response.status_code, data)
        return data, response

    def call_raw(self, method: str, path: str) -> bytes:
        headers = {"x-api-key": self._api_key}
        try:
            response = self._session.request(method, f"{self._base_url}{path}", headers=headers, timeout=self._timeout)
        except requests.Timeout as error:
            raise ScraperApiError(408, {
                "error": "mcp_request_timeout",
                "error_code": "mcp_request_timeout",
                "error_type": "timeout",
                "message": f"The client stopped waiting after {self._timeout:g}s. This does not prove server-side work stopped.",
                "retryable": True,
            }) from error
        if not response.ok:
            try:
                data = response.json()
            except ValueError:
                data = None
            raise ScraperApiError(response.status_code, data)
        return response.content


class YoutubeNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def harvest(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/youtube/harvest", params)

    def transcribe(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/youtube/transcribe", params)


class ScreenshotNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def capture(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/screenshot", params)


class FacebookNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def ad(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/facebook/ad", params)

    def page_intel(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/facebook/page-intel", params)

    def ad_transcribe(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/facebook/transcribe", params)

    def video_transcribe(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/facebook/video-transcribe", params)

    def search(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/facebook/search", params)

    def media(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/facebook/media", params)


class GoogleAdsNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def search(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/google-ads/search", params)

    def page_intel(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/google-ads/page-intel", params)

    def transcribe(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/google-ads/transcribe", params)


class InstagramNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def profile_content(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/instagram/profile-content", params)

    def media_download(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/instagram/media-download", params)


class RedditNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def thread(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/reddit/thread", params)


class VideoNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def analyze(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/video/analyze", params)

    def status(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/video/status", params)


class MapsNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def search(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/maps/search", params)

    def place(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/maps/place", params)


class DirectoryNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def run(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/directory/run", params)


class SerpIntelligenceNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def capture(
        self,
        params: JsonDict,
        *,
        idempotency_key: str | None = None,
    ) -> Any:
        headers = {} if idempotency_key is None else {"Idempotency-Key": idempotency_key}
        return self._r.call("POST", "/serp-intelligence/capture", params, headers)

    def capture_with_receipt(
        self,
        params: JsonDict,
        *,
        idempotency_key: str | None = None,
    ) -> JsonDict:
        headers = {} if idempotency_key is None else {"Idempotency-Key": idempotency_key}
        data, response = self._r.call_with_receipt(
            "POST", "/serp-intelligence/capture", params, headers
        )
        return {
            "data": data,
            "idempotency_key": response.headers.get("Idempotency-Key"),
        }

    def page_snapshots(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/serp-intelligence/page-snapshots", params)


class WorkflowsNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def list_definitions(self) -> Any:
        return self._r.call("GET", "/workflows/definitions")

    def run(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/workflows/run", params)

    def advance_step(self, run_id: str) -> Any:
        return self._r.call("POST", f"/workflows/runs/{quote(run_id)}/step")

    def list_runs(self) -> Any:
        return self._r.call("GET", "/workflows/runs")

    def get_run(self, run_id: str) -> Any:
        return self._r.call("GET", f"/workflows/runs/{quote(run_id)}")

    def get_run_artifact(self, run_id: str, artifact_id: str) -> bytes:
        return self._r.call_raw("GET", f"/workflows/runs/{quote(run_id)}/artifacts/{quote(artifact_id)}")

    def create_schedule(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/workflows/schedules", params)

    def list_schedules(self) -> Any:
        return self._r.call("GET", "/workflows/schedules")

    def patch_schedule(self, schedule_id: str, params: JsonDict) -> Any:
        return self._r.call("PATCH", f"/workflows/schedules/{quote(schedule_id)}", params)

    def delete_schedule(self, schedule_id: str) -> Any:
        return self._r.call("DELETE", f"/workflows/schedules/{quote(schedule_id)}")

    def run_schedule_now(self, schedule_id: str) -> Any:
        return self._r.call("POST", f"/workflows/schedules/{quote(schedule_id)}/run")


class GmailNamespace:
    def __init__(self, r: _Requester) -> None:
        self._r = r

    def search_messages(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/api/gmail/messages/search", params)

    def get_message(self, message_id: str, params: JsonDict) -> Any:
        return self._r.call("POST", f"/api/gmail/messages/{quote(message_id, safe='')}", params)

    def get_attachment(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/api/gmail/attachments/get", params)

    def prepare_selection(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/api/gmail/selections", params)

    def export_selection(self, selection_id: str, params: JsonDict) -> Any:
        return self._r.call("POST", f"/api/gmail/selections/{quote(selection_id, safe='')}/export", params)

    def bulk_manage(self, selection_id: str, params: JsonDict, *, idempotency_key: str) -> Any:
        return self._r.call("POST", f"/api/gmail/selections/{quote(selection_id, safe='')}/manage", params, {"Idempotency-Key": idempotency_key})

    def bulk_delete(self, selection_id: str, params: JsonDict, *, idempotency_key: str) -> Any:
        return self._r.call("POST", f"/api/gmail/selections/{quote(selection_id, safe='')}/delete", params, {"Idempotency-Key": idempotency_key})

    def prepare_memory_import(self, params: JsonDict) -> Any:
        return self._r.call("POST", "/api/gmail/imports/prepare", params)

    def import_to_memory(self, import_plan_id: str, *, idempotency_key: str) -> Any:
        return self._r.call("POST", f"/api/gmail/imports/{quote(import_plan_id, safe='')}/start", headers={"Idempotency-Key": idempotency_key})

    def import_status(self, ingest_id: str) -> Any:
        return self._r.call("GET", f"/api/gmail/imports/{quote(ingest_id, safe='')}")


class MemoryTools:
    """Dispatches to any of the 86 memory.mcpscraper.dev tools via POST /memory/mcp-call,
    using only this client's mcpscraper.dev API key. See contracts/memory.tools.json in the
    repo (or the mcpscraper-memory-sdk Python package, once published) for the full tool list
    and per-tool argument shapes - this is a generic call_tool(name, args) passthrough rather
    than a fully typed method per tool.
    """

    def __init__(self, r: _Requester) -> None:
        self._r = r

    def call_tool(self, tool_name: str, args: Optional[JsonDict] = None) -> Any:
        result = self._r.call("POST", "/memory/mcp-call", {"toolName": tool_name, "args": args or {}})
        if isinstance(result, dict) and result.get("ok") is False:
            raise ScraperApiError(200, {"message": result.get("error"), **result})
        return result


class ScraperClient:
    def __init__(self, api_key: str, base_url: str = "https://mcpscraper.dev", session: Optional[requests.Session] = None, request_timeout: float = 590.0) -> None:
        if request_timeout <= 0:
            raise ValueError("request_timeout must be positive")
        active_session = session or requests.Session()
        self._r = _Requester(api_key, base_url, active_session, request_timeout)
        self.tools = McpToolsClient(api_key, base_url, active_session, request_timeout=request_timeout)
        self.youtube = YoutubeNamespace(self._r)
        self.screenshot = ScreenshotNamespace(self._r)
        self.facebook = FacebookNamespace(self._r)
        self.google_ads = GoogleAdsNamespace(self._r)
        self.instagram = InstagramNamespace(self._r)
        self.reddit = RedditNamespace(self._r)
        self.video = VideoNamespace(self._r)
        self.maps = MapsNamespace(self._r)
        self.directory = DirectoryNamespace(self._r)
        self.serp_intelligence = SerpIntelligenceNamespace(self._r)
        self.workflows = WorkflowsNamespace(self._r)
        self.gmail = GmailNamespace(self._r)
        self.memory_tools = MemoryTools(self._r)

    def search_serp(self, query: str, **kwargs: Any) -> Any:
        return self._r.call("POST", "/harvest/sync", {"query": query, "serpOnly": True, **kwargs})

    def start_harvest(self, query: str, **kwargs: Any) -> Any:
        return self._r.call("POST", "/harvest", {"query": query, **kwargs})

    def harvest_paa(self, query: str, **kwargs: Any) -> Any:
        return self._r.call("POST", "/harvest/sync", {"query": query, **kwargs})

    def extract_url(self, url: str, *, idempotency_key: str | None = None, **kwargs: Any) -> Any:
        headers = {} if idempotency_key is None else {"Idempotency-Key": idempotency_key}
        return self._r.call("POST", "/extract-url", {"url": url, **kwargs}, headers)

    def map_site_urls(self, url: str, **kwargs: Any) -> Any:
        return self._r.call("POST", "/map-urls", {"url": url, **kwargs})

    def extract_site(
        self,
        url: str,
        *,
        idempotency_key: str | None = None,
        **kwargs: Any,
    ) -> Any:
        headers = {} if idempotency_key is None else {"Idempotency-Key": idempotency_key}
        return self._r.call("POST", "/extract-site", {"url": url, **kwargs}, headers)

    def audit_site(self, url: str, *, idempotency_key: str | None = None, **kwargs: Any) -> Any:
        return self.extract_site(url, idempotency_key=idempotency_key, **kwargs)

    def get_extract_site_status(self, job_id: str) -> Any:
        return self._r.call("GET", f"/extract-site/status/{quote(job_id)}")

    def read_extract_site_export(self, job_id: str, **kwargs: Any) -> Any:
        return self._r.call("POST", "/extract-site/read", {"jobId": job_id, **kwargs})

    def read_extract_site_image(self, job_id: str, image_id: str) -> Any:
        return self._r.call("POST", "/extract-site/image", {"jobId": job_id, "imageId": image_id})

    def archive_read(self, url: str, **kwargs: Any) -> Any:
        return self._r.call("POST", "/archive/read", {"url": url, **kwargs})

    def list_jobs(self) -> Any:
        return self._r.call("GET", "/jobs")

    def get_job(self, job_id: str) -> Any:
        return self._r.call("GET", f"/jobs/{quote(job_id)}")

    def get_history(self) -> Any:
        return self._r.call("GET", "/history")

    def get_ledger(self) -> Any:
        return self._r.call("GET", "/ledger")
