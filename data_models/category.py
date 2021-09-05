from sqlalchemy import (
    Column,
    Integer,
    String
)

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    item = relationship("Item", backref="category")
