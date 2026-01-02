from pydantic import BaseModel

# To create contracts that enable data validation and documentation
from typing import Optional


class Message(BaseModel):
    message: str
    description: Optional[str] = None
    # it accepts both {'message':'xx'} and {'message':'xx', description:'xx'}


class Contact(BaseModel):
    contact: str
