"""add content column to post table

Revision ID: 89007d4158db
Revises: b5d42edc8adc
Create Date: 2024-06-27 13:06:19.471288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89007d4158db'
down_revision: Union[str, None] = 'b5d42edc8adc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
