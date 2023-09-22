from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey,String, CheckConstraint, DateTime, Boolean
from datetime import datetime
from databse.connection import Base



class Listing(Base):
    __tablename__ = "listings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, CheckConstraint("type IN ('HOUSE', 'APARTMENT')", name="check_type"), nullable=False)
    avalibalieNow = Column(Boolean, default=True)
    ownerId = Column(Integer, ForeignKey("users.id"))
    address = Column(String, nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updatedAt = Column(DateTime, default=datetime.utcnow(), nullable=False)
    user = relationship("User", back_populates="listing")



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String, nullable=False)
    fullName = Column(String)
    email = Column(String, nullable=False)
    hashedPassword = Column(String, nullable=False)
    DoB = Column(String, nullable=False)
    gender = Column(String, CheckConstraint("gender IN ('Male', 'Female')", name="check_gender"))
    createdAt = Column(DateTime, default=datetime.utcnow(),  nullable=False)
    updatedAt = Column(DateTime, default=datetime.utcnow(), nullable=False)
    listing = relationship("Listing", back_populates="user")