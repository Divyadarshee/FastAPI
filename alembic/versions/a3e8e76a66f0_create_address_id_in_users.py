"""Create address_id in users

Revision ID: a3e8e76a66f0
Revises: 7bb829a010d3
Create Date: 2022-04-16 17:34:07.284413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3e8e76a66f0'
down_revision = '7bb829a010d3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_foreign_key', 'users', 'address', local_cols=['address_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('address_users_foreign_key', 'users')
    op.drop_column('users', 'address_id')
