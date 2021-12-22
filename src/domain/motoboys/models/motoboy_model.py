from dataclasses import dataclass
from typing import List, Optional
from src.shared.models.base_model import BaseModel
from datetime import datetime

@dataclass
class MotoboyStoreModel(BaseModel):

    name: str
    motoboy_percent: int

    @classmethod
    def dict_filters(cls) -> list:
        return ["name", "motoboy_percent"]

@dataclass
class MotoboyOrderModel(BaseModel):
    
    name: str
    store: MotoboyStoreModel
    total_value: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def dict_filters(cls) -> list:
        return ["name", "store", "total_value", "created_at", "updated_at"]

    @classmethod
    def dict_types(cls) -> dict:
        return {
            "store": MotoboyStoreModel
        }

@dataclass
class MotoboyModel(BaseModel):
    
    id: int
    name: str
    fixed_rate: int
    created_at: datetime
    updated_at: datetime

    orders: Optional[List[MotoboyOrderModel]] = None
    stores: Optional[List[MotoboyStoreModel]] = None

    @classmethod
    def dict_filters(cls) -> list:
        return ["id", "name", "fixed_rate", "orders", "stores", "created_at", "updated_at"]

    @classmethod
    def dict_types(cls) -> dict:
        return {
            "orders": MotoboyOrderModel,
            "stores": MotoboyStoreModel
        }

@dataclass
class ListMotoboyModel(BaseModel):

    count: int
    pages: int
    results: Optional[List[MotoboyModel]] = None

    @classmethod
    def dict_filters(cls) -> list:
        return ['count', 'pages', 'results']

    @classmethod
    def dict_types(cls) -> dict:
        return {
            'results': MotoboyModel
        }

@dataclass
class CreateMotoboyModel(BaseModel):
    
    name: str
    fixed_rate: int

    @classmethod
    def dict_filters(cls) -> list:
        return ["name", "fixed_rate"]
