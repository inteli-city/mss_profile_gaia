import pytest
from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.user_repository_cognito_mock import UserRepositoryCognitoMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserUsecase:

    def test_create_user_usecase_requester_user_none(self):
        repo = UserRepositoryMock()
        cognito_repo = UserRepositoryCognitoMock()

        usecase = CreateUserUsecase(repo=repo, cognito_repo=cognito_repo)

        with pytest.raises(NoItemsFound):
            user = usecase(
                requester_user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e199",
                email="gabriel123@outlook.com",
                name="Gabriel",
                department="INTELICITY",
            )
    
    def test_create_user_usecase_requester_user_role_usuarios_not_trues(self):
        repo = UserRepositoryMock()
        cognito_repo = UserRepositoryCognitoMock()

        usecase = CreateUserUsecase(repo=repo, cognito_repo=cognito_repo)

        with pytest.raises(ForbiddenAction):
            user = usecase(
                requester_user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e456",
                email="gabriel123@outlook.com",
                name="Gabriel",
                department="INTELICITY",
            )
    
    def test_create_user_usecase_requester_user_not_enabled(self):
        repo = UserRepositoryMock()
        cognito_repo = UserRepositoryCognitoMock()

        usecase = CreateUserUsecase(repo=repo, cognito_repo=cognito_repo)

        with pytest.raises(ForbiddenAction):
            user = usecase(
                requester_user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e457",
                email="gabriel123@outlook.com",
                name="Gabriel",
                department="INTELICITY",
            )

    def test_create_user_usecase_not_in_cognito(self):
        repo = UserRepositoryMock()
        cognito_repo = UserRepositoryCognitoMock()

        usecase = CreateUserUsecase(repo=repo, cognito_repo=cognito_repo)

        user = usecase(
            requester_user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            email="gabriel.godoybz@outlook.com",
            name="Gabriel",
            department="INTELICITY",
            role_dashboard_qualidade=True,
            role_dashboard_deteccao=True,
            role_dashboard_tempo=True,
            role_dashboard_geoinfra=True,
            role_dashboard_recapeamento=True,
            role_dashboard_anel_viario=True,
            role_dashboard_sist_unificado=True,
            role_modfisc_convias=True,
            role_modfisc_osmv=True,
            role_modfisc_osct=True,
            role_modfisc_relatoriomv=True,
            role_modfisc_vistoriapv=True,
            role_modfisc_vistoriarecape=True,
            role_interf_mapa=True,
            role_interf_protproc=True,
            role_drenagem_ativos=True,
            role_drenagem_redes=True,
            role_usuarios=True,
            role_tickets=True,
        )

        assert user.user_id == "e73626b5-462d-4a3f-bef5-ae7cbb45e458"
        assert user.email == "gabriel.godoybz@outlook.com"
        assert user.name == "Gabriel"
        assert user.department == "INTELICITY"
        assert user.role_dashboard_qualidade == True
        assert user.role_dashboard_deteccao == True
        assert user.role_dashboard_tempo == True
        assert user.role_dashboard_geoinfra == True
        assert user.role_dashboard_recapeamento == True
        assert user.role_dashboard_anel_viario == True
        assert user.role_dashboard_sist_unificado == True
        assert user.role_modfisc_convias == True
        assert user.role_modfisc_osmv == True
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
        assert repo.users_list[3].user_id == "e73626b5-462d-4a3f-bef5-ae7cbb45e458"
        assert cognito_repo.users[3].user_id == "e73626b5-462d-4a3f-bef5-ae7cbb45e458"

    def test_create_user_usecase_in_cognito(self):
        repo = UserRepositoryMock()
        cognito_repo = UserRepositoryCognitoMock()

        usecase = CreateUserUsecase(repo=repo, cognito_repo=cognito_repo)

        user = usecase(
            requester_user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            email="gabriel123@outlook.com",
            name="Gabriel",
            department="INTELICITY",
        )

        assert user.user_id == "e73626b5-462d-4a3f-bef5-ae7cbb45e460"
        assert user.email == "gabriel123@outlook.com"
        assert user.name == "User Gabriel"
        assert user.enabled == True
        assert user.department == "INTELICITY"
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
    
    def test_create_user_usecase_in_cognito_but_not_in_group(self):
        repo = UserRepositoryMock()
        cognito_repo = UserRepositoryCognitoMock()

        usecase = CreateUserUsecase(repo=repo, cognito_repo=cognito_repo)

        user = usecase(
            requester_user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            email="gabriel123@gmail.com",
            name="Gabriel",
            department="INTELICITY",
        )

        assert user.user_id == "e73626b5-462d-4a3f-bef5-ae7cbb45e459"
        assert user.email == "gabriel123@gmail.com"
        assert user.name == "User Gabriel"
        assert user.enabled == True
        assert user.department == "INTELICITY"
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
    
    def test_create_user_usecase_in_cognito_and_gaia(self):
        repo = UserRepositoryMock()
        cognito_repo = UserRepositoryCognitoMock()

        usecase = CreateUserUsecase(repo=repo, cognito_repo=cognito_repo)

        user = usecase(
            requester_user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            email="gabriel@hotmail.com",
            name="Gabriel",
            department="INTELICITY",
        )

        assert user.user_id == "e73626b5-462d-4a3f-bef5-ae7cbb45e123"
        assert user.email == "gabriel@hotmail.com"
        assert user.name == "Gabriel"
        assert user.enabled == True
        assert user.department == "INTELICITY"
        assert user.role_dashboard_qualidade == True
        assert user.role_dashboard_deteccao == True
        assert user.role_dashboard_tempo == True
        assert user.role_dashboard_geoinfra == True
        assert user.role_dashboard_recapeamento == True
        assert user.role_dashboard_anel_viario == True
        assert user.role_dashboard_sist_unificado == True
        assert user.role_modfisc_convias == True
        assert user.role_modfisc_osmv == True
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