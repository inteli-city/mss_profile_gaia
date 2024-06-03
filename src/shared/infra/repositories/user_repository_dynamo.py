from typing import List, Optional
import boto3
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, InvalidTokenError, NoItemsFound, UserNotValid
from src.shared.infra.dtos.user_dynamo_dto import UserDynamoDTO
from botocore.exceptions import ClientError

from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class UserRepositoryDynamo(IUserRepository):
    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key="PK",
                                       )

    @staticmethod
    def partition_key_format(user_id: str) -> str:
        return f"{user_id}"     
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        user_data = self.dynamo.get_item(partition_key=self.partition_key_format(user_id=user_id))                    
        
        if 'Item' not in user_data:
            return None

        user = UserDynamoDTO.from_dynamo(user_data.get("Item")).to_entity()

        return user

    def get_all_users(self) -> List[User]:
        response = self.dynamo.get_all_items()

        users= list()

        for item in response["Items"]:
            users.append(UserDynamoDTO.from_dynamo(item).to_entity())
        
        return users

    def create_profile(self, user: User) -> User:
        item = UserDynamoDTO.from_entity(user=user).to_dynamo()

        resp = self.dynamo.put_item(
            partition_key=self.partition_key_format(user.user_id),
            item=item,
            is_decimal=True
        )

        return user

    def update_user_by_id(self, user_id: str, new_user_data: dict) -> User:

        response = self.dynamo.update_item(
            partition_key=self.partition_key_format(user_id=user_id),
            sort_key=None,
            update_dict=new_user_data)

        if "Attributes" not in response:
            return None

        return UserDynamoDTO.from_dynamo(response["Attributes"]).to_entity()