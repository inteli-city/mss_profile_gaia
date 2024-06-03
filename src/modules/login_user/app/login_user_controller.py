from src.shared.infra.dtos.user_gaia_api_gateway_dto import UserGaiaApiGatewayDTO
from .login_user_usecase import LoginUserUsecase
from .login_user_viewmodel import LoginUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import InvalidTokenError, NoItemsFound, ForbiddenAction, InvalidCredentials, UserNotValid
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, OK, Forbidden, \
    Unauthorized


class LoginUserController:

    def __init__(self, usecase: LoginUserUsecase):
        self.loginUserUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserGaiaApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            user = self.loginUserUsecase(
                requester_user_id=requester_user.user_id,
                name=requester_user.name,
                email=requester_user.email
            )

            viewmodel = LoginUserViewmodel(user=user)
            response = OK(viewmodel.to_dict())

            return response

        except NoItemsFound as err:
            return NotFound(body='Nenhum usuário encontrado')

        except ForbiddenAction as err:
            return Forbidden(body=f"Ação não permitida: {err.message}")

        except MissingParameters as err:
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except EntityError as err:
            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except InvalidTokenError as err:
            return Unauthorized(body="Token inválido ou expirado")
        
        except UserNotValid as err:
            return Unauthorized(body="Usuário inválido")
        
        except InvalidCredentials as e:
            return Unauthorized(body="Credenciais inválidas")

        except Exception as err:
            return InternalServerError(body=err.args[0])

