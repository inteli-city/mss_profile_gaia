import pytest
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.user_repository_dynamo import UserRepositoryDynamo


class Test_UserRepositoryDb:
    
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_check_user_group(self):
        repo = UserRepositoryDynamo()
        resp = repo.check_user_group(email="gabriel@hotmail.com")
        assert resp == True

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_check_user_group_wrong_email(self):
        repo = UserRepositoryDynamo()
        with pytest.raises(NoItemsFound):
            repo.check_user_group(email="123")

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_user_by_id(self):
        repo = UserRepositoryDynamo()
        user = repo.update_user_by_id(user_id="125fb34e-aacf-4a47-9914-82ea64ff9f32", new_user_data={"name": "User Teste", "department": None})
        assert user.name == "User Teste"
