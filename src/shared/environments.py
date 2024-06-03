import enum
from enum import Enum
import os
from src.shared.domain.repositories.user_repository_cognito_interface import IUserRepositoryCognito
from src.shared.domain.repositories.user_repository_interface import IUserRepository


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    HOMOLOG = "HOMOLOG"
    PROD = "PROD"
    TEST = "TEST"

class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE
    region: str
    endpoint_url: str = None
    dynamo_table_name: str
    dynamo_partition_key: str
    user_pool_id: str
    client_id: str

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.DOTENV.value

    def load_envs(self):
        if "STAGE" not in os.environ:
            os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.DEV.value

        self.stage = STAGE[os.environ.get("STAGE")]

        if self.stage == STAGE.TEST:
            self.region = "sa-east-1"
            self.endpoint_url = "test"
            self.dynamo_table_name = "user"
            self.dynamo_partition_key = "pk"
            self.user_pool_id = "test"
            self.client_id = "test"
        else:
            self.region = os.environ.get("AWS_REGION")
            self.endpoint_url = os.environ.get("ENDPOINT_URL")
            self.dynamo_table_name = os.environ.get("DYNAMO_TABLE_NAME")
            self.dynamo_partition_key = os.environ.get("DYNAMO_PARTITION_KEY")
            self.user_pool_id = os.environ.get("USER_POOL_ID")
            self.client_id = os.environ.get("APP_CLIENT_ID")

    @staticmethod
    def get_user_repo() -> IUserRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
            return UserRepositoryMock
        elif Environments.get_envs().stage in [STAGE.PROD, STAGE.DEV, STAGE.HOMOLOG]:
            from src.shared.infra.repositories.user_repository_dynamo import UserRepositoryDynamo
            return UserRepositoryDynamo
        else:
            raise Exception("No repository found for this stage")

    @staticmethod
    def get_user_repo_cognito() -> IUserRepositoryCognito:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.user_repository_cognito_mock import UserRepositoryCognitoMock
            return UserRepositoryCognitoMock
        elif Environments.get_envs().stage in [STAGE.PROD, STAGE.DEV, STAGE.HOMOLOG]:
            from src.shared.infra.repositories.user_repository_cognito import UserRepositoryCognito
            return UserRepositoryCognito
        else:
            raise Exception("No repository found for this stage")


    @staticmethod
    def get_envs() -> "Environments":
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__