from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING: 
    from models.product import Product 


class ProductVariant (SQLModel, table=True):
    
    __tablename__="variants"
    #Entidades#
    id : int | None = Field(default=None, primary_key=True)
    size:str
    color:str
    
    #FK
    product_id : int = Field (foreign_key="products.id") 

   #Relation ORM
    product : Optional["Product"] = Relationship(back_populates="variants")