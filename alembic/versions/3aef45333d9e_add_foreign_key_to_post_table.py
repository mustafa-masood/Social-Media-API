"""add foreign-key to post table

Revision ID: 3aef45333d9e
Revises: 4b797cd525ce
Create Date: 2024-06-27 13:52:13.264305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3aef45333d9e'
down_revision: Union[str, None] = '4b797cd525ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
        op.drop_constraint('post_users_fk', table_name="posts")
        op.drop_column('posts','owner_id')
        pass
