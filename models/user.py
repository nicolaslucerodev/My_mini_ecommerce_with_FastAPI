from sqlmodel import Relationship, Field, SQLModel
from typing import TYPE_CHECKING, Optional
from datetime import datetime
from enum import Enum
from backend.utils.dates import utc_now

if TYPE_CHECKING: 
    from models.order import Order
    from models.cart import Cart


class Role(str, Enum):
    ADMIN = "admin"
    CUSTOMER= "customer"



class User (SQLModel, table=True):

    __tablename__ = "users"

    id : int | None = Field(default=None, primary_key= True)
    name : str = Field(max_length=40)
    last_name : str = Field(max_length=40)
    email:str = Field (unique=True, index=True, max_length=100)
    hashed_password : str = Field (max_length=100) #El límite de largo de la contraseña real se valida en el schema, antes de hashearla.
    phone : str = Field(default=None,unique=True)

    created_at:datetime =Field(default_factory=utc_now) 

    role : Role = Field(default=Role.CUSTOMER)

    
   

    orders : list["Order"] = Relationship(back_populates="user",sa_relationship_kwargs={"cascade":"all, delete-orphan"})
    cart: Optional["Cart"] = Relationship(back_populates="user", sa_relationship_kwargs={"uselist":False,"cascade":"all, delete-orphan"}) 
    #uselist: False le dice a SQLAlchemy que espere un solo objeto y no una lista

