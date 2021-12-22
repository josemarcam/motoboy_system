from http import HTTPStatus

from src.shared.exceptions.base_exception import BaseException


class ServiceUnavaliableException(BaseException):
    
    def __init__(self, message=None):
        
        message = message or HTTPStatus.SERVICE_UNAVAILABLE.phrase

        super().__init__(message=message, status_code=HTTPStatus.SERVICE_UNAVAILABLE.value)
