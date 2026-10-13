from sqlmodel import SQLModel, Relationship, Field
from typing import  Optional, TYPE_CHECKING


if TYPE_CHECKING: 
    from models.cart import Cart
    from models.product_variant import ProductVariant
    from models.product import Product



class CartItem (SQLModel, table = True):

    __tablename__ ="cart_items"
    id:int | None = Field(default=None, primary_key=True)
    quantity: int = Field(default=1)

#FK
    cart_id : int = Field (foreign_key="carts.id", index= True)
    product_id: int=Field(foreign_key="products.id")
    product_variant_id: Optional[int] = Field (foreign_key="variants.id", default= None)


    product: Optional["Product"] =Relationship()
    product_variant :Optional["ProductVariant"]  = Relationship()
    carts : Optional["Cart"] = Relationship(back_populates="cart_items")