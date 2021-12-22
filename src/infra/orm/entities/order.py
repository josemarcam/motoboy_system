from src.config.database import db


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(255), nullable=False)
    total_value = db.Column('total_value', db.String(255), nullable=False)
    store_id = db.Column('store_id', db.Integer, db.ForeignKey('stores.id'))
    motoboy_id = db.Column('motoboy_id', db.Integer, db.ForeignKey('motoboys.id'))

    motoboy = db.relationship("Motoboy", back_populates='orders', uselist=False)
    store = db.relationship("Store", back_populates='orders', uselist=False)

    created_at = db.Column('created_at', db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())