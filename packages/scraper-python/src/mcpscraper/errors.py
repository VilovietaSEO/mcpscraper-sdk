from __future__ import annotations

import math
import re
from typing import Any


def _read_string(body: Any, key: str) -> str | None:
    if isinstance(body, dict):
        value = body.get(key)
        if isinstance(value, str):
            return value
    return None


_PUBLIC_SERVICE_UNAVAILABLE_MESSAGE = "This operation is temporarily unavailable. Please retry later."
_PUBLIC_ERROR_CODES = {
    "request_aborted",
    "captcha_exhausted",
    "captcha_or_blocked",
    "location_mismatch",
    "proxy_tunnel_failed",
    "proxy_unavailable",
    "harvest_timeout",
    "mcp_request_timeout",
    "mcp_http_error",
    "extraction_failed",
    "concurrency_limit_exceeded",
    "unauthorized",
    "forbidden",
    "invalid_request",
    "idempotency_in_progress",
    "idempotency_conflict",
    "rate_limited",
    "upstream_rate_limited",
    "insufficient_balance",
    "service_unavailable",
    "response_lost",
    "vendor_unavailable",
    "page_not_found",
    "page_forbidden",
    "page_rate_limited",
    "page_server_error",
    "page_http_error",
    "bot_check_unresolved",
    "page_too_large",
    "page_unreachable",
    "browser_session_interrupted",
    "site_export_not_found",
    "directory_job_not_found",
    "site_export_format_unavailable",
    "site_export_read_failed",
    "site_export_image_not_found",
    "image_url_invalid", "image_url_not_https", "image_host_unresolvable", "image_host_blocked",
    "image_redirect_invalid", "image_source_unavailable", "image_too_large", "image_redirect_limit",
    "image_base64_invalid", "image_source_missing", "image_source_ambiguous", "image_source_type_invalid",
    "image_artifact_not_found", "image_page_too_large", "page_image_not_found", "page_image_candidates_unusable",
    "image_format_unsupported", "image_storage_unconfigured", "featured_image_unhostable",
}
_PUBLIC_ERROR_FIELDS = {
    "error",
    "error_code",
    "errorCode",
    "error_type",
    "message",
    "retryable",
    "retry_after_seconds",
    "charge_status",
    "details",
    "active",
    "limit",
    "operation",
    "upgrade",
    "upgrade_url",
    "upgrade_command",
    "balance_credits",
    "required_credits",
    "topup_url",

}
_PUBLIC_DETAIL_FIELDS = {
    "active",
    "limit",
    "operation",
    "upgrade_url",
    "topup_url",
    "upgrade_command",
    "slots_per_pack",
    "pack_price_usd",
    "balance_credits",
    "required_credits",
    "retry_guidance",
    "http_status",
}


def _recognized_public_details(value: Any) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        return None
    details = {}
    for key, child in value.items():
        if key not in _PUBLIC_DETAIL_FIELDS:
            continue
        if isinstance(child, str):
            details[key] = child[:500] if key == "retry_guidance" else child
        elif child is None or isinstance(child, bool) or (isinstance(child, (int, float)) and math.isfinite(child)):
            details[key] = child
    return details or None


