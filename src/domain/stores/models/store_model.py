from dataclasses import dataclass
from typing import List, Optional
from src.shared.models.base_model import BaseModel
from datetime import datetime

@dataclass
class StoreMotoboyModel(BaseModel):

    id: int
    name: str
    fixed_rate: int

    @classmethod
    def dict_filters(cls) -> list:
        return ["id", "name", "fixed_rate"]

@dataclass
class StoreOrderModel(BaseModel):
    
    id: int
    name: str
    total_value: int
    motoboy: StoreMotoboyModel
    created_at: datetime
    updated_at: datetime

    @classmethod
    def dict_filters(cls) -> list:
        return ["id", "name", "motoboy", "total_value", "created_at", "updated_at"]

    @classmethod
    def dict_types(cls) -> dict:
        return {
            "motoboy": StoreMotoboyModel
        }

@dataclass
class StoreModel(BaseModel):
    
    id: int
    name: str
    motoboy_percent: int
    created_at: datetime
    updated_at: datetime

    orders: Optional[List[StoreOrderModel]] = None
    motoboys: Optional[List[StoreMotoboyModel]] = None

    @classmethod
    def dict_filters(cls) -> list:
        return ["id", "name", "motoboy_percent", "orders", "motoboys", "created_at", "updated_at"]

    @classmethod
    def dict_types(cls) -> dict:
        return {
            "orders": StoreOrderModel,
            "motoboys": StoreMotoboyModel
        }

@dataclass
class ListStoreModel(BaseModel):

    count: int
    pages: int
    results: Optional[List[StoreModel]] = None

    @classmethod
    def dict_filters(cls) -> list:
        return ['count', 'pages', 'results']

    @classmethod
    def dict_types(cls) -> dict:
        return {
            'results': StoreModel
        }
