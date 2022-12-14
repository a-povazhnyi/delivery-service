from typing import Any


class DeliveryServiceException(Exception):
    def __init__(self, status_code: int, details: Any):
        self.status_code = status_code
        self.details = details
