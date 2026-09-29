from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError
from src.database.models import Roles, Permissions, RolePermissions
from src.repositories.permission import RoleRepository, PermissionRepository, RolePermissionsRepository
from src.schemas.permission_schema import RoleUpdate, PermissionUpdate, AssignPermissionToRole
from src.services.base import BaseService


class RoleService(BaseService[Roles]):
    def __init__(self, role_repo: RoleRepository) -> None:
        self.role_repo = role_repo
        super().__init__(role_repo)

    def update(self, session: Session, id: int, obj: RoleUpdate) -> Roles:
        role = self.repository.get(session, id)

        if not role:
            raise NotFoundError(detail="Roles not found")

        update_data = obj.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(role, field, value)

        updated_obj = self.repository.update(session, role)
        session.commit()
        session.refresh(updated_obj)
        return updated_obj

    def delete(self, session: Session, id: int) -> None:
        role = self.repository.get(session, id)

        if not role:
            raise NotFoundError(detail="Roles not found")

        self.repository.delete(session, role)


class PermissionService(BaseService[Permissions]):
    def __init__(self, permission_repo: PermissionRepository) -> None:
        self.permission_repo = permission_repo
        super().__init__(permission_repo)

    def update(self, session: Session, id: int, obj: PermissionUpdate) -> Permissions:
        permission = self.repository.get(session, id)

        if not permission:
            raise NotFoundError(detail="Permission not found")

        update_data = obj.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(permission, field, value)

        updated_obj = self.repository.update(session, permission)
        session.commit()
        session.refresh(updated_obj)
        return updated_obj

    def delete(self, session: Session, id: int) -> None:
        permission = self.repository.get(session, id)

        if not permission:
            raise NotFoundError(detail="Permission not found")

        self.repository.delete(session, permission)


class RolePermissionsService(BaseService):
    def __init__(self, role_repo: RoleRepository, role_permission_repo: RolePermissionsRepository) -> None:
        self.role_repo = role_repo
        self.role_permission_repo = role_permission_repo
        super().__init__(role_permission_repo)

    def assign_permission(self, session: Session, obj: AssignPermissionToRole) -> Roles:
        role = self.role_repo.get(session, obj.role_id)
        if not role:
            raise NotFoundError(detail="Roles not found")

        assign_obj = RolePermissions(**obj.model_dump(exclude_unset=True))

        self.role_permission_repo.create(session, assign_obj)
        session.commit()
        return role

    def unassign_permission(self, session: Session, obj: AssignPermissionToRole) -> Roles:
        role = self.role_repo.get(session, obj.role_id)
        if not role:
            raise NotFoundError(detail="Roles not found")

        assign_obj = RolePermissions(**obj.model_dump(exclude_unset=True))

        self.role_permission_repo.delete(session, assign_obj)
        session.commit()
        return role