import pytest
from src.modules.get_all_users.app.get_all_users_usecase import GetAllUsersUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllUsersUsecase:
    def test_get_all_users_usecase(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)

        all_users = usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123')

        assert len(all_users) == 3
    
    def test_get_all_users_usecase_requester_user_id_not_found(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e154')
    
    def test_get_all_users_usecase_requester_user_not_allowed_none(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)

        with pytest.raises(ForbiddenAction):
            usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e456')
    
    def test_get_all_users_usecase_not_allowed_false(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)

        with pytest.raises(ForbiddenAction):
            usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e457')
    
    def test_get_all_users_usecase_no_users_found(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)

        repo.users_list = []

        with pytest.raises(NoItemsFound):
            usecase(requester_user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123')
