from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from .schema import ListingIn,ListingCh
from databse import Listing

# Create
async def create_listing(db: Session, item:ListingIn, id: int):
    async with db.begin():
        obj = Listing(type=item.type, avalibalieNow=item.avalibalieNow, ownerId=id, address=item.address)
        db.add(obj)
        await db.commit()
        return obj

# Read
async def get_listing_by_id(db:Session, id: int):
    async with db.begin():
        stmt = select(Listing).where(Listing.id == id)
        result = await db.execute(stmt)
        user_obj = result.scalar()
        if user_obj:
            return {"type": user_obj.type, "avalibalieNow": user_obj.avalibalieNow, "address": user_obj.address}

        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail={"detail": "Item Not Founded"})


# Update
async def update_listing_by_id(db: Session, user_id: int, chitem:ListingCh):
    async with db.begin():
        stmt = select(Listing).where(Listing.ownerId == user_id)
        result = await db.execute(stmt)
        user_obj = result.scalar_one_or_none()
        if not user_obj:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"detail": "You don't have any listing"})
        if user_obj.ownerId != user_id:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"detail":"You don't have the primission to change the address"})
        user_obj.address = chitem.address
        await db.commit()
        return user_obj


async def delete_by_id(db: Session, id: int):
    async with db.begin():
        stmt = select(Listing).where(Listing.ownerId == id)
        result = await db.execute(stmt)
        user_obj = result.scalar_one_or_none()
        if user_obj:
            await db.delete(user_obj)
            await db.commit()
            return {"status_code":status.HTTP_200_OK, "detail":{"message":"Item deleted successfully"}}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message":"The House doesn't exist"})
