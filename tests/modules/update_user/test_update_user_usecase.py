import pytest
from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserUsecase:
    def test_update_user_usecase(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        user = usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123', 
                        user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123', 
                        new_user_data={
                            "name": "User Teste",
                            "enabled": False,
                            "department": "INTELICITY",
                            "role_dashboard_qualidade": False,
                            "role_dashboard_deteccao": False,
                            "role_dashboard_tempo": False,
                            "role_dashboard_geoinfra": False,
                            "role_dashboard_recapeamento": False,
                            "role_dashboard_anel_viario": False,
                            "role_dashboard_sist_unificado": False,
                            "role_modfisc_convias": False,
                            "role_modfisc_osmv": False,
                            "role_modfisc_osct": False,
                            "role_modfisc_relatoriomv": False,
                            "role_modfisc_vistoriapv": False,
                            "role_modfisc_vistoriarecape": False,
                            "role_interf_mapa": False,
                            "role_interf_protproc": False,
                            "role_drenagem_ativos": False,
                            "role_drenagem_redes": False,
                            "role_usuarios": False,
                            "role_tickets": False
                        }
                    )

        assert user.email == 'gabriel@hotmail.com'
        assert user.name == 'User Teste'
        assert user.enabled == False
        assert user.department == 'INTELICITY'
        assert user.role_dashboard_qualidade == False
        assert user.role_dashboard_deteccao == False
        assert user.role_dashboard_tempo == False
        assert user.role_dashboard_geoinfra == False
        assert user.role_dashboard_recapeamento == False
        assert user.role_dashboard_anel_viario == False
        assert user.role_dashboard_sist_unificado == False
        assert user.role_modfisc_convias == False
        assert user.role_modfisc_osmv == False
        assert user.role_modfisc_osct == False
        assert user.role_modfisc_relatoriomv == False
        assert user.role_modfisc_vistoriapv == False
        assert user.role_modfisc_vistoriarecape == False
        assert user.role_interf_mapa == False
        assert user.role_interf_protproc == False
        assert user.role_drenagem_ativos == False
        assert user.role_drenagem_redes == False
        assert user.role_usuarios == False
        assert user.role_tickets == False
    
    def test_update_user_with_none_fields(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        user = usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123', 
                        user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123', 
                        new_user_data={
                            "name": "User Teste",
                            "enabled": False,
                            "department": None,
                            "role_dashboard_qualidade": None,
                            "role_dashboard_deteccao": None,
                            "role_dashboard_tempo": None,
                            "role_dashboard_geoinfra": None,
                            "role_dashboard_recapeamento": None,
                            "role_dashboard_anel_viario": None,
                            "role_dashboard_sist_unificado": None,
                            "role_modfisc_convias": None,
                            "role_modfisc_osmv": None
                        }
                    )

        assert user.email == 'gabriel@hotmail.com'
        assert user.name == 'User Teste'
        assert user.enabled == False
        assert user.department == None
        assert user.role_dashboard_qualidade == None
        assert user.role_dashboard_deteccao == None
        assert user.role_dashboard_tempo == None
        assert user.role_dashboard_geoinfra == None
        assert user.role_dashboard_recapeamento == None
        assert user.role_dashboard_anel_viario == None
        assert user.role_dashboard_sist_unificado == None
        assert user.role_modfisc_convias == None
        assert user.role_modfisc_osmv == None
        assert user.role_modfisc_osct == True
        assert user.role_modfisc_relatoriomv == True
        assert user.role_modfisc_vistoriapv == True
        assert user.role_modfisc_vistoriarecape == True
        assert user.role_interf_mapa == True
        assert user.role_interf_protproc == True
        assert user.role_drenagem_ativos == True
        assert user.role_drenagem_redes == True
        assert user.role_usuarios == True
        assert user.role_tickets == True

    
    def test_update_user_usecase_requester_user_id_not_found(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e254', user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e456', new_user_data={})
    
    def test_update_user_usecase_requester_user_not_allowed_none(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        with pytest.raises(ForbiddenAction):
            usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e456', user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e456', new_user_data={})
    
    def test_update_user_usecase_not_allowed_false(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        with pytest.raises(ForbiddenAction):
            usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e457', user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e456', new_user_data={})
    
    def test_update_user_usecase_user_to_update_not_found(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123', user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e198', new_user_data={})