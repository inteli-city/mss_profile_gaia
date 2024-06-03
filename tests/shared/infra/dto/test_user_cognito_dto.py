import datetime
from src.shared.infra.dtos.user_cognito_dto import UserCognitoDTO
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserCognitoDTO:

    def test_from_cognito(self):
        data = {
                        'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
                                                             'content-length': '709',
                                                             'content-type': 'application/x-amz-json-1.1',
                                                             'date': 'Sat, 04 Feb 2023 13:45:05 GMT',
                                                             'x-amzn-requestid': '8b8fba2d-b2c7-4346-a441-e285892af0a3'},
                                             'HTTPStatusCode': 200,
                                             'RequestId': '8b8fba2d-b2c7-4346-a441-e285892af0a3',
                                             'RetryAttempts': 0},
                        'UserAttributes': [{'Name': 'custom:general_role', 'Value': 'COLLABORATOR'},
                                           {'Name': 'name', 'Value': 'joao'},
                                           {'Name': 'email', 'Value': 'joao@hotmail.com'},
                                            {'Name': 'sub',
                                        'Value': '123'}
                                           ],
                        'UserCreateDate': datetime.datetime(2023, 2, 3, 23, 27, 48, 713000),
                        'UserLastModifiedDate': datetime.datetime(2023, 2, 3, 23, 27, 48, 713000),
                        'UserStatus': 'UNCONFIRMED',
                        'Enabled': 'true',
                        'Username': 'gabriel@gmail.com'}

        user_cognito_dto = UserCognitoDTO.from_cognito(data)

        expected_dto = UserCognitoDTO(
            user_id="123",
            email="joao@hotmail.com",
            name="joao",
            in_group=False
        )

        assert user_cognito_dto.user_id == expected_dto.user_id
        assert user_cognito_dto.email == expected_dto.email
        assert user_cognito_dto.name == expected_dto.name
        assert user_cognito_dto.in_group == expected_dto.in_group
    
    def test_to_cognito_attributes(self):
        user_cognito_dto = UserCognitoDTO(
            user_id="123",
            email="joao@hotmail.com",
            name="joao",
            in_group=True
        )
        cognito = user_cognito_dto.to_cognito_attributes()

        assert cognito[0]['Name'] == 'email'
        assert cognito[0]['Value'] == 'joao@hotmail.com'
        assert cognito[1]['Name'] == 'name'
        assert cognito[1]['Value'] == 'joao'
        assert len(cognito) == 2