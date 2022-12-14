from sqlalchemy import select

from apps.base.service import BaseService
from apps.couriers.service import CourierService
from apps.deliveries.schemas import DeliveryCreateSchema
from exceptions import DeliveryServiceException
from models import Delivery, DeliveryZone


class DeliveryService(BaseService):
    model = Delivery

    async def delivery(self, data: DeliveryCreateSchema):

        point_str = f'POINT({data.destination_point.latitude} ' \
                    f'{data.destination_point.longitude})'

        # get zone for given coords
        zone = (await self.manager.execute(
            select(DeliveryZone).where(
                DeliveryZone.geo_data.contains(point_str)
            ))).scalars().first()

        if not zone:
            raise DeliveryServiceException(
                status_code=422, details='Can not deliver here.'
            )

        courier_service = CourierService(session=self.session)
        courier = (await courier_service.manager.execute(
            courier_service._generate_select_query(
                is_available=True, zone_id=zone.id)
        )).scalars().first()

        if not courier:
            raise DeliveryServiceException(
                status_code=400, details='No available couriers for now.'
            )  # TODO add some kind of queue or periodic task for these cases

        # set courier's status as "not available"
        courier_service.manager.update(
            instance=courier.id, data={'is_available': False}
        )

        delivery_data = data.dict()
        delivery_data['courier_id'] = courier.id
        delivery_data['destination_point'] = point_str

        await self.session.commit()

        delivery = await self.manager.create(Delivery, delivery_data)

        return delivery
