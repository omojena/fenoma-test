from pydantic import BaseModel

from database.database import Base, engine
from sqlalchemy import Column, Integer, String, Float


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
    status: str


Base.metadata.create_all(engine)
