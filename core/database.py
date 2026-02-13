from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from config.settings import settings

DATABASE_URL = settings.DATABASE_URL

engine = None
SessionLocal = None

if DATABASE_URL:
    engine = create_async_engine(
        DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"),
        echo=False,
        future=True
    )

    SessionLocal = async_sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

async def check_database():
    if not engine:
        return False
    try:
        async with engine.begin() as conn:
            await conn.execute("SELECT 1")
        return True
    except SQLAlchemyError:
        return False
