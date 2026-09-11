from src.database.models.admin import Admin
from src.repositories.base import BaseRepository


class AdminRepository(BaseRepository[Admin]):
    model = Admin
