from src.repositories.client import ClientRepository
from src.services.client import ClientService
from src.repositories.menu import MenuRepository
from src.services.menu import MenuService
from src.repositories.manager import ManagerRepository
from src.services.manager import ManagerService
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

def get_manager_service() -> ManagerService:
    repository = ManagerRepository()
    return ManagerService(repository)

def get_menu_service() -> MenuService:
    menu_repo = MenuRepository()
    category_repo = CategoryRepository()
    return MenuService(menu_repo, category_repo)

def get_client_service() -> ClientService:
    repository = ClientRepository()
    return ClientService(repository)