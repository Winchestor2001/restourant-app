from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError
from src.database.models import Roles, Permissions
from src.database.models.role import RolePermissions
from src.repositories.base import BaseRepository


class RoleRepository(BaseRepository[Roles]):
    model = Roles

    def update(self, session: Session, obj: Roles) -> Roles:
        session.flush()
        return obj


class RolePermissionsRepository(BaseRepository[RolePermissions]):
    model = RolePermissions

    def delete(self, session: Session, obj: RolePermissions) -> None:
        stmt = select(RolePermissions).where(
            RolePermissions.role_id == obj.role_id,
            RolePermissions.permission_id == obj.permission_id,
        )

        assign_obj = session.scalar(stmt)

        if assign_obj is None:
            raise NotFoundError("Permission is not assigned to this role")
        session.delete(assign_obj)

class PermissionRepository(BaseRepository[Permissions]):
    model = Permissions

    def update(self, session: Session, obj: Permissions) -> Permissions:
        session.flush()
        return obj