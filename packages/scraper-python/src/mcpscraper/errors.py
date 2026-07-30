from __future__ import annotations

from typing import Any


def _read_string(body: Any, key: str) -> str | None:
    if isinstance(body, dict):
        value = body.get(key)
        if isinstance(value, str):
            return value
    return None


_PUBLIC_SERVICE_UNAVAILABLE_MESSAGE = "This operation is temporarily unavailable. Please retry later."


def _public_error_body(status: int, body: Any) -> Any:
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
