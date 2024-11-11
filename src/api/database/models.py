from sqlalchemy import BigInteger
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase

from src.others import get_current_timestamp


class Base(DeclarativeBase):
    pass 


class User(Base): 
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(BigInteger, nullable=False) 
    is_enabled: Mapped[bool] = mapped_column(default=False) 
    date: Mapped[int] = mapped_column(BigInteger, default=get_current_timestamp)
