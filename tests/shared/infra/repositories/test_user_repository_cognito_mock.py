from src.shared.infra.repositories.user_repository_cognito_mock import UserRepositoryCognitoMock


class Test_UserRepositoryCognitoMock:

    def test_in_gaia_group(self):
        user_repository = UserRepositoryCognitoMock()
        in_group = user_repository.in_gaia_group("gabriel@hotmail.com")

        assert in_group is True
    
    def test_get_user_by_email(self):
        user_repository = UserRepositoryCognitoMock()
        user = user_repository.get_user_by_email("gabriel@hotmail.com")

        assert user.email == "gabriel@hotmail.com"
        assert user.name == "User Gabriel"
        assert user.user_id == "e73626b5-462d-4a3f-bef5-ae7cbb45e123"
        assert user.in_group is True

    def test_create_user(self):
        user_repository = UserRepositoryCognitoMock()
        user = user_repository.create_user(email="gabriel@outlook.com", name="User 2")

        assert user.email == "gabriel@outlook.com"
        assert user.name == "User 2"
        assert user.user_id == "e73626b5-462d-4a3f-bef5-ae7cbb45e458"
        assert user.in_group is False
        assert len(user_repository.users) == 4

    def test_add_user_to_group(self):
        user_repository = UserRepositoryCognitoMock()
        user_repository.add_user_to_group("gabriel123@gmail.com")

        assert user_repository.users[1].in_group is True


        