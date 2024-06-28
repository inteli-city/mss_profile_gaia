from src.modules.login_user.app.login_user_viewmodel import LoginUserViewmodel, UserViewmodel
from src.shared.domain.entities.user import User
from src.shared.domain.enum.group_enum import GROUP
from src.shared.domain.enum.role_recape_enum import ROLE_RECAPE


class Test_LoginUserViewmodel:
    def test_login_user_viewmodel(self):
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

        login_user_viewmodel = LoginUserViewmodel(data)

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
            'message': 'Login realizado com sucesso!',
        }

        assert login_user_viewmodel.to_dict() == expected

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
            role_recape=ROLE_RECAPE.FISCALIZACAO,
        )
        )

        response = viewmodel.to_dict()

        data = {
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
            'role_recape': 'FISCALIZACAO',
        }
    
        assert response == data


