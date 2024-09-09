import pytest
import pytest_asyncio
from aws_management.src.services.bedrock_ops import invoke_model
from botocore.exceptions import ClientError
from botocore.stub import Stubber
import boto3

@pytest.fixture
def bedrock_client():
    """Create a stubbed Bedrock client for testing.

    Yeilds a tuple of (stubber, client) for the Bedrock service.
    """
    client = boto3.client('bedrock-runtime', region_name='us-east-1')
    with Stubber(client) as stubber:
        yield stubber, client

async def test_invoke_model_success(bedrock_client):
    """Test invoking a model successfully."""
    stubber, client = bedrock_client
    model_id = "ai21.j2-ultra-v1"
    prompt = "Translate 'Hello' to French"
    
    # Stub the invoke_model response
    response = {
        'body': b'{"completions": [{"data": "Bonjour"}]}',
        'contentType': 'application/json',
    }
    expected_params = {
        'body': '{"prompt": "Translate \'Hello\' to French"}',
        'modelId': 'ai21.j2-ultra-v1',
        'accept': 'application/json',
        'contentType': 'application/json',
    }
    stubber.add_response('invoke_model', response, expected_params)
    
    result = await invoke_model(prompt, model=model_id)
    assert "Bonjour" in result  # noqa: S101

async def test_invoke_model_failure(bedrock_client):
    """Test invoking a non-existent model."""
    stubber, client = bedrock_client
    prompt = "This should fail"
    with pytest.raises(ClientError):
        await invoke_model(prompt, model="non_existent_model")

@pytest.mark.parametrize("model, prompt, expected", [
    ("anthropic.claude-v2", "Capital of France", "Paris"),
])
async def test_invoke_model_parametrized(bedrock_client, model, prompt, expected):
    """Test the invoke_model function with various models and prompts."""
    stubber, client = bedrock_client
    result = await invoke_model(prompt, model=model)
    assert expected in result  # noqa: S101

async def test_invoke_model_with_empty_prompt(bedrock_client):
    """Test invoking a model with an empty prompt."""
    stubber, client = bedrock_client
    prompt = ""
    with pytest.raises(ValueError):
        await invoke_model(prompt)

async def test_invoke_model_with_long_prompt(bedrock_client):
    """Test invoking a model with a very long prompt."""
    stubber, client = bedrock_client
    prompt = "x" * 10000  # Very long prompt
    result = await invoke_model(prompt)
    assert len(result) > 0  # noqa: S101, PLR201

@pytest.mark.parametrize("invalid_model", [
    "",
    "invalid.model",
    "ai21.nonexistent",
])
async def test_invoke_model_with_invalid_model_id(bedrock_client, invalid_model):
    """Test invoking a model with an invalid model ID."""
    stubber, client = bedrock_client
    prompt = "Test prompt"
    with pytest.raises(ClientError):
        await invoke_model(prompt, model=invalid_model)


async def test_invoke_model_success(bedrock_client):
    """Test invoking a model successfully."""
    stubber, client = bedrock_client
    model_id = "ai21.j2-ultra-v1"
    prompt = "Translate 'Hello' to French"
    
    # Stub the invoke_model response
    response = {
        'body': b'{"completions": [{"data": "Bonjour"}]}',
        'contentType': 'application/json',
    }
    expected_params = {
        'body': '{"prompt": "Translate \'Hello\' to French"}',
        'modelId': 'ai21.j2-ultra-v1',
        'accept': 'application/json',
        'contentType': 'application/json',
    }
    stubber.add_response('invoke_model', response, expected_params)
    
    result = await invoke_model(prompt, model=model_id)
    assert "Bonjour" in result  # noqa: S101

# Update other test functions to use the tuple(stubber, client) = bedrock_client