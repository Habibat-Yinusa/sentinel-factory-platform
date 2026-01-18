from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    machine_type = Column(String, nullable=False)
    location = Column(String, nullable=True)
