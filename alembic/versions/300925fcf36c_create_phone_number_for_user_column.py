"""Create phone number for User column

Revision ID: 300925fcf36c
Revises: 
Create Date: 2022-04-16 17:14:59.376586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '300925fcf36c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')
