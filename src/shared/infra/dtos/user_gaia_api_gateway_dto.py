from typing import List

from src.shared.helpers.errors.usecase_errors import ForbiddenAction

class UserGaiaApiGatewayDTO:
    name: str
    email: str
    user_id: str

    def __init__(self, name: str, email:str, user_id: str):
        self.name = name
        self.email = email
        self.user_id = user_id

    @staticmethod
    def from_api_gateway(user_data: dict) -> 'UserGaiaApiGatewayDTO':
        """
        This method is used to convert the user data from the API Gateway to a UserApiGatewayDTO object.
        """
        groups = [group.strip().upper() for group in user_data.get('cognito:groups', '').split(',') if group.strip()]

        if "GAIA" not in groups:
            raise ForbiddenAction('Usuário não esta apto para o sistema')

        return UserGaiaApiGatewayDTO(
            name=user_data['name'],
            email=user_data['email'],
            user_id=user_data['sub'],
        )
    
    def __eq__(self, other):
        return self.name == other.name and self.email == other.email and self.user_id == other.user_id