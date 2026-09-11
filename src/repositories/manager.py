from src.database.models.manager import Manager
from src.repositories.base import BaseRepository


class ManagerRepository(BaseRepository[Manager]):
    model = Manager
