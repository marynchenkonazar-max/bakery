import uuid
from src.models import User
from sqlalchemy.orm import Session
class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    def get(self, id:uuid.UUID) -> type[User] | None:
        return self.session.get(User, id)
    def add(self, category:User) -> User:
        self.session.add(category)
        self.session.flush()
        return category
    def delete(self, category:User) -> None:
        self.session.delete(category)
        self.session.flush()