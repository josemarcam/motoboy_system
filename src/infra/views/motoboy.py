from flask import Blueprint, request
from injector import inject

from src.shared.http.url_helpers import query_parameters_to_dict
from src.shared.http import Response
from src.shared.exceptions import NotFoundException
from src.domain.motoboys.services import MotoboyService
from src.domain.motoboys.models import CreateMotoboyModel

motoboy_bp = Blueprint("motoboys", __name__, url_prefix="/api/motoboys")


@motoboy_bp.route('/<string:name>', methods=['GET'])
@inject
def get_motoboy_by_name(name: str, service: MotoboyService):
    name = name.replace("-"," ")
    motoboy_model = service.get(name = name)
    if motoboy_model:
        return Response().force_type(Response.OK, "", motoboy_model.to_dict())

    raise NotFoundException("Motoboy não encontrado")

@motoboy_bp.route('', methods=['GET'])
@inject
def get_motoboy_list(service: MotoboyService):

    request_data = query_parameters_to_dict(request)
        
    json_data = service.get_motoboy_list(page=request_data.get("page",1), per_page=request_data.get("per_page",20))

    return Response().force_type(Response.OK, "", json_data)

@motoboy_bp.route('', methods=['POST'])
@inject
def create_motoboy(service: MotoboyService):

    request_data = request.get_json()
    create_motoboy_model = CreateMotoboyModel.from_dict(request_data)

    motoboy_model = service.create_motoboy(create_motoboy_model)

    return Response().force_type(Response.CREATED, "", motoboy_model)