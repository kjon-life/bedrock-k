import pytest
import boto3
import uuid
from botocore.stub import Stubber
from botocore.exceptions import ClientError
from aws_management.src.services.s3_ops import create_bucket, upload_file

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="botocore.auth")

@pytest.fixture
def s3_client():
    """Fixture for mocked AWS S3 client."""
    client = boto3.client('s3')
    with Stubber(client) as stubber:
        yield stubber, client
        stubber.assert_no_pending_responses()

def test_create_bucket(s3_client):
    stubber, client = s3_client
    bucket_name = 'test-bucket'
    
    # Stub the create_bucket response
    stubber.add_response('create_bucket', {}, {'Bucket': bucket_name})
    
    # Call the function
    result = create_bucket(bucket_name)
    
    # Assert the result
    assert result is True

def test_upload_file(s3_client):
    stubber, client = s3_client
    bucket_name = 'test-bucket'
    file_name = 'test.txt'
    object_name = 'test.txt'
    
    # Stub the upload_file response
    stubber.add_response('put_object', {}, {'Bucket': bucket_name, 'Key': object_name})
    
    # Call the function
    result = upload_file(file_name, bucket_name, object_name)
    
    # Assert the result
    assert result is True