from abc import ABC

from src.shared.infra.dtos.user_cognito_dto import UserCognitoDTO


class IUserRepositoryCognito(ABC):

    def in_gaia_group(self, email: str) -> bool:
        pass

    def get_user_by_email(self, email: str) -> UserCognitoDTO:
        pass

    def create_user(self, email: str, name: str) -> UserCognitoDTO:
        pass

    def add_user_to_group(self, user_email: str) -> None:
        pass

