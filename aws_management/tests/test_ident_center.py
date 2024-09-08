import pytest
from aws_management.services.identity_center_operations import create_user, assign_user_to_group

def test_create_user_success(identity_center_client):
    user_name = "testuser"
    result = create_user(identity_center_client, user_name)
    assert result['UserName'] == user_name

def test_create_user_failure(identity_center_client):
    user_name = "testuser"
    create_user(identity_center_client, user_name)
    with pytest.raises(Exception):
        create_user(identity_center_client, user_name)  # User already exists

@pytest.mark.parametrize("user_name, group_name", [
    ("user1", "group1"),
    ("user2", "group2"),
])
def test_assign_user_to_group(identity_center_client, user_name, group_name):
    create_user(identity_center_client, user_name)
    result = assign_user_to_group(identity_center_client, user_name, group_name)
    assert result == True

def test_create_user_with_invalid_characters(identity_center_client):
    invalid_user_name = "user@invalid"
    with pytest.raises(Exception):
        create_user(identity_center_client, invalid_user_name)

def test_assign_user_to_nonexistent_group(identity_center_client):
    user_name = "testuser"
    nonexistent_group = "nonexistent_group"
    create_user(identity_center_client, user_name)
    with pytest.raises(Exception):
        assign_user_to_group(identity_center_client, user_name, nonexistent_group)

def test_assign_nonexistent_user_to_group(identity_center_client):
    nonexistent_user = "nonexistent_user"
    group_name = "testgroup"
    with pytest.raises(Exception):
        assign_user_to_group(identity_center_client, nonexistent_user, group_name)

def test_create_group_with_invalid_name(identity_center_client):
    invalid_group_name = "group@invalid"
    with pytest.raises(Exception):
        create_group(identity_center_client, invalid_group_name)

def test_assign_group_to_nonexistent_user(identity_center_client):
    group_name = "testgroup"
    nonexistent_user = "nonexistent_user"
    create_group(identity_center_client, group_name)
    with pytest.raises(Exception):
        assign_group_to_user(identity_center_client, group_name, nonexistent_user) 