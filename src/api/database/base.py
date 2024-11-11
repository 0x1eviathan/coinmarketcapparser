from typing import Any, List

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .models import Base, User

from src.config import settings


class DatabaseAPI:
    def __init__(self): 
        self.engine = create_async_engine(url=settings.database_url, echo=False)
        self.async_session_maker = async_sessionmaker(bind=self.engine, expire_on_commit=False)
        self.user = self.User(async_session_maker=self.async_session_maker)

    async def init_models(self) -> None: 
        async with self.engine.begin() as engine: 
            await engine.run_sync(Base.metadata.create_all)
            
    class User: 
        def __init__(self, async_session_maker: async_sessionmaker): 
            self.async_session_maker = async_session_maker
            
        async def add(self, chat_id: int) -> None: 
            async with self.async_session_maker.begin() as session: 
                stmt = insert(User).values(chat_id=chat_id) 
                
                await session.execute(stmt)
        
        async def get(self, chat_id: int) -> User: 
            async with self.async_session_maker.begin() as session: 
                stmt = select(User).where(User.chat_id == chat_id) 
                result = await session.execute(stmt) 
                
                user = result.scalar() 
                
                return user
            
        async def update(self, chat_id: int, **kwargs: Any) -> None: 
            async with self.async_session_maker.begin() as session: 
                stmt = select(User).where(User.chat_id == chat_id) 
                result = await session.execute(stmt) 
                
                user = result.scalar() 
                
                for key, value in kwargs.items():
                    setattr(user, key, value)
            
        # async def gets(self, **kwargs: Any) -> List[User]: 
        #     async with self.async_session_maker.begin as session: 
        #         stmt = select(User).where(
        #             *[getattr(User, key) == value for key, value in kwargs.items()]
        #         )
                
        #         result = await session.execute(stmt)
        #         users = result.scalars().all()
                
        #         return users
