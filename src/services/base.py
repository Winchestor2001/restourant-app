from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError
from src.database.base import Base
from src.repositories.base import BaseRepository

ModelType = TypeVar("ModelType", bound=Base)


class BaseService(Generic[ModelType]):
    def __init__(self, repository: BaseRepository[ModelType]) -> None:
        self.repository = repository

    def get(self, session: Session, pk: int) -> ModelType | None:
        db_obj = self.repository.get(session, pk)
        if not db_obj:
            raise NotFoundError(detail="Not found")
        return self.repository.get(session, pk)

    def get_all(self, session: Session) -> list[ModelType]:
        return self.repository.get_all(session)

    def create(self, session: Session, obj: ModelType) -> ModelType:
        return self.repository.create(session, obj)

    def update(self, session: Session, obj: ModelType) -> ModelType:
        return self.repository.update(session, obj)

    def delete(self, session: Session, obj: ModelType) -> None:
        self.repository.delete(session, obj)
