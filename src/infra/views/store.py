from flask import Blueprint, request
from injector import inject
from src.domain.stores.models.order_model import CreateOrderModel, UpdateOrderModel

from src.shared.http import (
    Response
)

from src.shared.exceptions import NotFoundException

from src.domain.stores.services import (
 StoreService   
)
from src.shared.http.url_helpers import query_parameters_to_dict

store_bp = Blueprint("stores", __name__, url_prefix="/api/stores")


@store_bp.route('/<int:id>', methods=['GET'])
@inject
def get_store(id: int, service: StoreService):
    store_model = service.get_store(id)
    if store_model:
        return Response().force_type(Response.OK, "", store_model.to_dict())

    raise NotFoundException("Loja não encontrado")

@store_bp.route('', methods=['GET'])
@inject
def get_store_list(service: StoreService):

    request_data = query_parameters_to_dict(request)
        
    json_data = service.get_store_list(page=request_data.get("page",1), per_page=request_data.get("per_page",20))

    return Response().force_type(Response.OK, "", json_data)

@store_bp.route('/<int:store_id>/order', methods=['POST'])
@inject
def create_order(store_id: int, service: StoreService):

    request_data = request.get_json()
    request_data['store_id'] = store_id
    create_order_model = CreateOrderModel.from_dict(request_data)

    order_model = service.create_order(create_order_model)

    return Response().force_type(Response.CREATED, "", order_model)

@store_bp.route('/<int:store_id>/<int:order_id>', methods=['PUT'])
@inject
def update_order(store_id: int, order_id: int, service: StoreService):

    request_data = request.get_json()
    request_data['store_id'] = store_id
    request_data['id'] = order_id

    create_order_model = UpdateOrderModel.from_dict(request_data)

    order_model = service.update_order(create_order_model)

    return Response().force_type(Response.CREATED, "", order_model)

@store_bp.route('/<int:store_id>/register_motoboy/<int:motoboy_id>', methods=['PATCH'])
@inject
def register_motoboy(store_id: int, motoboy_id: int, service: StoreService):


    store_model = service.register_motoboy(store_id=store_id, motoboy_id=motoboy_id)

    return Response().force_type(Response.OK, "", store_model)