from src.services.admin import AdminService
from src.repositories.admin import AdminRepository
from src.repositories.category import CategoryRepository
from src.services.category import CategoryService


def get_category_service() -> CategoryService:
    repository = CategoryRepository()
    return CategoryService(repository)


def get_admin_service() -> AdminService:
    repository = AdminRepository()
    return AdminService(repository)
