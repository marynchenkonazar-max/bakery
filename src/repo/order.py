import uuid
from src.models import Order
from sqlalchemy.orm import Session
class OrderRepository:
    def __init__(self, session: Session):
        self.session = session
    def get(self, id:uuid.UUID) -> type[Order] | None:
        return self.session.get(Order, id)
    def add(self, category:Order) -> Order:
        self.session.add(category)
        self.session.flush()
        return category
    def delete(self, category:Order) -> None:
        self.session.delete(category)
        self.session.flush()