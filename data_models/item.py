from pydantic import BaseModel
from sqlalchemy import (
    Column,
    Integer,
    String,
    ARRAY,
    Float,
    ForeignKey,
    JSON
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ItemFromNeuralApi(BaseModel):
    item_id: int


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    cte_id = Column(Integer)
    cte_name = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))
    description = Column(String)
    cte_props = Column(JSON)
    regions = Column(ARRAY(String))
    made_contracts = Column(Integer)
    suppliers = Column(JSON)
    country = Column(String)
    other_items_in_contracts = Column(String)
    cpgz_id = Column(Float)
    cpgz_code = Column(String)
    model = Column(String)
    price = Column(JSON)
