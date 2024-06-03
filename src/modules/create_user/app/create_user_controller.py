from .create_user_usecase import CreateUserUsecase
from .create_user_viewmodel import CreateUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, InternalServerError, NotFound
from src.shared.infra.dtos.user_gaia_api_gateway_dto import UserGaiaApiGatewayDTO


class CreateUserController:
    def __init__(self, usecase: CreateUserUsecase):
        self.createUserController = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserGaiaApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get('email') is None:
                raise MissingParameters('email')
            
            if request.data.get('name') is None:
                raise MissingParameters('name')
            
            if request.data.get('department') is None:
                raise MissingParameters('department')
            
            user = self.createUserController(
                requester_user_id=requester_user.user_id,
                email=request.data.get('email'),
                name=request.data.get('name'),
                department=request.data.get('department'),
                role_dashboard_qualidade=request.data.get('role_dashboard_qualidade'),
                role_dashboard_deteccao=request.data.get('role_dashboard_deteccao'),
                role_dashboard_tempo=request.data.get('role_dashboard_tempo'),
                role_dashboard_geoinfra=request.data.get('role_dashboard_geoinfra'),
                role_dashboard_recapeamento=request.data.get('role_dashboard_recapeamento'),
                role_dashboard_anel_viario=request.data.get('role_dashboard_anel_viario'),
                role_dashboard_sist_unificado=request.data.get('role_dashboard_sist_unificado'),
                role_modfisc_convias=request.data.get('role_modfisc_convias'),
                role_modfisc_osmv=request.data.get('role_modfisc_osmv'),
                role_modfisc_osct=request.data.get('role_modfisc_osct'),
                role_modfisc_relatoriomv=request.data.get('role_modfisc_relatoriomv'),
                role_modfisc_vistoriapv=request.data.get('role_modfisc_vistoriapv'),
                role_modfisc_vistoriarecape=request.data.get('role_modfisc_vistoriarecape'),
                role_interf_mapa=request.data.get('role_interf_mapa'),
                role_interf_protproc=request.data.get('role_interf_protproc'),
                role_drenagem_ativos=request.data.get('role_drenagem_ativos'),
                role_drenagem_redes=request.data.get('role_drenagem_redes'),
                role_usuarios=request.data.get('role_usuarios'),
                role_tickets=request.data.get('role_tickets'),
            )

            viewmodel = CreateUserViewmodel(user)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=f'{err.message}')

        except MissingParameters as err:
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except ForbiddenAction as err:
            return Forbidden(body=f"Ação não permitida: {err.message}")

        except EntityError as err:
            return BadRequest(body=f'Parâmetro inválido: {err.message}')

        except Exception as err:
            return InternalServerError(body=err.args[0])