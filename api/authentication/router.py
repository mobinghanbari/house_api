from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException, status, Request, Response
from fastapi import BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
import uuid
from sqlalchemy.orm import Session
from sqlalchemy import select
from databse import User
from databse.connection import get_db
from .oauth2 import create_access_token, current_user
from .endpoints import show_user
from ..users.hash_engine import Hash
from fastapi.security import OAuth2PasswordBearer

app_authentication = APIRouter(tags=["Authentication"])

@app_authentication.post("/token", summary="Get Token")
async def login_for_access_token(background_tasks: BackgroundTasks, request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    async with db.begin():
        pr = select(User).where(User.id == id)
        statement = await db.execute(pr)
        user = statement.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The Username Doesn't Have Exist")

        if not Hash.verify(user.hashedPassword, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The Password Is Incorrect")

        uuid_code = str(uuid.uuid1())
        user.session_uuid = uuid_code
        await db.commit()
        access_token = create_access_token(data={"sub": request.username, "uuid": uuid_code},
                                       expires_delta=timedelta(minutes=30))
        background_tasks.add_task(show_user, f"Welcome {user.fullName}")
        return {
            'access_token': access_token,
            'type_token': 'bearer',
            'userID': user.id,
            'username': user.email
        }

