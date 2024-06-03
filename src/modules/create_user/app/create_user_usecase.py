from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_cognito_interface import IUserRepositoryCognito
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class CreateUserUsecase:
    def __init__(self, repo: IUserRepository, cognito_repo: IUserRepositoryCognito):
        self.repo = repo
        self.cognito_repo = cognito_repo
    
    def __call__(self, 
                requester_user_id: str,
                email: str, 
                name: str, 
                department: str, 
                role_dashboard_qualidade: bool = None, 
                role_dashboard_deteccao: bool = None,
                role_dashboard_tempo: bool = None,
                role_dashboard_geoinfra: bool = None,
                role_dashboard_recapeamento: bool = None,
                role_dashboard_anel_viario: bool = None,
                role_dashboard_sist_unificado: bool = None,
                role_modfisc_convias: bool = None,
                role_modfisc_osmv: bool = None,
                role_modfisc_osct: bool = None,
                role_modfisc_relatoriomv: bool = None,
                role_modfisc_vistoriapv: bool = None,
                role_modfisc_vistoriarecape: bool = None,
                role_interf_mapa: bool = None,
                role_interf_protproc: bool = None,
                role_drenagem_ativos: bool = None,
                role_drenagem_redes: bool = None,
                role_usuarios: bool = None,
                role_tickets: bool = None,
            ) -> User:
        
        # valida se requester esta autorizado

        requester_user = self.repo.get_user_by_id(user_id=requester_user_id)

        if requester_user is None:
            raise NoItemsFound('Usuário não encontrado')
        if not requester_user.role_usuarios:
            raise ForbiddenAction('Usuário não tem permissão')
        if not requester_user.enabled:
            raise ForbiddenAction('Usuário desabilitado')

        user_cognito = self.cognito_repo.get_user_by_email(email=email)

        if user_cognito is not None:
            if not user_cognito.in_group:
                self.cognito_repo.add_user_to_group(user_email=user_cognito.email)
                user_cognito.in_group = True
        else:
            user_cognito = self.cognito_repo.create_user(email=email, name=name)
        
        user_to_create = User(
                user_id=user_cognito.user_id,
                email=user_cognito.email,
                name=user_cognito.name,
                enabled=True,
                department=department,
                role_dashboard_qualidade=role_dashboard_qualidade,
                role_dashboard_deteccao=role_dashboard_deteccao,
                role_dashboard_tempo=role_dashboard_tempo,
                role_dashboard_geoinfra=role_dashboard_geoinfra,
                role_dashboard_recapeamento=role_dashboard_recapeamento,
                role_dashboard_anel_viario=role_dashboard_anel_viario,
                role_dashboard_sist_unificado=role_dashboard_sist_unificado,
                role_modfisc_convias=role_modfisc_convias,
                role_modfisc_osmv=role_modfisc_osmv,
                role_modfisc_osct=role_modfisc_osct,
                role_modfisc_relatoriomv=role_modfisc_relatoriomv,
                role_modfisc_vistoriapv=role_modfisc_vistoriapv,
                role_modfisc_vistoriarecape=role_modfisc_vistoriarecape,
                role_interf_mapa=role_interf_mapa,
                role_interf_protproc=role_interf_protproc,
                role_drenagem_ativos=role_drenagem_ativos,
                role_drenagem_redes=role_drenagem_redes,
                role_usuarios=role_usuarios,
                role_tickets=role_tickets,
            )

        user = self.repo.get_user_by_id(user_id=user_cognito.user_id)
        
        if user is None:
            user = self.repo.create_profile(user=user_to_create)

        return user