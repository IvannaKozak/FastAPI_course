"""Create phone number for user column

Revision ID: ad9a04d3c1f7
Revises: 
Create Date: 2023-12-01 20:20:57.952132

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad9a04d3c1f7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String, nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
