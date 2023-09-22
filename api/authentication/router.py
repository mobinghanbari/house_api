from fastapi import Depends, APIRouter, HTTPException, status, Request
from fastapi import BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
import time
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from databse import User
from databse.connection import get_db
from log.proccess import create_log
from .oauth2 import create_access_token
from .endpoints import show_user
from ..users.hash_engine import Hash
from sqlalchemy import select
app_authentication = APIRouter(tags=["Authentication"])

@app_authentication.post("/token", summary="Get Token")
async def login_for_access_token(background_tasks: BackgroundTasks, request: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    # user = db.query(User).filter(User.email == request.username).first()
    async with db.begin():
        statement = select(User).where(User.email == request.username)
        exc = await db.execute(statement)
        user = exc.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The Username Doesn't Have Exist")

    if not Hash.verify(user.hashedPassword, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The Password Is Incorrect")

    access_token = create_access_token(data={"sub": request.username})
    background_tasks.add_task(show_user, f"Welcome {user.fullName}")
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    return {
        'access_token': access_token,
        'type_token': 'bearer',
        'userID': user.id,
        'username': user.email
    }

