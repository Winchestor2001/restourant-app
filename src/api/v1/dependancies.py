import jwt
from fastapi import Security, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.exceptions import NotFoundError
from src.core.security import get_client_id_from_token
from src.database.models import Client
from src.database.session import get_session
from src.repositories.client import ClientRepository
from src.services.client import ClientService
from src.repositories.menu import MenuRepository
from src.services.menu import MenuService
from src.repositories.manager import ManagerRepository
from src.services.manager import ManagerService
from src.services.admin import AdminService
from src.repositories.admin import AdminRepository
from src.repositories.category import CategoryRepository
from src.services.category import CategoryService

access_token_scheme = HTTPBearer(scheme_name="access-token", auto_error=False)


def get_category_service() -> CategoryService:
    repository = CategoryRepository()
    return CategoryService(repository)


def get_admin_service() -> AdminService:
    repository = AdminRepository()
    return AdminService(repository)


def get_manager_service() -> ManagerService:
    repository = ManagerRepository()
    return ManagerService(repository)


def get_menu_service() -> MenuService:
    menu_repo = MenuRepository()
    category_repo = CategoryRepository()
    return MenuService(menu_repo, category_repo)


def get_client_service() -> ClientService:
    repository = ClientRepository()
    return ClientService(repository)


def get_current_client(
        credentials: HTTPAuthorizationCredentials | None = Security(access_token_scheme),
        session: AsyncSession = Depends(get_session),
        service: ClientService = Depends(get_client_service),
) -> Client:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token invalid or expired",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if credentials is None:
        raise credentials_exception

    try:
        client_id = get_client_id_from_token(credentials.credentials)
    except jwt.PyJWTError as exc:
        raise credentials_exception

    try:
        client = service.get(session=session, pk=client_id)
    except NotFoundError:
        raise credentials_exception

    if not client.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Member is inactive",
        )

    return client
