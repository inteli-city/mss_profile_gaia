import pytest
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.dtos.user_gaia_api_gateway_dto import UserGaiaApiGatewayDTO

class Test_UserApiGatewayDTO:
    
    def test_user_api_gateway_dto_from_api_gateway(self):
        user_data = {
            'sub': 'd61dbf66-a10f-11ed-a8fc-0242ac120002',
            'name': 'Gabriel Godoy',
            'email': 'gabriel.godoy@gmail.com', 
            'cognito:groups': "GAIA,JUNDIAI"
            }

        user_dto = UserGaiaApiGatewayDTO.from_api_gateway(user_data)

        expected_user_dto = UserGaiaApiGatewayDTO(
            user_id = "d61dbf66-a10f-11ed-a8fc-0242ac120002",
            name = "Gabriel Godoy",
            email = "gabriel.godoy@gmail.com",
            )
        
        assert user_dto == expected_user_dto
    
    def test_user_api_gateway_dto_from_api_gateway_gaia_not_in_groups(self):
        user_data = {
            'sub': 'd61dbf66-a10f-11ed-a8fc-0242ac120002',
            'name': 'Gabriel Godoy',
            'email': 'gabriel.godoy@gmail.com', 
            'cognito:groups': "JUNDIAI"
            }

        
        with pytest.raises(ForbiddenAction):
            UserGaiaApiGatewayDTO.from_api_gateway(user_data)