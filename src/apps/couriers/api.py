from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.base import get_session
from apps.couriers.schemas import (
    CourierCreateSchema,
    CourierGetSchema,
    CourierUpdateSchema
)
from apps.couriers.service import CourierService

router = APIRouter(prefix='/courier', tags=['Couriers'])


@router.get('/{courier_id}', response_model=CourierGetSchema)
async def get_courier(
        courier_id: str, session: AsyncSession = Depends(get_session)
):
    """Get courier by ID."""
    return await CourierService(session=session).get_by_id(
        instance_id=int(courier_id)
    )


@router.get('/list/', response_model=list[CourierGetSchema])
async def get_couriers_list(session: AsyncSession = Depends(get_session)):
    """Get all couriers."""
    return await CourierService(session=session).list()


@router.post('/', response_model=CourierGetSchema)
async def create_courier(
        data: CourierCreateSchema, session: AsyncSession = Depends(get_session)
):
    """Create courier."""
    return await CourierService(session=session).create(data=data)


@router.patch('/{courier_id}', response_model=CourierGetSchema)
async def update_courier(
        courier_id: str,
        data: CourierUpdateSchema,
        session: AsyncSession = Depends(get_session)
):
    """Update courier by ID."""
    return await CourierService(session=session).update(
        instance_id=int(courier_id), data=data
    )


@router.delete('/{courier_id}')
async def delete_courier(
        courier_id: str, session: AsyncSession = Depends(get_session)
):
    """Delete courier by ID."""
    return await CourierService(session=session).delete(
        instance_id=int(courier_id)
    )
