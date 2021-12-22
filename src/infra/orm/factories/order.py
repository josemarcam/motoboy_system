from random import randint

from factory import alchemy, Faker, SubFactory, List

from src.config.database import db

from src.infra.orm.entities import Order
from src.infra.orm.factories import (
    MotoboyFactory, 
    StoreFactory
)

class OrderFactory(alchemy.SQLAlchemyModelFactory):
    
    class Meta:
        model = Order
        sqlalchemy_session = db.session

    name = Faker('street_name')
    store = SubFactory(StoreFactory)
    motoboy = SubFactory(MotoboyFactory)
    total_value = Faker('random_int',min=100,max=10000)