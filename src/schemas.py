from pydantic import BaseModel, EmailStr
from typing import Optional

# pydantic: to create contracts that enable data validation and documentation


class Message(BaseModel):
    message: str
    description: Optional[str] = None
    # it accepts both {'message':'xx'} and {'message':'xx', description:'xx'}


class UserSchema(BaseModel):  # what comes in
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):  # what goes out
    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):  # what exists inside the DB
    # UserDB inherits all fields from UserSchema and adds the database id
    id: int
