"""add content column to posts table

Revision ID: a3c5baa004fd
Revises: 086015c521a9
Create Date: 2026-10-06 11:44:17.565803

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3c5baa004fd'
down_revision: Union[str, Sequence[str], None] = '086015c521a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","content")
    pass
