from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from src.shared.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def create_profile(self, user: User) -> User:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def update_user_by_id(self, user_id: str, new_user_data: dict) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass