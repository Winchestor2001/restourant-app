from sqlalchemy import Column, DateTime, ForeignKey, String, Table, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column(
        "role_id",
        ForeignKey("roles.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "permission_id",
        ForeignKey("permissions.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


admin_roles = Table(
    "admin_roles",
    Base.metadata,
    Column(
        "admin_id",
        ForeignKey("admins.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "role_id",
        ForeignKey("roles.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "granted_at",
        DateTime(),
        server_default=text("TIMEZONE('utc', now())"),
        nullable=False,
    ),
)


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
    is_protected: Mapped[bool] = mapped_column(default=False)

    permissions: Mapped[list["Permissions"]] = relationship(
        secondary=role_permissions,
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
