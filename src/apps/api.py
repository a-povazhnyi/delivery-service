from fastapi import APIRouter

from apps.couriers import router as couriers_router
from apps.deliveries import router as deliveries_router
from apps.delivery_zones import router as delivery_zones_router

router = APIRouter()

router.include_router(deliveries_router)
router.include_router(couriers_router)
router.include_router(delivery_zones_router)


@router.get('/healthcheck/', tags=['Test'])
async def healthcheck():
    """
    Healthcheck endpoint.
    """
    return {'status': 'alive'}
