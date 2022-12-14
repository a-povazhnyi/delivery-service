from typing import Optional

from pydantic import BaseModel

from apps.base.schemas import PointCoordinatesSchema


class DeliveryCommon(BaseModel):
    courier_id: int
    destination_point: str
    comment: str
    status: str

    class Config:
        fields = {
            'courier_id': {
                'title': 'Courier ID.',
                'example': 3
            },
            'destination_point': {
                'title': 'Destination point.',
                'example': "POINT(4 1)"
            },
            'comment': {
                'title': 'Comment.',
                'example': 'Please deliver ASAP!'
            },
            'status': {
                'title': 'Delivery status.',
                'example': 'created'
            },
        }


class DeliveryCreateManuallySchema(DeliveryCommon):
    pass


class DeliveryCreateSchema(BaseModel):
    destination_point: PointCoordinatesSchema
    comment: str

    class Config:
        fields = {
            'destination_point': {
                'title': 'Destination point.',
                'example': {
                    'latitude': 55.75,
                    'longitude': 37.61
                }
            },
            'comment': {
                'title': 'Comment',
                'example': 'ASAP please!'
            },
        }


class DeliveryGetSchema(DeliveryCommon):
    id: int

    class Config:
        orm_mode = True
        fields = {
            'id': {
                'example': 43
            }
        }


class DeliveryUpdateSchema(DeliveryCommon):
    courier_id: Optional[int]
    destination_point: Optional[str]
    comment: Optional[str]
    status: Optional[str]
    courier: Optional[int]
