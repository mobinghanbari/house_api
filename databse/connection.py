# from sqlalchemy import create_engine
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from databases import Database
# from databases import DatabaseURL
#
#
# # DATABASE_URL = "postgresql://postgres:ir.developer.py@localhost/postgres"
# DATABASE_URL = "postgresql://postgres:ir.developer.py@localhost/postgres"
#
# engine = create_engine(DATABASE_URL)
#
# Session = sessionmaker(bind=engine)
#
# Base = declarative_base()
#
#
# def get_db() -> Session:
#     db = Session()
#     try:
#         yield db
#     finally:
#         db.close()
#
#









from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://username:password@localhost/db_name"

engine = create_async_engine(
    url=DATABASE_URL,
    echo = True
)

Session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

Base = declarative_base()


async def get_db() -> Session:
    db = Session()
    try:
        yield db
    finally:
        await db.close()

