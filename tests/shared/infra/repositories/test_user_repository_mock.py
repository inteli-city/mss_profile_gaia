import pytest
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:
    
    def test_get_user_by_id(self):
        repo = UserRepositoryMock()
        user = repo.get_user_by_id(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123')

        assert user.name == 'Gabriel'
        assert type(user) == User
    
    def test_get_user_by_id_not_found(self):
        repo = UserRepositoryMock()
        user = repo.get_user_by_id(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e435')

        assert user == None
    
    def test_get_all_users(self):
        repo = UserRepositoryMock()
        users = repo.get_all_users()

        assert type(users[0]) == User
        assert type(users) == list
        assert users[0].name == 'Gabriel'
        assert len(users) == 3
    
    def test_get_all_users_empty(self):
        repo = UserRepositoryMock()
        repo.users_list = []
        users = repo.get_all_users()

        assert users == None
    
    def test_create_profile(self):
        repo = UserRepositoryMock()
        user_to_create = User(
            user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            email="gabriel.godoybz@gmail.com",
            name="User Teste",
            enabled=True,
        )
        user = repo.create_profile(
                user=user_to_create
        )

        assert user.name == 'User Teste'
        assert user.enabled == True
    
    def test_update_user(self):
        repo = UserRepositoryMock()
        repo.update_user_by_id(
                user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            new_user_data={
                "enabled": False,
                "name": "User Teste",
                "department": 'Teste',
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

        assert repo.users_list[0].name == 'User Teste'
        assert repo.users_list[0].enabled == False
        assert repo.users_list[0].department == 'Teste'
        assert repo.users_list[0].role_dashboard_qualidade == False
        assert repo.users_list[0].role_dashboard_deteccao == False
        assert repo.users_list[0].role_dashboard_tempo == False
        assert repo.users_list[0].role_dashboard_geoinfra == False
        assert repo.users_list[0].role_dashboard_recapeamento == False
        assert repo.users_list[0].role_dashboard_anel_viario == False
        assert repo.users_list[0].role_dashboard_sist_unificado == False
        assert repo.users_list[0].role_modfisc_convias == False
        assert repo.users_list[0].role_modfisc_osmv == False
        assert repo.users_list[0].role_modfisc_osct == False
        assert repo.users_list[0].role_modfisc_relatoriomv == False
        assert repo.users_list[0].role_modfisc_vistoriapv == False
        assert repo.users_list[0].role_modfisc_vistoriarecape == False
        assert repo.users_list[0].role_interf_mapa == False
        assert repo.users_list[0].role_interf_protproc == False
        assert repo.users_list[0].role_drenagem_ativos == False
        assert repo.users_list[0].role_drenagem_redes == False
        assert repo.users_list[0].role_usuarios == False
        assert repo.users_list[0].role_tickets == False

    def test_update_user_non_exists(self):
        repo = UserRepositoryMock()

        user = repo.update_user_by_id(
                user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e167",
            new_user_data={
                "enabled": False,
                "name": "User Teste",
                "department": 'Teste',
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

        assert user == None