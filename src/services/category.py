from src.database.models.category import Category
from src.repositories.category import CategoryRepository
from src.services.base import BaseService


class CategoryService(BaseService[Category]):
    def __init__(self, repository: CategoryRepository) -> None:
        super().__init__(repository)
