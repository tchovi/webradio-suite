from sqlalchemy import Column, Integer, String
from .database import Base

class Show(Base):
    __tablename__ = "shows"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    host = Column(String)
    start_time = Column(String)
    end_time = Column(String)
