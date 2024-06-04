from src.modules.create_user.app.create_user_controller import CreateUserController
from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_cognito_mock import UserRepositoryCognitoMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserController:

    def test_create_user_controller(self):
        repo = UserRepositoryMock()
        cognito_repo = UserRepositoryCognitoMock()
        usecase = CreateUserUsecase(repo=repo, cognito_repo=cognito_repo)

        controller = CreateUserController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
                "name": repo.users_list[0].name,
                "email": repo.users_list[0].email,
                "cognito:groups": "GAIA, JUNDIAI"
            },
            'email': 'gabriel.godoybz@outlook.com',
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'group': 'USUARIO',
            'role_dashboard_qualidade': False,
            'role_dashboard_deteccao': False,
            'role_dashboard_tempo': False,
            'role_dashboard_geoinfra': False,
            'role_dashboard_recapeamento': False,
            'role_dashboard_anel_viario': False,
            'role_dashboard_sist_unificado': False,
            'role_modfisc_convias': False,
            'role_modfisc_osmv': False,
            'role_modfisc_osct': False,
            'role_modfisc_relatoriomv': False,
            'role_modfisc_vistoriapv': False,
            'role_modfisc_vistoriarecape': False,
            'role_interf_mapa': False,
            'role_interf_protproc': False,
            'role_drenagem_ativos': False,
            'role_drenagem_redes': False,
            'role_usuarios': False,
            'role_tickets': False,
        })

        response = controller(data)

        assert response.status_code == 200
        assert response.body["user"]['user_id'] == "e73626b5-462d-4a3f-bef5-ae7cbb45e458"
        assert response.body["user"]['email'] == "gabriel.godoybz@outlook.com"
        assert response.body["user"]['name'] == "User Teste"
        assert response.body["user"]['department'] == "INTELICITY"
        assert response.body["user"]['group'] == "USUARIO"
        assert response.body["user"]['role_dashboard_qualidade'] == False
        assert response.body["user"]['role_dashboard_deteccao'] == False
        assert response.body["user"]['role_dashboard_tempo'] == False
        assert response.body["user"]['role_dashboard_geoinfra'] == False
        assert response.body["user"]['role_dashboard_recapeamento'] == False
        assert response.body["user"]['role_dashboard_anel_viario'] == False
        assert response.body["user"]['role_dashboard_sist_unificado'] == False
        assert response.body["user"]['role_modfisc_convias'] == False
        assert response.body["user"]['role_modfisc_osmv'] == False
        assert response.body["user"]['role_modfisc_osct'] == False
        assert response.body["user"]['role_modfisc_relatoriomv'] == False
        assert response.body["user"]['role_modfisc_vistoriapv'] == False
        assert response.body["user"]['role_modfisc_vistoriarecape'] == False
        assert response.body["user"]['role_interf_mapa'] == False
        assert response.body["user"]['role_interf_protproc'] == False
        assert response.body["user"]['role_drenagem_ativos'] == False
        assert response.body["user"]['role_drenagem_redes'] == False
        assert response.body["user"]['role_usuarios'] == False
        assert response.body["user"]['role_tickets'] == False
        