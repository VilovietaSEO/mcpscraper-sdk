from __future__ import annotations

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
    "site_export_format_unavailable",
    "site_export_read_failed",
    "site_export_image_not_found",
}
_PUBLIC_ERROR_FIELDS = {
    "error",
    "error_code",
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
}


def _recognized_public_details(value: Any) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        return None
    details = {
        key: child
        for key, child in value.items()
        if key in _PUBLIC_DETAIL_FIELDS and (child is None or isinstance(child, (str, int, float, bool)))
    }
    return details or None


def _recognized_public_error_body(body: Any) -> dict[str, Any] | None:
    if not isinstance(body, dict):
        return None
    code = _read_string(body, "error_code")
    if code not in _PUBLIC_ERROR_CODES:
        return None
    safe = {key: value for key, value in body.items() if key in _PUBLIC_ERROR_FIELDS}
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
    }


class ScraperApiError(Exception):
    def __init__(self, status: int, body: Any) -> None:
        safe_body = _public_error_body(status, body)
        message = _read_string(safe_body, "message") or f"mcpscraper.dev API request failed with status {status}"
        super().__init__(message)
        self.status = status
        self.code = _read_string(safe_body, "error_code") or _read_string(safe_body, "error")
        self.body = safe_body

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
