from sqlalchemy.orm import Mapped

from microshop.core.models import Base


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
