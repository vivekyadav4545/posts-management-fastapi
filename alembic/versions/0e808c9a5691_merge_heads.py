"""merge heads

Revision ID: 0e808c9a5691
Revises: c83c886316de, 39d1cb38f3e5
Create Date: 2026-07-21 21:38:08.327622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e808c9a5691'
down_revision: Union[str, Sequence[str], None] = ('c83c886316de', '39d1cb38f3e5')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
