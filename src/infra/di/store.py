from injector import Binder
from flask_injector import request
from src.domain.stores.services import StoreService
from src.domain.stores.repositories import StoreRepository, OrderRepository


def store_module(binder: Binder):
        
        binder.bind(
            StoreRepository,
            to=StoreRepository,
            scope=request
        )
        
        binder.bind(
            StoreService,
            to=StoreService,
            scope=request
        )
        
        binder.bind(
            OrderRepository,
            to=OrderRepository,
            scope=request
        )
