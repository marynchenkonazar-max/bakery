import uuid
from src.models import ProductCategory
from src.repo.product_category import ProductCategoryRepository
from sqlalchemy.orm import Session
class ProductCategoryService:
    def __init__(self, session):
        self.session = session
        self.repo = ProductCategoryRepository(session)
