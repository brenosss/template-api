from sqlalchemy import Boolean, Column, String, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SQLAlchemyCart(Base):
    __tablename__ = "carts"

    uuid = Column(String, primary_key=True, index=True)
    total_amount = Column(Numeric, nullable=False)
    closed = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)
