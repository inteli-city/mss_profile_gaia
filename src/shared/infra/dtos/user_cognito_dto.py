from enum import Enum
from typing import List, Optional
from src.shared.domain.entities.user import User

class UserCognitoDTO:
    user_id: str
    name: str
    email: str
    in_group: bool = False

    def __init__(self, user_id: str, email: str, name: str, in_group: bool = False):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.in_group = in_group

    TO_COGNITO_DICT = {
        "email": "email",
        "name": "name",
    }

    FROM_COGNITO_DICT = {value: key for key, value in TO_COGNITO_DICT.items()}
    FROM_COGNITO_DICT["sub"] = "user_id"

    def to_cognito_attributes(self) -> List[dict]:
        user_attributes = []
        for att, name in self.TO_COGNITO_DICT.items():
            value = getattr(self, att)
            if isinstance(value, Enum):  # Verifica se é um enum
                value = value.value  # Obtém o valor do enum
            user_attributes.append(self.parse_attribute(value=value, name=name))
        
        user_attributes = [att for att in user_attributes if att["Value"] != str(None)]

        return user_attributes
    
    @staticmethod
    def from_cognito(data: dict) -> "UserCognitoDTO":
        user_data = next((value for key, value in data.items() if "Attribute" in key), None)
        user_data = {UserCognitoDTO.FROM_COGNITO_DICT[att["Name"]]: att["Value"] for att in user_data if att["Name"] in UserCognitoDTO.FROM_COGNITO_DICT}
        # user_data["created_at"] = data.get("UserCreateDate")
        # user_data["updated_at"] = data.get("UserLastModifiedDate")
        # user_data["status"] = f'{data.get("UserStatus")}'

        print(user_data.get("enabled"))
        return UserCognitoDTO(
            user_id=str(user_data["user_id"]),
            email=str(user_data["email"]),
            name=str(user_data["name"]),
            in_group=False
        )
    
    @staticmethod
    def parse_attribute(name, value) -> dict:
        return {'Name': name, 'Value': str(value)}


