from dataclasses import dataclass
from typing import Optional
from src.shared.models import BaseModel

@dataclass
class CreateOrderModel(BaseModel):
    
    name: str
    total_value: int
    store_id: int
    motoboy_id: Optional[int] = None

    @classmethod
    def dict_filters(cls) -> list:
        return ["name", "total_value", "store_id", "motoboy_id"]
    



@dataclass
class OrderStoreModel(BaseModel):
    
    id:int
    name:str
    
    @classmethod
    def dict_filters(cls) -> list:
        return ["id", "name"]

@dataclass
class OrderMotoboyModel(BaseModel):
    
    id:int
    name:str

    @classmethod
    def dict_filters(cls) -> list:
        return ["id", "name"]

@dataclass
class UpdateOrderModel(BaseModel):
    
    id: int
    name: str
    total_value: int
    store_id: int
    motoboy_id: int

    @classmethod
    def dict_filters(cls) -> list:
        return ["id", "name", "total_value", "store_id", "motoboy_id"]

@dataclass
class OrderModel(BaseModel):
    
    id: str
    name: str
    total_value: int
    store: OrderStoreModel
    motoboy: OrderMotoboyModel

    @classmethod
    def dict_filters(cls) -> list:
        return ["id", "name", "total_value", "store", "motoboy"]

    @classmethod
    def dict_types(cls) -> dict:
        return {
            "store": OrderStoreModel,
            "motoboy": OrderMotoboyModel
        }
