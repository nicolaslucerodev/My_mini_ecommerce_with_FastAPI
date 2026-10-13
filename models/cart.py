from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.cart_item import CartItem
    from models.user import User

class Cart (SQLModel, table = True):

    __tablename__="carts"
    id : Optional[int] = Field (default=None, primary_key= True)

    user_id : int = Field (foreign_key="users.id", index=True, unique=True)


    user : Optional["User"] = Relationship(back_populates="cart")
    cart_items: list["CartItem"] = Relationship(back_populates="carts", sa_relationship_kwargs={"cascade":"all, delete-orphan"})


    #Nota 1: sa_relationship_kwargs={"cascade":"all, delete-orphan"}