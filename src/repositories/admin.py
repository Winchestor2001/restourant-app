from sqlalchemy.orm import Session
from src.database.models.admin import Admin
from src.repositories.base import BaseRepository


class AdminRepository(BaseRepository[Admin]):
    model = Admin

    def update(self, session: Session, obj: Admin) -> Admin:
        session.flush()
        return obj
