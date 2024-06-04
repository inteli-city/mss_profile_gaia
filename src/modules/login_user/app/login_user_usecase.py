from src.shared.domain.entities.user import User
from src.shared.domain.enum.group_enum import GROUP
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, InvalidCredentials


class LoginUserUsecase:

    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, requester_user_id: str, name: str, email: str) -> User:

        user = self.repo.get_user_by_id(user_id=requester_user_id)

        if user is not None:
            if not user.enabled:
                raise ForbiddenAction("Usuário desabilitado")
            return user

        user = User(user_id=requester_user_id,name=name, email=email, group=GROUP.USUARIO, enabled=True)
        return self.repo.create_profile(user=user)