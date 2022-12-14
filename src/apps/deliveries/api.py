from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.base import get_session
from apps.deliveries.schemas import (
    DeliveryCreateManuallySchema,
    DeliveryCreateSchema,
    DeliveryGetSchema,
    DeliveryUpdateSchema
)
from apps.deliveries.service import DeliveryService

router = APIRouter(prefix='/delivery', tags=['Deliveries'])


@router.post('/manually', response_model=DeliveryGetSchema)
async def create_delivery_manually(
        data: DeliveryCreateManuallySchema,
        session: AsyncSession = Depends(get_session)
):
    """Create delivery manually. May be used by management."""
    return await DeliveryService(session=session).create(data=data)


@router.post('/', response_model=DeliveryGetSchema)
async def create_delivery(
        data: DeliveryCreateSchema,
        session: AsyncSession = Depends(get_session)
):
    """Create delivery."""
    return await DeliveryService(session=session).delivery(data=data)


@router.get('/{delivery_id}', response_model=DeliveryGetSchema)
async def get_delivery(
        delivery_id: str, session: AsyncSession = Depends(get_session)
):
    """Get delivery by ID"""
    return await DeliveryService(session=session).get_by_id(
        instance_id=int(delivery_id)
    )


@router.patch('/{delivery_id}/', response_model=DeliveryGetSchema)
async def update_delivery(
        delivery_id: str,
        data: DeliveryUpdateSchema,
        session: AsyncSession = Depends(get_session)
):
    """Update delivery."""
    return await DeliveryService(session=session).update(
        instance_id=int(delivery_id), data=data
    )


@router.delete('/{delivery_id}/')
async def delete_delivery(
        delivery_id: str, session: AsyncSession = Depends(get_session)
):
    """Delete delivery."""
    return await DeliveryService(session=session).delete(
        instance_id=int(delivery_id)
    )


@router.get('/list/', response_model=list[DeliveryGetSchema])
async def get_deliveries_list(session: AsyncSession = Depends(get_session)):
    """Get all deliveries."""
    return await DeliveryService(session=session).list()
