from typing import Optional

from pydantic import BaseModel, Field


class CourierCommon(BaseModel):
    name: str
    phone: str = Field(max_length=12)
    zone_id: int

    class Config:
        orm_mode = True

        fields: dict = {
            'name': {
                'title': "Courier's name.",
                'example': 'John Doe'
            },
            'phone': {
                'title': "Courier's phone number.",
                'example': '74956291010'
            },
            'zone_id': {
                'title': 'ID of delivery zone.',
                'example': 5
            },
        }


class CourierGetSchema(CourierCommon):
    id: int
    is_available: bool

    class Config:
        orm_mode = True
        fields: dict = {
            'id': {
                'title': "Courier's ID.",
                'example': 2
            }
        }


class CourierCreateSchema(CourierCommon):
    pass


class CourierUpdateSchema(CourierCommon):
    name: Optional[str]
    phone: Optional[str] = Field(max_length=12)
    zone_id: Optional[int]
