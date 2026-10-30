import uuid
from src.models import ProductCategory
from sqlalchemy.orm import Session
class ProductCategoryRepository:
    def __init__(self, session: Session):
        self.session = session
    def get(self, id:uuid.UUID) -> type[ProductCategory] | None:
        return self.session.get(ProductCategory, id)
    def add(self, category:ProductCategory) -> ProductCategory:
        self.session.add(category)
        self.session.flush()
        return category
    def delete(self, category:ProductCategory) -> None:
        self.session.delete(category)
        self.session.flush()
# def find_by_username(self, username: str) -> UserModel:
        #return self.session.query(self.model).filter_by(username=username).first()
#ToDO orm, як зробити репо