from sqlalchemy.sql.schema import Table
from src.config.database import db

exclusivity_table = Table('exclusivities', db.metadata,
    db.Column("motoboy_id", db.ForeignKey("motoboys.id"), primary_key=True),
    db.Column("store_id", db.ForeignKey("stores.id"), primary_key=True)
)

class Motoboy(db.Model):
    __tablename__ = "motoboys"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(255), nullable=False)
    fixed_rate = db.Column('fixed_rate', db.Integer, nullable=False)

    orders = db.relationship("Order", back_populates='motoboy')

    stores = db.relationship("Store", secondary=exclusivity_table, back_populates='motoboys')

    created_at = db.Column('created_at', db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())