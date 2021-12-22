from flask_script import Command, Option
from src.infra.orm.factories.order import OrderFactory
from src.infra.orm.factories.motoboy import MotoboyFactory
from src.infra.orm.factories.store import StoreFactory
from src.config.database import db
class SimulateEnviroment(Command):

    def run(self):
        pedidos_loja1 = [
            OrderFactory(name="PEDIDO 1", store=None, motoboy=None, total_value=5000),
            OrderFactory(name="PEDIDO 2", store=None, motoboy=None, total_value=5000),
            OrderFactory(name="PEDIDO 3", store=None, motoboy=None, total_value=5000)
        ]
        pedidos_loja2 = [
            OrderFactory(name="PEDIDO 1", store=None, motoboy=None, total_value=5000),
            OrderFactory(name="PEDIDO 2", store=None, motoboy=None, total_value=5000),
            OrderFactory(name="PEDIDO 3", store=None, motoboy=None, total_value=5000),
            OrderFactory(name="PEDIDO 4", store=None, motoboy=None, total_value=5000)
        ]
        pedidos_loja3 = [
            OrderFactory(name="PEDIDO 1", store=None, motoboy=None, total_value=5000),
            OrderFactory(name="PEDIDO 2", store=None, motoboy=None, total_value=5000),
            OrderFactory(name="PEDIDO 3", store=None, motoboy=None, total_value=10000)
        ]

        motoboy1 = MotoboyFactory(name="Motoboy 1")
        motoboy2 = MotoboyFactory(name="Motoboy 2")
        motoboy3 = MotoboyFactory(name="Motoboy 3")
        motoboy4 = MotoboyFactory(name="Motoboy 4")
        motoboy5 = MotoboyFactory(name="Motoboy 5")

        loja1 = StoreFactory(name="Loja1", motoboy_percent=5, orders=pedidos_loja1, motoboys=[motoboy4])
        loja2 = StoreFactory(name="Loja2", motoboy_percent=5, orders=pedidos_loja2, motoboys=[])
        loja3 = StoreFactory(name="Loja3", motoboy_percent=15, orders=pedidos_loja3, motoboys=[])

        db.session.add(loja1)
        db.session.add(loja2)
        db.session.add(loja3)

        db.session.add(motoboy1)
        db.session.add(motoboy2)
        db.session.add(motoboy3)
        db.session.add(motoboy5)
        db.session.commit()
        print("Dados Criados com sucesso")
        

