from flask import Flask, jsonify

from src.shared.http import Response
from src.shared.exceptions import (
    ValidationException,
    NotFoundException,
    ForbiddenException,
    BadRequestException,
    InternalServerErrorException,
    UnauthorizedException,
    ServiceUnavaliableException
)


def init_app(app: Flask):

    @app.errorhandler(ValidationException)
    def validation_error(error: ValidationException):
        return Response().force_type(
            response=error.status_code, 
            data=error.to_dict(),
            message=error.message
        )
    
    @app.errorhandler(NotFoundException)
    def not_found_error(error: NotFoundException):
        return Response().force_type(
            response=error.status_code, 
            data=error.to_dict(),
            message=error.message
        )

    @app.errorhandler(ForbiddenException)
    def forbidden_error(error: ForbiddenException):
        return Response().force_type(
            response=error.status_code,
            data=error.to_dict(),
            message=error.message
        )
    
    @app.errorhandler(BadRequestException)
    def bad_request_error(error: BadRequestException):
        return Response().force_type(
            response=error.status_code,
            data=error.to_dict(),
            message=error.message
        )

    @app.errorhandler(InternalServerErrorException)
    def internal_server_error(error: InternalServerErrorException):
        return Response().force_type(
            response=error.status_code,
            data=error.to_dict(),
            message=error.message
        ) 

    @app.errorhandler(UnauthorizedException)
    def unauthorized_error(error: UnauthorizedException):
        return Response().force_type(
            response=error.status_code,
            data=error.to_dict(),
            message=error.message
        ) 
            
    @app.errorhandler(ServiceUnavaliableException)
    def service_unavaliable_error(error: ServiceUnavaliableException):
        return Response().force_type(
            response=error.status_code,
            data=error.to_dict(),
            message=error.message
        ) 

        