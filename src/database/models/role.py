from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, Table, text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base

class RolePermissions(Base):
    __tablename__ = "role_permissions"

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True)


class AdminRoles(Base):
    __tablename__ = "admin_roles"

    admin_id: Mapped[int] = mapped_column(ForeignKey("admins.id", ondelete="CASCADE"), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
    granted_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)


class Roles(Base):
    __tablename__ = "roles"
    '''admin, support, superadmin'''
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )
    description: Mapped[str | None] = mapped_column(
        String(255),
        default=None
    )
    permissions: Mapped[list["Permissions"]] = relationship(
        secondary=RolePermissions.__table__,
        lazy="selectin",
    )


class Permissions(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )
    description: Mapped[str | None] = mapped_column(
        String(255),
        default=None
    )
