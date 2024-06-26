from typing import List, Optional
from src.shared.domain.entities.user import User
from src.shared.domain.enum.group_enum import GROUP
from src.shared.domain.enum.role_recape_enum import ROLE_RECAPE
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class UserRepositoryMock(IUserRepository):

    users: List[User]

    def __init__(self):
        self.users_list = [
             User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123", email="gabriel@hotmail.com", name='Gabriel', enabled=True, group=GROUP.USUARIO, department='INTELICITY', role_dashboard_qualidade=True, role_dashboard_deteccao=True, role_dashboard_tempo=True, role_dashboard_geoinfra=True, role_dashboard_recapeamento=True, role_dashboard_anel_viario=True, role_dashboard_sist_unificado=True, role_modfisc_convias=True, role_modfisc_osmv=True, role_modfisc_osct=True, role_modfisc_relatoriomv=True, role_modfisc_vistoriapv=True, role_modfisc_vistoriarecape=True, role_interf_mapa=True, role_interf_protproc=True, role_drenagem_ativos=True, role_drenagem_redes=True, role_usuarios=True, role_tickets=True, role_recape=ROLE_RECAPE.ADMIN),
             User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e456", email="gabriel.godoybz@gmail.com", name='Gabriel', group=GROUP.USUARIO, department='CONVIAS', enabled=True,),
             User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e457", email="gabriel.godoybz@hotmail.com", name='Gabriel', group=GROUP.USUARIO, department='CONVIAS', enabled=False, role_tickets=False),
        ]
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        for user in self.users_list:
            if user_id == user.user_id:
                return user
        return None
    
    def get_all_users(self) -> List[User]:
        if len(self.users_list) > 0:
            return self.users_list
        else:
            return None
    
    def create_profile(self, user: User) -> User:
        self.users_list.append(user)
        return user
    
    def update_user_by_id(self, user_id: str, new_user_data: dict) -> User:
        for index, userx in enumerate(self.users_list):
            if userx.user_id == user_id:
                for key, value in new_user_data.items():
                    setattr(userx, key, value)
                return userx
        return None