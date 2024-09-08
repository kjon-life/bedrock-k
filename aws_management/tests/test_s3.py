import pytest
from botocore.exceptions import ClientError
from your_package.s3_operations import create_bucket, upload_file


def test_create_bucket_success(s3_client):
    """Test creating a bucket successfully."""
    bucket_name = "test-bucket"
    result = create_bucket(s3_client, bucket_name)
    assert result  # noqa: S101
    assert s3_client.head_bucket(Bucket=bucket_name)  # noqa: S101

def test_create_bucket_failure(s3_client):
    """Test creating a bucket that already exists."""
    bucket_name = "test-bucket"
    create_bucket(s3_client, bucket_name)
    with pytest.raises(ClientError):
        create_bucket(s3_client, bucket_name)  # Bucket already exists

@pytest.mark.parametrize("file_name, content", [
    ("test1.txt", b"Hello World"),
    ("test2.txt", b"Python Testing"),
])
def test_upload_file(s3_client, file_name, content):
    """Test uploading a file to S3 bucket."""
    bucket_name = "test-bucket"
    create_bucket(s3_client, bucket_name)
    result = upload_file(s3_client, bucket_name, file_name, content)
    assert result  # noqa: S101
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    assert obj["Body"].read() == content  # noqa: S101

def test_upload_large_file(s3_client):
    """Test uploading a large file to S3 bucket."""
    bucket_name = "test-bucket"
    create_bucket(s3_client, bucket_name)
    large_content = b"x" * 1024 * 1024 * 6  # 6 MB file
    result = upload_file(s3_client, bucket_name, "large_file.bin", large_content)
    assert result  # noqa: S101
    obj = s3_client.get_object(Bucket=bucket_name, Key="large_file.bin")
    assert obj["ContentLength"] == len(large_content)  # noqa: S101

def test_upload_empty_file(s3_client):
    """Test uploading an empty file to S3 bucket."""
    bucket_name = "test-bucket"
    create_bucket(s3_client, bucket_name)
    result = upload_file(s3_client, bucket_name, "empty.txt", b"")
    assert result  # noqa: S101
    obj = s3_client.get_object(Bucket=bucket_name, Key="empty.txt")
    assert obj["ContentLength"] == 0  # noqa: S101

def test_create_bucket_with_invalid_name(s3_client):
    """Test that creating a bucket with an invalid name raises a ClientError.

    This test ensures that the create_bucket function properly handles
    invalid bucket names by raising a ClientError with an 'InvalidBucketName'
    message.

    Args:
        s3_client: A boto3 S3 client fixture.

    Raises:
        AssertionError: If the expected ClientError is not raised or if the
                        error message doesn't contain 'InvalidBucketName'.
    """
    invalid_bucket_name = "Invalid Bucket Name"
    with pytest.raises(ClientError) as excinfo:
        create_bucket(s3_client, invalid_bucket_name)

    assert "InvalidBucketName" in str(excinfo.value)  # noqa: S101
