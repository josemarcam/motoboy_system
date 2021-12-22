from injector import Binder

from flask import Flask
from flask_injector import FlaskInjector, singleton
from flask_sqlalchemy import SQLAlchemy

from src.config.database import db
from src.infra.di import (
    motoboy_module,
    store_module
)


def init_app(app: Flask):

    def application_module(binder: Binder):
        binder.bind(
            SQLAlchemy,
            to=db,
            scope=singleton,
        )

    FlaskInjector(app=app, modules=[
        application_module,
        motoboy_module,
        store_module,
    ])
