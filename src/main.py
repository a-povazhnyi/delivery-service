import uvicorn
from fastapi import FastAPI

from apps import router
from exceptions import DeliveryServiceException
from handlers import handle_http_exception
from settings import settings

app = FastAPI()

app.include_router(router)

app.add_exception_handler(DeliveryServiceException, handle_http_exception)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        debug=True
    )
