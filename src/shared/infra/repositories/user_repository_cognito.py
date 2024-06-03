import json
import time
from typing import Tuple, List

import boto3
from botocore.exceptions import ClientError

from src.shared.domain.repositories.user_repository_cognito_interface import IUserRepositoryCognito
from src.shared.environments import Environments
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, InvalidCredentials, InvalidTokenError
from src.shared.infra.dtos.user_cognito_dto import UserCognitoDTO


class UserRepositoryCognito(IUserRepositoryCognito):

    client: boto3.client
    user_pool_id: str
    client_id: str

    def __init__(self):
        self.client = boto3.client('cognito-idp', region_name=Environments.get_envs().region)
        self.user_pool_id = Environments.get_envs().user_pool_id
        self.client_id = Environments.get_envs().client_id
    
    def in_gaia_group(self, email: str) -> bool:
        try:
            response = self.client.admin_list_groups_for_user(
                Username=email,
                UserPoolId=self.user_pool_id
            )
            groups = response.get('Groups')
            if groups is not None:
                group_names = [group.get('GroupName') for group in groups]
                return 'GAIA' in group_names
            else:
                return False
        
        except self.client.exceptions.UserNotFoundException as e:
            return False

    
    def get_user_by_email(self, email: str) -> UserCognitoDTO:
        try:
            response = self.client.admin_get_user(
                UserPoolId=self.user_pool_id,
                Username=email
            )

            user = UserCognitoDTO.from_cognito(response)
            user.in_group = self.in_gaia_group(email)

            return user

        except self.client.exceptions.UserNotFoundException:
            return None
    
    def create_user(self, email: str, name: str) -> UserCognitoDTO:
        cognito_attributes = [
            {
                "Name": "email",
                "Value": email
            },
            {
                "Name": "name",
                "Value": name
            },
            {
                "Name": "custom:general_role",
                "Value": "USER"
            }
        ]
        cognito_attributes.append({
            "Name": "email_verified",
            "Value": "True"
        })

        try:

            self.client.admin_create_user(
                UserPoolId=self.user_pool_id,
                Username=email,
                DesiredDeliveryMediums=["EMAIL"],
                UserAttributes=cognito_attributes)
            
            self.add_user_to_group(user_email=email)
                
            return self.get_user_by_email(email)

        except self.client.exceptions.UsernameExistsException:
            raise DuplicatedItem("user")

        except self.client.exceptions.InvalidParameterException as e:
            raise EntityError(e.response.get('Error').get('Message'))
    
    
    def add_user_to_group(self, user_email: str) -> None:
        try:
            self.client.admin_add_user_to_group(
                UserPoolId=self.user_pool_id,
                Username=user_email,
                GroupName="GAIA"
            )
        except self.client.exceptions.ResourceNotFoundException as e:
            raise EntityError(e.response.get('Error').get('Message'))

        except self.client.exceptions.InvalidParameterException as e:
            raise EntityError(e.response.get('Error').get('Message'))