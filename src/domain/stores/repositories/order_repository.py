from typing import Union

from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import and_
from src.domain.stores.models.order_model import CreateOrderModel, OrderModel, UpdateOrderModel
from src.infra.orm.entities.order import Order
from src.shared.repositories.base_repository import BaseRepository


class OrderRepository(BaseRepository):

    def find_order(self, id: int = None, **kwargs) -> Union[OrderModel, None]:
        
        with self.session as session:
            query = session.query(Order)
            if id:
                order_entity = query.options(
                    joinedload(Order.store)
                ).options(
                    joinedload(Order.motoboy)
                ).filter(Order.id == id).first()
            else:
                
                filter_list = []
                for key in kwargs.keys():
                    filter_list.append(getattr(Order,key) == kwargs[key])
                
                order_entity = query.options(
                    joinedload(Order.store)
                ).options(
                    joinedload(Order.motoboy)
                ).filter(and_(True,*filter_list)).first()
            
            if order_entity:
                session.expunge_all()
            
            session.commit()
            
        
        if order_entity:
            order_entity = order_entity.__dict__
            return OrderModel.from_dict(order_entity)
        return None

    def create_order(self,create_order_model: CreateOrderModel) -> OrderModel:
        
        order_entity = Order()

        for field in create_order_model.dict_filters():
            setattr(order_entity,field,getattr(create_order_model,field))

        self.model = order_entity

        self.save()

        return self.find_order(self.model.id)

    def update_order(self,update_order_model: UpdateOrderModel) -> OrderModel:

        with self.session as session:

            query = session.query(Order)
            order_entity = query.filter(Order.id == update_order_model.id).first()
            
            session.expunge_all()
            session.commit()
            
        for field in update_order_model.dict_filters():
            setattr(order_entity,field,getattr(update_order_model,field))

        self.model = order_entity
        self.save()

        return self.find_order(self.model.id)