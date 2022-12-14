from apps.base.service import BaseService
from apps.delivery_zones.schemas import DeliveryZoneCreateSchema
from models import DeliveryZone


class DeliveryZoneService(BaseService):
    model = DeliveryZone

    async def create(self, data: DeliveryZoneCreateSchema):
        """Convert coords in form POLYGON(...)"""
        coords = ''
        for i in data.geo_data:
            coords += f'{i.latitude} {i.longitude}, '
        coords = coords[:-2]
        data.geo_data = f'POLYGON(({coords}))'
        return await super().create(data=data)
