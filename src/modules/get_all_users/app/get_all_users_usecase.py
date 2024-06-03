

from typing import List
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class GetAllUsersUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
    
    def __call__(self, requester_user_id: str) -> List[User]:

        user = self.repo.get_user_by_id(user_id=requester_user_id)

        if user is None:
            raise NoItemsFound("Usuário não cadastrado")
                
        if user.role_usuarios is None or not user.role_usuarios:
            raise ForbiddenAction("Usuário não tem acesso a essa funcionalidade")
        
        all_users = self.repo.get_all_users()

        if not all_users:
            raise NoItemsFound("Nenhuma lista de usuários encontrada")
        
        return all_users