"""The existing MemoryClient convenience methods accept the common delivery result."""

import importlib.util
import json
from pathlib import Path

import pytest
import responses
from pydantic import ValidationError

from mcpscraper_memory import MemoryClient
from mcpscraper_memory._artifact_delivery import ArtifactDelivery
from mcpscraper_memory.models.memory_get import MemoryGetOutput
from mcpscraper_memory.direct_models.research_person_capture import ResearchPersonCaptureOutput


BASE_URL = "https://mcpscraper.dev/mcp"
ROOT = Path(__file__).resolve().parents[3]


def delivery_payload():
    return {
        "delivery": {
            "mode": "artifact", "status": "complete", "retainedRepresentation": "formatted-tool-result",
            "sourceIsError": False, "artifacts": [{
                "artifactId": "artifact_1", "filename": "full-note.md", "contentType": "text/markdown",
                "bytes": 120000, "sha256": "a" * 64, "expiresAt": "2026-10-19T00:00:00Z",
                "capabilities": ["read", "download"], "downloadUrl": "https://example.com/full-note.md",
                "downloadUrlExpiresAt": "2026-10-13T00:00:00Z", "downloadState": "available",
                "resourceUri": "mcp-scraper://artifact/artifact_1",
            }], "downloadLinksOmitted": False, "scopeOmittedFields": 0,
            "storageFailure": None, "nextAction": "Use artifact_read to retrieve the complete note.",
        }, "preview": "Note preview", "scope": {"bytes": 120000, "complete": True, "url": None},
        "recovery": {"runId": "run_1", "idempotencyKey": "note:1"},
    }


def invoke(client, tool):
    if tool == "memory-get":
        return client.memory.get(path="projects/long-note")
    return client.research.person_capture(
        base_revision=0, idempotency_key="research:1", display_name="Historical Person",
        source_evidence=[{"sourceRef": "https://example.test/source"}],
        lineage={"sensitivity": "public", "observedAt": "2026-10-12T00:00:00.000Z"},
    )


def respond(payload):
    responses.add(responses.POST, BASE_URL, status=200, json={
        "jsonrpc": "2.0", "id": 1, "result": {"structuredContent": payload},
    })


@pytest.mark.parametrize("tool", ["memory-get", "research-person-capture"])
@responses.activate
def test_legacy_convenience_methods_return_complete_validated_delivery(tool):
    payload = delivery_payload()
    respond(payload)
    result = invoke(MemoryClient(api_key="sk_test"), tool)
    assert isinstance(result, ArtifactDelivery)
    assert result.model_dump(by_alias=True) == payload
    assert result.delivery["artifacts"][0]["resourceUri"] == "mcp-scraper://artifact/artifact_1"
    assert type(result.delivery["artifacts"][0]["bytes"]) is int
    sent = json.loads(responses.calls[0].request.body)
    assert sent["params"]["name"] == tool


@pytest.mark.parametrize("tool, payload, model", [
    ("memory-get", {"ok": True, "note": {"content": "The complete original note", "tags": ["a"]}}, MemoryGetOutput),
    ("research-person-capture", {"ok": True, "message": "Captured", "record": {"content": "Complete knowledge"}}, ResearchPersonCaptureOutput),
])
@responses.activate
def test_legacy_inline_model_names_and_nested_values_stay_compatible(tool, payload, model):
    respond(payload)
    result = invoke(MemoryClient(api_key="sk_test"), tool)
    assert isinstance(result, model)
    assert result.ok is True
    for key, value in payload.items():
        assert getattr(result, key) == value


@pytest.mark.parametrize("tool", ["memory-get", "research-person-capture"])
@pytest.mark.parametrize("corruption", ["invalid_mode", "missing_download_metadata"])
@responses.activate
def test_invalid_delivery_never_falls_through_to_legacy_domain_validation(tool, corruption):
    payload = delivery_payload()
    payload.update(ok=True, message="This must not make an invalid delivery acceptable")
    if corruption == "invalid_mode":
        payload["delivery"]["mode"] = "inline"
    else:
        del payload["delivery"]["artifacts"][0]["downloadUrl"]
    respond(payload)
    with pytest.raises(ValidationError):
        invoke(MemoryClient(api_key="sk_test"), tool)


def test_legacy_generator_refresh_is_idempotent_and_refuses_an_unrecognized_validation_seam():
    path = ROOT / "packages/memory-python/scripts/generate_models.py"
    spec = importlib.util.spec_from_file_location("memory_models_generator", path)
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    source = (ROOT / "packages/memory-python/src/mcpscraper_memory/_generated_client.py").read_text()
    transformed = generator.refresh_legacy_client(source)
    assert generator.refresh_legacy_client(transformed) == transformed
    assert "return validate_tool_output(" in transformed
    assert ".model_validate(result)" not in transformed
    invalid = transformed.replace("return validate_tool_output(result, MemoryGetOutput)", "return result", 1)
    with pytest.raises(RuntimeError, match="Unexpected legacy result validation"):
        generator.refresh_legacy_client(invalid)


def test_direct_generator_preserves_inline_fields_beside_delivery_and_error_alternatives():
    path = ROOT / "packages/memory-python/scripts/generate_models.py"
    spec = importlib.util.spec_from_file_location("memory_models_generator", path)
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    manifest = json.loads((ROOT / "contracts/memory.tools.json").read_text())
    tool = next(tool for tool in manifest["tools"] if tool["name"] == "researchPersonCaptureTool")
    inline = generator.inline_output_schema(tool["outputSchema"])
    assert {"ok", "message"}.issubset(inline["properties"])
    assert {"ok", "message"}.issubset(inline["required"])
    assert ResearchPersonCaptureOutput.model_fields["ok"].is_required()
    assert ResearchPersonCaptureOutput.model_fields["message"].is_required()
    with pytest.raises(ValidationError):
        ResearchPersonCaptureOutput.model_validate({"record": {"content": "Incomplete result"}})
