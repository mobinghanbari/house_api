from fastapi import APIRouter, Depends, Request, BackgroundTasks
from sqlalchemy.orm import Session
from databse import User
from databse.connection import get_db
from log.proccess import create_log
from .schema import ListingIn, ListingCh, ListingOU
from .endpoints import create_listing, get_listing_by_id, update_listing_by_id, delete_by_id
from ..authentication.oauth2 import current_user

listing_app = APIRouter(tags=["Listings"])


@listing_app.get("/listing/{id}", summary="Get A Listing", response_model=None)
async def get_lis(request: Request, background_tasks: BackgroundTasks, id: int, db: Session = Depends(get_db)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    return await get_listing_by_id(db=db, id=id)

@listing_app.post("/listing", summary="Create A Listing")
async def create(request: Request, background_tasks: BackgroundTasks, data: ListingIn, db: Session = Depends(get_db), current_user: User = Depends(current_user)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    return await create_listing(db=db, item=data, id=current_user.id)


@listing_app.put("/listing", summary="Update A Listing")
async def update_lis(request: Request, background_tasks: BackgroundTasks, data: ListingCh, db: Session = Depends(get_db), current_user: User = Depends(current_user)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    return await  update_listing_by_id(db=db, user_id=current_user.id, chitem=data)


@listing_app.delete("/listing", summary="Delete A Listing")
async def delete_lis(request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user: User = Depends(current_user)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    return await delete_by_id(db=db, id=current_user.id)
