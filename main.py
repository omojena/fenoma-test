from fastapi import FastAPI
from routers import orders
import redis

app = FastAPI(title="Management Orders",
              description="Api for management orders",
              summary="",
              version="0.0.1",
              contact={
                  "email": "osmel.dubet@gmail.com",
              },)

app.include_router(orders.router)
redis_client = redis.Redis(host='localhost', port=6379)
