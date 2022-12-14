from typing import TypeVar, Union

from pydantic import BaseModel
from sqlalchemy import select

from db.postgres import Base, BaseManager
from exceptions import DeliveryServiceException

ModelType = TypeVar('ModelType', bound=Base)


class BaseService:
    """Base service for handling CRUD operations."""

    model = None

    def __init__(self, session):
        self.manager = BaseManager(session=session)
        self.session = session

    def _generate_select_query(self, *fields, **conditions):
        """Generate select query for any fields and conditions"""
        selects = fields if fields else (self.model,)
        query = select(*selects)

        for condition in (
            (getattr(self.model, attr) == value)
            for attr, value in conditions.items()
            if value is not None
        ):
            query = query.where(condition)

        return query

    async def _get_instance(self, id_instance: int):
        """Get single instance by id"""
        return (await self.manager.execute(
            self._generate_select_query().where(self.model.id == id_instance)
        )).scalars().first()

    async def get_by_id(self, instance_id: int):
        """Get instance, raise 404 if not exist"""
        instance = await self._get_instance(instance_id)
        if not instance:
            raise DeliveryServiceException(
                status_code=404, details='Not found.'
            )
        return instance

    async def list(self):
        """Get list of instances"""
        res = (await self.manager.execute(select(self.model))).scalars().all()
        if not res:
            return []
        return res

    async def create(self, data: Union[BaseModel, dict]):
        """Create instance by id."""
        return await self.manager.create(model=self.model, data=data)

    async def update(self, instance_id: int, data: Union[BaseModel, dict]):
        """Update instance by id."""
        instance = await self._get_instance(instance_id)
        return await self.manager.update(instance, data)

    async def delete(self, instance_id: int):
        """Delete instance by id."""
        instance = await self.get_by_id(instance_id=instance_id)
        await self.manager.delete(instance=instance)
