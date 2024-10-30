from dataclasses import dataclass
from datetime import datetime

from carts.models import SQLAlchemyCart


@dataclass
class Cart:
    uuid: str
    total_amount: float
    created_at: datetime
    closed: bool

    def to_sqlalchemy(self):
        return SQLAlchemyCart(
            uuid=self.uuid,
            total_amount=self.total_amount,
            created_at=self.created_at,
            closed=self.closed,
        )
