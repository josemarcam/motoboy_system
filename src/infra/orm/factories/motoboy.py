from random import randint

from factory import alchemy, Faker, SubFactory, List

from src.config.database import db

from src.infra.orm.entities import Motoboy

class MotoboyFactory(alchemy.SQLAlchemyModelFactory):
    
    class Meta:
        model = Motoboy
        sqlalchemy_session = db.session

    name = Faker("first_name")
    fixed_rate = 2
    orders = []