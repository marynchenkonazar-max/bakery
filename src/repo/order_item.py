import uuid
from src.models import OrderItem
from sqlalchemy.orm import Session
class OrderItemRepository:
    def __init__(self, session: Session):
        self.session = session
    def get(self, id:uuid.UUID) -> type[OrderItem] | None:
        return self.session.get(OrderItem, id)
    def add(self, category:OrderItem) -> OrderItem:
        self.session.add(category)
        self.session.flush()
        return category
    def delete(self, category:OrderItem) -> None:
        self.session.delete(category)
        self.session.flush()