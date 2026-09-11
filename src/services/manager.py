from src.database.models.manager import Manager
from src.repositories.manager import ManagerRepository
from src.services.base import BaseService


class ManagerService(BaseService[Manager]):
    def __init__(self, repository: ManagerRepository) -> None:
        super().__init__(repository)
