from sqlalchemy.ext.asyncio import AsyncSession

from db.postgres import async_session


async def get_session() -> AsyncSession:
    """Yields async session for database."""
    async with async_session() as session:
        yield session