def _public_recovery_fields(body: Any) -> dict[str, Any]:
    if not isinstance(body, dict):
        return {}
    safe: dict[str, Any] = {}
    for key, maximum in {"job_id": 200, "jobId": 200, "runId": 200, "status": 100, "runStatus": 100,
                         "billingState": 100, "idempotencyKey": 512}.items():
        value = body.get(key)
        if isinstance(value, str) and 0 < len(value) <= maximum:
            safe[key] = value
    for key in ("statusTool", "status_tool"):
        value = body.get(key)
        if isinstance(value, str) and re.fullmatch(r"[a-z][a-z0-9_]{0,99}", value):
            safe[key] = value
    for key in ("idempotencyFingerprint", "idempotency_fingerprint"):
        value = body.get(key)
        if isinstance(value, str) and re.fullmatch(r"[a-f0-9]{16}", value):
            safe[key] = value
    if body.get("executionState") == "unknown":
        safe["executionState"] = "unknown"
    if body.get("hold_state") in ("held", "unconfirmed"):
        safe["hold_state"] = body["hold_state"]
    if isinstance(body.get("replayed"), bool):
        safe["replayed"] = body["replayed"]
    for key in ("maximumAuthorizationMc", "balanceMc"):
        value = body.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value):
            safe[key] = value
    if isinstance(body.get("statusPath"), str) and safe.get("runId") and body["statusPath"] == f"/maps/place/runs/{safe['runId']}":
        safe["statusPath"] = body["statusPath"]
    status_url = body.get("statusUrl")
    if isinstance(status_url, str) and len(status_url) <= 512 and re.fullmatch(r"/(?:directory/jobs|extract-site/status)/[a-zA-Z0-9_-]{1,200}", status_url):
        safe["statusUrl"] = status_url
    operation = body.get("operation")
    if isinstance(operation, dict):
        run, key, state = operation.get("runId"), operation.get("idempotencyKey"), operation.get("state")
        if "runId" in operation and (run is None or isinstance(run, str) and 0 < len(run) <= 200) and isinstance(key, str) and 0 < len(key) <= 512 and isinstance(state, str) and 0 < len(state) <= 100:
            safe["operation"] = {"runId": run, "idempotencyKey": key, "state": state}
    recovery = body.get("recovery")
    if isinstance(recovery, dict):
        job, tool = recovery.get("jobId"), recovery.get("statusTool")
        if isinstance(job, str) and re.fullmatch(r"[a-zA-Z0-9-]{1,100}", job) and isinstance(tool, str) and re.fullmatch(r"[a-z][a-z0-9_]{0,99}", tool) and recovery.get("executionState") == "unknown" and recovery.get("holdState") in ("held", "unconfirmed"):
            safe["recovery"] = {"jobId": job, "statusTool": tool, "executionState": "unknown", "holdState": recovery["holdState"]}
    return safe


def _recognized_public_error_body(body: Any) -> dict[str, Any] | None:
    if not isinstance(body, dict):
        return None
    code = _read_string(body, "error_code") or _read_string(body, "errorCode")
    if code not in _PUBLIC_ERROR_CODES:
        return None
    safe = {key: value for key, value in body.items()
            if key in _PUBLIC_ERROR_FIELDS and (value is None or isinstance(value, (str, int, float, bool)))}
    safe.update(_public_recovery_fields(body))
    details = _recognized_public_details(body.get("details"))
    if details is not None:
        safe["details"] = details
    else:
        safe.pop("details", None)
    return safe


def _public_error_body(status: int, body: Any) -> Any:
    recognized = _recognized_public_error_body(body)
    if recognized is not None:
        return recognized
    if status < 500:
        return body
    return {
        "error": "service_unavailable",
        "error_code": "service_unavailable",
        "error_type": "service_unavailable",
        "retryable": True,
        "status": status,
        "message": _PUBLIC_SERVICE_UNAVAILABLE_MESSAGE,
        **_public_recovery_fields(body),
    }


class ScraperApiError(Exception):
    def __init__(self, status: int, body: Any, *, request_id: str | None = None) -> None:
        safe_body = _public_error_body(status, body)
        message = _read_string(safe_body, "message") or f"mcpscraper.dev API request failed with status {status}"
        super().__init__(message)
        self.status = status
        self.code = _read_string(safe_body, "error_code") or _read_string(safe_body, "errorCode") or _read_string(safe_body, "error")
        self.body = safe_body
        self.request_id = request_id

    def is_insufficient_balance(self) -> bool:
        return self.code == "insufficient_balance"

    def is_concurrency_limit_exceeded(self) -> bool:
        return self.code == "concurrency_limit_exceeded"

    def is_structured_error(self) -> bool:
        return _read_string(self.body, "error_type") is not None

    def is_verification_challenge(self) -> bool:
        return self.code in {"captcha_exhausted", "captcha_or_blocked"}

    def is_timeout(self) -> bool:
        return self.code in {"harvest_timeout", "mcp_request_timeout"}
