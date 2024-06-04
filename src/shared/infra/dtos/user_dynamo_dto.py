from typing import Optional
from src.shared.domain.entities.user import User
from src.shared.domain.enum.group_enum import GROUP


class UserDynamoDTO:
    user_id: str
    email: str
    name: str
    enabled: bool
    group: GROUP
    department: Optional[str] = None
    role_dashboard_qualidade: Optional[bool] = None
    role_dashboard_deteccao: Optional[bool] = None
    role_dashboard_tempo: Optional[bool] = None
    role_dashboard_geoinfra: Optional[bool] = None
    role_dashboard_recapeamento: Optional[bool] = None
    role_dashboard_anel_viario: Optional[bool] = None
    role_dashboard_sist_unificado: Optional[bool] = None
    role_modfisc_convias: Optional[bool] = None
    role_modfisc_osmv: Optional[bool] = None
    role_modfisc_osct: Optional[bool] = None
    role_modfisc_relatoriomv: Optional[bool] = None
    role_modfisc_vistoriapv: Optional[bool] = None
    role_modfisc_vistoriarecape: Optional[bool] = None
    role_interf_mapa: Optional[bool] = None
    role_interf_protproc: Optional[bool] = None
    role_drenagem_ativos: Optional[bool] = None
    role_drenagem_redes: Optional[bool] = None
    role_usuarios: Optional[bool] = None
    role_tickets: Optional[bool] = None


    def __init__(self, user_id: str, email: str, name: str, enabled: bool, group: GROUP, department: Optional[str] = None,
                 role_dashboard_qualidade: Optional[bool] = None, role_dashboard_deteccao: Optional[bool] = None,
                 role_dashboard_tempo: Optional[bool] = None, role_dashboard_geoinfra: Optional[bool] = None,
                 role_dashboard_recapeamento: Optional[bool] = None, role_dashboard_anel_viario: Optional[bool] = None,
                 role_dashboard_sist_unificado: Optional[bool] = None, role_modfisc_convias: Optional[bool] = None,
                 role_modfisc_osmv: Optional[bool] = None, role_modfisc_osct: Optional[bool] = None,
                 role_modfisc_relatoriomv: Optional[bool] = None, role_modfisc_vistoriapv: Optional[bool] = None,
                 role_modfisc_vistoriarecape: Optional[bool] = None, role_interf_mapa: Optional[bool] = None,
                 role_interf_protproc: Optional[bool] = None, role_drenagem_ativos: Optional[bool] = None,
                 role_drenagem_redes: Optional[bool] = None, role_usuarios: Optional[bool] = None,
                 role_tickets: Optional[bool] = None):
        self.email = email
        self.name = name
        self.user_id = user_id
        self.enabled = enabled
        self.group = group
        self.department = department
        self.role_dashboard_qualidade = role_dashboard_qualidade
        self.role_dashboard_deteccao = role_dashboard_deteccao
        self.role_dashboard_tempo = role_dashboard_tempo
        self.role_dashboard_geoinfra = role_dashboard_geoinfra
        self.role_dashboard_recapeamento = role_dashboard_recapeamento
        self.role_dashboard_anel_viario = role_dashboard_anel_viario
        self.role_dashboard_sist_unificado = role_dashboard_sist_unificado
        self.role_modfisc_convias = role_modfisc_convias
        self.role_modfisc_osmv = role_modfisc_osmv
        self.role_modfisc_osct = role_modfisc_osct
        self.role_modfisc_relatoriomv = role_modfisc_relatoriomv
        self.role_modfisc_vistoriapv = role_modfisc_vistoriapv
        self.role_modfisc_vistoriarecape = role_modfisc_vistoriarecape
        self.role_interf_mapa = role_interf_mapa
        self.role_interf_protproc = role_interf_protproc
        self.role_drenagem_ativos = role_drenagem_ativos
        self.role_drenagem_redes = role_drenagem_redes
        self.role_usuarios = role_usuarios
        self.role_tickets = role_tickets

    @staticmethod
    def from_entity(user: User):
        return UserDynamoDTO(
            email=user.email,
            name=user.name,
            user_id=user.user_id,
            enabled=user.enabled,
            group=user.group,
            department=user.department,
            role_dashboard_qualidade=user.role_dashboard_qualidade,
            role_dashboard_deteccao=user.role_dashboard_deteccao,
            role_dashboard_tempo=user.role_dashboard_tempo,
            role_dashboard_geoinfra=user.role_dashboard_geoinfra,
            role_dashboard_recapeamento=user.role_dashboard_recapeamento,
            role_dashboard_anel_viario=user.role_dashboard_anel_viario,
            role_dashboard_sist_unificado=user.role_dashboard_sist_unificado,
            role_modfisc_convias=user.role_modfisc_convias,
            role_modfisc_osmv=user.role_modfisc_osmv,
            role_modfisc_osct=user.role_modfisc_osct,
            role_modfisc_relatoriomv=user.role_modfisc_relatoriomv,
            role_modfisc_vistoriapv=user.role_modfisc_vistoriapv,
            role_modfisc_vistoriarecape=user.role_modfisc_vistoriarecape,
            role_interf_mapa=user.role_interf_mapa,
            role_interf_protproc=user.role_interf_protproc,
            role_drenagem_ativos=user.role_drenagem_ativos,
            role_drenagem_redes=user.role_drenagem_redes,
            role_usuarios=user.role_usuarios,
            role_tickets=user.role_tickets
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from UserDynamoDTO to dict
        """
        data = {
            "name": self.name,
            "email": self.email,
            "user_id": self.user_id,
            "enabled": self.enabled,
            "group": self.group.value,
            "department": self.department,
            "role_dashboard_qualidade": self.role_dashboard_qualidade,
            "role_dashboard_deteccao": self.role_dashboard_deteccao,
            "role_dashboard_tempo": self.role_dashboard_tempo,
            "role_dashboard_geoinfra": self.role_dashboard_geoinfra,
            "role_dashboard_recapeamento": self.role_dashboard_recapeamento,
            "role_dashboard_anel_viario": self.role_dashboard_anel_viario,
            "role_dashboard_sist_unificado": self.role_dashboard_sist_unificado,
            "role_modfisc_convias": self.role_modfisc_convias,
            "role_modfisc_osmv": self.role_modfisc_osmv,
            "role_modfisc_osct": self.role_modfisc_osct,
            "role_modfisc_relatoriomv": self.role_modfisc_relatoriomv,
            "role_modfisc_vistoriapv": self.role_modfisc_vistoriapv,
            "role_modfisc_vistoriarecape": self.role_modfisc_vistoriarecape,
            "role_interf_mapa": self.role_interf_mapa,
            "role_interf_protproc": self.role_interf_protproc,
            "role_drenagem_ativos": self.role_drenagem_ativos,
            "role_drenagem_redes": self.role_drenagem_redes,
            "role_usuarios": self.role_usuarios,
            "role_tickets": self.role_tickets
        }

        return data

    @staticmethod
    def from_dynamo(user_data: dict) -> "UserDynamoDTO":
        """
        Parse data from DynamoDB to UserDynamoDTO
        @param user_data: dict from DynamoDB
        """
        return UserDynamoDTO(
            name=str(user_data["name"]),
            email=str(user_data["email"]),
            user_id=str(user_data["user_id"]),
            enabled=bool(user_data["enabled"]),
            group=GROUP(user_data["group"]),
            department=str(user_data["department"]) if "department" in user_data else None,
            role_dashboard_qualidade=bool(user_data["role_dashboard_qualidade"]) if "role_dashboard_qualidade" in user_data else None,
            role_dashboard_deteccao=bool(user_data["role_dashboard_deteccao"]) if "role_dashboard_deteccao" in user_data else None,
            role_dashboard_tempo=bool(user_data["role_dashboard_tempo"]) if "role_dashboard_tempo" in user_data else None,
            role_dashboard_geoinfra=bool(user_data["role_dashboard_geoinfra"]) if "role_dashboard_geoinfra" in user_data else None,
            role_dashboard_recapeamento=bool(user_data["role_dashboard_recapeamento"]) if "role_dashboard_recapeamento" in user_data else None,
            role_dashboard_anel_viario=bool(user_data["role_dashboard_anel_viario"]) if "role_dashboard_anel_viario" in user_data else None,
            role_dashboard_sist_unificado=bool(user_data["role_dashboard_sist_unificado"]) if "role_dashboard_sist_unificado" in user_data else None,
            role_modfisc_convias=bool(user_data["role_modfisc_convias"]) if "role_modfisc_convias" in user_data else None,
            role_modfisc_osmv=bool(user_data["role_modfisc_osmv"]) if "role_modfisc_osmv" in user_data else None,
            role_modfisc_osct=bool(user_data["role_modfisc_osct"]) if "role_modfisc_osct" in user_data else None,
            role_modfisc_relatoriomv=bool(user_data["role_modfisc_relatoriomv"]) if "role_modfisc_relatoriomv" in user_data else None,
            role_modfisc_vistoriapv=bool(user_data["role_modfisc_vistoriapv"]) if "role_modfisc_vistoriapv" in user_data else None,
            role_modfisc_vistoriarecape=bool(user_data["role_modfisc_vistoriarecape"]) if "role_modfisc_vistoriarecape" in user_data else None,
            role_interf_mapa=bool(user_data["role_interf_mapa"]) if "role_interf_mapa" in user_data else None,
            role_interf_protproc=bool(user_data["role_interf_protproc"]) if "role_interf_protproc" in user_data else None,
            role_drenagem_ativos=bool(user_data["role_drenagem_ativos"]) if "role_drenagem_ativos" in user_data else None,
            role_drenagem_redes=bool(user_data["role_drenagem_redes"]) if "role_drenagem_redes" in user_data else None,
            role_usuarios=bool(user_data["role_usuarios"]) if "role_usuarios" in user_data else None,
            role_tickets=bool(user_data["role_tickets"]) if "role_tickets" in user_data else None
        )
    
    def to_entity(self) -> User:
        """
        Parse data from UserDynamoDTO to User
        """
        return User(
            name=self.name,
            email=self.email,
            user_id=self.user_id,
            enabled=self.enabled,
            group=self.group,
            department=self.department,
            role_dashboard_qualidade=self.role_dashboard_qualidade,
            role_dashboard_deteccao=self.role_dashboard_deteccao,
            role_dashboard_tempo=self.role_dashboard_tempo,
            role_dashboard_geoinfra=self.role_dashboard_geoinfra,
            role_dashboard_recapeamento=self.role_dashboard_recapeamento,
            role_dashboard_anel_viario=self.role_dashboard_anel_viario,
            role_dashboard_sist_unificado=self.role_dashboard_sist_unificado,
            role_modfisc_convias=self.role_modfisc_convias,
            role_modfisc_osmv=self.role_modfisc_osmv,
            role_modfisc_osct=self.role_modfisc_osct,
            role_modfisc_relatoriomv=self.role_modfisc_relatoriomv,
            role_modfisc_vistoriapv=self.role_modfisc_vistoriapv,
            role_modfisc_vistoriarecape=self.role_modfisc_vistoriarecape,
            role_interf_mapa=self.role_interf_mapa,
            role_interf_protproc=self.role_interf_protproc,
            role_drenagem_ativos=self.role_drenagem_ativos,
            role_drenagem_redes=self.role_drenagem_redes,
            role_usuarios=self.role_usuarios,
            role_tickets=self.role_tickets
        )
    
    def __repr__(self):
        return f"UserDynamoDto(name={self.name}, email={self.email}, user_id={self.user_id}, enabled={self.enabled}, group={self.group.value}, department={self.department}, role_dashboard_qualidade={self.role_dashboard_qualidade}, role_dashboard_deteccao={self.role_dashboard_deteccao}, role_dashboard_tempo={self.role_dashboard_tempo}, role_dashboard_geoinfra={self.role_dashboard_geoinfra}, role_dashboard_recapeamento={self.role_dashboard_recapeamento}, role_dashboard_anel_viario={self.role_dashboard_anel_viario}, role_dashboard_sist_unificado={self.role_dashboard_sist_unificado}, role_modfisc_convias={self.role_modfisc_convias}, role_modfisc_osmv={self.role_modfisc_osmv}, role_modfisc_osct={self.role_modfisc_osct}, role_modfisc_relatoriomv={self.role_modfisc_relatoriomv}, role_modfisc_vistoriapv={self.role_modfisc_vistoriapv}, role_modfisc_vistoriarecape={self.role_modfisc_vistoriarecape}, role_interf_mapa={self.role_interf_mapa}, role_interf_protproc={self.role_interf_protproc}, role_drenagem_ativos={self.role_drenagem_ativos}, role_drenagem_redes={self.role_drenagem_redes}, role_usuarios={self.role_usuarios}, role_tickets={self.role_tickets})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__