import ast
import importlib.util
import json
import keyword
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = REPO_ROOT / "contracts" / "memory.tools.json"
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = PACKAGE_ROOT / "src" / "mcpscraper_memory" / "direct_models"
CLIENT_GENERATED_PATH = PACKAGE_ROOT / "src" / "mcpscraper_memory" / "_direct_generated_client.py"
NAME_MAP_PATH = PACKAGE_ROOT / "src" / "mcpscraper_memory" / "_direct_tool_name_map.py"
LEGACY_CLIENT_PATH = PACKAGE_ROOT / "src" / "mcpscraper_memory" / "_generated_client.py"
DELIVERY_PATH = PACKAGE_ROOT / "src" / "mcpscraper_memory" / "_artifact_delivery.py"
UNIFIED_MANIFEST_PATH = REPO_ROOT / "contracts" / "mcp.tools.json"

CATEGORIES = [
    "access", "artifacts", "capture", "channels", "crm", "facts", "files", "graph", "images", "library", "memory", "recall",
    "research", "storage", "tables", "tags", "vaults", "video", "webhooks",
]


def to_snake_case(value: str) -> str:
    value = re.sub(r"[-\s]+", "_", value)
    value = re.sub(r"(?<!^)(?=[A-Z])", "_", value)
    snake = value.lower().strip("_")
    return f"{snake}_" if keyword.iskeyword(snake) else snake


def derive_method_name(legacy_id: str, category: str) -> str:
    for candidate in (category, category.rstrip("s")):
        for separator in ("-", "_"):
            prefix = f"{candidate}{separator}"
            if legacy_id.startswith(prefix) and len(legacy_id) > len(prefix):
                return to_snake_case(legacy_id[len(prefix):])
    return to_snake_case(legacy_id)


def to_pascal_case(value: str) -> str:
    parts = re.split(r"[-_\s]+", value)
    return "".join(p[0].upper() + p[1:] for p in parts if p)


def json_type_to_python(schema: dict, class_name_hint: str) -> str:
    if "enum" in schema:
        literal_values = ", ".join(repr(v) for v in schema["enum"])
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
    extra = "forbid" if schema.get("additionalProperties") is False else "allow"
    if not properties:
        return f'class {class_name}(BaseModel):\n    model_config = ConfigDict(populate_by_name=True, extra="{extra}")\n'
    lines = [f"class {class_name}(BaseModel):", f'    model_config = ConfigDict(populate_by_name=True, extra="{extra}")', ""]
    for prop_name, prop_schema in properties.items():
        lines.append(field_definition(prop_name, prop_schema, prop_name in required, class_name))
    return "\n".join(lines) + "\n"


def inline_output_schema(schema: dict) -> dict:
    """Keep convenience model names for inline results; delivery validates separately."""
    alternatives = schema.get("anyOf", [])
    if not any(candidate.get("properties", {}).get("delivery", {}).get("properties", {})
               .get("mode", {}).get("const") == "artifact" for candidate in alternatives):
        return schema
    inline = []
    transport_alternatives = 0
    for candidate in alternatives:
        properties = candidate.get("properties", {})
        delivery_mode = properties.get("delivery", {}).get("properties", {}).get("mode", {})
        public_error = {"error_code", "error_type", "message", "retryable"}.issubset(
            set(candidate.get("required", []))
        )
        if delivery_mode.get("const") == "artifact" or public_error:
            transport_alternatives += 1
        else:
            inline.append(candidate)
    if transport_alternatives and len(inline) == 1:
        return inline[0]
    return schema


