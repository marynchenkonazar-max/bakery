from src.models import User
from src.repo.user import UserRepository
from sqlalchemy.orm import Session
class UserService:
    def __init__(self, session:Session):
        self.session = session
        self.repo = UserRepository(session)
    def create(self, name:str, phone_number:str, email:str, addresses:list, orders:list) -> User:
        user=User(name=name, phone_number=phone_number, email=email, addresses=addresses, orders=orders)
        user = self.repo.add(user)
        self.session.commit()
        return user