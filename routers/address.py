# import sys
# sys.path.append("..")
#
# from typing import Optional
# from fastapi import APIRouter, Depends, HTTPException
# import models
# from database import engine, SessionLocal
# from sqlalchemy.orm import Session
# from pydantic import BaseModel, Field
# from .auth import get_current_user, get_user_exception
#
#
# router = APIRouter(
#     prefix="/address",
#     tags=["address"],
#     responses={404: {"description": "Not Found"}}
# )
#
#
# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()
#
#
# class Address(BaseModel):
#     address1: str
#     address2: Optional[str]
#     city: str
#     state: str
#     country: str
#     postal_code: str
#
#
# @router.post("/")
# async def create_address(address: Address,
#                          db: Session = Depends(get_db),
#                          user: dict() = Depends(get_current_user)):
#     if not user:
#         return get_user_exception()
#     address_model = models.Address()
#     address_model.address1 = address.address1
#     address_model.address2 = address.address2
#     address_model.city = address.city
#     address_model.state = address.state
#     address_model.country = address.country
#     address_model.postal_code = address.postal_code
#
#     db.add(address_model)
#     db.flush()  # it is like commit instead it stages the changes to be committed hint: git add.
#                 # It returns an ID - in our case the address.id
#
#     user_model = db.query(models.Users).filter(models.Users.id == user.get("Id")).first()
#     user_model.address_id = address_model.id
#
#     db.add(user_model)
#     db.commit()
#     return successful_response(201)
#
#
# def successful_response(status_code: int):
#     return {"Status Code": status_code, "Transaction": "Successful"}
#
#
# @router.get("/")
# async def get_addresses(db: Session = Depends(get_db)):
#     return db.query(models.Address).all()
#
#
# @router.get("/user")
# async def read_all_by_user(user: dict() = Depends(get_current_user),
#         db: Session = Depends(get_db)):
#     return db.query(models.Address).filter(models.Address.user_address == user.get("Id")).all()
