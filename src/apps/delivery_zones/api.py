from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.base import get_session
from apps.delivery_zones.schemas import (
    DeliveryZoneCreateSchema,
    DeliveryZoneGetSchema,
    DeliveryZoneUpdateSchema
)
from apps.delivery_zones.service import DeliveryZoneService

router = APIRouter(prefix='/delivery_zone', tags=['Delivery Zones'])


@router.get('/{delivery_zone_id}', response_model=DeliveryZoneGetSchema)
async def get_delivery_zone(
        delivery_zone_id: str, session: AsyncSession = Depends(get_session)
):
    """Get delivery zone by ID."""
    return await DeliveryZoneService(session=session).get_by_id(
        instance_id=int(delivery_zone_id)
    )


@router.get('/list/', response_model=list[DeliveryZoneGetSchema])
async def get_delivery_zones_list(
        session: AsyncSession = Depends(get_session)
):
    """Get all delivery zones."""
    return await DeliveryZoneService(session=session).list()


@router.post('/', response_model=DeliveryZoneGetSchema)
async def create_delivery_zone(
        data: DeliveryZoneCreateSchema,
        session: AsyncSession = Depends(get_session)
):
    """Create delivery zone."""
    return await DeliveryZoneService(session=session).create(data=data)


@router.patch('/{delivery_zone_id}/', response_model=DeliveryZoneGetSchema)
async def update_delivery_zone(
        delivery_zone_id: str,
        data: DeliveryZoneUpdateSchema,
        session: AsyncSession = Depends(get_session)
):
    """Update delivery zone by ID."""
    return await DeliveryZoneService(session=session).update(
        instance_id=int(delivery_zone_id), data=data
    )


@router.delete('/{delivery_zone_id}/')
async def delete_delivery_zone(
        delivery_zone_id: str, session: AsyncSession = Depends(get_session)
):
    """Delete delivery zone by ID."""
    return await DeliveryZoneService(session=session).delete(
        instance_id=int(delivery_zone_id)
    )
