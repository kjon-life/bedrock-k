import uuid

import boto3
import pytest
from moto import mock_bedrock, mock_s3, mock_sso

dummy_token = str(uuid.uuid4())

@pytest.fixture(scope="function")
def aws_credentials():
    """Mock AWS Credentials for moto."""
    import os
    os.environ["AWS_ACCESS_KEY_ID"] = dummy_token
    os.environ["AWS_SECRET_ACCESS_KEY"] = dummy_token
    os.environ["AWS_SECURITY_TOKEN"] = dummy_token
    os.environ["AWS_SESSION_TOKEN"] = dummy_token

@pytest.fixture(scope="function")
def s3_client(aws_credentials):
    """Mock S3 client for testing."""
    with mock_s3():
        yield boto3.client("s3", region_name="us-east-1")

@pytest.fixture(scope="function")
def identity_center_client(aws_credentials):
    """Mock Identity Center client for testing."""
    with mock_sso():
        yield boto3.client("sso", region_name="us-east-1")

@pytest.fixture(scope="function")
def bedrock_client(aws_credentials):
    """Mock Bedrock client for testing."""
    with mock_bedrock():
        yield boto3.client("bedrock", region_name="us-east-1")
