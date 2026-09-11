from src.database.models.category import Category
from src.repositories.base import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    model = Category
