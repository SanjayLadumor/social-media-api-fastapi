from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, Annotated
from pydantic.types import conint

class PostModel(BaseModel):
    title : str
    content : str
    published : bool = True

class UpdatePost(BaseModel):
    title : str
    content : str
    published : bool = True

class UserResponse(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime

class PostResponse(BaseModel):
    id : int
    title : str
    content : str
    published : bool = True
    created_at : datetime
    owner_id : int
    owner : UserResponse

class PostOut(BaseModel):
    Post : PostResponse
    votes : int

class CreateUser(BaseModel):
    email : EmailStr
    password : str

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None

class Vote(BaseModel):
    post_id : int
    dir : Annotated[int, Field(le=1)]