from fastapi import FastAPI
from routers import orders

app = FastAPI(title="Management Orders",
              description="Api for managing orders",
              summary="",
              version="0.0.1",
              contact={
                  "email": "osmel.dubet@gmail.com",
              },)

app.include_router(orders.router)
