from fastapi import Request
from starlette.responses import JSONResponse

from exceptions import DeliveryServiceException


def handle_http_exception(
        request: Request, exception: DeliveryServiceException
):
    return JSONResponse(status_code=exception.status_code, content={
            'error': {
                'details': exception.details
            }
        }
    )
