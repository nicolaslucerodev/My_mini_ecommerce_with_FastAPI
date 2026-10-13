from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING



if TYPE_CHECKING:
    from models.product import Product

class Category(SQLModel, table=True):

    __tablename__="categories"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100, unique=True)
    description: Optional[str] = Field(default=None, max_length=600)
    is_active: bool =Field(default=True)

    #Relation ORM
    products : list["Product"] = Relationship(back_populates="category", sa_relationship_kwargs={"cascade":"all, delete-orphan"})