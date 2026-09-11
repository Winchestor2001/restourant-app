from src.repositories.category import CategoryRepository
from src.services.category import CategoryService


def get_category_service(repository: CategoryRepository) -> CategoryService:
    return CategoryService(repository)