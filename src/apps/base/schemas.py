from pydantic import BaseModel


class PointCoordinatesSchema(BaseModel):
    latitude: float
    longitude: float

    class Config:
        fields = {
            'latitude': {
                'title': "Point's latitude.",
                'example': 55.75
            },
            'longitude': {
                'title': "Point's longitude.",
                'example': 37.61
            },
        }
