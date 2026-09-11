from src.database.models.client import Client
from src.repositories.base import BaseRepository


class ClientRepository(BaseRepository[Client]):
    model = Client
