from apps.base.service import BaseService
from models import Courier


class CourierService(BaseService):
    model = Courier
