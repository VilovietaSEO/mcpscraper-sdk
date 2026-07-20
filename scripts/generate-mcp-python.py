import json
import keyword
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO_ROOT / "contracts" / "mcp.tools.json"
TARGETS = [
    (REPO_ROOT / "packages" / "scraper-python" / "src" / "mcpscraper", "mcpscraper"),
    (REPO_ROOT / "packages" / "memory-python" / "src" / "mcpscraper_memory", "mcpscraper_memory"),
]


def to_snake_case(value: str) -> str:
    value = re.sub(r"[-\s]+", "_", value)
    value = re.sub(r"(?<!^)(?=[A-Z])", "_", value)
    snake = value.lower().strip("_")
    return f"{snake}_" if keyword.iskeyword(snake) else snake


def to_pascal_case(value: str) -> str:
    return "".join(part[0].upper() + part[1:] for part in re.split(r"[-_\s]+", value) if part)


def json_type_to_python(schema: dict) -> str:
    if "enum" in schema:
        return "Literal[" + ", ".join(json.dumps(value) for value in schema["enum"]) + "]"
    json_type = schema.get("type")
    if json_type == "string":
        return "str"
    if json_type == "integer":
        return "int"
    if json_type == "number":
        return "float"
    if json_type == "boolean":
        return "bool"
    if json_type == "array":
        return f"list[{json_type_to_python(schema.get('items', {}))}]"
    if json_type == "object" or "properties" in schema:
        return "dict[str, Any]"
    return "Any"


def field_definition(name: str, schema: dict, required: bool) -> str:
    py_type = json_type_to_python(schema)
    if not required:
        py_type = f"{py_type} | None"
    description = schema.get("description", "").replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    default = "..." if required else "None"
    return f'    {to_snake_case(name)}: {py_type} = Field({default}, alias="{name}", description="{description}")'


def render_model(class_name: str, schema: dict) -> str:
    properties = schema.get("properties", {}) or {}
    required = set(schema.get("required", []) or [])
    if not properties:
        return f'class {class_name}(BaseModel):\n    model_config = ConfigDict(populate_by_name=True, extra="allow")\n'
    lines = [
        f"class {class_name}(BaseModel):",
        '    model_config = ConfigDict(populate_by_name=True, extra="allow")',
        "",
    ]
    for prop_name, prop_schema in properties.items():
        lines.append(field_definition(prop_name, prop_schema, prop_name in required))
    return "\n".join(lines) + "\n"


def generate_target(package_root: Path, package_name: str, tools: list[dict]) -> None:
    models_dir = package_root / "mcp_models"
    generated_client_path = package_root / "_mcp_generated_client.py"
    shutil.rmtree(models_dir, ignore_errors=True)
    models_dir.mkdir(parents=True, exist_ok=True)
    (models_dir / "__init__.py").write_text("")

    by_category: dict[str, list[dict]] = {}
    import_lines: list[str] = []
    for tool in tools:
        by_category.setdefault(tool["category"], []).append(tool)
        module_name = to_snake_case(tool["name"])
        model_prefix = to_pascal_case(tool["name"])
        input_class = model_prefix + "Input"
        output_class = model_prefix + "Output"
        content = [
            "from typing import Any, Literal",
            "from pydantic import BaseModel, ConfigDict, Field",
            "",
            "",
            render_model(input_class, tool["inputSchema"]),
            "",
            render_model(output_class, tool["outputSchema"]),
        ]
        (models_dir / f"{module_name}.py").write_text("\n".join(content))
        import_lines.append(
            f"from .mcp_models.{module_name} import {input_class}, {output_class}"
        )

    namespace_blocks: list[str] = []
    property_lines: list[str] = []
    initializer_lines: list[str] = []
    for category, category_tools in by_category.items():
        class_name = to_pascal_case(category) + "Namespace"
        property_name = to_snake_case(category)
        property_lines.append(f"        self.{property_name} = {class_name}(call_tool)")
        method_blocks: list[str] = []
        for tool in category_tools:
            model_prefix = to_pascal_case(tool["name"])
            input_class = model_prefix + "Input"
            output_class = model_prefix + "Output"
            method_name = to_snake_case(tool["methodName"])
            if tool.get("outputSchemaProvided"):
                method_blocks.append(
                    f'    def {method_name}(self, **kwargs: Any) -> {output_class}:\n'
                    f'        payload = {input_class}(**kwargs).model_dump(by_alias=True, exclude_none=True)\n'
                    f'        result = self._call_tool("{tool["name"]}", payload)\n'
                    f'        return {output_class}.model_validate(result)\n'
                )
            else:
                method_blocks.append(
                    f'    def {method_name}(self, **kwargs: Any) -> Any:\n'
                    f'        payload = {input_class}(**kwargs).model_dump(by_alias=True, exclude_none=True)\n'
                    f'        return self._call_tool("{tool["name"]}", payload)\n'
                )
        namespace_blocks.append(
            f"class {class_name}:\n"
            f"    def __init__(self, call_tool):\n"
            f"        self._call_tool = call_tool\n\n"
            + "\n".join(method_blocks)
        )

    bindings = [
        {"name": tool["name"], "category": tool["category"], "method_name": to_snake_case(tool["methodName"])}
        for tool in tools
    ]
    generated = (
        "from typing import Any\n\n"
        + "\n".join(sorted(set(import_lines)))
        + "\n\n\n"
        + f"MCP_TOOL_BINDINGS = {repr(bindings)}\n"
        + "MCP_TOOL_COUNT = len(MCP_TOOL_BINDINGS)\n\n\n"
        + "\n\n".join(namespace_blocks)
        + "\n\n\nclass GeneratedMcpToolsClient:\n"
        + "    def __init__(self, call_tool):\n"
        + "\n".join(property_lines)
        + "\n"
    )
    generated_client_path.write_text(generated)
    print(f"Generated {len(tools)} unified MCP methods for {package_name}.")


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text())
    tools = manifest["tools"]
    if manifest.get("toolCount") != 165 or len(tools) != 165:
        raise RuntimeError(f"Unified manifest must contain exactly 165 tools; received {len(tools)}")
    for package_root, package_name in TARGETS:
        generate_target(package_root, package_name, tools)


if __name__ == "__main__":
    main()
