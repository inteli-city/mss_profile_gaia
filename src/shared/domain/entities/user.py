import abc
import re
from src.shared.domain.enum.group_enum import GROUP
from src.shared.domain.enum.role_recape_enum import ROLE_RECAPE
from src.shared.helpers.errors.domain_errors import EntityError


class User(abc.ABC):
    user_id: str
    email: str
    name: str
    group: GROUP
    department: str = None
    enabled: bool
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

    MIN_NAME_LENGTH = 2
    USER_ID_LENGTH = 36

    def __init__(self, user_id: str, email: str, name: str,
            enabled: bool,
            group: GROUP,
            department: str = None,
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
            role_recape: ROLE_RECAPE = None,
        ):

        if not User.validate_user_id(user_id):
            raise EntityError("user_id")
        self.user_id = user_id
        
        if not User.validate_email(email):
            raise EntityError("email")
        self.email = email

        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name

        if type(enabled) is not bool:
            raise EntityError("enabled")
        self.enabled = enabled

        if type(group) is not GROUP:
            raise EntityError("group")
        self.group = group

        if department is not None:
            if type(department) != str:
                raise EntityError("department")
        self.department = department

        if role_dashboard_qualidade is not None:
            if type(role_dashboard_qualidade) != bool:
                raise EntityError("role_dashboard_qualidade")
        self.role_dashboard_qualidade = role_dashboard_qualidade

        if role_dashboard_deteccao is not None:
            if type(role_dashboard_deteccao) != bool:
                raise EntityError("role_dashboard_deteccao")
        self.role_dashboard_deteccao = role_dashboard_deteccao

        if role_dashboard_tempo is not None:
            if type(role_dashboard_tempo) != bool:
                raise EntityError("role_dashboard_tempo")
        self.role_dashboard_tempo = role_dashboard_tempo

        if role_dashboard_geoinfra is not None:
            if type(role_dashboard_geoinfra) != bool:
                raise EntityError("role_dashboard_geoinfra")
        self.role_dashboard_geoinfra = role_dashboard_geoinfra

        if role_dashboard_recapeamento is not None:
            if type(role_dashboard_recapeamento) != bool:
                raise EntityError("role_dashboard_recapeamento")
        self.role_dashboard_recapeamento = role_dashboard_recapeamento

        if role_dashboard_anel_viario is not None:
            if type(role_dashboard_anel_viario) != bool:
                raise EntityError("role_dashboard_anel_viario")
        self.role_dashboard_anel_viario = role_dashboard_anel_viario

        if role_dashboard_sist_unificado is not None:
            if type(role_dashboard_sist_unificado) != bool:
                raise EntityError("role_dashboard_sist_unificado")
        self.role_dashboard_sist_unificado = role_dashboard_sist_unificado

        if role_modfisc_convias is not None:
            if type(role_modfisc_convias) != bool:
                raise EntityError("role_modfisc_convias")
        self.role_modfisc_convias = role_modfisc_convias

        if role_modfisc_osmv is not None:
            if type(role_modfisc_osmv) != bool:
                raise EntityError("role_modfisc_osmv")
        self.role_modfisc_osmv = role_modfisc_osmv

        if role_modfisc_osct is not None:
            if type(role_modfisc_osct) != bool:
                raise EntityError("role_modfisc_osct")
        self.role_modfisc_osct = role_modfisc_osct

        if role_modfisc_relatoriomv is not None:
            if type(role_modfisc_relatoriomv) != bool:
                raise EntityError("role_modfisc_relatoriomv")
        self.role_modfisc_relatoriomv = role_modfisc_relatoriomv

        if role_modfisc_vistoriapv is not None:
            if type(role_modfisc_vistoriapv) != bool:
                raise EntityError("role_modfisc_vistoriapv")
        self.role_modfisc_vistoriapv = role_modfisc_vistoriapv

        if role_modfisc_vistoriarecape is not None:
            if type(role_modfisc_vistoriarecape) != bool:
                raise EntityError("role_modfisc_vistoriarecape")
        self.role_modfisc_vistoriarecape = role_modfisc_vistoriarecape

        if role_interf_mapa is not None:
            if type(role_interf_mapa) != bool:
                raise EntityError("role_interf_mapa")
        self.role_interf_mapa = role_interf_mapa

        if role_interf_protproc is not None:
            if type(role_interf_protproc) != bool:
                raise EntityError("role_interf_protproc")
        self.role_interf_protproc = role_interf_protproc

        if role_drenagem_ativos is not None:
            if type(role_drenagem_ativos) != bool:
                raise EntityError("role_drenagem_ativos")
        self.role_drenagem_ativos = role_drenagem_ativos

        if role_drenagem_redes is not None:
            if type(role_drenagem_redes) != bool:
                raise EntityError("role_drenagem_redes")
        self.role_drenagem_redes = role_drenagem_redes

        if role_usuarios is not None:
            if type(role_usuarios) != bool:
                raise EntityError("role_usuarios")
        self.role_usuarios = role_usuarios

        if role_tickets is not None:
            if type(role_tickets) != bool:
                raise EntityError("role_tickets")
        self.role_tickets = role_tickets

        if role_recape is not None:
            if type(role_recape) != ROLE_RECAPE:
                raise EntityError("role_recape")
        self.role_recape = role_recape

    @staticmethod
    def validate_email(email) -> bool:
        if email == None:
            return False
        elif type(email) != str:
            return False

        regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        return bool(re.fullmatch(regex, email))

    @staticmethod
    def validate_name(name: str) -> bool:

        if name is None:
            return False
        elif type(name) != str:
            return False
        elif len(name) <= User.MIN_NAME_LENGTH:
            return False
        
        return True

    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str:
            return False
        if len(user_id) != User.USER_ID_LENGTH:
            return False
        return True

    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'email': self.email,
            'name': self.name,
            'department': self.department,
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
            'role_tickets': self.role_tickets
        }
