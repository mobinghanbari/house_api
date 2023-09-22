import redis.asyncio as redis
from fastapi import FastAPI, Depends, Request, BackgroundTasks
import time
from datetime import datetime, timedelta

from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from api import user_app, app_authentication, listing_app
from api.users.seeder import seed_users
from log.proccess import insert, create_log

app = FastAPI(title="Real State", description="House Information")
app.include_router(user_app)
app.include_router(app_authentication, dependencies=[Depends(RateLimiter(times=5, minutes=1))])
app.include_router(listing_app)

@app.on_event("startup")
async def startup():
    rediss = redis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(rediss)

@app.get("/", dependencies=[Depends(RateLimiter(times=5, minutes=1))], summery="Home")
async def index(request: Request, background_tasks: BackgroundTasks):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port} {request.url}', Client Host='{request.client.host}'")
    return {"msg": "Hello World"}
insert()



