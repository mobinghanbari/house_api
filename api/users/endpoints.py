from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from api.users.schema import UserIn, UserCh
from databse import User
from .hash_engine import Hash

# Create User
async def create_user(db: Session, student: UserIn):
    async with db.begin():
        obj = User(userName=student.userName, fullName=student.fullName, email=student.email, hashedPassword=Hash.bcrypt(student.hashedPassword), DoB=student.DoB, gender=student.gender)
        db.add(obj)
        await db.commit()
        return obj

# Read Users
async def get_user_by(id: int, db: AsyncSession):
    async with db.begin():
        pr = select(User).where(User.id == id)
        statement = await db.execute(pr)
        user = statement.scalar_one_or_none()
        return user

# Update Users
async def update_user_by_id(id: int, user: UserCh, db: AsyncSession):
    async with db.begin():
        # Fetch the user asynchronously
        stmt = select(User).where(User.id == id)
        result = await db.execute(stmt)
        user_obj = result.scalar_one_or_none()

        if user_obj:
            # Update the user's email
            user_obj.email = user.email
            await db.commit()

        return user_obj

# Delete Users
async def delete_user_by_id(id: int, db: Session):
    async with db.begin():
        stmt = select(User).where(User.id == id)
        result = await db.execute(stmt)
        user_obj = result.scalar_one_or_none()


        if user_obj:
            await db.delete(user_obj)
            await db.commit()
            return {"status_code":status.HTTP_200_OK, "detail":{"message":"Item deleted successfully"}}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message":"The user doesn't exist"})
