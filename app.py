from flask import Flask
from src import config
from flask_migrate import Migrate
from src.config import database, views, exceptions, di

def create_app(runtime_config: dict = None) -> Flask:
        
    app = Flask(__name__)
    config.init_app(app, runtime_config)
    database.init_app(app)
    migrate = Migrate(app, app.db)
    views.init_app(app)
    exceptions.init_app(app)
    di.init_app(app)
    # jwt.init_app(app)
    # shell.init_app(app)
    # templates.init_app(app)

    return app
