from src.shared.domain.enum.group_enum import GROUP
from src.shared.domain.enum.role_recape_enum import ROLE_RECAPE
from src.shared.infra.dtos.user_dynamo_dto import UserDynamoDTO
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserDynamoDto:
    def test_from_entity(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO.from_entity(user=repo.users_list[0])

        expected_user_dto = UserDynamoDTO(
            user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            email="gabriel@hotmail.com",
            name='Gabriel',
            enabled=True,
            department='INTELICITY',
            group=GROUP.USUARIO,
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

        assert user_dto == expected_user_dto
    
    def test_to_dynamo(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO(
            user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            email="gabriel@hotmail.com",
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
            role_tickets=True
        )

        expected_dict = user_dto.to_dynamo()

        excepted_user_dynamo = {
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': "gabriel@hotmail.com",
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
            'role_tickets': True
        }
    
    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'name': 'Gabriel Godoy',
                                'email' : 'gab.godoy@gmail.com',
                                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48abb',
                                'group': 'USUARIO',
                                'role_dashboard_qualidade': "true",
                                'role_dashboard_deteccao': "true",
                                'role_dashboard_tempo': "true",
                                'role_dashboard_geoinfra': "true",
                                'role_dashboard_recapeamento': "true",
                                'role_dashboard_anel_viario': "true",
                                'role_dashboard_sist_unificado': "true",
                                'role_modfisc_convias': "true",
                                'role_modfisc_osmv': "true",
                                'role_modfisc_osct': "true",
                                'role_modfisc_relatoriomv': "true",
                                'role_modfisc_vistoriapv': "true",
                                'role_modfisc_vistoriarecape': "true",
                                'role_interf_mapa': "true",
                                'role_interf_protproc': "true",
                                'role_drenagem_ativos': "true",
                                'role_drenagem_redes': "true",
                                'role_usuarios': "true",
                                'role_tickets': "true",
                                'enabled': "true",
                                },
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}
        user_dto = UserDynamoDTO.from_dynamo(user_data=dynamo_dict["Item"])

        expected_user_dto = UserDynamoDTO(
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            email="gab.godoy@gmail.com",
            name='Gabriel Godoy',
            enabled=True,
            group=GROUP.USUARIO,
            department=None,
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
            role_tickets=True
        )

        assert user_dto == expected_user_dto
    
    def test_to_entity(self):
        repo = UserRepositoryMock()

        user_dto = UserDynamoDTO(
            user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            email="gab.godoy@gmail.com",
            name='Gabriel Godoy',
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
            role_tickets=True
        )

        user = user_dto.to_entity()

        assert user.user_id == user_dto.user_id
        assert user.email == user_dto.email
        assert user.name == user_dto.name
        assert user.enabled == user_dto.enabled
        assert user.group == user_dto.group
        assert user.department == user_dto.department
        assert user.role_dashboard_qualidade == user_dto.role_dashboard_qualidade
        assert user.role_dashboard_deteccao == user_dto.role_dashboard_deteccao
        assert user.role_dashboard_tempo == user_dto.role_dashboard_tempo
        assert user.role_dashboard_geoinfra == user_dto.role_dashboard_geoinfra
        assert user.role_dashboard_recapeamento == user_dto.role_dashboard_recapeamento
        assert user.role_dashboard_anel_viario == user_dto.role_dashboard_anel_viario
        assert user.role_dashboard_sist_unificado == user_dto.role_dashboard_sist_unificado
        assert user.role_modfisc_convias == user_dto.role_modfisc_convias
        assert user.role_modfisc_osmv == user_dto.role_modfisc_osmv
        assert user.role_modfisc_osct == user_dto.role_modfisc_osct
        assert user.role_modfisc_relatoriomv == user_dto.role_modfisc_relatoriomv
        assert user.role_modfisc_vistoriapv == user_dto.role_modfisc_vistoriapv
        assert user.role_modfisc_vistoriarecape == user_dto.role_modfisc_vistoriarecape
        assert user.role_interf_mapa == user_dto.role_interf_mapa
        assert user.role_interf_protproc == user_dto.role_interf_protproc
        assert user.role_drenagem_ativos == user_dto.role_drenagem_ativos
        assert user.role_drenagem_redes == user_dto.role_drenagem_redes
        assert user.role_usuarios == user_dto.role_usuarios
        assert user.role_tickets == user_dto.role_tickets
