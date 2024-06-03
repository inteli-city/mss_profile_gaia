from src.modules.get_all_users.app.get_all_users_controller import GetAllUsersController
from src.modules.get_all_users.app.get_all_users_usecase import GetAllUsersUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllUsersController:
    
    def test_get_all_users_controller(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)
        controller = GetAllUsersController(usecase)

        request = HttpRequest(body={"requester_user": {
                "sub": 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
                "name": repo.users_list[0].name,
                "email": repo.users_list[0].email,
                "cognito:groups": "GAIA, JUNDIAI"
            },
            })

        response = controller(request)

        assert response.status_code == 200
        assert len(response.body['user_list']) == 3
        assert response.body['message'] == 'Usuários retornados com sucesso!'
    
    def test_get_all_users_controller_no_requester_user(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)
        controller = GetAllUsersController(usecase)

        request = HttpRequest(body={})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: requester_user"
    
    def test_get_all_users_controller_user_not_in_gaia(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)

        controller = GetAllUsersController(usecase)

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
    