from src.repositories.category import CategoryRepository
from src.services.category import CategoryService


def get_category_service() -> CategoryService:
    repository = CategoryRepository()
    return CategoryService(repository)
