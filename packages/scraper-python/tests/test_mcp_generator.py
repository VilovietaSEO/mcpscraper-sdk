"""Exercise the real generator and the Pydantic types it emits, without network calls."""

import copy
import importlib
import importlib.util
import sys
from pathlib import Path

import pytest
from pydantic import BaseModel, TypeAdapter, ValidationError


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("mcp_python_generator", ROOT / "scripts/generate-mcp-python.py")
generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generator)


def object_schema(properties, required=None):
    return {"type": "object", "properties": properties,
            "required": list(properties) if required is None else required,
            "additionalProperties": False}


NULLABLE_STRING = {"anyOf": [{"type": "string"}, {"type": "null"}]}
ARTIFACT = object_schema({
    "artifactId": {"type": "string"}, "filename": {"type": "string"},
    "contentType": {"type": "string"}, "bytes": {"type": "number"},
    "sha256": {"type": "string"}, "expiresAt": {"type": "string"},
    "capabilities": {"type": "array", "items": {"type": "string"}},
    "downloadUrl": NULLABLE_STRING, "downloadUrlExpiresAt": NULLABLE_STRING,
    "downloadState": {"enum": ["available", "local", "unavailable"]},
})
DELIVERY = object_schema({
    "delivery": object_schema({
        "mode": {"const": "artifact"},
        "status": {"enum": ["complete", "partial", "unavailable"]},
        "retainedRepresentation": {"const": "formatted-tool-result"},
        "sourceIsError": {"type": "boolean"},
        "artifacts": {"type": "array", "items": ARTIFACT},
        "downloadLinksOmitted": {"type": "boolean"},
        "scopeOmittedFields": {"type": "integer", "minimum": 0},
        "storageFailure": {"anyOf": [object_schema({
            "artifactId": NULLABLE_STRING,
            "outcome": {"enum": ["unknown", "bytes-stored-metadata-pending", "failed"]},
        }), {"type": "null"}]},
        "nextAction": {"type": "string"},
    }),
    "preview": {"type": "string"},
    "scope": {"type": "object", "additionalProperties": {"anyOf": [
        {"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "null"},
    ]}},
    "recovery": object_schema({"runId": {"type": "string"},
                               "idempotencyKey": {"type": "string"}}, required=[]),
})
TRANSCRIPT = object_schema({
    "videoId": NULLABLE_STRING, "url": NULLABLE_STRING,
    "wordCount": {"type": "integer", "minimum": 0},
    "chunkCount": {"type": "integer", "minimum": 0},
    "durationMs": {"anyOf": [{"type": "number"}, {"type": "null"}]},
    "transcriptText": {"type": "string"},
    "chunks": {"type": "array", "items": object_schema({
        "startSec": {"type": "number"}, "endSec": {"type": "number"}, "text": {"type": "string"},
    })},
    "resolvedInputs": object_schema({"videoId": NULLABLE_STRING, "url": NULLABLE_STRING}),
})


@pytest.fixture
def generated(tmp_path):
    package_name = "generated_fixture"
    package_root = tmp_path / package_name
    package_root.mkdir()
    (package_root / "__init__.py").write_text("")
    tools = [
        {"name": "youtube_transcribe", "category": "youtube", "methodName": "transcribe",
         "inputSchema": object_schema({"videoId": {"type": "string"}}, required=[]),
         "outputSchema": {"type": "object", "anyOf": [TRANSCRIPT, DELIVERY]},
         "outputSchemaProvided": True},
        {"name": "legacy_status", "category": "legacy", "methodName": "status",
         "inputSchema": object_schema({"connectionId": {"type": "string"}}),
         "outputSchema": object_schema({"ok": {"type": "boolean"},
             "details": object_schema({"source": {"type": "string"}})}),
         "outputSchemaProvided": True},
        {"name": "set-agent-identity", "category": "legacy", "methodName": "setAgentIdentity",
         "inputSchema": object_schema({"displayName": NULLABLE_STRING,
             "optionalNote": NULLABLE_STRING}, required=["displayName"]),
         "outputSchema": object_schema({"ok": {"type": "boolean"}}),
         "outputSchemaProvided": True},
        {"name": "generic_status", "category": "legacy", "methodName": "genericStatus",
         "inputSchema": object_schema({}, required=[]),
         "outputSchema": {"type": "object", "anyOf": [
             object_schema({"ok": {"type": "boolean"}}, required=[]), DELIVERY,
         ]}, "outputSchemaProvided": True},
        {"name": "select_preset", "category": "legacy", "methodName": "selectPreset",
         "inputSchema": {"type": "object", "oneOf": [
             object_schema({"presetKey": {"const": "paper"}, "name": {"type": "string"}}),
             object_schema({"presetKey": {"const": "ink"}, "theme": {"type": "string"}}),
         ]}, "outputSchema": object_schema({"ok": {"type": "boolean"}}),
         "outputSchemaProvided": True},
    ]
    generator.generate_target(package_root, package_name, tools)
    sys.path.insert(0, str(tmp_path))
    try:
        client_module = importlib.import_module(f"{package_name}._mcp_generated_client")
        models_module = importlib.import_module(f"{package_name}.mcp_models.youtube_transcribe")
        yield client_module.GeneratedMcpToolsClient, models_module
    finally:
        sys.path.remove(str(tmp_path))
        for name in list(sys.modules):
            if name == package_name or name.startswith(package_name + "."):
                del sys.modules[name]


def inline_transcript():
    return {
        "videoId": "hour-long-video", "url": None, "wordCount": 12000, "chunkCount": 1,
        "durationMs": 3600000, "transcriptText": "The full transcript. " * 12000,
        "chunks": [{"startSec": 0, "endSec": 3600, "text": "Entire hour", "speaker": "A"}],
        "resolvedInputs": {"videoId": "hour-long-video", "url": None},
        "newServerMetadata": {"language": "en"},
    }


def artifact_delivery():
    return {
        "delivery": {
            "mode": "artifact", "status": "complete", "retainedRepresentation": "formatted-tool-result",
            "sourceIsError": False, "artifacts": [{
                "artifactId": "artifact_1", "filename": "transcript.zip", "contentType": "application/zip",
                "bytes": 120000, "sha256": "a" * 64, "expiresAt": "2026-10-19T00:00:00Z",
                "capabilities": ["download"], "downloadUrl": "https://example.com/transcript.zip",
                "downloadUrlExpiresAt": "2026-10-13T00:00:00Z", "downloadState": "available",
                "resourceUri": "mcp-scraper://artifact/artifact_1",
            }], "downloadLinksOmitted": False, "scopeOmittedFields": 0,
            "storageFailure": None, "nextAction": "Use artifact_download to retrieve the complete file.",
        }, "preview": "Transcript preview", "scope": {"wordCount": 12000, "complete": True, "url": None},
        "recovery": {"runId": "run_1", "idempotencyKey": "transcript:1"},
    }


def test_inline_union_returns_full_typed_transcript_without_root_wrapper(generated):
    client_class, models = generated
    payload = inline_transcript()
    client = client_class(lambda name, arguments: copy.deepcopy(payload))
    result = client.youtube.transcribe(video_id="hour-long-video")

    assert isinstance(result, models.YoutubeTranscribeOutputVariant1)
    assert isinstance(result, BaseModel)
    assert result.transcript_text == payload["transcriptText"]
    assert result.chunks == payload["chunks"]
    assert result.chunks[0]["startSec"] == 0
    assert type(result.chunks[0]["startSec"]) is int
    assert type(result.duration_ms) is int
    assert result.resolved_inputs == payload["resolvedInputs"]
    assert result.model_dump(by_alias=True) == payload
    assert not hasattr(result, "root")


def test_artifact_union_preserves_complete_binary_pointer_and_recovery(generated):
    client_class, models = generated
    payload = artifact_delivery()
    result = client_class(lambda name, arguments: copy.deepcopy(payload)).youtube.transcribe()

    assert isinstance(result, models.YoutubeTranscribeOutputVariant2)
    assert result.delivery["mode"] == "artifact"
    assert result.delivery["artifacts"][0]["resourceUri"] == "mcp-scraper://artifact/artifact_1"
    assert result.delivery["artifacts"][0]["contentType"] == "application/zip"
    assert result.recovery["runId"] == "run_1"
    assert result.scope["complete"] is True
    assert type(result.scope["wordCount"]) is int
    assert type(result.delivery["artifacts"][0]["bytes"]) is int
    assert result.model_dump(by_alias=True) == payload
    assert TypeAdapter(models.YoutubeTranscribeOutput).validate_python(payload).delivery == payload["delivery"]


@pytest.mark.parametrize("change", [
    lambda payload: payload.pop("transcriptText"),
    lambda payload: payload.update(wordCount="12000"),
    lambda payload: payload["chunks"][0].pop("text"),
])
def test_incomplete_or_coercible_inline_payload_does_not_silently_pass(generated, change):
    client_class, _ = generated
    payload = inline_transcript()
    change(payload)
    with pytest.raises(ValidationError):
        client_class(lambda name, arguments: payload).youtube.transcribe()


@pytest.mark.parametrize("change", [
    lambda payload: payload["delivery"].update(mode="inline"),
    lambda payload: payload["delivery"]["artifacts"][0].pop("downloadUrl"),
    lambda payload: payload["delivery"].update(scopeOmittedFields=-1),
    lambda payload: payload["delivery"].update(sourceIsError="false"),
])
def test_nested_artifact_contract_rejects_invalid_discriminator_and_required_metadata(generated, change):
    client_class, _ = generated
    payload = artifact_delivery()
    change(payload)
    with pytest.raises(ValidationError):
        client_class(lambda name, arguments: payload).youtube.transcribe()


def test_required_nullable_metadata_and_nested_unavailable_outcome(generated):
    client_class, _ = generated
    payload = artifact_delivery()
    payload["delivery"]["artifacts"][0].update(downloadUrl=None, downloadUrlExpiresAt=None,
                                               downloadState="unavailable")
    payload["delivery"]["storageFailure"] = {"artifactId": None, "outcome": "unknown"}
    result = client_class(lambda name, arguments: payload).youtube.transcribe()
    assert result.model_dump(by_alias=True) == payload


def test_existing_model_methods_keep_snake_aliases_dictionary_shapes_and_extras(generated):
    client_class, _ = generated
    calls = []
    payload = {"ok": True, "details": {"source": "server", "newField": 17}, "requestId": "req_1"}
    def call(name, arguments):
        calls.append((name, arguments))
        return payload
    result = client_class(call).legacy.status(connection_id="conn_1")
    assert calls == [("legacy_status", {"connectionId": "conn_1"})]
    assert result.ok is True
    assert result.details["newField"] == 17
    assert result.model_dump(by_alias=True) == payload


def test_top_level_input_union_validates_and_serializes_selected_branch(generated):
    client_class, _ = generated
    calls = []
    def call(name, arguments):
        calls.append((name, arguments))
        return {"ok": True}
    client = client_class(call)
    client.legacy.select_preset(preset_key="ink", theme="dark")
    assert calls == [("select_preset", {"presetKey": "ink", "theme": "dark"})]
    with pytest.raises(ValidationError):
        client.legacy.select_preset(preset_key="unknown", name="Invalid")
    assert len(calls) == 1


def test_artifact_branch_wins_over_permissive_legacy_output(generated):
    client_class, _ = generated
    payload = artifact_delivery()
    result = client_class(lambda name, arguments: payload).legacy.generic_status()
    assert type(result).__name__ == "GenericStatusOutputVariant2"
    assert result.model_dump(by_alias=True) == payload


def test_required_and_explicit_optional_nulls_survive_while_omitted_fields_stay_absent(generated):
    client_class, _ = generated
    calls = []
    def call(name, arguments):
        calls.append((name, arguments))
        return {"ok": True}
    client = client_class(call)
    client.legacy.set_agent_identity(display_name=None, optional_note=None)
    client.legacy.set_agent_identity(display_name=None)
    assert calls == [
        ("set-agent-identity", {"displayName": None, "optionalNote": None}),
        ("set-agent-identity", {"displayName": None}),
    ]
    with pytest.raises(ValidationError):
        client.legacy.set_agent_identity()
    assert len(calls) == 2
