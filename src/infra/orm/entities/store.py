from src.config.database import db
from src.infra.orm.entities.motoboy import exclusivity_table

class Store(db.Model):
    __tablename__ = "stores"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(255), nullable=False)
    motoboy_percent = db.Column('motoboy_percent', db.Integer, nullable=False)

    orders = db.relationship("Order", back_populates='store')
    
    motoboys = db.relationship("Motoboy", secondary=exclusivity_table, back_populates='stores')

    created_at = db.Column('created_at', db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())