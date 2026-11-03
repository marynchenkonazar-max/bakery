from decimal import Decimal
from src.models import ProductCategory
from src.repo.product_category import ProductCategoryRepository
from sqlalchemy.orm import Session
class ProductCategoryService:
    def __init__(self, session:Session):
        self.session = session
        self.repo = ProductCategoryRepository(session)
    def create(self, name:str, base_price:Decimal) -> ProductCategory:
        category=ProductCategory(name=name, base_price=base_price)
        category = self.repo.add(category)
        self.session.commit()
        return category
