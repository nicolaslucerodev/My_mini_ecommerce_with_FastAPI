from sqlmodel import Field, SQLModel, Relationship


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    
    products: list["Product"] = Relationship(back_populates="category")