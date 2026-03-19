from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Inventry(Base):
    __tablename__ = "inventry"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    qty = Column(Integer, nullable=False)
    description = Column(String, nullable=True)