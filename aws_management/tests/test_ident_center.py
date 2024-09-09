import pytest
from botocore.exceptions import ClientError
from botocore.stub import Stubber
import boto3

from aws_management.src.services.conf_ops import (
    assign_group_to_user,
    assign_user_to_group,
    create_group,
    create_user,
)

@pytest.fixture
def identity_center_client():
    """Fixture for mocked AWS Identity Center client."""
    client = boto3.client('identitystore')
    with Stubber(client) as stubber:
        yield stubber, client
        stubber.assert_no_pending_responses()

@pytest.fixture
def sso_admin_client():
    """Fixture for mocked AWS SSO Admin client."""
    client = boto3.client('sso-admin')
    with Stubber(client) as stubber:
        yield stubber, client
        stubber.assert_no_pending_responses()

@pytest.fixture
def identity_store_id():
    """Fixture for Identity Store ID."""
    return "d-1234567890"

def test_list_users(identity_center_client, identity_store_id):
    """Test listing users in Identity Center."""
    stubber, client = identity_center_client
    
    expected_params = {
        'IdentityStoreId': identity_store_id,
        'MaxResults': 100
    }
    response = {
        'Users': [
            {'UserName': 'user1', 'UserId': 'id1', 'IdentityStoreId': identity_store_id},
            {'UserName': 'user2', 'UserId': 'id2', 'IdentityStoreId': identity_store_id}
        ],
        'NextToken': 'sometoken'
    }
    stubber.add_response('list_users', response, expected_params)
    
    with stubber:
        try:
            result = client.list_users(**expected_params)
        except ClientError as e:
            print(f"ClientError: {e}")
        except ParamValidationError as e:
            print(f"ParamValidationError: {e}")
            raise
    
    assert len(result['Users']) == 2  # noqa: S101
    assert result['Users'][0]['UserName'] == 'user1'  # noqa: S101
    assert result['Users'][1]['UserName'] == 'user2'  # noqa: S101

def test_create_user_success(identity_center_client, identity_store_id):
    user_name = "testuser"
    email = "testuser@example.com"
    given_name = "Test"
    family_name = "User"
    
    stubber, client = identity_center_client
    expected_params = {
        'IdentityStoreId': identity_store_id,
        'UserName': user_name,
        'Name': {
            'GivenName': given_name,
            'FamilyName': family_name
        },
        'Emails': [{'Type': 'Work', 'Value': email}]
    }
    response = {
        'UserId': 'test-user-id',
        'IdentityStoreId': identity_store_id  # Include IdentityStoreId in the response
    }
    stubber.add_response('create_user', response, expected_params)
    
    with stubber:
        result = create_user(client, identity_store_id, user_name, email, given_name, family_name)
    
    assert result["UserId"] == 'test-user-id'  # noqa: S101

def test_create_user_failure(identity_center_client, identity_store_id):
    """Test creating a user that already exists."""
    user_name = "testuser"
    email = "testuser@example.com"
    given_name = "Test"
    family_name = "User"
    
    stubber, client = identity_center_client
    stubber.add_client_error('create_user', 'ResourceAlreadyExistsException')
    
    with stubber:
        with pytest.raises(ClientError):
            create_user(client, identity_store_id, user_name, email, given_name, family_name)

@pytest.mark.parametrize("user_name, group_name", [
    ("user1", "group1"),
    ("user2", "group2"),
])
def test_assign_user_to_group(identity_center_client, identity_store_id, user_name, group_name):
    stubber, client = identity_center_client
    email = f"{user_name}@example.com"
    given_name = "Test"
    family_name = "User"

    stubber.add_response('create_user', {
        'UserId': 'test-user-id',
        'IdentityStoreId': identity_store_id  # Include IdentityStoreId in the response
    }, {
        'IdentityStoreId': identity_store_id,
        'UserName': user_name,
        'Name': {
            'GivenName': given_name,
            'FamilyName': family_name
        },
        'Emails': [{'Type': 'Work', 'Value': email}]  # Ensure 'Type' is included
    })

    stubber.add_response('create_group', {
        'GroupId': 'test-group-id',
        'IdentityStoreId': identity_store_id  # Add IdentityStoreId to the response
    }, {
        'IdentityStoreId': identity_store_id,
        'DisplayName': group_name,
        'Description': 'Test group'
    })

    stubber.add_response('create_group_membership', {
        'MembershipId': 'test-membership-id',
        'IdentityStoreId': identity_store_id  # Add IdentityStoreId to the response
    }, {
        'IdentityStoreId': identity_store_id,
        'GroupId': 'test-group-id',
        'MemberId': {'UserId': 'test-user-id'}
    })

    with stubber:
        user_id = create_user(client, identity_store_id, user_name, email, given_name, family_name)['UserId']
        group_id = create_group(client, identity_store_id, group_name, "Test group")['GroupId']
        result = assign_user_to_group(client, identity_store_id, group_id, user_id)

    assert result['MembershipId']  # noqa: S101

