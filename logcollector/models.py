from sqlalchemy import Column, Integer, Float
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class DataPoint(Base):
    __tablename__ = 'datapoint'

    id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP)
    dim1 = Column(Integer)
    dim2 = Column(Integer)
    value = Column(Float)

    def __init__(self, timestamp, dim1, dim2, value):
        self.timestamp = timestamp
        self.dim1 = dim1
        self.dim2 = dim2
        self.value = value
