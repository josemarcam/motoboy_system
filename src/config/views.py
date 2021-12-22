from flask import Flask

from src.infra.views.motoboy import motoboy_bp
from src.infra.views.store import store_bp

def init_app(app: Flask):
    app.register_blueprint(motoboy_bp)
    app.register_blueprint(store_bp)