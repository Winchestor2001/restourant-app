from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError
from src.database.models.admin import Admin
from src.repositories.admin import AdminRepository
from src.schemas.admin_schema import AdminUpdate
from src.services.base import BaseService


class AdminService(BaseService[Admin]):
    def __init__(self, repository: AdminRepository) -> None:
        super().__init__(repository)

    def update(self, session: Session, id: int, obj: AdminUpdate) -> Admin:
        admin = self.repository.get(session, id)

        if not admin:
            raise NotFoundError(detail="Admin not found")

        update_data = obj.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(admin, field, value)

        updated_obj = self.repository.update(session, admin)
        session.commit()
        session.refresh(updated_obj)
        return updated_obj

    def delete(self, session: Session, id: int) -> None:
        admin = self.repository.get(session, id)

        if not admin:
            raise NotFoundError(detail="Admin not found")

        self.repository.delete(session, admin)