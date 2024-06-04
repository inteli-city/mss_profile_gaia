import pytest
from src.modules.login_user.app.login_user_usecase import LoginUserUsecase
from src.shared.domain.enum.group_enum import GROUP
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, InvalidCredentials
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_LoginUserUsecase:

    def test_login_user_usecase(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        user = usecase(requester_user_id=repo.users_list[1].user_id, name=repo.users_list[1].name, email=repo.users_list[1].email)

        assert user.user_id == repo.users_list[1].user_id
        assert user.email == repo.users_list[1].email
        assert user.name == repo.users_list[1].name
        assert user.department == 'CONVIAS'
        assert user.group == GROUP.USUARIO
        assert user.enabled == True
        assert user.role_dashboard_qualidade == None
        assert user.role_dashboard_deteccao == None
        assert user.role_dashboard_tempo == None
        assert user.role_dashboard_geoinfra == None
        assert user.role_dashboard_recapeamento == None
        assert user.role_dashboard_anel_viario == None
        assert user.role_dashboard_sist_unificado == None
        assert user.role_modfisc_convias == None
        assert user.role_modfisc_osmv == None
        assert user.role_modfisc_osct == None
        assert user.role_modfisc_relatoriomv == None
        assert user.role_modfisc_vistoriapv == None
        assert user.role_modfisc_vistoriarecape == None
        assert user.role_interf_mapa == None
        assert user.role_interf_protproc == None
        assert user.role_drenagem_ativos == None
        assert user.role_drenagem_redes == None
        assert user.role_usuarios == None
        assert user.role_tickets == None
    
    def test_login_user_usecase_create_user(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        user = usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e127', name='Gabriel', email='gabriel@hotmail.com')

        assert user.user_id == 'e73626b5-462d-4a3f-bef5-ae7cbb45e127'
        assert user.email == 'gabriel@hotmail.com'
        assert user.name == 'Gabriel'
        assert user.department == None
        assert user.enabled == True
        assert user.role_dashboard_qualidade == None
        assert user.role_dashboard_deteccao == None
        assert user.role_dashboard_tempo == None
        assert user.role_dashboard_geoinfra == None
        assert user.role_dashboard_recapeamento == None
        assert user.role_dashboard_anel_viario == None
        assert user.role_dashboard_sist_unificado == None
        assert user.role_modfisc_convias == None
        assert user.role_modfisc_osmv == None
        assert user.role_modfisc_osct == None
        assert user.role_modfisc_relatoriomv == None
        assert user.role_modfisc_vistoriapv == None
        assert user.role_modfisc_vistoriarecape == None
        assert user.role_interf_mapa == None
        assert user.role_interf_protproc == None
        assert user.role_drenagem_ativos == None
        assert user.role_drenagem_redes == None
        assert user.role_usuarios == None
        assert user.role_tickets == None
    
    def test_login_user_usecase_not_enabled(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        with pytest.raises(ForbiddenAction):
            usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e457', name='Gabriel', email='gabriel@hotmail.com')
