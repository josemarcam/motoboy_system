from random import randint

from factory import alchemy, Faker, SubFactory, List

from src.config.database import db

from src.infra.orm.entities import Store
from src.infra.orm.factories.motoboy import MotoboyFactory

class StoreFactory(alchemy.SQLAlchemyModelFactory):
    
    class Meta:
        model = Store
        sqlalchemy_session = db.session

    name = Faker('company', locale='pt_BR')
    motoboy_percent = Faker('random_int',min=1,max=10)
    orders = []
    motoboys = List( SubFactory(MotoboyFactory) for _ in range(randint(1,3)) )