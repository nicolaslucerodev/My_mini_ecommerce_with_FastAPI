from sqlmodel import Field, Relationship, SQLModel


class Product (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description:str 
    price: float 
    stock:int 
    category_id: int =Field(foreign_key="category.id")
    image_url:str

    category: "Category" =Relationship(back_populates="products")
    