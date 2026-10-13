from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from utils.dates import utc_now
if TYPE_CHECKING:
    from models.order import Order
    from models.product import Product
    from models.product_variant import ProductVariant


class OrderItem(SQLModel, table=True):
    __tablename__ = "order_items"

    id: int | None = Field(default=None, primary_key=True)
    quantity: int = Field(default=1)
    date: datetime=Field(default_factory=utc_now) 
    


    order_id: int = Field(foreign_key="orders.id", index=True)
    product_id: int = Field(foreign_key="products.id", index=True)
    product_variant_id: int | None = Field(foreign_key="variants.id", default=None, index=True)
    

    # Relationships
    order: "Order" = Relationship(back_populates="order_items")
    product: "Product" = Relationship()
    product_variant: "ProductVariant" | None = Relationship()