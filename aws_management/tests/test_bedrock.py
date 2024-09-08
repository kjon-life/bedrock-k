import pytest
from bedrock_k.aws_management.bedrock_operations import invoke_model
from botocore.exceptions import ClientError


def test_invoke_model_success(bedrock_client):
    """Test invoking a model successfully."""
    model_id = "ai21.j2-ultra-v1"
    prompt = "Translate 'Hello' to French"
    result = invoke_model(bedrock_client, model_id, prompt)
    assert "Bonjour" in result  # noqa: S101

def test_invoke_model_failure(bedrock_client):
    """Test invoking a non-existent model."""
    model_id = "non_existent_model"
    prompt = "This should fail"
    with pytest.raises(ClientError):
        invoke_model(bedrock_client, model_id, prompt)

@pytest.mark.parametrize("model_id, prompt, expected", [
    ("anthropic.claude-v2", "Capital of France", "Paris"),
])
def test_invoke_model_parametrized(bedrock_client, model_id, prompt, expected):
    """Test the invoke_model function with various models and prompts.

    This parametrized test checks if the invoke_model function correctly
    processes different model IDs and prompts, and returns expected results.

    Args:
        bedrock_client (MagicMock): A mocked Bedrock client.
        model_id (str): The ID of the model to be tested.
        prompt (str): The input prompt for the model.
        expected (str): The expected substring in the model's response.

    Raises:
        AssertionError: If the expected substring is not found in the model's response.
    """
    result = invoke_model(bedrock_client, model_id, prompt)
    assert expected in result  # noqa: S101

def test_invoke_model_with_empty_prompt(bedrock_client):
    """Test invoking a model with an empty prompt."""
    model_id = "ai21.j2-ultra-v1"
    prompt = ""
    with pytest.raises(ValueError):
        invoke_model(bedrock_client, model_id, prompt)

def test_invoke_model_with_long_prompt(bedrock_client):
    """Test invoking a model with a very long prompt."""
    model_id = "anthropic.claude-v2"
    prompt = "x" * 10000  # Very long prompt
    result = invoke_model(bedrock_client, model_id, prompt)
    assert len(result) > 0  # noqa: S101, PLR201

@pytest.mark.parametrize("invalid_model_id", [
    "",
    "invalid.model",
    "ai21.nonexistent",
])
def test_invoke_model_with_invalid_model_id(bedrock_client, invalid_model_id):
    """Test invoking a model with an invalid model ID."""
    prompt = "Test prompt"
    with pytest.raises(ClientError):
        invoke_model(bedrock_client, invalid_model_id, prompt)
