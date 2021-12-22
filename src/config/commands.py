from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.infra.commands.simulate_enviroment import SimulateEnviroment

def init_app(app: Flask) -> Manager: 
    migrate = Migrate(app, app.db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('create-zax-environment', SimulateEnviroment)

    return manager
