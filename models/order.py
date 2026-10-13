from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING,  Optional
from datetime import datetime
from utils.dates import utc_now
from enum import Enum
from decimal import Decimal


class OrderState(str, Enum):
    PENDING = "pending" #
    COMPLETED = "completed"
    CANCELED = "canceled"


if TYPE_CHECKING:
    from models.user import User
    from models.order_item import OrderItem


class Order (SQLModel, table= True):

    __tablename__="orders"

    #Entidades
    id : int | None =  Field(default=None, primary_key=True)
    created_at: datetime =Field(default_factory=utc_now) 
    state: OrderState = Field(default=OrderState.PENDING, index=True)
    total: Decimal = Field(max_digits=12,decimal_places=2)
    name: str = Field(default=None, max_length=100)
    last_name: str = Field(default=None, max_length=100)
    email: str = Field(default=None, max_length=100, index=True)
    phone: str = Field(default=None, max_length=20)
    
    
    
    #relaciones 
    user_id: Optional[int] = Field (default=None, foreign_key="users.id", index=True) #¿De quién es la orden de compra?
    
    #orm 
    user: Optional["User"] = Relationship(back_populates="orders") # ¿De quién es la orden de compra?
    items: list["OrderItem"] = Relationship(back_populates="order", sa_relationship_kwargs={"cascade":"all, delete-orphan"}) # ¿Qué items tiene la orden de compra?
