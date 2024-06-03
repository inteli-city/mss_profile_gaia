from typing import Optional
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnecessaryUpdate


class UpdateUserUsecase:
    
    def __init__(self, repo: IUserRepository):
        self.repo = repo
        self.mutable_fields = ['name', 'department', 'enabled', 'role_dashboard_qualidade', 'role_dashboard_deteccao', 'role_dashboard_tempo', 'role_dashboard_geoinfra', 'role_dashboard_recapeamento', 'role_dashboard_anel_viario', 'role_dashboard_sist_unificado', 'role_modfisc_convias', 'role_modfisc_osmv', 'role_modfisc_osct', 'role_modfisc_relatoriomv', 'role_modfisc_vistoriapv', 'role_modfisc_vistoriarecape', 'role_interf_mapa', 'role_interf_protproc', 'role_drenagem_ativos', 'role_drenagem_redes', 'role_usuarios', 'role_tickets']

    def __call__(self, requester_user_id: str, 
                    user_id: str, 
                    new_user_data: dict,
                 ) -> User:
        
        requester_user = self.repo.get_user_by_id(user_id=requester_user_id)

        if requester_user is None:
            raise NoItemsFound("Usuário não cadastrado")
                        
        if requester_user.role_usuarios is None or not requester_user.role_usuarios:
            raise ForbiddenAction("Usuário não tem acesso a essa funcionalidade")
        
        old_user = self.repo.get_user_by_id(user_id=user_id)

        if old_user is None:
            raise NoItemsFound("Usuário a ser atualizado não encontrado")
        
        old_user_data = User.to_dict(old_user)
        
         # Atualiza apenas os campos que estão em mutable_fields
        kvp_to_update = {k: v for k, v in new_user_data.items() if k in self.mutable_fields}

        # Atualiza os campos vazios para None
        for k, v in kvp_to_update.items():
            kvp_to_update[k] = v if v != "" else None

        # Converte valores booleanos representados como strings em valores booleanos reais
        bool_items = [User.__annotations__[k] for k in self.mutable_fields if User.__annotations__[k] == bool]
        kvp_to_update = {k: eval(v.title()) if User.__annotations__[k] in bool_items and type(v) == str else v for k, v in kvp_to_update.items()}

        # Converte todos os valores para string
        # kvp_to_update = {k: str(v) for k, v in kvp_to_update.items()}

        # Realiza a atualização do usuário
        return self.repo.update_user_by_id(user_id=user_id, new_user_data=kvp_to_update)