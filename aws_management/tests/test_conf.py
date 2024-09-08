import pytest
import boto3
from moto import mock_s3, mock_sso, mock_bedrock

@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    import os
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"

@pytest.fixture(scope="function")
def s3_client(aws_credentials):
    with mock_s3():
        yield boto3.client("s3", region_name="us-east-1")

@pytest.fixture(scope="function")
def identity_center_client(aws_credentials):
    with mock_sso():
        yield boto3.client("sso", region_name="us-east-1")

@pytest.fixture(scope="function")
def bedrock_client(aws_credentials):
    with mock_bedrock():
        yield boto3.client("bedrock", region_name="us-east-1")