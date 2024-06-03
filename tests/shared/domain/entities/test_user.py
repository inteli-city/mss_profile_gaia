import pytest
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError

class Test_User:

    def test_user(self):
        User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email="gabriel@hotmail.com", name='Gabriel', department='CONVIAS', enabled=True, role_dashboard_qualidade=True, role_dashboard_deteccao=True, role_dashboard_tempo=True, role_dashboard_geoinfra=True, role_dashboard_recapeamento=True, role_dashboard_anel_viario=True, role_dashboard_sist_unificado=True, role_modfisc_convias=True, role_modfisc_osmv=True, role_modfisc_osct=True, role_modfisc_relatoriomv=True, role_modfisc_vistoriapv=True, role_modfisc_vistoriarecape=True, role_interf_mapa=True, role_interf_protproc=True, role_drenagem_ativos=True, role_drenagem_redes=True, role_usuarios=True, role_tickets=True)
    
    def test_user_id_is_none(self):
        with pytest.raises(EntityError):
            User(user_id=None,email='gabriel@hotmail.com', name='Gabriel', department='Teste', enabled=True)
    
    def test_user_id_is_not_str(self):
        with pytest.raises(EntityError):
            User(user_id=123, email='gabriel@hotmail.com', name='Gabriel', department='Teste', enabled=True)
    
    def test_user_id_is_not_validate(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5", email='gabriel@hotmail.com', name='Gabriel', department='Teste', enabled=True)

    def test_user_email_is_none(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93",email=None, name='Gabriel', department='Teste', enabled=True)
    
    def test_user_email_is_not_str(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email=123, name='Gabriel', department='Teste', enabled=True)
    
    def test_user_email_is_not_validate(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel', name='Gabriel', department='Teste', enabled=True)
    
    def test_user_name_is_none(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name=None, department='Teste', enabled=True)
    
    def test_user_name_is_not_str(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name=123, department='Teste', enabled=True)
    
    def test_user_name_is_not_min_length(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='GA', enabled=True)
    
    def test_user_department_is_not_str(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department=123, enabled=True)
    
    def test_user_role_dashboard_qualidade_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_dashboard_qualidade=123)
    
    def test_user_role_dashboard_deteccao_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_dashboard_deteccao=123)
    
    def test_user_role_dashboard_tempo_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_dashboard_tempo=123)
    
    def test_user_role_dashboard_geoinfra_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_dashboard_geoinfra=123)
    
    def test_user_role_dashboard_recapeamento_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_dashboard_recapeamento=123)
    
    def test_user_role_dashboard_anel_viario_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_dashboard_anel_viario=123)
    
    def test_user_role_dashboard_sist_unificado_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_dashboard_sist_unificado=123)

    def test_user_role_modfisc_convias_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_modfisc_convias=123)
    
    def test_user_role_modfisc_osmv_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_modfisc_osmv=123)
    
    def test_user_role_modfisc_osct_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_modfisc_osct=123)
    
    def test_user_role_modfisc_relatoriomv_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_modfisc_relatoriomv=123)
    
    def test_user_role_modfisc_vistoriapv_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_modfisc_vistoriapv=123)
    
    def test_user_role_modfisc_vistoriarecape_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_modfisc_vistoriarecape=123)
    
    def test_user_role_interf_mapa_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_interf_mapa=123)
    
    def test_user_role_interf_protproc_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_interf_protproc=123)
    
    def test_user_role_drenagem_ativos_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_drenagem_ativos=123)
    
    def test_user_role_drenagem_redes_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_drenagem_redes=123)
    
    def test_user_role_usuarios_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_usuarios=123)

    def test_user_role_tickets_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel@hotmail.com', name='Gabriel', department='123', enabled=True, role_tickets=123)
    
    def test_user_enabled_is_none(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email="gabriel@hotmail.com", name='Gabriel', enabled=None)
    
    def test_user_enabled_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email="gabriel@hotmail.com", name='Gabriel',enabled=123)