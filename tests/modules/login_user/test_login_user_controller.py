from src.modules.login_user.app.login_user_controller import LoginUserController
from src.modules.login_user.app.login_user_usecase import LoginUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_LoginUserController:
    def test_login_user_controller(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        controller = LoginUserController(usecase)

        request = HttpRequest(body={"requester_user": {
                "sub": repo.users_list[1].user_id,
                "name": repo.users_list[1].name,
                "email": repo.users_list[1].email,
                "cognito:groups": "GAIA, JUNDIAI"
            },
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["user"]["user_id"] == repo.users_list[1].user_id
        assert response.body["user"]["email"] == repo.users_list[1].email
        assert response.body["user"]["name"] == repo.users_list[1].name
        assert response.body["user"]["enabled"] == True
        assert response.body["user"]["department"] == 'CONVIAS'
        assert response.body["user"]["role_dashboard_qualidade"] == None
        assert response.body["user"]["role_dashboard_deteccao"] == None
        assert response.body["user"]["role_dashboard_tempo"] == None
        assert response.body["user"]["role_dashboard_geoinfra"] == None
        assert response.body["user"]["role_dashboard_recapeamento"] == None
        assert response.body["user"]["role_dashboard_anel_viario"] == None
        assert response.body["user"]["role_dashboard_sist_unificado"] == None
        assert response.body["user"]["role_modfisc_convias"] == None
        assert response.body["user"]["role_modfisc_osmv"] == None
        assert response.body["user"]["role_modfisc_osct"] == None
        assert response.body["user"]["role_modfisc_relatoriomv"] == None
        assert response.body["user"]["role_modfisc_vistoriapv"] == None
        assert response.body["user"]["role_modfisc_vistoriarecape"] == None
        assert response.body["user"]["role_interf_mapa"] == None
        assert response.body["user"]["role_interf_protproc"] == None
        assert response.body["user"]["role_drenagem_ativos"] == None
        assert response.body["user"]["role_drenagem_redes"] == None
        assert response.body["user"]["role_usuarios"] == None
        assert response.body["user"]["role_tickets"] == None
        assert response.body["message"] == "Login realizado com sucesso!"
    
    def test_login_user_controller_no_requester_user(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)
        controller = LoginUserController(usecase)

        request = HttpRequest(body={})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: requester_user"
    
    def test_login_user_controller_user_not_in_gaia(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        controller = LoginUserController(usecase)

        request = HttpRequest(body={"requester_user": {
                "sub": repo.users_list[0].user_id,
                "name": repo.users_list[0].name,
                "email": repo.users_list[0].email,
                "cognito:groups": "JUNDIAI"
            },
        })

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "Ação não permitida: Usuário não esta apto para o sistema"