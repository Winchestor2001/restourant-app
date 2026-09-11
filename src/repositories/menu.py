from src.database.models.menu import Menu
from src.repositories.base import BaseRepository


class MenuRepository(BaseRepository[Menu]):
    model = Menu
