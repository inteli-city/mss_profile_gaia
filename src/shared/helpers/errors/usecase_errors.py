from src.shared.helpers.errors.base_error import BaseError


class NoItemsFound(BaseError):
    def __init__(self, message: str):
        super().__init__(message)


class DuplicatedItem(BaseError):
    def __init__(self, message: str):
        super().__init__(message)


class ForbiddenAction(BaseError):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidCredentials(BaseError):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidTokenError(BaseError):
    def __init__(self, message: str):
        super().__init__(message)
        self.__message = message

    @property
    def message(self):
        return self.__message
    
class UserNotValid(BaseError):
    def __init__(self, message: str):
        super().__init__(message)

class UnecessaryUpdate(BaseError):
    def __init__(self, message: str):
        super().__init__(message)
