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


class SchemaRenderer:
    """Render JSON Schema alternatives without wrapping method results in RootModel."""

    def __init__(self, *, strict: bool = False) -> None:
        self.strict = strict
        self.definitions: list[str] = []
        self.names: set[str] = set()

    def unique_name(self, name: str) -> str:
        candidate = name
        index = 2
        while candidate in self.names:
            candidate = f"{name}{index}"
            index += 1
        self.names.add(candidate)
        return candidate

    def python_type(self, schema: dict, name: str) -> str:
        if not isinstance(schema, dict):
            return "Any"
        if "const" in schema:
            return f"Literal[{schema['const']!r}]"
        if schema.get("enum"):
            return "Literal[" + ", ".join(repr(value) for value in schema["enum"]) + "]"
        alternatives = schema.get("anyOf") or schema.get("oneOf")
        if alternatives:
            types = [self.python_type(branch, f"{name}Variant{index}")
                     for index, branch in enumerate(alternatives, 1)]
            return self.union(types)
        json_type = schema.get("type")
        if isinstance(json_type, list):
            return self.union([self.python_type({**schema, "type": item}, name)
                               for item in json_type])
        if json_type == "null":
            return "None"
        if json_type == "array":
            py_type = f"list[{self.python_type(schema.get('items', {}), name + 'Item')}]"
        elif json_type == "object" or "properties" in schema:
            properties = schema.get("properties") or {}
            if not properties:
                additional = schema.get("additionalProperties", {})
                value_type = self.python_type(additional, name + "Value")
                return f"dict[str, {value_type}]"
            return self.render_typed_dict(name, schema)
        else:
            py_type = {"string": "str", "integer": "int", "number": "Union[float, int]",
                       "boolean": "bool"}.get(json_type, "Any")
        constraints = []
        mapping = {"minimum": "ge", "maximum": "le", "exclusiveMinimum": "gt",
                   "exclusiveMaximum": "lt", "minLength": "min_length",
                   "maxLength": "max_length", "minItems": "min_length", "maxItems": "max_length"}
        for json_name, python_name in mapping.items():
            if json_name in schema:
                constraints.append(f"{python_name}={schema[json_name]!r}")
        # JSON Schema patterns use ECMAScript semantics; leave those checks to
        # the server rather than rejecting valid schemas in Pydantic's regex engine.
        if constraints:
            return f"Annotated[{py_type}, Field({', '.join(constraints)})]"
        return py_type

    @staticmethod
    def union(types: list[str]) -> str:
        unique = list(dict.fromkeys(types))
        return unique[0] if len(unique) == 1 else "Union[" + ", ".join(unique) + "]"

    def render_typed_dict(self, name: str, schema: dict) -> str:
        # Nested values have always been dictionaries. TypedDict validates their
        # branches and required keys while preserving that public return shape.
        name = self.unique_name(name)
        required = set(schema.get("required") or [])
        fields = []
        for prop_name, prop_schema in (schema.get("properties") or {}).items():
            py_type = self.python_type(prop_schema, name + to_pascal_case(prop_name))
            wrapper = "Required" if prop_name in required else "NotRequired"
            fields.append(f"    {prop_name!r}: {wrapper}[{py_type}],")
        self.definitions.append(
            f"{name} = TypedDict({name!r}, {{\n" + "\n".join(fields) + "\n})\n"
            + f'{name}.__pydantic_config__ = ConfigDict(extra="allow", strict={self.strict!r})\n'
        )
        return name

    def render_model(self, class_name: str, schema: dict) -> str:
        alternatives = schema.get("anyOf") or schema.get("oneOf")
        if alternatives:
            branches = []
            for index, branch in enumerate(alternatives, 1):
                branch_name = f"{class_name}Variant{index}"
                # JSON Schema keywords beside anyOf/oneOf also constrain every
                # branch; retain common properties and requirements when present.
                common = {key: value for key, value in schema.items()
                          if key not in ("anyOf", "oneOf")}
                merged = {**common, **branch}
                merged["properties"] = {**common.get("properties", {}), **branch.get("properties", {})}
                merged["required"] = list(dict.fromkeys(
                    (common.get("required") or []) + (branch.get("required") or [])))
                self.render_model(branch_name, merged)
                branches.append((len(merged["required"]), branch_name))
            # Older Pydantic 2 versions select the first valid model. Put
            # constrained branches before permissive ones so an artifact is
            # not mistaken for a domain result with no required properties.
            branches = [name for _, name in sorted(branches, key=lambda item: -item[0])]
            self.definitions.append(
                "# Union schema: validate external payloads with TypeAdapter(" + class_name + ").\n"
                + f"{class_name} = {self.union(branches)}\n"
            )
            return class_name
        lines = [f"class {class_name}(BaseModel):",
                 f'    model_config = ConfigDict(populate_by_name=True, extra="allow", strict={self.strict!r})', ""]
        required = set(schema.get("required") or [])
        for name, prop_schema in (schema.get("properties") or {}).items():
            py_type = self.python_type(prop_schema, class_name + to_pascal_case(name))
            is_required = name in required
            if not is_required:
                py_type = self.union([py_type, "None"])
            default = "..." if is_required else "None"
            lines.append(f"    {to_snake_case(name)}: {py_type} = Field({default}, "
                         f"alias={name!r}, description={prop_schema.get('description', '')!r})")
        self.definitions.append("\n".join(lines) + "\n")
        return class_name


def render_model(class_name: str, schema: dict, *, strict: bool = False) -> str:
    renderer = SchemaRenderer(strict=strict)
    renderer.render_model(class_name, schema)
    return "\n\n".join(renderer.definitions)


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
        content = "\n".join([
            "from typing import Annotated, Any, Literal, Union",
            "from typing_extensions import NotRequired, Required, TypedDict",
            "from pydantic import BaseModel, ConfigDict, Field, TypeAdapter",
            "",
            "",
            render_model(input_class, tool["inputSchema"]),
            "",
            render_model(output_class, tool["outputSchema"], strict=True),
            f"_{input_class}Adapter = TypeAdapter({input_class})",
            f"_{output_class}Adapter = TypeAdapter({output_class})",
        ])
        (models_dir / f"{module_name}.py").write_text(content)
        import_lines.append(
            f"from .mcp_models.{module_name} import {input_class}, {output_class}, _{input_class}Adapter, _{output_class}Adapter"
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
                    f'        payload = _{input_class}Adapter.validate_python(kwargs).model_dump(by_alias=True, exclude_unset=True)\n'
                    f'        result = self._call_tool("{tool["name"]}", payload)\n'
                    f'        return _{output_class}Adapter.validate_python(result)\n'
                )
            else:
                method_blocks.append(
                    f'    def {method_name}(self, **kwargs: Any) -> Any:\n'
                    f'        payload = _{input_class}Adapter.validate_python(kwargs).model_dump(by_alias=True, exclude_unset=True)\n'
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
    if manifest.get("toolCount") != len(tools):
        raise RuntimeError(f"Unified manifest toolCount does not match tools length; received {len(tools)}")
    for package_root, package_name in TARGETS:
        generate_target(package_root, package_name, tools)


if __name__ == "__main__":
    main()
