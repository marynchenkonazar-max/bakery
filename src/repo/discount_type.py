import uuid
from src.models import DiscountType
from sqlalchemy.orm import Session
class DiscountTypeRepository:
    def __init__(self, session: Session):
        self.session = session
    def get(self, id:uuid.UUID) -> type[DiscountType] | None:
        return self.session.get(DiscountType, id)
    def add(self, category:DiscountType) -> DiscountType:
        self.session.add(category)
        self.session.flush()
        return category
    def delete(self, category:DiscountType) -> None:
        self.session.delete(category)
        self.session.flush()