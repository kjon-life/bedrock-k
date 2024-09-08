import pytest
from your_package.s3_operations import create_bucket, upload_file

def test_create_bucket_success(s3_client):
    bucket_name = "test-bucket"
    result = create_bucket(s3_client, bucket_name)
    assert result == True
    assert s3_client.head_bucket(Bucket=bucket_name)

def test_create_bucket_failure(s3_client):
    bucket_name = "test-bucket"
    create_bucket(s3_client, bucket_name)
    with pytest.raises(Exception):
        create_bucket(s3_client, bucket_name)  # Bucket already exists

@pytest.mark.parametrize("file_name, content", [
    ("test1.txt", b"Hello World"),
    ("test2.txt", b"Python Testing"),
])
def test_upload_file(s3_client, file_name, content):
    bucket_name = "test-bucket"
    create_bucket(s3_client, bucket_name)
    result = upload_file(s3_client, bucket_name, file_name, content)
    assert result == True
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    assert obj['Body'].read() == content

def test_upload_large_file(s3_client):
    bucket_name = "test-bucket"
    create_bucket(s3_client, bucket_name)
    large_content = b"x" * 1024 * 1024 * 6  # 6 MB file
    result = upload_file(s3_client, bucket_name, "large_file.bin", large_content)
    assert result == True
    obj = s3_client.get_object(Bucket=bucket_name, Key="large_file.bin")
    assert obj['ContentLength'] == len(large_content)

def test_upload_empty_file(s3_client):
    bucket_name = "test-bucket"
    create_bucket(s3_client, bucket_name)
    result = upload_file(s3_client, bucket_name, "empty.txt", b"")
    assert result == True
    obj = s3_client.get_object(Bucket=bucket_name, Key="empty.txt")
    assert obj['ContentLength'] == 0

def test_create_bucket_with_invalid_name(s3_client):
    invalid_bucket_name = "Invalid Bucket Name"
    with pytest.raises(Exception):
        create_bucket(s3_client, invalid_bucket_name)