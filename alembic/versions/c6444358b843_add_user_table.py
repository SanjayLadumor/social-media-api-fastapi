"""add user table

Revision ID: c6444358b843
Revises: a3c5baa004fd
Create Date: 2026-10-06 11:46:58.971345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6444358b843'
down_revision: Union[str, Sequence[str], None] = 'a3c5baa004fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users",
                    sa.Column("id",sa.Integer(),nullable=False),
                    sa.Column("email",sa.String(),nullable=False),
                    sa.Column("password",sa.String(),nullable=False),
                    sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text("now()"),nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email"))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
    pass
