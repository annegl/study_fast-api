from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    message: str
    description: Optional[str] = None
    # it accepts both {'message':'xx'} and {'message':'xx', description:'xx'}


class Contact(BaseModel):
    contact: str
