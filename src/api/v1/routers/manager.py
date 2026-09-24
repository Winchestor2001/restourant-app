from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from src.core.security import hash_password
from src.database.models import Manager
from src.schemas.manager_schema import ManagerCreate, ManagerBase, ManagerUpdate, ManagerFilter
from src.api.v1.dependancies import get_manager_service
from src.services.manager import ManagerService
from src.database.session import get_session

router = APIRouter(prefix="/managers", tags=["Managers"])


@router.get("/", response_model=list[ManagerBase])
def get_all_managers(
        filters: ManagerFilter = Query(None),
        session: Session = Depends(get_session),
        service: ManagerService = Depends(get_manager_service),
):
    return service.get_all(session=session)


@router.post("/", response_model=ManagerBase, status_code=status.HTTP_201_CREATED)
def create_manager(
        payload: ManagerCreate,
        session: Session = Depends(get_session),
        service: ManagerService = Depends(get_manager_service),
):
    payload_dump = payload.model_dump()
    hashed_password = hash_password(payload_dump.get("password"))
    payload_dump["hashed_password"] = hashed_password
    payload_dump.pop("password")
    '''
    {
        "full_name2": "Bexruz",
        "email": "user@example.com",
        "hashed_password": "hgevwfuybwfuyw"
    }
    '''
    db_manager = Manager(**payload_dump)
    new_manager = service.create(session=session, obj=db_manager)
    return new_manager


@router.get("/{manager_id}", response_model=ManagerBase, status_code=status.HTTP_200_OK)
def get_manager_by_id(
        manager_id: int,
        session: Session = Depends(get_session),
        service: ManagerService = Depends(get_manager_service),
):
    return service.get(session, manager_id)


@router.patch("/{manager_id}", response_model=ManagerBase, status_code=status.HTTP_200_OK)
def update_manager(
        payload: ManagerUpdate,
        manager_id: int,
        session: Session = Depends(get_session),
        service: ManagerService = Depends(get_manager_service),
):

    return service.update(session, manager_id, payload)


@router.delete("/{manager_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_manager(
        manager_id: int,
        session: Session = Depends(get_session),
        service: ManagerService = Depends(get_manager_service),
):
    return service.delete(session, manager_id)  # noqa