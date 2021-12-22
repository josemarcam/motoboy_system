from injector import Binder
from flask_injector import request
from src.domain.motoboys.services import MotoboyService
from src.domain.motoboys.repositories import MotoboyRepository


def motoboy_module(binder: Binder):
        binder.bind(
            MotoboyRepository,
            to=MotoboyRepository,
            scope=request
        )
        
        binder.bind(
            MotoboyService,
            to=MotoboyService,
            scope=request
        )
