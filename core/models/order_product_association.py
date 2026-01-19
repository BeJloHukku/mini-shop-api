from typing import TYPE_CHECKING

from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .order import Order
    from .product import Product


class OrderProductAssociation(Base):
    __tablename__ = "order_product_association"
    __table_args__ = (
        UniqueConstraint(
            "product_id",
            "order_id",
            name="idx_unique_order_product",
        ),
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"),
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
    )
    count: Mapped[int] = mapped_column(
        default=1,
        server_default="1",
    )
    # unit_price: Mapped[int] = mapped_column(default=1)
    order: Mapped["Order"] = relationship(
        back_populates="product_details",
    )
    product: Mapped["Product"] = relationship(
        back_populates="order_details",
    )
