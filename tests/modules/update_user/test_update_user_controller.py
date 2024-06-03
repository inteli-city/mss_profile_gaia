from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.modules.update_user.app.update_user_controller import UpdateUserController
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserController:

    def test_update_user_controller(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
                "name": repo.users_list[0].name,
                "email": repo.users_list[0].email,
                "cognito:groups": "GAIA, JUNDIAI"
            },
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
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
        assert response.body["user"]["user_id"] == "e73626b5-462d-4a3f-bef5-ae7cbb45e123"
        assert response.body["user"]["email"] == repo.users_list[0].email
        assert response.body["user"]["name"] == 'User Teste'
        assert response.body["user"]["enabled"] == False
        assert response.body["user"]["department"] == 'INTELICITY'
        assert response.body["user"]["role_dashboard_qualidade"] == False
        assert response.body["user"]["role_dashboard_deteccao"] == False
        assert response.body["user"]["role_dashboard_tempo"] == False
        assert response.body["user"]["role_dashboard_geoinfra"] == False
        assert response.body["user"]["role_dashboard_recapeamento"] == False
        assert response.body["user"]["role_dashboard_anel_viario"] == False
        assert response.body["user"]["role_dashboard_sist_unificado"] == False
        assert response.body["user"]["role_modfisc_convias"] == False
        assert response.body["user"]["role_modfisc_osmv"] == False
        assert response.body["user"]["role_modfisc_osct"] == False
        assert response.body["user"]["role_modfisc_relatoriomv"] == False
        assert response.body["user"]["role_modfisc_vistoriapv"] == False
        assert response.body["user"]["role_modfisc_vistoriarecape"] == False
        assert response.body["user"]["role_interf_mapa"] == False
        assert response.body["user"]["role_interf_protproc"] == False
        assert response.body["user"]["role_drenagem_ativos"] == False
        assert response.body["user"]["role_drenagem_redes"] == False
        assert response.body["user"]["role_usuarios"] == False
        assert response.body["user"]["role_tickets"] == False
        assert response.body['message'] == 'Usuário atualizado com sucesso!'
    
    def test_update_user_controller_dont_change_with_params_not_in_json(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
                "name": repo.users_list[0].name,
                "email": repo.users_list[0].email,
                "cognito:groups": "GAIA, JUNDIAI"
            },
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'name': 'User Teste',
            'enabled': False,
            'department': None,
            'role_interf_protproc': False,
        })

        response = controller(data)

        assert response.status_code == 200
        assert response.body["user"]["user_id"] == "e73626b5-462d-4a3f-bef5-ae7cbb45e123"
        assert response.body["user"]["email"] == repo.users_list[0].email
        assert response.body["user"]["name"] == 'User Teste'
        assert response.body["user"]["enabled"] == False
        assert response.body["user"]["department"] == None
        assert response.body["user"]["role_dashboard_qualidade"] == True
        assert response.body["user"]["role_dashboard_deteccao"] == True
        assert response.body["user"]["role_dashboard_tempo"] == True
        assert response.body["user"]["role_dashboard_geoinfra"] == True
        assert response.body["user"]["role_dashboard_recapeamento"] == True
        assert response.body["user"]["role_dashboard_anel_viario"] == True
        assert response.body["user"]["role_dashboard_sist_unificado"] == True
        assert response.body["user"]["role_modfisc_convias"] == True
        assert response.body["user"]["role_modfisc_osmv"] == True
        assert response.body["user"]["role_modfisc_osct"] == True
        assert response.body["user"]["role_modfisc_relatoriomv"] == True
        assert response.body["user"]["role_modfisc_vistoriapv"] == True
        assert response.body["user"]["role_modfisc_vistoriarecape"] == True
        assert response.body["user"]["role_interf_mapa"] == True
        assert response.body["user"]["role_interf_protproc"] == False
        assert response.body["user"]["role_drenagem_ativos"] == True
        assert response.body["user"]["role_drenagem_redes"] == True
        assert response.body["user"]["role_usuarios"] == True
        assert response.body["user"]["role_tickets"] == True
        assert response.body['message'] == 'Usuário atualizado com sucesso!'
    
    def test_update_user_controller_with_null_params(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
                "name": repo.users_list[0].name,
                "email": repo.users_list[0].email,
                "cognito:groups": "GAIA, JUNDIAI"
            },
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'name': 'User Teste',
            'enabled': False,
            'department': None,
            'role_dashboard_qualidade': None,
            'role_dashboard_deteccao': None,
            'role_dashboard_tempo': None,
            'role_dashboard_geoinfra': None,
            'role_dashboard_recapeamento': None,
            'role_dashboard_anel_viario': None,
            'role_dashboard_sist_unificado': None,
            'role_modfisc_convias': None,
            'role_modfisc_osmv': None,
            'role_modfisc_osct': None,
            'role_modfisc_relatoriomv': None,
            'role_modfisc_vistoriapv': None,
            'role_modfisc_vistoriarecape': None,
            'role_interf_mapa': None,
            'role_interf_protproc': None,
            'role_drenagem_ativos': None,
            'role_drenagem_redes': None,
            'role_usuarios': None,
            'role_tickets': None,
            
        })

        response = controller(data)

        assert response.status_code == 200
        assert response.body["user"]["user_id"] == "e73626b5-462d-4a3f-bef5-ae7cbb45e123"
        assert response.body["user"]["email"] == repo.users_list[0].email
        assert response.body["user"]["name"] == 'User Teste'
        assert response.body["user"]["enabled"] == False
        assert response.body["user"]["department"] == None
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
        assert response.body['message'] == 'Usuário atualizado com sucesso!'
    
    def test_update_user_controller_no_requester_user(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)
        controller = UpdateUserController(usecase)

        request = HttpRequest(body={})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: requester_user"

    def test_update_user_controller_user_not_in_gaia(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

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
    
    def test_update_user_controller_missing_user_id(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
                "name": repo.users_list[0].name,
                "email": repo.users_list[0].email,
                "cognito:groups": "GAIA, JUNDIAI"
            },
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: user_id'
    
    def test_update_user_controller_missing_no_user_to_update_found(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
                "name": repo.users_list[0].name,
                "email": repo.users_list[0].email,
                "cognito:groups": "GAIA, JUNDIAI"
            },
            'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e198',
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
        })

        response = controller(data)
        
        assert response.status_code == 404
        assert response.body == 'Usuário a ser atualizado não encontrado'