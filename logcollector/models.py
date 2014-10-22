from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DataPoint(Base):
    __tablename__ = 'datapoint'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    dim1 = Column(Integer)
    dim2 = Column(Integer)
    value = Column(Float)

    def __init__(self, timestamp, dim1, dim2, value):
        self.timestamp = datetime.fromtimestamp(int(timestamp))
        self.dim1 = int(dim1)
        self.dim2 = int(dim2)
        self.value = float(value)
