from src.database.models.admin import Admin
from src.repositories.admin import AdminRepository
from src.services.base import BaseService


class AdminService(BaseService[Admin]):
    def __init__(self, repository: AdminRepository) -> None:
        super().__init__(repository)
