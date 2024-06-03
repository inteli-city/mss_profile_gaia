from src.shared.domain.entities.user import User
from src.shared.infra.dtos.user_gaia_api_gateway_dto import UserGaiaApiGatewayDTO
from .update_user_usecase import UpdateUserUsecase
from .update_user_viewmodel import UpdateUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, InvalidCredentials, InvalidTokenError, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden, Unauthorized


class UpdateUserController:

    def __init__(self, usecase: UpdateUserUsecase):
        self.UpdateUserUsecase = usecase
        self.mutable_fields = ['name', 'department', 'enabled', 'role_dashboard_qualidade', 'role_dashboard_deteccao', 'role_dashboard_tempo', 'role_dashboard_geoinfra', 'role_dashboard_recapeamento', 'role_dashboard_anel_viario', 'role_dashboard_sist_unificado', 'role_modfisc_convias', 'role_modfisc_osmv', 'role_modfisc_osct', 'role_modfisc_relatoriomv', 'role_modfisc_vistoriapv', 'role_modfisc_vistoriarecape', 'role_interf_mapa', 'role_interf_protproc', 'role_drenagem_ativos', 'role_drenagem_redes', 'role_usuarios', 'role_tickets']
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserGaiaApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
            
            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')
            
            user_data = {k: v for k, v in request.data.items() if k in self.mutable_fields}

            user = self.UpdateUserUsecase(
                    requester_user_id=requester_user.user_id,
                    user_id=request.data.get('user_id'),
                    new_user_data=user_data,
                )
            
            viewmodel = UpdateUserViewmodel(user)
            response = OK(viewmodel.to_dict())

            return response
        
        except NoItemsFound as err:
            return NotFound(body=f'{err.message}')

        except MissingParameters as err:
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except EntityError as err:
            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except InvalidCredentials as err:
            return BadRequest(body=f"Token inválido: {err.message}")

        except ForbiddenAction as err:
            return Forbidden(body=f"Ação não permitida: {err.message}")

        except InvalidTokenError as e:
            return Unauthorized(body="Token inválido ou expirado")
        
        except Exception as err:
            return InternalServerError(body=err.args[0])