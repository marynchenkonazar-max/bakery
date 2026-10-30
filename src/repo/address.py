import uuid
from src.models import Address
from sqlalchemy.orm import Session
class AddressRepository:
    def __init__(self, session: Session):
        self.session = session
    def get(self, id:uuid.UUID) -> type[Address] | None:
        return self.session.get(Address, id)
    def add(self, category:Address) -> Address:
        self.session.add(category)
        self.session.flush()
        return category
    def delete(self, category:Address) -> None:
        self.session.delete(category)
        self.session.flush()