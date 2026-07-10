import json
import keyword
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = REPO_ROOT / "contracts" / "memory.tools.json"
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = PACKAGE_ROOT / "src" / "mcpscraper_memory" / "models"
CLIENT_GENERATED_PATH = PACKAGE_ROOT / "src" / "mcpscraper_memory" / "_generated_client.py"

CATEGORIES = [
    "access", "capture", "channels", "facts", "graph", "library", "memory", "recall",
    "schedule", "storage", "tables", "tags", "vaults", "video", "webhooks",
]


def to_snake_case(value: str) -> str:
    value = re.sub(r"[-\s]+", "_", value)
    value = re.sub(r"(?<!^)(?=[A-Z])", "_", value)
    snake = value.lower().strip("_")
    return f"{snake}_" if keyword.iskeyword(snake) else snake


def derive_method_name(legacy_id: str, category: str) -> str:
    for candidate in (category, category.rstrip("s")):
        prefix = f"{candidate}-"
        if legacy_id.startswith(prefix) and len(legacy_id) > len(prefix):
            return to_snake_case(legacy_id[len(prefix):])
    return to_snake_case(legacy_id)


def to_pascal_case(value: str) -> str:
    parts = re.split(r"[-_\s]+", value)
    return "".join(p[0].upper() + p[1:] for p in parts if p)


def json_type_to_python(schema: dict, class_name_hint: str) -> str:
    if "enum" in schema:
        literal_values = ", ".join(json.dumps(v) for v in schema["enum"])
        return f"Literal[{literal_values}]"
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
        item_schema = schema.get("items", {})
        item_type = json_type_to_python(item_schema, class_name_hint)
        return f"list[{item_type}]"
    if json_type == "object" or "properties" in schema:
        return "dict[str, Any]"
    return "Any"


def field_definition(name: str, schema: dict, required: bool, class_name_hint: str) -> str:
    py_type = json_type_to_python(schema, class_name_hint)
    if not required:
        py_type = f"{py_type} | None"
    description = schema.get("description", "").replace('"', '\\"')
    default = "None" if not required else "..."
    return f'    {to_snake_case(name)}: {py_type} = Field({default}, alias="{name}", description="{description}")'


def render_model(class_name: str, schema: dict) -> str:
    properties = schema.get("properties", {}) or {}
    required = set(schema.get("required", []) or [])
    if not properties:
        return f"class {class_name}(BaseModel):\n    model_config = ConfigDict(populate_by_name=True, extra=\"allow\")\n"
    lines = [f"class {class_name}(BaseModel):", '    model_config = ConfigDict(populate_by_name=True, extra="allow")', ""]
    for prop_name, prop_schema in properties.items():
        lines.append(field_definition(prop_name, prop_schema, prop_name in required, class_name))
    return "\n".join(lines) + "\n"


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text())
    tools = manifest["tools"]

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    (MODELS_DIR / "__init__.py").write_text("")

    by_category: dict[str, list[dict]] = {}
    for tool in tools:
        by_category.setdefault(tool["category"], []).append(tool)

    for tool in tools:
        legacy = tool["legacyId"]
        module_name = to_snake_case(legacy)
        input_class = to_pascal_case(legacy) + "Input"
        output_class = to_pascal_case(legacy) + "Output"

        content = [
            "from typing import Any, Literal",
            "from pydantic import BaseModel, ConfigDict, Field",
            "",
            "",
            render_model(input_class, tool["inputSchema"]),
            "",
            render_model(output_class, tool["outputSchema"]),
        ]
        (MODELS_DIR / f"{module_name}.py").write_text("\n".join(content))

    namespace_blocks = []
    import_lines = []
    for category in CATEGORIES:
        class_name = to_pascal_case(category) + "Namespace"
        method_blocks = []
        used_names: set[str] = set()
        for tool in by_category.get(category, []):
            legacy = tool["legacyId"]
            wire_name = tool["name"]
            module_name = to_snake_case(legacy)
            input_class = to_pascal_case(legacy) + "Input"
            output_class = to_pascal_case(legacy) + "Output"
            method_name = derive_method_name(legacy, category)
            if method_name in used_names:
                method_name = to_snake_case(legacy)
            used_names.add(method_name)

            import_lines.append(
                f"from .models.{module_name} import {input_class}, {output_class}"
            )
            method_blocks.append(
                f'    def {method_name}(self, **kwargs: Any) -> {output_class}:\n'
                f'        payload = {input_class}(**kwargs).model_dump(by_alias=True, exclude_none=True)\n'
                f'        result = self._call_tool("{wire_name}", payload)\n'
                f'        return {output_class}.model_validate(result)\n'
            )
        namespace_blocks.append(
            f"class {class_name}:\n"
            f"    def __init__(self, call_tool):\n"
            f"        self._call_tool = call_tool\n\n"
            + "\n".join(method_blocks)
        )

    generated = (
        "from typing import Any, Callable\n\n"
        + "\n".join(sorted(set(import_lines)))
        + "\n\n\n"
        + "\n\n".join(namespace_blocks)
        + "\n"
    )
    CLIENT_GENERATED_PATH.write_text(generated)

    print(f"Generated {len(tools)} tool model pairs across {len(by_category)} categories.")


if __name__ == "__main__":
    main()
