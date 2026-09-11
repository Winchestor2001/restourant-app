from typing import Generic, TypeVar

from src.database.base import Base
from src.repositories.base import BaseRepository

ModelType = TypeVar("ModelType", bound=Base)


class BaseService(Generic[ModelType]):
    def __init__(self, repository: BaseRepository[ModelType]) -> None:
        self.repository = repository

    def get(self, pk: int) -> ModelType | None:
        return self.repository.get(pk)

    def get_all(self) -> list[ModelType]:
        return self.repository.get_all()

    def create(self, obj: ModelType) -> ModelType:
        return self.repository.create(obj)

    def update(self, obj: ModelType) -> ModelType:
        return self.repository.update(obj)

    def delete(self, obj: ModelType) -> None:
        self.repository.delete(obj)
