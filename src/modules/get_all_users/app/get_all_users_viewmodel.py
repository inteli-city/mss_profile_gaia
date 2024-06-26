from typing import List, Optional

from src.shared.domain.entities.user import User
from src.shared.domain.enum.group_enum import GROUP
from src.shared.domain.enum.role_recape_enum import ROLE_RECAPE


class UserViewmodel:
    user_id: str
    email: str
    name: str
    enabled: bool
    group: GROUP
    department: str
    role_dashboard_qualidade: bool = None
    role_dashboard_deteccao: bool = None
    role_dashboard_tempo: bool = None
    role_dashboard_geoinfra: bool = None
    role_dashboard_recapeamento: bool = None
    role_dashboard_anel_viario: bool = None
    role_dashboard_sist_unificado: bool = None
    role_modfisc_convias: bool = None
    role_modfisc_osmv: bool = None
    role_modfisc_osct: bool = None
    role_modfisc_relatoriomv: bool = None
    role_modfisc_vistoriapv: bool = None
    role_modfisc_vistoriarecape: bool = None
    role_interf_mapa: bool = None
    role_interf_protproc: bool = None
    role_drenagem_ativos: bool = None
    role_drenagem_redes: bool = None
    role_usuarios: bool = None
    role_tickets: bool = None
    role_recape: ROLE_RECAPE = None

    def __init__(self, user: User):
        self.user_id = user.user_id
        self.email = user.email
        self.name = user.name
        self.enabled = user.enabled
        self.group = user.group
        self.department = user.department
        self.role_dashboard_qualidade = user.role_dashboard_qualidade
        self.role_dashboard_deteccao = user.role_dashboard_deteccao
        self.role_dashboard_tempo = user.role_dashboard_tempo
        self.role_dashboard_geoinfra = user.role_dashboard_geoinfra
        self.role_dashboard_recapeamento = user.role_dashboard_recapeamento
        self.role_dashboard_anel_viario = user.role_dashboard_anel_viario
        self.role_dashboard_sist_unificado = user.role_dashboard_sist_unificado
        self.role_modfisc_convias = user.role_modfisc_convias
        self.role_modfisc_osmv = user.role_modfisc_osmv
        self.role_modfisc_osct = user.role_modfisc_osct
        self.role_modfisc_relatoriomv = user.role_modfisc_relatoriomv
        self.role_modfisc_vistoriapv = user.role_modfisc_vistoriapv
        self.role_modfisc_vistoriarecape = user.role_modfisc_vistoriarecape
        self.role_interf_mapa = user.role_interf_mapa
        self.role_interf_protproc = user.role_interf_protproc
        self.role_drenagem_ativos = user.role_drenagem_ativos
        self.role_drenagem_redes = user.role_drenagem_redes
        self.role_usuarios = user.role_usuarios
        self.role_tickets = user.role_tickets
        self.role_recape = user.role_recape

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'name': self.name,
            'department': self.department,
            'group': self.group.value,
            'enabled': self.enabled,
            'role_dashboard_qualidade': self.role_dashboard_qualidade,
            'role_dashboard_deteccao': self.role_dashboard_deteccao,
            'role_dashboard_tempo': self.role_dashboard_tempo,
            'role_dashboard_geoinfra': self.role_dashboard_geoinfra,
            'role_dashboard_recapeamento': self.role_dashboard_recapeamento,
            'role_dashboard_anel_viario': self.role_dashboard_anel_viario,
            'role_dashboard_sist_unificado': self.role_dashboard_sist_unificado,
            'role_modfisc_convias': self.role_modfisc_convias,
            'role_modfisc_osmv': self.role_modfisc_osmv,
            'role_modfisc_osct': self.role_modfisc_osct,
            'role_modfisc_relatoriomv': self.role_modfisc_relatoriomv,
            'role_modfisc_vistoriapv': self.role_modfisc_vistoriapv,
            'role_modfisc_vistoriarecape': self.role_modfisc_vistoriarecape,
            'role_interf_mapa': self.role_interf_mapa,
            'role_interf_protproc': self.role_interf_protproc,
            'role_drenagem_ativos': self.role_drenagem_ativos,
            'role_drenagem_redes': self.role_drenagem_redes,
            'role_usuarios': self.role_usuarios,
            'role_tickets': self.role_tickets,
            'role_recape': self.role_recape.value if self.role_recape is not None else None,
        }

class GetAllUsersViewmodel:
    user_list_dict_list: List[UserViewmodel]

    def __init__(self, user_list_dict_list: List[User]):
        self.user_list_dict_list = [UserViewmodel(user=user) for user in user_list_dict_list]

    def to_dict(self):
        return {
            'user_list': [user.to_dict() for user in self.user_list_dict_list],
            'message': 'Usuários retornados com sucesso!'
        }