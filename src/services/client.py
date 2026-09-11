from src.database.models.client import Client
from src.repositories.client import ClientRepository
from src.services.base import BaseService


class ClientService(BaseService[Client]):
    def __init__(self, repository: ClientRepository) -> None:
        super().__init__(repository)
