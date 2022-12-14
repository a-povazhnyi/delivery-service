from typing import Optional

from pydantic import BaseModel

from apps.base.schemas import PointCoordinatesSchema


class DeliveryZoneCommon(BaseModel):
    name: str
    geo_data: list[PointCoordinatesSchema]
    couriers: Optional[list[int]]

    class Config:
        fields = {
            'name': {
                'title': "Delivery zone's name.",
                'example': 'Brooklyn'
            },
            'geo_data': {
                'title': 'GEO data'
            },
            'couriers': {
                'title': 'List of couriers fot this zone.',
                'example': [2, 3, 23]
            },
        }


class DeliveryZoneCreateSchema(DeliveryZoneCommon):
    couriers: Optional[list[int]]


class DeliveryZoneUpdateSchema(DeliveryZoneCommon):
    name: Optional[str]
    geo_data: Optional[str]
    couriers: Optional[list[int]]


class DeliveryZoneGetSchema(DeliveryZoneCommon):
    id: int
    geo_data: str

    class Config:
        orm_mode = True
        fields = {
            'id': {
                'example': 42
            }
        }
