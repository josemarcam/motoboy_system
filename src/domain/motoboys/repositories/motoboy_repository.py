from typing import Union

from sqlalchemy.orm import joinedload
from sqlalchemy import and_, desc

from src.config.database import db
from src.domain.motoboys.models.motoboy_model import CreateMotoboyModel, ListMotoboyModel
from src.infra.orm.entities import Motoboy
from src.infra.orm.entities.order import Order
from src.shared.repositories.base_repository import BaseRepository
from src.domain.motoboys.models import MotoboyModel


class MotoboyRepository(BaseRepository):
    
    def find_motoboy(self, id: int = None, **kwargs) -> Union[MotoboyModel, None]:
        
        with self.session as session:
            query = session.query(Motoboy)
            if id:
                motoboy_entity = query.options(
                    joinedload(Motoboy.orders)
                ).options(
                    joinedload(Motoboy.orders, Order.store)
                ).options(
                    joinedload(Motoboy.stores)
                ).filter(Motoboy.id == id).first()
            else:
                filter_list = []
                for key in kwargs.keys():
                    filter_list.append(getattr(Motoboy,key) == kwargs[key])
                motoboy_entity = query.options(
                    joinedload(Motoboy.orders)
                ).options(
                    joinedload(Motoboy.orders, Order.store)
                ).options(
                    joinedload(Motoboy.stores)
                ).filter(and_(True,*filter_list)).first()
            
            if motoboy_entity:
                session.expunge_all()
            
            session.commit()
            
        if motoboy_entity:
            motoboy_entity = motoboy_entity.__dict__
            return MotoboyModel.from_dict(motoboy_entity)
        return None

    def find_list_motoboy(self,page: int = 1, per_page: int = 20) -> ListMotoboyModel:
        
            
        query = db.session.query(Motoboy)
        
        motoboys_entity = query.options(
            joinedload(Motoboy.orders)
        ).options(
            joinedload(Motoboy.orders, Order.store)
        ).options(
            joinedload(Motoboy.stores)
        ).order_by(desc(Motoboy.id))
        
        motoboys_paginated = motoboys_entity.paginate(page, per_page)

        dict_paginated_model = {"count":motoboys_paginated.total,"pages":motoboys_paginated.pages,"results":motoboys_paginated.items or None}

        
        paginated_model = ListMotoboyModel.from_dict(dict_paginated_model)
        
        return paginated_model

    def create_motoboy(self,create_motoboy_model: CreateMotoboyModel) -> MotoboyModel:
        
        motoboy_entity = Motoboy()

        for field in create_motoboy_model.dict_filters():
            setattr(motoboy_entity,field,getattr(create_motoboy_model,field))

        self.model = motoboy_entity

        self.save()

        return self.find_motoboy(self.model.id)