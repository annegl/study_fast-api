from pydantic import BaseModel
from typing import Optional

# pydantic: to create contracts that enable data validation and documentation


class Message(BaseModel):
    message: str
    description: Optional[str] = None
    # it accepts both {'message':'xx'} and {'message':'xx', description:'xx'}


class Contact(BaseModel):
    contact: str
