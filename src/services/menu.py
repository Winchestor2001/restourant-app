from src.database.models.menu import Menu
from src.repositories.menu import MenuRepository
from src.services.base import BaseService


class MenuService(BaseService[Menu]):
    def __init__(self, repository: MenuRepository) -> None:
        super().__init__(repository)
