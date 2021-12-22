from flask import Flask
from src import config
from src.config import database, commands, di

def create_app():
    
    app = Flask(__name__)

    config.init_app(app)
    database.init_app(app)
    manager = commands.init_app(app)
    di.init_app(app)

    return manager

if __name__ == "__main__":
    manager = create_app()
    manager.run()
