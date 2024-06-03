from typing import List
from src.shared.domain.repositories.user_repository_cognito_interface import IUserRepositoryCognito
from src.shared.infra.dtos.user_cognito_dto import UserCognitoDTO


class UserRepositoryCognitoMock(IUserRepositoryCognito):

    users: List[UserCognitoDTO]

    def __init__(self):
        self.users = [
            UserCognitoDTO(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123", name="User Gabriel", email="gabriel@hotmail.com", in_group=True),
            UserCognitoDTO(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e459", name="User Gabriel", email="gabriel123@gmail.com", in_group=False),
            UserCognitoDTO(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e460", name="User Gabriel", email="gabriel123@outlook.com", in_group=True),
        ]
    
    def in_gaia_group(self, email: str) -> bool:
        for user in self.users:
            if email == user.email:
                return user.in_group
        return False
    
    def get_user_by_email(self, email: str) -> UserCognitoDTO:
        for user in self.users:
            if email == user.email:
                return user
        return None
    
    def create_user(self, email: str, name: str) -> UserCognitoDTO:
        user = UserCognitoDTO(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e458", name=name, email=email, in_group=False)
        self.users.append(user)
        return user
    
    def add_user_to_group(self, user_email: str) -> None:
        for user in self.users:
            if user_email == user.email:
                user.in_group = True
                return None
        return None