def shared_schema_renderer():
    spec = importlib.util.spec_from_file_location("mcp_python_generator", REPO_ROOT / "scripts" / "generate-mcp-python.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def render_inline_output(class_name: str, schema: dict) -> str:
    schema = inline_output_schema(schema)
    if schema.get("anyOf") or schema.get("oneOf"):
        return shared_schema_renderer().render_model(class_name, schema)
    return render_model(class_name, schema)


def render_artifact_delivery(unified_manifest: dict) -> str:
    """Reuse the server's common delivery alternative; never maintain a second schema."""
    tool = next((tool for tool in unified_manifest["tools"] if tool["name"] == "artifact_describe"), None)
    if tool is None:
        raise RuntimeError("Unified contract is missing artifact_describe")
    alternatives = tool["outputSchema"].get("anyOf", [])
    schemas = [schema for schema in alternatives
               if schema.get("properties", {}).get("delivery", {}).get("properties", {})
               .get("mode", {}).get("const") == "artifact"]
    if len(schemas) != 1:
        raise RuntimeError("artifact_describe must declare exactly one common artifact delivery alternative")
    model = shared_schema_renderer().render_model("ArtifactDelivery", schemas[0], strict=True)
    return (
        '"""Generated from artifact_describe in contracts/mcp.tools.json."""\n\n'
        "from typing import Annotated, Any, Literal, TypeVar, Union\n"
        "from typing_extensions import NotRequired, Required, TypedDict\n"
        "from pydantic import BaseModel, ConfigDict, Field, TypeAdapter\n\n"
        + model + "\n"
        + "_ArtifactDeliveryAdapter = TypeAdapter(ArtifactDelivery)\n"
        + '_OutputModel = TypeVar("_OutputModel", bound=BaseModel)\n\n'
        + "def validate_tool_output(value: Any, output_model: type[_OutputModel]) -> _OutputModel | ArtifactDelivery:\n"
        + '    if isinstance(value, dict) and "delivery" in value:\n'
        + "        return _ArtifactDeliveryAdapter.validate_python(value)\n"
        + "    return output_model.model_validate(value)\n"
    )


def refresh_legacy_client(source: str) -> str:
    """Keep legacy model imports and method bindings while updating their result seam."""
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    methods = [method for cls in tree.body if isinstance(cls, ast.ClassDef)
               for method in cls.body if isinstance(method, ast.FunctionDef) and method.name != "__init__"]
    if not methods:
        raise RuntimeError("Legacy generated client contains no convenience methods")
    for method in methods:
        annotation = method.returns
        if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
            if not isinstance(annotation.right, ast.Name) or annotation.right.id != "ArtifactDelivery":
                raise RuntimeError(f"Unexpected legacy output annotation: {method.name}")
            annotation = annotation.left
        if not isinstance(annotation, ast.Name) or not annotation.id.endswith("Output"):
            raise RuntimeError(f"Unexpected legacy output model: {method.name}")
        output = annotation.id
        returns = [node for node in method.body if isinstance(node, ast.Return)]
        if len(returns) != 1:
            raise RuntimeError(f"Expected exactly one legacy result validation: {method.name}")
        result = returns[0]
        expression = ast.unparse(result.value)
        if expression not in (f"{output}.model_validate(result)", f"validate_tool_output(result, {output})"):
            raise RuntimeError(f"Unexpected legacy result validation: {method.name}")
        header = lines[method.lineno - 1]
        suffix = f" -> {output} | ArtifactDelivery:"
        updated, count = re.subn(r" -> " + re.escape(output) + r"(?: \| ArtifactDelivery)?:", suffix, header)
        if count != 1:
            raise RuntimeError(f"Unexpected legacy method declaration: {method.name}")
        lines[method.lineno - 1] = updated
        indent = lines[result.lineno - 1][:result.col_offset]
        lines[result.lineno - 1] = f"{indent}return validate_tool_output(result, {output})\n"
        for node in method.body:
            if isinstance(node, ast.Assign):
                line = lines[node.lineno - 1]
                if ".model_dump(" in line:
                    lines[node.lineno - 1] = line.replace("exclude_none=True", "exclude_unset=True")
    source = "".join(lines)
    import_line = "from ._artifact_delivery import ArtifactDelivery, validate_tool_output\n"
    if import_line not in source:
        source = import_line + source
    return source


def retire_legacy_methods(source: str, tools: list[dict]) -> str:
    """Keep retained convenience names while deriving allowed calls from the registry."""
    available = {tool["name"]: tool for tool in tools}
    tree = ast.parse(source)
    retained_classes = []
    model_bindings: dict[str, dict] = {}
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        kept_methods = []
        for method in node.body:
            if not isinstance(method, ast.FunctionDef) or method.name == "__init__":
                kept_methods.append(method)
                continue
            calls = [call for call in ast.walk(method) if isinstance(call, ast.Call)
                     and isinstance(call.func, ast.Attribute) and call.func.attr == "_call_tool"]
            if len(calls) != 1 or not calls[0].args or not isinstance(calls[0].args[0], ast.Constant):
                raise RuntimeError(f"Unexpected legacy wire binding: {node.name}.{method.name}")
            wire_name = calls[0].args[0].value
            if wire_name not in available:
                continue
            kept_methods.append(method)
            for child in ast.walk(method):
                if isinstance(child, ast.Name) and child.id.endswith(("Input", "Output")):
                    model_bindings[child.id] = available[wire_name]
        if not any(isinstance(method, ast.FunctionDef) and method.name != "__init__" for method in kept_methods):
            continue
        node.body = kept_methods
        if node.name == "ScheduleNamespace":
            # The only retained methods from the former scheduling namespace are
            # generic artifact templates, now exposed without a recurrence API.
            node.name = "ArtifactsNamespace"
        retained_classes.append(node)

    imports = []
    model_dir = PACKAGE_ROOT / "src" / "mcpscraper_memory" / "models"
    for node in tree.body:
        if not isinstance(node, ast.ImportFrom) or not (node.module or "").startswith("models."):
            continue
        names = [alias for alias in node.names if alias.name in model_bindings]
        if not names:
            continue
        if len(names) != 2:
            raise RuntimeError(f"Incomplete legacy model import: {node.module}")
        input_name = next(alias.name for alias in names if alias.name.endswith("Input"))
        output_name = next(alias.name for alias in names if alias.name.endswith("Output"))
        tool = model_bindings[input_name]
        if tool != model_bindings[output_name]:
            raise RuntimeError(f"Conflicting legacy model binding: {node.module}")
        imports.append(ast.unparse(node))
        union_output = inline_output_schema(tool["outputSchema"]).get("anyOf") or inline_output_schema(tool["outputSchema"]).get("oneOf")
        model_imports = ["from typing import Annotated, Any, Literal, Union" if union_output else "from typing import Any, Literal"]
        if union_output:
            model_imports.append("from typing_extensions import NotRequired, Required, TypedDict")
        model_imports.append("from pydantic import BaseModel, ConfigDict, Field")
        module_name = node.module.removeprefix("models.")
        (model_dir / f"{module_name}.py").write_text("\n".join([
            *model_imports, "", "", render_model(input_name, tool["inputSchema"]), "",
            render_inline_output(output_name, tool["outputSchema"]),
        ]))
    for model_path in model_dir.glob("*.py"):
        if "schedule" in model_path.stem or model_path.stem in {"answer_inbox_item", "auto_optimization"}:
            model_path.unlink()
    return "from ._artifact_delivery import ArtifactDelivery, validate_tool_output\nfrom typing import Any, Callable\n\n" + "\n".join(imports) + "\n\n\n" + "\n\n".join(ast.unparse(node) for node in retained_classes) + "\n"


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text())
    tools = manifest["tools"]
    delivery = render_artifact_delivery(json.loads(UNIFIED_MANIFEST_PATH.read_text()))
    legacy_client = refresh_legacy_client(retire_legacy_methods(LEGACY_CLIENT_PATH.read_text(), tools))

    shutil.rmtree(MODELS_DIR, ignore_errors=True)
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
        output_schema = inline_output_schema(tool["outputSchema"])
        union_output = output_schema.get("anyOf") or output_schema.get("oneOf")
        imports = ["from typing import Annotated, Any, Literal, Union" if union_output else "from typing import Any, Literal"]
        if union_output:
            imports.append("from typing_extensions import NotRequired, Required, TypedDict")
        imports.append("from pydantic import BaseModel, ConfigDict, Field")

        content = [
            *imports,
            "",
            "",
            render_model(input_class, tool["inputSchema"]),
            "",
            render_inline_output(output_class, tool["outputSchema"]),
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
                f"from .direct_models.{module_name} import {input_class}, {output_class}"
            )
            method_blocks.append(
                f'    def {method_name}(self, **kwargs: Any) -> {output_class} | ArtifactDelivery:\n'
                f'        payload = {input_class}(**kwargs).model_dump(by_alias=True, exclude_unset=True)\n'
                f'        result = self._call_tool("{wire_name}", payload)\n'
                f'        return validate_tool_output(result, {output_class})\n'
            )
        namespace_blocks.append(
            f"class {class_name}:\n"
            f"    def __init__(self, call_tool):\n"
            f"        self._call_tool = call_tool\n\n"
            + "\n".join(method_blocks)
        )

    generated = (
        "from typing import Any, Callable\n"
        + "from ._artifact_delivery import ArtifactDelivery, validate_tool_output\n\n"
        + "\n".join(sorted(set(import_lines)))
        + "\n\n\n"
        + "\n\n".join(namespace_blocks)
        + "\n"
    )
    DELIVERY_PATH.write_text(delivery)
    LEGACY_CLIENT_PATH.write_text(legacy_client)
    CLIENT_GENERATED_PATH.write_text(generated.rstrip() + "\n")
    name_map = {tool["name"]: tool["legacyId"] for tool in tools}
    NAME_MAP_PATH.write_text(
        "DIRECT_TO_UNIFIED_TOOL_NAMES: dict[str, str] = "
        + repr(dict(sorted(name_map.items())))
        + "\n"
    )

    print(f"Generated {len(tools)} tool model pairs across {len(by_category)} categories.")


if __name__ == "__main__":
    main()
