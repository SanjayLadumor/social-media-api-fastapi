"""create posts table

Revision ID: 086015c521a9
Revises: 
Create Date: 2026-10-06 10:59:44.127303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '086015c521a9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),sa.Column("title",sa.String(),nullable=False))
    pass

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
    pass
