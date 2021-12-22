from dataclasses import field
from typing import Union, List
from injector import inject
from src.domain.stores.models.order_model import UpdateOrderModel

from src.domain.stores.repositories import StoreRepository, OrderRepository
from src.domain.motoboys.services import MotoboyService

from src.domain.stores.models import (
    StoreModel,
    ListStoreModel,
    CreateOrderModel,
    OrderModel
)
from src.shared.exceptions import ValidationException


class StoreService:
    
    @inject
    def __init__(self,repository: StoreRepository, motoboy_service: MotoboyService, order_repository: OrderRepository):
        self._repository = repository
        self._order_repository = order_repository
        self._motoboy_service = motoboy_service

    def get_store(self, id:int = None, **kwargs) -> StoreModel:
        return self._repository.find_store(id,**kwargs)

    def get_store_list(self, page, per_page) -> ListStoreModel:
        
        return self._repository.find_list_store(
            page=int(page),
            per_page=int(per_page)
        )
    
    def register_motoboy(self, store_id:int, motoboy_id: int):

        store_model = self.get_store(store_id)
        motoboy_model = self._motoboy_service.get(motoboy_id)

        if not store_model:
            raise ValidationException(
                message="Loja não existente no sistema",
                field="store_id",
                field_message="id não existente no sistema",
                validation_type="not_found"
            )
        
        if not motoboy_model:
            raise ValidationException(
                message="Motoboy não existente no sistema",
                field="motoboy_id",
                field_message="id não existente no sistema",
                validation_type="not_found"
            )
        if store_model.motoboys:
            for motoboy in store_model.motoboys:
                if motoboy.id == motoboy_id:
                    raise ValidationException(
                        message=f"Motoboy ja registrado para a loja {store_id}",
                        field="motoboy_id",
                        field_message=f"id ja registrado para a loja {store_id}",
                        validation_type=""
                    )
        return self._repository.register_motoboy(store_id, motoboy_id)


    def create_order(self, create_order_model:CreateOrderModel) -> OrderModel:
        
        store_model = self.get_store(create_order_model.store_id)
        
        if not store_model:
            raise ValidationException(
                message="Loja não existente no sistema",
                field="store_id",
                field_message="id não existente no sistema",
                validation_type="not_found"
            )
        
        if create_order_model.motoboy_id:
            
            motoboy_model = self._motoboy_service.get(create_order_model.motoboy_id)
            if not motoboy_model:
                raise ValidationException(
                message="Motoboy não existente no sistema",
                field="motoboy_id",
                field_message="id não existente no sistema",
                validation_type="not_found"
            )

        return self._order_repository.create_order(create_order_model)

    def update_order(self, update_order_model: UpdateOrderModel):

        store_model = self.get_store(update_order_model.store_id)
        
        if not store_model:
            raise ValidationException(
                message="Loja não existente no sistema",
                field="store_id",
                field_message="id não existente no sistema",
                validation_type="not_found"
            )
        
        if update_order_model.motoboy_id:
            
            motoboy_model = self._motoboy_service.get(update_order_model.motoboy_id)
            if not motoboy_model:
                raise ValidationException(
                message="Motoboy não existente no sistema",
                field="motoboy_id",
                field_message="id não existente no sistema",
                validation_type="not_found"
            )

        return self._order_repository.update_order(update_order_model)