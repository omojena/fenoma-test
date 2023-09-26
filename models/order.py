from enum import Enum

from pydantic import BaseModel

from database.database import Base, engine
from sqlalchemy import Column, Integer, String, Float, Enum as EnumColumn


class OrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELED = "canceled"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    item = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    status = Column(String)


class OrderResponse(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: OrderStatus


Base.metadata.create_all(engine)
