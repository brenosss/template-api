from abc import ABC, abstractmethod
from typing import Optional

from carts.dependencies import get_db
from carts.domain.models import Cart
from carts.models import SQLAlchemyCart


class CartRepository(ABC):
    @abstractmethod
    def save(self, cart: Cart) -> None:
        pass

    @abstractmethod
    def get(self, cart_uuid: str) -> Optional[Cart]:
        pass

    @abstractmethod
    def get_all(self) -> list[Cart]:
        pass

    @abstractmethod
    def update(self, cart: Cart) -> None:
        pass

    @abstractmethod
    def delete(self, cart_uuid: str) -> None:
        pass


class SQLAlchemyRepository(CartRepository):
    def save(self, cart: Cart) -> None:
        sqlalchemy_cart = cart.to_sqlalchemy()
        db = next(get_db())
        db.add(sqlalchemy_cart)
        db.commit()

    def get(self, cart_uuid: str) -> Optional[Cart]:
        db = next(get_db())
        sqlalchemy_cart = db.query(SQLAlchemyCart).filter_by(uuid=cart_uuid).first()
        if not sqlalchemy_cart:
            return None
        return Cart.from_sqlalchemy(sqlalchemy_cart)

    def get_all(self) -> list[Cart]:
        db = next(get_db())
        carts = db.query(SQLAlchemyCart).all()
        return [Cart.from_sqlalchemy(cart) for cart in carts]

    def update(self, cart: Cart) -> None:
        db = next(get_db())
        db.query(SQLAlchemyCart).filter_by(uuid=cart.uuid).update(
            {
                "total_amount": cart.total_amount,
                "closed": cart.closed,
            }
        )
        db.commit()

    def delete(self, cart_uuid: str) -> None:
        db = next(get_db())
        db.query(SQLAlchemyCart).filter_by(uuid=cart_uuid).delete()
        db.commit()


cart_repository = SQLAlchemyRepository()
