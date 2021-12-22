from typing import Union

from sqlalchemy.orm import joinedload
from sqlalchemy import and_, desc
from src.config.database import db

from src.infra.orm.entities import Store
from src.infra.orm.entities.motoboy import Motoboy
from src.infra.orm.entities.order import Order
from src.shared.repositories.base_repository import BaseRepository
from src.domain.stores.models import (
    CreateOrderModel, 
    OrderModel, 
    UpdateOrderModel, 
    ListStoreModel, 
    StoreModel
)


class StoreRepository(BaseRepository):
    
    def find_store(self, id: int = None, **kwargs) -> Union[StoreModel, None]:
        
        with self.session as session:
            query = session.query(Store)
            if id:
                store_entity = query.options(
                    joinedload(Store.orders)
                ).options(
                    joinedload(Store.orders, Order.motoboy)
                ).options(
                    joinedload(Store.motoboys)
                ).filter(Store.id == id).first()
            else:
                
                filter_list = []
                for key in kwargs.keys():
                    filter_list.append(getattr(Store,key) == kwargs[key])
                
                store_entity = query.options(
                    joinedload(Store.orders)
                ).options(
                    joinedload(Store.orders, Order.motoboy)
                ).options(
                    joinedload(Store.motoboys)
                ).filter(and_(True,*filter_list)).first()
            
            if store_entity:
                session.expunge_all()
            
            session.commit()
            
        
        if store_entity:
            store_entity = store_entity.__dict__
            return StoreModel.from_dict(store_entity)
        return None

    def find_list_store(self,page: int = 1, per_page: int = 20) -> ListStoreModel:
        
            
        query = db.session.query(Store)
        
        stores_entity = query.options(
            joinedload(Store.orders)
        ).options(
            joinedload(Store.orders, Order.motoboy)
        ).options(
            joinedload(Store.motoboys)
        ).order_by(desc(Store.id))
        
        stores_paginated = stores_entity.paginate(page, per_page)

        dict_paginated_model = {"count":stores_paginated.total,"pages":stores_paginated.pages,"results":stores_paginated.items or None}

        
        paginated_model = ListStoreModel.from_dict(dict_paginated_model)
        
        return paginated_model
    
    def register_motoboy(self, store_id: int, motoboy_id: int) -> StoreModel:
        
        with self.session as session:
            store_query = session.query(Store)
            motoboy_query = session.query(Motoboy)
            
            store_entity = store_query.options(
                joinedload(Store.motoboys)
            ).filter(Store.id == store_id).first()

            motoboy_entity = motoboy_query.filter(Motoboy.id == motoboy_id).first()

            
            session.expunge_all()
            session.commit()
        
        store_entity.motoboys.append(motoboy_entity)

        self.model = store_entity
        self.save()
        
        return self.find_store(store_id)
