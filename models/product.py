from sqlmodel import Field, Relationship, SQLModel

from typing import Optional, TYPE_CHECKING
from decimal import Decimal

if TYPE_CHECKING:
    from models.category import Category
    from models.product_variant import ProductVariant

    
class Product (SQLModel, table=True):

    __tablename__="products"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    description: Optional[str] = Field(default=None, max_length=600)  
    is_active : bool= Field(default=True)
    price : Decimal = Field(max_digits=10, decimal_places=2)
    stock:int = Field(default=0)
    image_url:Optional[str] = Field(default=None, max_length=500)
#FK
    category_id : int= Field(foreign_key="categories.id", index=True)
#Relation ORM
    category : Optional["Category"] = Relationship(back_populates="products")
    variants:list["ProductVariant"] = Relationship(back_populates="product", sa_relationship_kwargs={"cascade":"all, delete-orphan"})