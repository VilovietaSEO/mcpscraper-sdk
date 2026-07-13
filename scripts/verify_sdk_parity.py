import json
import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = 158


def load_bindings(package_src: Path, module_name: str) -> list[dict]:
    sys.path.insert(0, str(package_src))
    try:
        module = __import__(f"{module_name}._mcp_generated_client", fromlist=["MCP_TOOL_BINDINGS"])
        return list(module.MCP_TOOL_BINDINGS)
    finally:
        sys.path.pop(0)
        for loaded in list(sys.modules):
            if loaded == module_name or loaded.startswith(f"{module_name}."):
                del sys.modules[loaded]


def to_snake_case(value: str) -> str:
    value = re.sub(r"[-\s]+", "_", value)
    return re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower().strip("_")


def assert_exact(label: str, actual: list[dict], expected: list[dict]) -> None:
    actual_names = {binding["name"] for binding in actual}
    expected_names = {binding["name"] for binding in expected}
    missing = sorted(expected_names - actual_names)
    extra = sorted(actual_names - expected_names)
    expected_by_name = {
        tool["name"]: (tool["category"], to_snake_case(tool["methodName"]))
        for tool in expected
    }
    drift = sorted(
        binding["name"]
        for binding in actual
        if expected_by_name.get(binding["name"]) != (binding["category"], binding["method_name"])
    )
    if len(actual) != EXPECTED or missing or extra or drift:
        raise RuntimeError(
            f"{label} parity failed: count={len(actual)}, missing={missing}, extra={extra}, binding_drift={drift}"
        )
    print(f"{label}: {len(actual)}/{EXPECTED}")


def main() -> None:
    manifest = json.loads((ROOT / "contracts" / "mcp.tools.json").read_text())
    expected = manifest["tools"]
    assert_exact(
        "Python scraper package",
        load_bindings(ROOT / "packages" / "scraper-python" / "src", "mcpscraper"),
        expected,
    )
    assert_exact(
        "Python memory package",
        load_bindings(ROOT / "packages" / "memory-python" / "src", "mcpscraper_memory"),
        expected,
    )


if __name__ == "__main__":
    main()
