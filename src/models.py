from geoalchemy2 import Geometry
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from db.postgres import Base

STATUSES_ENUM_TUPLE = ('created', 'in_progress', 'delivered')


class DeliveryZone(Base):
    __tablename__ = 'delivery_zones'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String)
    geo_data = Column(Geometry('POLYGON', spatial_index=False))

    couriers = relationship('Courier', backref='delivery_zone')


class Courier(Base):
    __tablename__ = 'couriers'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String)
    phone = Column(String, unique=True)

    # True if courier is in process of delivery now
    is_available = Column(
        Boolean, server_default='t', default=True, nullable=False
    )
    zone_id = Column(Integer, ForeignKey('delivery_zones.id'))

    deliveries = relationship(
        'Delivery', back_populates='couriers', uselist=False
    )


class Delivery(Base):
    __tablename__ = 'deliveries'

    id = Column(Integer, primary_key=True, autoincrement=True)

    courier_id = Column(Integer, ForeignKey('couriers.id'))
    destination_point = Column(Geometry('POINT', spatial_index=False))
    comment = Column(String)

    status = Column(
        ENUM(
            *STATUSES_ENUM_TUPLE,
            name='statuses_enum',
            create_type=False,
        ),
        default='created',
        server_default='created'
    )

    couriers = relationship(
        'Courier', back_populates='deliveries', uselist=False
    )
