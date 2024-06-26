from src.modules.update_user.app.update_user_viewmodel import UpdateUserViewmodel, UserViewmodel
from src.shared.domain.entities.user import User
from src.shared.domain.enum.group_enum import GROUP
from src.shared.domain.enum.role_recape_enum import ROLE_RECAPE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserViewmodel:

    def test_update_user_viewmodel(self):
        data = User(
            user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123',
            email='v1zg0@example.com',
            name='Gabriel',
            enabled=True,
            group=GROUP.USUARIO,
            department='INTELICITY',
            role_dashboard_qualidade=True,
            role_dashboard_deteccao=True,
            role_dashboard_tempo=True,
            role_dashboard_geoinfra=True,
            role_dashboard_recapeamento=True,
            role_dashboard_anel_viario=True,
            role_dashboard_sist_unificado=True,
            role_modfisc_convias=True,
            role_modfisc_osmv=True,
            role_modfisc_osct=True,
            role_modfisc_relatoriomv=True,
            role_modfisc_vistoriapv=True,
            role_modfisc_vistoriarecape=True,
            role_interf_mapa=True,
            role_interf_protproc=True,
            role_drenagem_ativos=True,
            role_drenagem_redes=True,
            role_usuarios=True,
            role_tickets=True,
        )
        
        viewmodel = UpdateUserViewmodel(data)

        expected = {
            'user': {
                'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
                'email': 'v1zg0@example.com',
                'name': 'Gabriel',
                'enabled': True,
                'group': 'USUARIO',
                'department': 'INTELICITY',
                'role_dashboard_qualidade': True,
                'role_dashboard_deteccao': True,
                'role_dashboard_tempo': True,
                'role_dashboard_geoinfra': True,
                'role_dashboard_recapeamento': True,
                'role_dashboard_anel_viario': True,
                'role_dashboard_sist_unificado': True,
                'role_modfisc_convias': True,
                'role_modfisc_osmv': True,
                'role_modfisc_osct': True,
                'role_modfisc_relatoriomv': True,
                'role_modfisc_vistoriapv': True,
                'role_modfisc_vistoriarecape': True,
                'role_interf_mapa': True,
                'role_interf_protproc': True,
                'role_drenagem_ativos': True,
                'role_drenagem_redes': True,
                'role_usuarios': True,
                'role_tickets': True,
                'role_recape': None,
            },
            'message': 'Usuário atualizado com sucesso!',
        }

        assert viewmodel.to_dict() == expected
    
    def test_user_viewmodel(self):
        viewmodel = UserViewmodel(
           user=User(
            user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123',
            email='v1zg0@example.com',
            name='Gabriel',
            enabled=True,
            group=GROUP.USUARIO,
            department='INTELICITY',
            role_dashboard_qualidade=True,
            role_dashboard_deteccao=True,
            role_dashboard_tempo=True,
            role_dashboard_geoinfra=True,
            role_dashboard_recapeamento=True,
            role_dashboard_anel_viario=True,
            role_dashboard_sist_unificado=True,
            role_modfisc_convias=True,
            role_modfisc_osmv=True,
            role_modfisc_osct=True,
            role_modfisc_relatoriomv=True,
            role_modfisc_vistoriapv=True,
            role_modfisc_vistoriarecape=True,
            role_interf_mapa=True,
            role_interf_protproc=True,
            role_drenagem_ativos=True,
            role_drenagem_redes=True,
            role_usuarios=True,
            role_tickets=True,
            role_recape=ROLE_RECAPE.ADMIN
           )
        )

        response = viewmodel.to_dict()

        data = {
            'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
            'email': 'v1zg0@example.com',
            'name': 'Gabriel',
            'enabled': True,
            'department': 'INTELICITY',
            'group': 'USUARIO',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_recape': 'ADMIN',
        }
    
        assert response == data