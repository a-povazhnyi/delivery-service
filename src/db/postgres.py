from typing import Any, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import settings

engine = create_async_engine(settings.DATABASE_URL)

Base = declarative_base()

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class BaseManager:

    def __init__(self, session):
        self.session = session

    def execute(self, query):
        """Execute query."""
        return self.session.execute(query)

    async def create(
            self, model: Type[ModelType],
            data: Union[CreateSchemaType, dict]
    ):
        """Create model instance"""

        if isinstance(data, BaseModel):
            data = data.dict()

        instance = model(**data)
        self.session.add(instance)
        await self.session.commit()

        return instance

    async def update(
            self,
            instance: ModelType,
            data: Union[UpdateSchemaType, dict[str, Any]]
    ):
        """Update model instance."""
        instance_dict = jsonable_encoder(instance)
        if not isinstance(data, dict):
            data = data.dict(exclude_unset=True)
        for field in instance_dict:
            if field in data:
                setattr(instance, field, data.get(field))

        self.session.add(instance)
        await self.session.commit()

        return instance

    async def delete(self, instance: ModelType):
        """Delete model instance."""
        await self.session.delete(instance)
        await self.session.commit()

        return instance