def test_create_user_with_invalid_characters(identity_center_client, identity_store_id):
    """Test creating a user with invalid characters."""
    invalid_user_name = "user@invalid"
    email = "user.invalid@example.com"
    given_name = "Invalid"
    family_name = "User"

    stubber, client = identity_center_client
    stubber.add_client_error('create_user', 'ValidationException', 'Invalid username')

    with stubber:
        with pytest.raises(ClientError):
            create_user(client, identity_store_id, invalid_user_name, email, given_name, family_name)

def test_assign_user_to_nonexistent_group(identity_center_client, identity_store_id):
    """Test assigning a user to a nonexistent group."""
    user_name = "testuser"
    email = "email@example.com"
    given_name = "Test"
    family_name = "User"
    
    stubber, client = identity_center_client
    stubber.add_response('create_user', {
        'UserId': 'test-user-id',
        'IdentityStoreId': identity_store_id  # Include IdentityStoreId in the response
    }, {
        'IdentityStoreId': identity_store_id,
        'UserName': user_name,
        'Name': {
            'GivenName': given_name,
            'FamilyName': family_name
        },
        'Emails': [{'Type': 'Work', 'Value': email}]  # Ensure 'Type' is included
    })
    
    stubber.add_client_error('create_group_membership', 'ResourceNotFoundException')
    
    with stubber:
        create_user(client, identity_store_id, user_name, email, given_name, family_name)
        with pytest.raises(ClientError):
            assign_user_to_group(client, identity_store_id, 'nonexistent-group-id', 'test-user-id')

def test_assign_nonexistent_user_to_group(identity_center_client, identity_store_id):
    """Test assigning a nonexistent user to a group."""
    group_name = "testgroup"
    
    stubber, client = identity_center_client
    stubber.add_response('create_group', {
        'GroupId': 'test-group-id',
        'IdentityStoreId': identity_store_id  # Include IdentityStoreId in the response
    }, {
        'IdentityStoreId': identity_store_id,
        'DisplayName': group_name,
        'Description': 'Test group'
    })
    
    stubber.add_client_error('create_group_membership', 'ResourceNotFoundException')
    
    with stubber:
        create_group(client, identity_store_id, group_name, "Test group")
        with pytest.raises(ClientError):
            assign_user_to_group(client, identity_store_id, 'test-group-id', 'nonexistent-user-id')

def test_create_group_with_invalid_name(identity_center_client, identity_store_id):
    invalid_group_name = "group@invalid"
    description = "Test group"
    
    stubber, client = identity_center_client
    stubber.add_client_error('create_group', 'ValidationException', 'Invalid group name')
    
    with stubber:
        with pytest.raises(ClientError):
            create_group(client, identity_store_id, invalid_group_name, description)

def test_assign_group_to_nonexistent_user(identity_center_client, identity_store_id):
    group_name = "testgroup"
    nonexistent_user = "nonexistent_user"
    description = "Test group"
    
    stubber, client = identity_center_client
    stubber.add_response('create_group', {
        'GroupId': 'test-group-id',
        'IdentityStoreId': identity_store_id  # Include IdentityStoreId in the response
    }, {
        'IdentityStoreId': identity_store_id,
        'DisplayName': group_name,
        'Description': description
    })
    
    stubber.add_client_error('create_group_membership', 'ResourceNotFoundException')
    
    with stubber:
        group_id = create_group(client, identity_store_id, group_name, description)['GroupId']
        with pytest.raises(ClientError):
            assign_group_to_user(client, identity_store_id, group_id, nonexistent_user)