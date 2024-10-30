from abc import ABC, abstractmethod
from typing import Optional

from carts.dependencies import get_db
from carts.domain.models import Cart


class CartRepository(ABC):
    @abstractmethod
    def save(self, cart: Cart) -> None:
        pass

    @abstractmethod
    def get(self, cart_uuid: str) -> Optional[Cart]:
        pass

    @abstractmethod
    def get_all(self) -> Cart:
        pass

    @abstractmethod
    def update(self, cart: Cart) -> None:
        pass

    @abstractmethod
    def delete(self, cart: Cart) -> None:
        pass


class SQLAlchemyRepository(CartRepository):
    def save(self, cart: Cart) -> None:
        sqlalchemy_cart = cart.to_sqlalchemy()
        db = next(get_db())
        db.add(sqlalchemy_cart)
        db.commit()

    def get(self, cart_uuid: str) -> Optional[Cart]:
        pass

    def get_all(self) -> list[Cart]:
        pass

    def update(self, cart: Cart) -> None:
        pass

    def delete(self, cart: Cart) -> None:
        pass


cart_repository = SQLAlchemyRepository()
