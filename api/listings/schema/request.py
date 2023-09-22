from pydantic import BaseModel
from fastapi import Request
class ListingIn(BaseModel):
    type: str
    avalibalieNow: bool
    # ownerId: int
    address: str



class ListingCh(BaseModel):
    address: str