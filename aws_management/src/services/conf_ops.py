import boto3

def create_user(client, identity_store_id, username, email, given_name, family_name):
    response = client.create_user(
        IdentityStoreId=identity_store_id,
        UserName=username,
        Name={
            'GivenName': given_name,
            'FamilyName': family_name
        },
        Emails=[
            {
                'Value': email,
                'Type': 'Work'
            }
        ]
    )
    return {'UserId': response['UserId']}  # Return a dict to match test expectations

def create_group(client, identity_store_id, display_name, description):
    response = client.create_group(
        IdentityStoreId=identity_store_id,
        DisplayName=display_name,
        Description=description
    )
    return {'GroupId': response['GroupId']}  # Return a dict to match test expectations

def assign_user_to_group(client, identity_store_id, group_id, user_id):
    response = client.create_group_membership(
        IdentityStoreId=identity_store_id,
        GroupId=group_id,
        MemberId={
            'UserId': user_id
        }
    )
    return {'MembershipId': response['MembershipId']}  # Return a dict to match test expectations

def assign_group_to_user(client, identity_store_id, group_id, user_id):
    return assign_user_to_group(client, identity_store_id, group_id, user_id)