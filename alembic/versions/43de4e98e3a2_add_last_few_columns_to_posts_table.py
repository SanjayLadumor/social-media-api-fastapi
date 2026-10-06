"""add last few columns to posts table

Revision ID: 43de4e98e3a2
Revises: b881b89787c5
Create Date: 2026-10-06 11:55:41.792544

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43de4e98e3a2'
down_revision: Union[str, Sequence[str], None] = 'b881b89787c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("published",sa.Boolean(),nullable=False,server_default="TRUE"))
    op.add_column("posts",sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
