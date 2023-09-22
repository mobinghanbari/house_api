from fastapi import APIRouter, Depends, Request, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from databse import User
from log.proccess import create_log
from .endpoints import create_user, get_user_by, update_user_by_id, delete_user_by_id
from databse.connection import get_db
from .schema import UserIn, UserCh
from ..authentication.oauth2 import current_user

user_app = APIRouter(tags=["Users"])


# Read
@user_app.get("/users", summary="Recive Your Information")
async def get_user(request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user: User = Depends(current_user)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    return await get_user_by(id=current_user.id, db=db)


# Create
@user_app.post("/users", summary="Register New User")
async def create_new_user(request: Request, background_tasks: BackgroundTasks, user: UserIn,
                          db: Session = Depends(get_db)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    return await create_user(db=db, student=user)


# Update
@user_app.put("/users", summary="Change The User Info")
async def update_user(request: Request, background_tasks: BackgroundTasks, user: UserCh, db: AsyncSession = Depends(get_db), current_user: User = Depends(current_user)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    return await update_user_by_id(id=current_user.id, user=user, db=db)


# Delete
@user_app.delete("/users", summary="Delete The User")
async def delete_user(request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user: User = Depends(current_user)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    return await delete_user_by_id(id=current_user.id, db=db)
