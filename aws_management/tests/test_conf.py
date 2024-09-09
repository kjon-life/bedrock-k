import uuid
import boto3
import pytest
from moto import mock_aws
from botocore.stub import Stubber

dummy_token = str(uuid.uuid4())

@pytest.fixture(scope="function")
def aws_credentials():
    """Mock AWS Credentials for moto.
    
    This sets up mock AWS credentials for testing purposes.
"""
    import os
    os.environ["AWS_ACCESS_KEY_ID"] = dummy_token
    os.environ["AWS_SECRET_ACCESS_KEY"] = dummy_token
    os.environ["AWS_SECURITY_TOKEN"] = dummy_token
    os.environ["AWS_SESSION_TOKEN"] = dummy_token


@pytest.fixture(scope="function")
def s3_client(aws_credentials):
    """Mock S3 client for testing.
    
    This creates a mock S3 client for testing. We've changed mock_s3() to mock_aws() to work with the newer version of moto."""
    with mock_aws():
        yield boto3.client("s3", region_name="us-east-1")

@pytest.fixture(scope="function")
def identity_center_client(aws_credentials):
    """Mock Identity Center client for testing."""
    with mock_aws():
        yield boto3.client("sso", region_name="us-east-1")

@pytest.fixture(scope="function")
def bedrock_client(aws_credentials, monkeypatch):
    """Mock Bedrock client for testing using pytest's monkeypatch.
    
    This modification replaces the mock_bedrock() context manager with a custom fixture that uses pytest.monkeypatch and botocore.stub.Stubber. Here's a brief explanation of the changes:
    We import Stubber from botocore.stub.
    In the bedrock_client fixture, we create a mock client and a Stubber instance.
    We can add stubbed responses for specific Bedrock API calls using stubber.add_response(). You should add the necessary stubs based on the Bedrock API calls your tests will make.
    We use monkeypatch to replace the boto3.client function with a custom lambda that returns our mocked client for the "bedrock" service.
    The fixture yields the mock client for use in tests.
    After the tests, we deactivate the stubber.
    This approach allows you to have fine-grained control over the mocked Bedrock client's behavior in your tests. You can add specific stubbed responses for each Bedrock API call your tests need to make.
    Remember to update your tests to use this new fixture and add the necessary stubbed responses for each test case that interacts with the Bedrock client."""
    mock_client = boto3.client("bedrock", region_name="us-east-1")
    stubber = Stubber(mock_client)
    
    # Add any necessary stubbed responses here
    # For example:
    # stubber.add_response('list_foundation_models', {'modelSummaries': []})
    
    stubber.activate()
    
    monkeypatch.setattr(boto3, "client", lambda service, region_name: mock_client if service == "bedrock" else boto3.client(service, region_name=region_name))
    
    yield mock_client
    
    stubber.deactivate()