"""create posta table

Revision ID: 7023d1052656
Revises: 
Create Date: 2026-07-02 00:23:26.298753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7023d1052656'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


##it handles the changes. we write all the logic for creating a post table
def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=True,primary_key=True),
        sa.Column('title',sa.String(),nullable=False))
    pass



## in this we write all the logics to remove the changes in the  table
def downgrade() -> None:
    op.drop_table('posts')
    pass
