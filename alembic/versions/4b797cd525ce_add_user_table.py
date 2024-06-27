"""add user table

Revision ID: 4b797cd525ce
Revises: 89007d4158db
Create Date: 2024-06-27 13:18:15.032922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b797cd525ce'
down_revision: Union[str, None] = '89007d4158db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()') , nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email') )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
