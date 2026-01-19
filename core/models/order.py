from typing import TYPE_CHECKING
from datetime import datetime, UTC

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .product import Product
    from .order_product_association import OrderProductAssociation


class Order(Base):
    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(UTC),
    )
    products: Mapped[list["Product"]] = relationship(
        secondary="order_product_association",
        back_populates="orders",
    )
    product_details: Mapped[list["OrderProductAssociation"]] = relationship(
        back_populates="order",
    )
