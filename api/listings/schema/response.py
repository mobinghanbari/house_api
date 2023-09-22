from pydantic import BaseModel
from databse import User


class ListingOU(BaseModel):
    type: str
    avalibalieNow: bool
    address: str


