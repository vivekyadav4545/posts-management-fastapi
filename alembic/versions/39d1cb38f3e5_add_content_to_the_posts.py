"""add content to the posts

Revision ID: 39d1cb38f3e5
Revises: 7023d1052656
Create Date: 2026-07-21 21:30:07.759086

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39d1cb38f3e5'
down_revision: Union[str, Sequence[str], None] = '7023d1052656'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
