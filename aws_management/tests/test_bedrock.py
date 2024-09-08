import pytest
from bedrock_k.aws_management.bedrock_operations import invoke_model

def test_invoke_model_success(bedrock_client):
    model_id = "ai21.j2-ultra-v1"
    prompt = "Translate 'Hello' to French"
    result = invoke_model(bedrock_client, model_id, prompt)
    assert "Bonjour" in result

def test_invoke_model_failure(bedrock_client):
    model_id = "non_existent_model"
    prompt = "This should fail"
    with pytest.raises(Exception):
        invoke_model(bedrock_client, model_id, prompt)

@pytest.mark.parametrize("model_id, prompt, expected", [
    ("ai21.j2-ultra-v1", "1 + 1", "2"),
    ("anthropic.claude-v2", "Capital of France", "Paris"),
])
def test_invoke_model_parametrized(bedrock_client, model_id, prompt, expected):
    result = invoke_model(bedrock_client, model_id, prompt)
    assert expected in result

def test_invoke_model_with_empty_prompt(bedrock_client):
    model_id = "ai21.j2-ultra-v1"
    prompt = ""
    with pytest.raises(ValueError):
        invoke_model(bedrock_client, model_id, prompt)

def test_invoke_model_with_long_prompt(bedrock_client):
    model_id = "anthropic.claude-v2"
    prompt = "x" * 10000  # Very long prompt
    result = invoke_model(bedrock_client, model_id, prompt)
    assert len(result) > 0

@pytest.mark.parametrize("invalid_model_id", [
    "",
    "invalid.model",
    "ai21.nonexistent",
])
def test_invoke_model_with_invalid_model_id(bedrock_client, invalid_model_id):
    prompt = "Test prompt"
    with pytest.raises(Exception):
        invoke_model(bedrock_client, invalid_model_id, prompt)